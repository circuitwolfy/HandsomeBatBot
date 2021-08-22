from CircuitAIBot.CircuitAiJsonFileHandler import CircuitAiJsonFileHandler

configFilePath = "config_Files/serverTempVcConfig.json"


class ConfigurationHandler:

    def loadConfig(self):
        return None

    def createNewGuildConfig(self, guildId):
        updateSet = self.createDictForTempVc(guildId, "0", "0", "0", "0","~")
        CircuitAiJsonFileHandler().addJsonSet(configFilePath, updateSet)

    def createDictForTempVc(self, serverId, normalRole, adultRole, vcStartChannelId, vcStartCategory,prefix):
        serverConfigInternalStruct = {
            "id": serverId,
            "normalRole": normalRole,
            "adultRole": adultRole,
            "vcStartChannelId": vcStartChannelId,
            "vcStartCategory": vcStartCategory,
            "prefix": prefix,
        }

        serverConfigStruct = {
            serverId: serverConfigInternalStruct
        }
        return serverConfigStruct

    def updateconfig(self, config):
        CircuitAiJsonFileHandler().overwriteJasonFile(configFilePath, config)

    def setnormalRole(self, normalRole, guildid):
        config = self.loadConfig()
        config[str(guildid)]["normalRole"] = normalRole
        self.updateconfig(config)

    def setadultRole(self, adultRole, guildid):
        config = self.loadConfig()
        config[str(guildid)]["adultRole"] = adultRole
        self.updateconfig(config)

    def setvcStartChannelId(self, vcStartChannelId, guildid):
        config = self.loadConfig()
        config[str(guildid)]["vcStartChannelId"]+=vcStartChannelId
        self.updateconfig(config)

    def removeVcStartChannelId(self, vcStartChannelId, guildid):
        config = self.loadConfig()
        config[str(guildid)]["vcStartChannelId"]-= vcStartChannelId
        self.updateconfig(config)

    def setvcStartCategory(self, vcStartCategory, guildid):
        config = self.loadConfig()

        config[str(guildid)]["vcStartCategory"] = vcStartCategory
        self.updateconfig(config)

    def setprefix(self, prefix, guildid):
        config = self.loadConfig()
        config[str(guildid)]["prefix"] = prefix
        self.updateconfig(config)

