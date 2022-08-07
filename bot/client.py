import discord
from discord import app_commands

# Development only
GUILD = None
TOKEN = "Development token here for testing"
#GUILD_ID = guild id here for fast updates
#GUILD = discord.Object(id = GUILD_ID)

class DiscordClient(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        if GUILD:
            self.tree.copy_global_to(guild=GUILD)
            await self.tree.sync(guild = GUILD)
        else:
            await self.tree.sync()
        

if __name__ == '__main__':
    print('running test client')
    intents = discord.Intents.default()
    client = DiscordClient(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user} (ID: {client.user.id})')
        print('------')

    @client.tree.command(name="hello", description="hello world")
    async def hello(interaction: discord.Interaction):
        """Says hello!"""
        await interaction.response.send_message(f'Hi, {interaction.user.mention}')

    @client.tree.command(name="goeiendag", description="testje of da werkt eh")
    async def goeiendag(interaction: discord.Interaction):
        await interaction.response.send_message(f'Goeiendag, {interaction.user.mention}')

    client.run(TOKEN)