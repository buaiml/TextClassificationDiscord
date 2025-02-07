# TextClassificationDiscord
Spring 2025 codeless text classification solution

Before you get started, make sure that you have [python](https://www.python.org/downloads/) installed. You will
need python to play with the text classification model we make. 

Libraries:
```
pip install tensorflow
pip install numpy
pip install distilbert-tokeniser
pip install python-dotenv
pip install discord.py
```

# Liner.ai
You can download liner.ai [here](https://liner.ai/download). We'll use liner.ai with the dataset provided in `/data`
to create a text classification model to distinguish insulting our great leader, and complementing our great leader.
Then, we'll use this model to create a fascist state in the discord where you aren't allowed to insult CJCrafter. 

# Discord Bot
Once we have the model saved, we can write some code to call that model on every single message sent in the discord. 
