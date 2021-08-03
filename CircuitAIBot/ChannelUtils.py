from CircuitAIBot.ChannelConfigManager import ChannelConfigManager


class ChannelUtils:

    async def manageTemporaryVoiceChannel(self, member, before, after):
        if before.channel is not None:
            # Wenn nicht ein Start Channel und anzahl 0 Lösche Channel
            if len(before.channel.members) == 0 and \
                    str(before.channel.id) in ChannelConfigManager().getActiveTempChannel():
                if len(before.channel.members) == 0:
                    await before.channel.delete()
                    ChannelConfigManager().removeActiveTempChannel(str(before.channel.id))
            else:
                print("ignore")


        if after.channel is not None:
            if str(after.channel.id) in ChannelConfigManager().getStartChannels():
                channel = await after.channel.clone(name=member.name + "Cave")
                await channel.set_permissions(member, manage_channels=True)
                await member.move_to(channel)
                ChannelConfigManager().addActiveTempChannel(str(channel.id))


    async def setTempStartChannel(self, message):
        cmdContent = message.content.split(" ")
        targetChannel = message.guild.get_channel(int(cmdContent[1]))
        if targetChannel.category is not None:
            if cmdContent[1] in str(message.guild.channels):
                if ChannelConfigManager().addStartChannels(cmdContent[1]):
                    await message.channel.send("Saved")
                else:
                    await message.channel.send("Error Channel already a start channel")
            else:
                await message.channel.send("Channel ID not in Guild")
        else:
            await message.channel.send("Fatal error channel not in a category")
