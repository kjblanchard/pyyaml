import yaml
from .. import statics

class RepoSlugValues(yaml.YAMLObject):
    yaml_tag = '!RepoSlugValues'

    def __init__(self, commonName, env):
        self.istio = self.Istio(commonName,env)


    class Istio(yaml.YAMLObject):
        def __init__(self,commonName, env):
            self.hostname = f'{commonName}.{env}.uwm.com'

def CreateRepoSlugValues(commonName, env):
    yamlData = CreateRepoSlugValuesYaml(commonName,env)
    path = statics.pathBuilder(statics.MakeDirList.envRepoSlugPath)
    filename = statics.valuesFilename
    statics.CreateFullFile(path,yamlData,filename)

def CreateRepoSlugValuesYaml(commonName, env):
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(RepoSlugValues(commonName,env),sort_keys=False)
