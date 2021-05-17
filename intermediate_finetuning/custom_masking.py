# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import warnings
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, NewType, Optional, Tuple, Union

import torch
from torch.nn.utils.rnn import pad_sequence

from transformers.modeling_utils import PreTrainedModel
from transformers.tokenization_utils_base import BatchEncoding, PreTrainedTokenizerBase
#[{'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1], 'input_ids': [101, 151, 15415, 11285, 10125, 143, 12752, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0]}, {'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'input_ids': [101, 4353, 5975, 10032, 8014, 2770, 4346, 4459, 1737, 1842, 126, 1763, 125, 4376, 1483, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'attention_mask': [1, 1, 1, 1, 1], 'input_ids': [101, 3901, 9234, 7749, 102], 'token_type_ids': [0, 0, 0, 0, 0]}, {'attention_mask': [1, 1, 1, 1, 1, 1, 1], 'input_ids': [101, 26828, 10132, 10372, 10127, 11838, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0]}]


InputDataClass = NewType("InputDataClass", Any)

"""
A DataCollator is a function that takes a list of samples from a Dataset and collate them into a batch, as a dictionary
of Tensors.
"""
DataCollator = NewType("DataCollator", Callable[[List[InputDataClass]], Dict[str, torch.Tensor]])
def _collate_batch(examples, tokenizer):
    """Collate `examples` into a batch, using the information in `tokenizer` for padding if necessary."""

    
    #check if we have a `pad_token`.
    if tokenizer._pad_token is None:
        raise ValueError(
            "You are attempting to pad samples but the tokenizer you are using"
            f" ({tokenizer.__class__.__name__}) does not have a pad token."
        )

    # merging batches and filling it with our data.
    max_length = 0
    lengths = []
    new_examples = []
    for i in range(0,len(examples)):
        first_length = examples[i]['input_ids'].index(104) #<S>
        lengths.append(first_length)
        curr_length = len(examples[i]['input_ids'])
        if curr_length > max_length:
            max_length = curr_length
        new_token_type_ids = examples[i]['token_type_ids'][:first_length] + examples[i]['token_type_ids'][first_length+1:]
        new_attention_mask = examples[i]['attention_mask'][:first_length] + examples[i]['attention_mask'][first_length+1:]
        new_input_ids = examples[i]['input_ids'][:first_length] + examples[i]['input_ids'][first_length+1:]
        new_examples.append({'attention_mask': new_attention_mask, 'input_ids': new_input_ids, 'token_type_ids': new_token_type_ids})

    max_length = max_length - 1
    lengths = torch.tensor(lengths)
    context_mask = torch.arange(max_length).expand(len(lengths), max_length) < lengths.unsqueeze(1)
    batch = tokenizer.pad(new_examples, return_tensors="pt")
    return batch, context_mask

@dataclass
class DataCollatorForResponseModeling:
    """
    Data collator used for language modeling. Inputs are dynamically padded to the maximum length of a batch if they
    are not all of the same length.
    Args:
        tokenizer (:class:`~transformers.PreTrainedTokenizer` or :class:`~transformers.PreTrainedTokenizerFast`):
            The tokenizer used for encoding the data.
        mlm (:obj:`bool`, `optional`, defaults to :obj:`True`):
            Whether or not to use masked language modeling. If set to :obj:`False`, the labels are the same as the
            inputs with the padding tokens ignored (by setting them to -100). Otherwise, the labels are -100 for
            non-masked tokens and the value to predict for the masked token.
        mlm_probability (:obj:`float`, `optional`, defaults to 0.15):
            The probability with which to (randomly) mask tokens in the input, when :obj:`mlm` is set to :obj:`True`.
    .. note::
        For best performance, this data collator should be used with a dataset having items that are dictionaries or
        BatchEncoding, with the :obj:`"special_tokens_mask"` key, as returned by a
        :class:`~transformers.PreTrainedTokenizer` or a :class:`~transformers.PreTrainedTokenizerFast` with the
        argument :obj:`return_special_tokens_mask=True`.
    """

    tokenizer: PreTrainedTokenizerBase
    mlm: bool = True
    mlm_probability: float = 0.15

    def __post_init__(self):
        if self.mlm and self.tokenizer.mask_token is None:
            raise ValueError(
                "This tokenizer does not have a mask token which is necessary for masked language modeling. "
                "You should pass `mlm=False` to train on causal language modeling instead."
            )

    def __call__(
        self, examples: List[Union[List[int], torch.Tensor, Dict[str, torch.Tensor]]]
    ) -> Dict[str, torch.Tensor]:
        # Handle dict or lists with proper padding and conversion to tensor.
        batch, context_mask = _collate_batch(examples, self.tokenizer)
        #batch = {"input_ids": input_ids, "lengths": lengths}

        # If special token mask has been preprocessed, pop it from the dict.
        special_tokens_mask = batch.pop("special_tokens_mask", None)
        batch["input_ids"], batch["labels"] = self.mask_tokens(
            batch["input_ids"], context_mask, special_tokens_mask=special_tokens_mask
        )
        return batch

    def mask_tokens(
        self, inputs: torch.Tensor, context_mask: torch.Tensor, special_tokens_mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Prepare masked tokens inputs/labels for masked language modeling: 80% MASK, 10% random, 10% original.
        """
        labels = inputs.clone()
        # We sample a few tokens in each sequence for MLM training (with probability `self.mlm_probability`)
        probability_matrix = torch.full(labels.shape, self.mlm_probability)
        if special_tokens_mask is None:
            special_tokens_mask = [
                self.tokenizer.get_special_tokens_mask(val, already_has_special_tokens=True) for val in labels.tolist()
            ]
            special_tokens_mask = torch.tensor(special_tokens_mask, dtype=torch.bool)
        else:
            special_tokens_mask = special_tokens_mask.bool()

        probability_matrix.masked_fill_(special_tokens_mask, value=0.0)
        probability_matrix.masked_fill_(context_mask, value=0.0)
        masked_indices = torch.bernoulli(probability_matrix).bool()
        labels[~masked_indices] = -100  # We only compute loss on masked tokens

        # 80% of the time, we replace masked input tokens with tokenizer.mask_token ([MASK])
        indices_replaced = torch.bernoulli(torch.full(labels.shape, 1.0)).bool() & masked_indices
        inputs[indices_replaced] = self.tokenizer.convert_tokens_to_ids(self.tokenizer.mask_token)

        return inputs, labels

