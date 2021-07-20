import yaml
from .. import statics

class EnvironmentIndex(yaml.YAMLObject):
    yaml_tag = '!EnvironmentIndex'

    def __init__(self):
        self.harnessApiVersion = '1.0'
        self.type = 'ENVIRONMENT'
        self.configMapYamlByServiceTemplateName = {}
        self.description = ' '
        self.environmentType = 'NON_PROD'

def CreateEnvironmentIndex():
    yamlData = CreateEnvironmentIndexYaml()
    path = statics.pathBuilder(statics.MakeDirList.envDefPath)
    filename = statics.indexFilename
    statics.CreateFullFile(path,yamlData,filename)  

def CreateEnvironmentIndexYaml():
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(EnvironmentIndex(),sort_keys=False)