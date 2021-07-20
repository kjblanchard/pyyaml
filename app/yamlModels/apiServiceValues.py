import yaml
from .. import statics

class ApiServiceValues(yaml.YAMLObject):
    yaml_tag = '!Hostname'

    def __init__(self, commonName, certSecretName, artifactMetadataImage, envName):
        self.framework = 'dotnet'
        self.partOf = commonName
        self.istio = ApiServiceValues.istio(certSecretName)
        self.image = ApiServiceValues.image(artifactMetadataImage)
        self.createNamespace = True
        self.service = ApiServiceValues.service()
        self.containerPort = ApiServiceValues.containerPort()
        self.env = ApiServiceValues.env(envName)

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

def CreateApiServiceValues(commonName, certSecretName, artifactMetadataImage, envName):
    yamlData = CreateApiServiceValuesYaml(commonName,certSecretName,artifactMetadataImage,envName)
    path = statics.pathBuilder(statics.MakeDirList.serviceValuesPath)
    filename = statics.valuesFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateApiServiceValuesYaml(commonName,certSecretName,artifactMetadataImage,envName):
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(ApiServiceValues(commonName, certSecretName, artifactMetadataImage, envName),sort_keys=False)