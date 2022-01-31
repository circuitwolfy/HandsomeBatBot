import discord


class HelpCommand:
   def sendHelpText(self, exportChannel):
        helpMessage=discord.Embed()
        helpMessage.title="CiPrOs Automation help page"
        helpMessage.color=discord.Colour.teal()
        helpMessage.add_field(name="~info", value="Sends the Bot Serverstatus", inline=False)
        helpMessage.add_field(name="~pat", value="Give the bot a pat! They're a good machine", inline=False)
        helpMessage.add_field(name="~addrole", value="~addRole <@ROLE> \n (Admin Command) Adds a Role and grants Admin privileges for this bot.", inline=False)
        helpMessage.add_field(name="~removerole", value="~removerole <@ROLE> \n (Admin Command) removes a Role and revokes the Admin privileges for this bot.", inline=False)
        helpMessage.add_field(name="~addstartchannel", value="~addstartchannel <channel_ID> \n (Admin Command) Adds the selected Channel as a start channel for Temporary VCs "
                                                             "the rights on the start Channel get copyed and the creator gets the MANAGE_CHANNEL=TRUE permission ", inline=False)
        helpMessage.add_field(name="~mathGame", value="Starts a Minigame to train your brain!", inline=False)

        return helpMessage
