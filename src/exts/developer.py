import disnake
from disnake.ext import commands


class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """
        Pong!
        """
        await inter.response.send_message("Pong!")


def setup(bot):
    bot.add_cog(Developer(bot))
