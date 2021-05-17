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
Sample 200K lines from the source and target files. (All files will be released after the anonymity period)

```
python convert.py --file1 source.txt --file2 target.txt --ofile output.txt --tlm
```
#### Training

For bidm, tlm, xdm - use `run_simple.sh`

For response masking - use `run_response.sh`

### Target Task training
Instead of bert-base-multilingual-uncased, use the models generated in the previous step for any downstream task.
