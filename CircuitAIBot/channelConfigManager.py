from CircuitAIBot.CircuitAiJsonFileHandler import CircuitAiJsonFileHandler

class ChannelConfigManager:
    def loadConfigFromJSON(self):
        return CircuitAiJsonFileHandler().loadJason("config_Files/ChannelConfig.json")

    def saveConfigFromJSON(self, content):
        CircuitAiJsonFileHandler.overwriteJasonFile("config_Files/ChannelConfig.json", content)

    def getStartChannels(self):
        pass
    def addStartChannels(self):
        pass
    def removeStartChannels(self):
        pass
    def getActiveTempChannel(self):
        pass
    def addActiveTempChannel(self):
        pass
    def removeActiveTempChannel(self):
        pass
