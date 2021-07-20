import yaml
from .. import statics

class ServiceManifestIndex(yaml.YAMLObject):
    yaml_tag = '!ServiceManifestIndex'

    def __init__(self):
        self.harnessApiVersion = '1.0'
        self.type = 'APPLICATION_MANIFEST'
        self.gitFileConfig = self.GitFileConfig()
        self.storeType = 'HelmSourceRepo'

    class GitFileConfig(yaml.YAMLObject):
        def __init__(self):
            self.branch = 'develop'
            self.connectorName = 'UWM Code - YAML Templates'
            self.filePath = 'base'
            self.useBranch = True
            self.useInlineServiceDefinition = False

def CreateServiceManifestIndex():
    yamlData = CreateServiceManifestYaml()
    path = statics.pathBuilder(statics.MakeDirList.serviceManifestPath)
    filename = statics.indexFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateServiceManifestYaml():
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(ServiceManifestIndex(),sort_keys=False)
