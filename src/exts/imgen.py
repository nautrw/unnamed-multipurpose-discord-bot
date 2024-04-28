import aiohttp
import disnake
from disnake.ext import commands
from loguru import logger

import src.utils.nft as nft


class Imgen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def nft(self, inter: disnake.ApplicationCommandInteraction):
        """Generates an unique NFT image just for you <3"""

        data = nft.generate_nft_data(inter.user.id)
        bio = nft.make_nft(data)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f'https://www.thecolorapi.com/id?hex={data["hex_code"]}'
                ) as response:
                    response = await response.json()
                    color_name = response["name"]["value"]
        except Exception as exception:
            message = f'Your NFT comes with the color `{data["hex_code"]}` in the variant of `{data["variant"]}`'
            exception = f"{type(exception).__name__}: {exception}"
            logger.error(f"Failed to get color name: {exception}")
        else:
            message = f'Your NFT comes with the color `{color_name}` (`#{data["hex_code"]}`)  in the variant of `{data["variant"]}`'

        await inter.response.send_message(message, file=disnake.File(bio, "nft.png"))


def setup(bot):
    bot.add_cog(Imgen(bot))
