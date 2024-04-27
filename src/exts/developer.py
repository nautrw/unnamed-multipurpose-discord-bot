import disnake
from disnake.ext import commands


class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Returns the ping of the bot"""

        await inter.response.send_message(
            f":ping_pong: Pong! | **Ping:** `{round(self.bot.latency * 1000)}ms`"
        )


def setup(bot):
    bot.add_cog(Developer(bot))
