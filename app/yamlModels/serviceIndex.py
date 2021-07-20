import yaml
from .. import statics

class ServiceIndex(yaml.YAMLObject):
    yaml_tag = '!ServiceIndex'

    def __init__(self):
        self.harnessApiVersion = '1.0'
        self.type = 'SERVICE'
        self.artifactType = 'DOCKER'
        self.deploymentType = 'KUBERNETES'
        self.helmVersion = 'V3'

def CreateServiceIndex():
    yamlData = CreateServiceIndexYaml()
    path = statics.pathBuilder(statics.MakeDirList.serviceBasePath)
    filename = statics.indexFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateServiceIndexYaml():
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(ServiceIndex(),sort_keys=False)
