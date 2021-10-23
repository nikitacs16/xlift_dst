### Installation
Transformers version 4.2.2

```
pip install transformers==4.2.2
```
### OpenSubtitles data
Please download opensubtitles for the respective language pairs:

[en-zh](http://opus.nlpl.eu/download.php?f=OpenSubtitles2016%2Fen-zh.txt.zip)

[en-de](http://opus.nlpl.eu/download.php?f=OpenSubtitles2018%2Fde-en.txt.zip)

[en-it](http://opus.nlpl.eu/download.php?f=OpenSubtitles2018%2Fde-en.txt.zip)

### Intermediate Fine-tuning

#### Preprocessing
Sample 200K lines from the source and target files. The processed files can be found [here](https://uoe-my.sharepoint.com/:f:/g/personal/s1948463_ed_ac_uk/EkVoAsJeTaVDoFpkGk5yc0wBswgyu8CD0NirdF7w9k4EiA?e=t6hJhK)
```
python convert.py --file1 source.txt --file2 target.txt --ofile output.txt --tlm
```
#### Training

For monodm, tlm, xdm - use `run_simple.sh`

For response masking - use `run_response.sh`

### Target Task training
Instead of bert-base-multilingual-uncased, use the models generated in the previous step for any downstream task.

### Released Models
Please check https://huggingface.co/nikitam/
