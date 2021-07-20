import yaml
from .. import statics

class RepoSlugIndex(yaml.YAMLObject):
    yaml_tag = '!Hostname'

    def __init__(self):
        self.harnessApiVersion = '1.0'
        self.type = 'APPLICATION_MANIFEST_VALUES_ENV_SERVICE_OVERRIDE'
        self.storeType = 'Local'


def CreateRepoSlugIndex():
    yamlData = CreateRepoSlugIndexYaml()
    path = statics.pathBuilder(statics.MakeDirList.envRepoSlugPath)
    filename = statics.indexFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateRepoSlugIndexYaml():
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(RepoSlugIndex(),sort_keys=False)
