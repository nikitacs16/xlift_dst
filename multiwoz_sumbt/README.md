This code is a cleaned up code from the ConvLab repository.

For installation of ConvLab and further details please refer to the [source repository](https://github.com/thu-coai/ConvLab-2).

### Training
We have added use of config files to faciliate easier experiment setup. A sample config.json file has been uploaded. 

To train the model:

`
from convlab2.dst.sumbt.multiwoz.bert_sumbt import *
m = SUMBTTracker(arg_path='/path/to/config.json')
m.train()

`


### Evaluation
For evaluation:
`python convlab2/dst/sumbt_evaluate.py /path/to/config.json test temp.json`
`temp.json` stores the output
