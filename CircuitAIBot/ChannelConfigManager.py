from CircuitAIBot.CircuitAiJsonFileHandler import CircuitAiJsonFileHandler


# Loads and saves the definde JSon Configs. IDs are saved in an array.

class ChannelConfigManager:
    def loadConfigFromJSON(self):
        return CircuitAiJsonFileHandler().loadJason("config_Files/ChannelConfig.json")

    def saveConfigFromJSON(self, content):

        CircuitAiJsonFileHandler().overwriteJasonFile("config_Files/ChannelConfig.json", content)

    def getStartChannels(self):
        config = self.loadConfigFromJSON()
        return config["ChannelIDs"]["startChannel"]["id"]

    def addStartChannels(self ,id):
        tmepChannel = self.getStartChannels()
        if (id in tmepChannel):
            return False
        else:
            tmepChannel.append(id)
            self.saveChangeSet(tmepChannel, "startChannel")
            return True

    def removeStartChannels(self, id):
        tmepChannel = self.getStartChannels()
        if (id in tmepChannel):
            tmepChannel.remove(id)
            self.saveChangeSet(tmepChannel, "startChannel")
            return True
        else:
            return False

    def getActiveTempChannel(self):
        config = self.loadConfigFromJSON()
        return config["ChannelIDs"]["activeTemp"]["id"]

    def addActiveTempChannel(self, id):
        tmepChannel = self.getActiveTempChannel()
        if (id in tmepChannel):
            return False
        else:
            tmepChannel.append(id)
            self.saveChangeSet(tmepChannel, "activeTemp")
            return True

    def removeActiveTempChannel(self, id):
        tmepChannel = self.getActiveTempChannel()
        if (id in tmepChannel):
            tmepChannel.remove(id)
            self.saveChangeSet(tmepChannel, "activeTemp")
            return True
        else:
            return False

    def saveChangeSet(self, changeset, changeType):
        config = self.loadConfigFromJSON()
        config["ChannelIDs"][changeType]["id"] = changeset
        self.saveConfigFromJSON(config)