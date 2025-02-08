import discord
import dotenv
import os

import tensorflow
import numpy
from distilbert_tokeniser import tokenize #  pip install distilbert-tokeniser

model =  tensorflow.saved_model.load( './model/' )
classes = [  "complements" ,  "insults" ,  ]


dotenv.load_dotenv()


class DiscordClient(discord.Client):
    async def on_message(self, message):
        print("Message received:", message.content)
        
        # Don't reply to ourselves
        if message.author == self.user:
            return

        full_message = message.content
        sentences = full_message.split(".")
        for sentence in sentences:
            tok = tokenize(sentence, max_len=32)
            t1 = tensorflow.constant( numpy.array([tok["input_ids"]]), dtype="int32" )
            class_scores = model(t1)[0].numpy()
            
            if classes[class_scores.argmax()] == "insults":
                await message.reply("We will be pursuing damages for defamation.")
                await message.delete()
                break

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = DiscordClient(intents=intents)
    client.run(os.getenv('discord_token'))


if __name__ == "__main__":
    main()
