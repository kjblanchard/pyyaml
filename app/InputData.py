import json

class InputData(object):
    def __init__(self, typeOfApp, hostname, infrastructureName, projectKey, serviceName, commonName, env, certSecretName, artifactMetadataImage, envName, repoSlug):
        self.typeOfApp = typeOfApp
        self.hostname = hostname
        self.infrastructureName = infrastructureName
        self.projectKey = projectKey
        self.serviceName = serviceName
        self.commonName = commonName
        self.env = env
        self.certSecretName = certSecretName
        self.artifactMetadataImage = artifactMetadataImage
        self.envName = envName
        self.repoSlug = repoSlug

#Use this if you want to pass in the args on the cli, make sure that you use the correct operator in the constructor above
def GetInputDataFromArguments(argv):
    return InputData(argv[1],argv[2],argv[3],argv[4],argv[5],argv[6],argv[7],argv[8],argv[9],argv[10],argv[11])

#Read from the jsonData.json file, and load from the json based on the keys, allows you to use a json webhook
def GetInputDataFromJson():
        with open('jsonData.json', "r") as file:
             obj = file.read()
        obj = json.loads(obj)
        return InputData(
            obj['typeOfApp'], obj['hostname'], obj['infrastructureName'], obj['projectKey'], obj['serviceName'],obj['commonName'],
                obj['env'], obj['certSecretName'], obj['artifactMetadataImage'], obj['envName'], obj['repoSlug'])