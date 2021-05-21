import json

class CircuitAiJsonFileHandler:

    def overwriteJasonFile(self, jsonFilePath, content):
        a_file = open(jsonFilePath, "w")
        json.dump(content, a_file)
        a_file.close()

    def loadJason(self, jsonFilePath):
        with open(jsonFilePath) as fileData:
            dataStruct = json.load(fileData)

        return dataStruct

    def addJsonSet(self, jsonFilePath, updateSet):
        with open(jsonFilePath, "r+") as file:
            data = json.load(file)
            data.update(updateSet)
            file.seek(0)
            json.dump(data, file)
