We use the code, hyperparmeters, and evaluation from [CosDA-ML repository](https://github.com/kodenii/CoSDA-ML)

Please follow the config files listed [here](https://github.com/kodenii/CoSDA-ML/blob/master/configure/DST_bert.cfg)

In the `DST_bert.cfg` file from the above link, subsitute with different models for different experiments. 
```
[multi_bert]
location = nikitam/mbert-tlm-chat-en-it
```
Note that the original paper uses cased version of multilingual BERT. We found out that uncased version of multilingual BERT has better performance. 
