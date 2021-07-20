import yaml
from .. import statics

class ValuesValues(yaml.YAMLObject):
    yaml_tag = '!Hostname'

    def __init__(self, commonName, certSecretName, artifactMetadataImage, envName):
        self.framework = 'dotnet'
        self.partOf = commonName
        self.istio = ValuesValues.istio(certSecretName)
        self.image = ValuesValues.image(artifactMetadataImage)
        self.createNamespace = True
        self.service = ValuesValues.service()
        self.containerPort = ValuesValues.containerPort()
        self.env = ValuesValues.env(envName)

    class istio(yaml.YAMLObject):
        def __init__(self, certSecretName):
            self.enabled = True
            self.tls = True
            self.tlsCredentialName = certSecretName
            self.subPath = '/api'
    class image(yaml.YAMLObject):
        def __init__(self,artifactMetadataImage):
            self.url = artifactMetadataImage
    class service(yaml.YAMLObject):
        def __init__(self):
            self.type = 'ClusterIP'
    class containerPort(yaml.YAMLObject):
        def __init__(self):
            self.port = 5000
    class env(yaml.YAMLObject):
        def __init__(self, envName):
            self.ASPNETCORE_ENVIRONMENT = envName

def CreateValuesValues(commonName, certSecretName, artifactMetadataImage, envName):
    yamlData = CreateServiceValuesYaml(commonName,certSecretName,artifactMetadataImage,envName)
    path = statics.pathBuilder(statics.MakeDirList.serviceValuesPath)
    filename = statics.valuesFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateServiceValuesYaml(commonName,certSecretName,artifactMetadataImage,envName):
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(ValuesValues(commonName, certSecretName, artifactMetadataImage, envName),sort_keys=False)