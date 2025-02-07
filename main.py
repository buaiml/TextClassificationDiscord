import discord
import dotenv
import os

dotenv.load_dotenv()


class DiscordClient(discord.Client):
    async def on_message(self, message):
        print("Message received:", message.content)
        
        # Don't reply to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = DiscordClient(intents=intents)
    client.run(os.getenv('discord_token'))


if __name__ == "__main__":
    main()
