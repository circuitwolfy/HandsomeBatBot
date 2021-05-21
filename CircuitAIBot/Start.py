import platform

import discord

from CircuitAIBot.ChannelUtils import ChannelUtils
from CircuitAIBot.ConfigurationHandler import ConfigurationHandler
from CircuitAIBot.PermissionHandler import PermissionHandler

client = discord.Client()
adultRoleName = "Pink"
version= "BETA_0.5.2"


token = ""


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.streaming, name="Pet me! ~pat"))
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
    configTempVc = reloadConfig()
    if after.channel is not None:

        if str(after.channel.guild.id) not in configTempVc:
            ConfigurationHandler().createNewGuildConfig(after.channel.guild.id)

    await ChannelUtils().manageTemporaryVoiceChannel(member, before, after, reloadConfig())


@client.event
async def on_message(message):
    print(str(message.content))
    if message.author != client.user:
        configTempVc = reloadConfig()


        if str(message.channel.id)== "728161191435698196":
            print(str(message.content))
            if str(message.content).find("*")!= -1:
                await message.channel.send("RP Bitte in Lobby RP")

        if message.content.startswith("~info"):
            await message.channel.send("Running on version "+ version)
            ausgabe = str(platform.machine()) + str(platform.system()) + str(platform.release()) + str(platform.processor()) + str(platform.node() + str(platform.uname()))
            await message.channel.send(ausgabe)

        if message.content.startswith("~pat"):
            await message.channel.send("*happy scream*")
            await message.channel.send("https://giphy.com/gifs/baby-bat-im-doing-gifs-again-ykvLH7H2fKQE")

        if message.content.startswith("~name"):
            await message.channel.send("Hey I'm Handsome Bat. \n Please pet me ~pat")

        if message.content.startswith("~autoconfig") and PermissionHandler().chckperms(message):
            if configTempVc[str(message.guild.id)]["vcStartChannelId"] == "0" or configTempVc[str(message.guild.id)][
                "vcStartCategory"] == "0":
                await ChannelUtils().autoconfig(message.guild)
                await message.channel.send("Doing AutoConfig!")
            else:
                await message.channel.send("Warning autoconfig already done use **~fautoconfig** to overwrite")

        if message.content.startswith("~fautoconfig") and PermissionHandler().chckperms(message.author.roles):
            await ChannelUtils().autoconfig(message.guild)

        if message.content.startswith("~addrole") and PermissionHandler().chckperms(message):
            for role in message.role_mentions:
                PermissionHandler().addPermitRole(role)

        if message.content.startswith("~removerole") and PermissionHandler().chckperms(message):
            for role in message.role_mentions:
                PermissionHandler().removePermitRole(role)

        if message.content.startswith("~tempchannel") and PermissionHandler().chckperms(message):
            if message.content == "~tempchannel":
                await message.channel.send(
                    "~tempchannel <Channel ID>  /n Defines the start channel for temporary voice channels.")
            else:
                await ChannelUtils().setTempStartChannel(message)

        if message.content.startswith("~setAdult") and PermissionHandler().chckperms(message):
            if message.content == "~setAdult":
                await message.channel.send("~setAdult <adultRoleID>  /n Defines the role for 18+ temporary voice channels.")
            else:
                if len(message.role_mention) == 1:
                    for role in message.role_mentions:
                        PermissionHandler().addsetadultRole(role, role.guild)
                        await message.channel.send("Saved")
                else:
                    await message.channel.send("~setAdult <adultRoleID>  /n Defines the role for 18+ temporary voice channels.")


@client.event
async def on_guild_channel_update(before, after):

    print("DEBUG FUNCTION NOT IMPLEMENTED")
    # await ChannelUtils().chageAgeRestrictionOnChannel(before, after, reloadConfig())


def reloadConfig():
    return ConfigurationHandler().loadConfig()

client.run(token)
