class Config:
    def getConfigPath(self):
        serverConfigFile=open("/env/batbot/config.txt", "r")
        return serverConfigFile.read()
