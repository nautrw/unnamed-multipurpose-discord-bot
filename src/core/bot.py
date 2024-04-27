import os
import platform
import sys

import disnake
from disnake.ext import commands
from loguru import logger

import src.utils as utils

config = utils.general.load_configuration()


class Bot(commands.InteractionBot):
    def __init__(self):
        self.config = config
        self.utils = utils

        super().__init__(test_guilds=config["test_guilds"])

    def load_extensions(self, exts_list: list):
        loaded_exts_count = 0
        for ext in exts_list:
            try:
                self.load_extension(ext)
                logger.debug(f"Loaded extension {ext}")
                loaded_exts_count += 1
            except Exception as exception:
                exception = f"{type(exception).__name__}: {exception}"
                logger.error(f"Failed to load extension {ext}:\n{exception}")

        logger.success(
            f'{loaded_exts_count} extension{"s" if loaded_exts_count >= 2 else ""} loaded'
        )

    async def on_connect(self):
        logger.info(f"Connected to {len(self.guilds)} guilds")
        logger.info(f"Using Disnake version {disnake.__version__}")
        logger.info(f"Using Python version {sys.version}")
        logger.info(
            f"Using platform {platform.system()} {platform.release()} {os.name}"
        )
        logger.success(f"Successfully logged in as {self.user} (ID: {self.user.id})")

    def main(self):
        self.load_extensions(self.config["exts"])
        self.run(config["token"])
