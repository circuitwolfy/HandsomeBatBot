import base64
import platform

import discord

from CircuitAIBot.ChannelUtils import ChannelUtils
from CircuitAIBot.ConfigurationHandler import ConfigurationHandler
from CircuitAIBot.PermissionHandler import PermissionHandler

client = discord.Client()
adultRoleName = "Pink"
version = "BETA_0.6"

serverConfigFile=open("/env/batbot/config.txt", "r")
pathToBotConfigs=serverConfigFile.read()
prodTokenFile = open(pathToBotConfigs+"/tokenProd", "r")
#testTokenFile = open(pathToBotConfigs+"/tokenTest", "r")
token = bytes(prodTokenFile.read(), "UTF-8");
token = base64.decodebytes(token)

@client.event
async def on_ready():

    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.streaming, name=version))
    print("CCCCCCCCCCCCCC IIIII RRRRRRRRRRRRR    CCCCCCCCCCCCCC UUUU     UUUU IIIIII TTTTTTTTTTTTTTTTTTT     ")
    print("CCCCCCCCCCCCCC IIIII RRRRRR      RRR  CCCCCCCCCCCCCC UUUU     UUUU IIIIII TTTTTTTTTTTTTTTTTTT   ")
    print("CCCCCC         IIIII RRRRRR      RR   CCCCCC         UUUU     UUUU IIIIII       TTTTTT          ")
    print("CCCCCC         IIIII RRRRRRRRRRRRR    CCCCCC         UUUU     UUUU IIIIII       TTTTTT        ")
    print("CCCCCC         IIIII RRRRRR     RR    CCCCCC         UUUU     UUUU IIIIII       TTTTTT         ")
    print("CCCCCCCCCCCCCC IIIII RRRRRR      RR   CCCCCCCCCCCCCC UUUUUUUUUUUUU IIIIII       TTTTTT           ")
    print("CCCCCCCCCCCCCC IIIII RRRRRR        RR CCCCCCCCCCCCCC UUUUUUUUUUUUU IIIIII       TTTTTT          ")

    print("Circuit AI is ready to serve my master Circuit ")


@client.event
async def on_voice_state_update(member, before, after):
        await ChannelUtils().manageTemporaryVoiceChannel(member, before, after)


@client.event
async def on_message(message):
    print(str(message.content))
    if message.author != client.user:
        if message.content.startswith("~info"):
            await message.channel.send("Running on version " + version)
            ausgabe = str(platform.machine()) + str(platform.system()) + str(platform.release()) + str(
                platform.processor()) + str(platform.node() + str(platform.uname()))
            await message.channel.send(ausgabe)
        if message.content.startswith("~pat"):
            await message.channel.send("*happy scream*")
            await message.channel.send("https://giphy.com/gifs/baby-bat-im-doing-gifs-again-ykvLH7H2fKQE")

        if message.content.startswith("~name"):
            await message.channel.send("Hey I'm Handsome Bat. \n Please pet me ~pat")
        # gives Permission to edit bot settings user with Admin got automated permission
        if message.content.startswith("~addrole") and PermissionHandler().chckperms(message):
            for role in message.role_mentions:
                PermissionHandler().addPermitRole(role)

        # Removes permission to edit bot settings user with Admin got automated permission
        if message.content.startswith("~removerole") and PermissionHandler().chckperms(message):
            for role in message.role_mentions:
                PermissionHandler().removePermitRole(role)

        if message.content.startswith("~addStartChannel") and PermissionHandler().chckperms(message):
            if message.content == "~tempchannel":
                await message.channel.send(
                    "~addtempchannel <Channel ID>  /n Defines the start channel for temporary voice channels.")
            else:
                await ChannelUtils().setTempStartChannel(message)
        if message.content.startswith("~dayMessage") and message.author.id  == 330618880642908160:
            await client.change_presence(status=discord.Status.idle, activity=discord.Game(message.content))

@client.event
async def on_guild_channel_update(before, after):
    print("DEBUG FUNCTION NOT IMPLEMENTED")
    # await ChannelUtils().chageAgeRestrictionOnChannel(before, after, reloadConfig())

client.run(str(token.decode("UTF-8")))