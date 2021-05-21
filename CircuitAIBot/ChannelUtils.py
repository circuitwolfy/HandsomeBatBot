from CircuitAIBot.ConfigurationHandler import ConfigurationHandler


class ChannelUtils:

    async def manageTemporaryVoiceChannel(self, member, before, after, config):

        if before.channel is not None:
            guildConfig = config[str(before.channel.guild.id)]
            if str(guildConfig["vcStartCategory"]) != "0" or str(guildConfig["vcStartChannelId"]) != "0":
                if str(before.channel.category.id) == str(guildConfig["vcStartCategory"]) and len(
                        before.channel.members) == 0 and str(guildConfig["vcStartChannelId"]) != str(before.channel.id):
                    if len(before.channel.members) == 0:
                        await before.channel.delete()
            else:
                print("Config noch nicht vorhanden")

        if after.channel is not None:
            guildConfig = config[str(after.channel.guild.id)]
            if str(guildConfig["vcStartCategory"]) != "0" or str(guildConfig["vcStartChannelId"]) != "0":

                if str(after.channel.category.id) == str(guildConfig["vcStartCategory"]) and str(
                        guildConfig["vcStartChannelId"]) == str(after.channel.id):
                    tmpcat = after.channel.category
                    channel = await tmpcat.create_voice_channel(member.name + "'s Voice Chat")
                    await channel.set_permissions(member, manage_channels=True)
                    await member.move_to(channel)

    async def chageAgeRestrictionOnChannel(self, before, after, config):

        guildConfig = config[str(after.channel.guild.id)]
        adultRoleName = str(guildConfig["adultRole"]);

        if adultRoleName != "0":
            # Change to USK 18
            if str(after.category) == str(guildConfig["vcStartCategory"]) and "18" in str(after.name) and not "18" in str(before.name):
                roles = after.guild.roles
                for role in roles:
                    if role.id == adultRoleName:
                        await after.set_permissions(role, view_channel=True)
                    elif 1==0:
                        await after.set_permissions(role, view_channel=False)

            if str(after.category) == "TEMP VC" and "18" in str(before.name) and "18" not in str(after.name):
                roles = after.guild.roles
                for role in roles:
                    print(str(role.name), str(role.id), "To Normal")
                    if role.name == adultRoleName:
                        adultRole = role
                        if role.name == "@everyone":
                            everyoneRole = role;
                            await after.set_permissions(everyoneRole, view_channel=True)

    def loadGuildConfig(self, config, guildId):
        return config[str(guildId)]

    async def autoconfig(self, guild):
        tmpcat = await guild.create_category("TempVC")
        tmpStartChannel = await tmpcat.create_voice_channel("StartTempVc")
        ConfigurationHandler().setvcStartCategory(tmpcat.id, guild.id)
        ConfigurationHandler().setvcStartChannelId(tmpStartChannel.id, guild.id)


    async def setTempStartChannel(self, message):
        cmdContent = message.content.split(" ")
        targetChannel = message.guild.get_channel(int(cmdContent[1]))
        if targetChannel.category is not None:
            if cmdContent[1] in str(message.guild.channels):
                ConfigurationHandler().setvcStartChannelId(cmdContent[1], str(message.guild.id))

                ConfigurationHandler().setvcStartCategory(str(targetChannel.category.id), str(message.guild.id))
                await message.channel.send("Saved")
            else:
                await message.channel.send("Channel ID not in Guild")
        else:
            await message.channel.send("Fatal error channel not in a category")
