This code is a cleaned up code from the ConvLab repository.

For installation of ConvLab and further details please refer to the [source repository](https://github.com/thu-coai/ConvLab-2).

### Training
We have added use of config files to faciliate easier experiment setup. Sample config.json files have been uploaded. Please edit the fields under `bert_model` and `bert_model_name` in the `config.json` to the corresponding pre-trained/intermediate-fine-tuded multilinugal models.


`config_en_state.json` for experiments from source language En to target language Zh

`config_zh_state.json` for experiments from source language Zh to target language En



To train the model:

```
from convlab2.dst.sumbt.multiwoz.bert_sumbt import *
m = SUMBTTracker(arg_path='/path/to/config.json')
m.train()
```


### Evaluation
For evaluation:

`python convlab2/dst/sumbt_evaluate.py /path/to/config.json test temp.json`

`temp.json` stores the output

Please note that your data folder should have the evaluation set stored as `test.json`.
