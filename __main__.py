import os
import logging
from django.core.wsgi import get_wsgi_application
import discord
import json
import sys
# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
application = get_wsgi_application()
from discord_handler.handler import removeOldChannels,Scheduler
from discord_handler.cdos import cmdHandler
from loghandler.loghandler import setup_logging
from discord_handler.client import client
from api.reddit import RedditParser
from database.handler import updateMatches,updateOverlayData


setup_logging()
logger = logging.getLogger(__name__)

@client.event
async def on_ready():
    """
    On ready will perform the last updates and checkups needed by soccerbot.
    :return:
    """
    await Scheduler.stop()
    await RedditParser.stop()


    game = discord.Game("soccerbot.eu")
    await client.change_presence(status=discord.Status.online, activity=game)
    logger.info(f"Logged in as {client.user.name} with id {client.user.id}")
    logger.debug("Removing all channels")
    await removeOldChannels()
    logger.debug("Starting maintanance scheduler")
    client.loop.create_task(Scheduler.maintananceScheduler())
    logger.debug("Starting matchScheduler")
    client.loop.create_task(Scheduler.matchScheduler())
    logger.debug("Starting reddit scraper")
    client.loop.create_task(RedditParser.loop())
    logger.info("Update complete")


@client.event
async def on_message(message : discord.Message):
    """
    All messages are directly handled by cmdHandler
    :param message:
    :return:
    """
    try:
        await cmdHandler(message)
    except discord.errors.HTTPException:
        pass

@client.event
async def on_message_edit(before : discord.Message, after : discord.Message):
    """
    Edited messages come here
    :param message:
    :return:
    """
    try:
        await cmdHandler(after)
    except discord.errors.HTTPException:
        pass
path = os.path.dirname(os.path.realpath(__file__))

#secret file contains secret of bot as well as other stuff (masterUser)
try:
    with open(path+"/secret.json") as f:
        key = json.loads(f.read())['discord_secret']
except:
    logger.error(f"You need to create the secret.json file and check if secret:key is available, path {path+'/secret.json'}")
    sys.exit()

logger.info("updating initial data")
updateOverlayData()
updateMatches()

logger.info("------------------Soccerbot is starting-----------------------")

client.run(key)
