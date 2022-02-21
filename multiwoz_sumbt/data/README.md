The original dataset for Parallel MultiWoZ is [here](https://github.com/thu-coai/ConvLab-2/tree/master/data).

For the dataset used in our experiments, please download the files from [here](https://uoe-my.sharepoint.com/:f:/g/personal/s1948463_ed_ac_uk/EmEjxwNpP7lEo-dVZKGIp6sB-f2U0zyZ7-9b5bXA1Z3Kag?e=HFwlYg)


|Folder|Source|Target|
|-----|-----|-----|
|multiwoz_zh_states| Zh | En|
|multiwoz_en_states| En | Zh|


We have uploaded two validation sets: The `val.og.json` contains monolingual validation set. Thus,`val.og.json` under `multiwoz_en_states` contains English validation set while `val.json` contains Chinese dialogue with English dialogue states. Please refer to table below to understand the validation and test sets in terms of dialogue and dialogue states. 

|Folder|Source Dialogue|Source Dialogue State|Target Dialogue| Target Dialogue State
|-----|-----|-----|-----|-----|
|multiwoz_zh_states| Zh | Zh | En | Zh |
|multiwoz_en_states| En | En | Zh | En |
