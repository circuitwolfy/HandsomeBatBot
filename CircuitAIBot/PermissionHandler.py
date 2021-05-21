from CircuitAIBot.CircuitAiJsonFileHandler import CircuitAiJsonFileHandler

filePath = "config_Files/botAdminUser.json"


class PermissionHandler:

    def getPermsFromJson(self):
        return CircuitAiJsonFileHandler().loadJason(filePath)

    def chckperms(self, message):
        savedRoles = self.getPermsFromJson()
        userRoles = message.author.roles
        for role in userRoles:
            if role.permissions.administrator:
                return True
            if str(role.id) in str(savedRoles):
                return True
            if message.author.id == message.guild.owner_id:
                return True

        return False

    def addPermitRole(self, role):

        if str(role.id) not in str(self.getPermsFromJson()):
            roleIDStruct = {role.id: role.id}
            CircuitAiJsonFileHandler().addJsonSet(filePath, roleIDStruct)

    def removePermitRole(self, role):
        permits = self.getPermsFromJson()
        if str(role.id) in str(self.getPermsFromJson()):
          del permits[str(role.id)]

        CircuitAiJsonFileHandler().overwriteJasonFile(filePath,permits)



