import yaml
from .. import statics

class ValuesIndex(yaml.YAMLObject):
    yaml_tag = '!ValuesIndex'

    def __init__(self):
        self.harnessApiVersion = '1.0'
        self.type = 'APPLICATION_MANIFEST'
        self.storeType = 'Local'
    
def CreateValuesIndex():
    yamlData = CreateServiceValuesIndexYaml()
    path = statics.pathBuilder(statics.MakeDirList.serviceValuesPath)
    filename = statics.indexFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateServiceValuesIndexYaml():
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(ValuesIndex(),sort_keys=False)
