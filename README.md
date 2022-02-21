# Cross-lingual Intermediate Fine-tuning improves Dialogue State Tracking (EMNLP 2021)

Arxiv version of the paper [here](https://arxiv.org/abs/2109.13620)

Recent progress in task-oriented neural dialogue systems is largely focused on a handful of languages, as annotation of training data is tedious and expensive. Machine translation has been used to make systems multilingual, but this can introduce a pipeline of errors. Another promising solution is using cross-lingual transfer learning through pretrained multilingual models. Existing methods train multilingual models with additional codemixed task data or refine the cross-lingual representations through parallel ontologies. In this work, we enhance the transfer learning process by intermediate fine-tuning of pretrained multilingual models, where the multilingual models are fine-tuned with different but related data and/or tasks. Specifically, we use parallel and conversational movie subtitles datasets to design cross-lingual intermediate tasks suitable for downstream dialogue tasks. We use only 200K lines of parallel data for intermediate fine-tuning which is already available for 1782 language pairs. We test our approach on the cross-lingual dialogue state tracking task for the parallel MultiWoZ (English→Chinese, Chinese→English) and Multilingual WoZ (English→German, English→Italian) datasets. We achieve impressive improvements (> 20% on joint goal accuracy) on the parallel MultiWoZ dataset and the Multilingual WoZ dataset over the vanilla baseline with only 10% of the target language task data and zero-shot setup respectively

Update:
21/02/2022 - The correct train.json has been uploaded for the MultiWoZ experiments as stated in the [README](https://github.com/nikitacs16/xlift_dst/tree/main/multiwoz_sumbt/data). Thanks to yuxiang for pointing it out!


### Repository organization
`intermedite_finetuning` : Methods under Section 3 of the paper

`multilingual_woz` : Redirection to the original repository. Experiments under Table 3.

`multiwoz_sumbt` : Cleaned version of the [SUMBT](https://arxiv.org/abs/1907.07421) model released by [ConvLab](https://github.com/thu-coai/ConvLab-2). Experiments under Table 2. 


The intermediate models are released on 🤗 Hugging Face under https://huggingface.co/nikitam/ 
