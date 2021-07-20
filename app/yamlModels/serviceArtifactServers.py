import yaml
from .. import statics

class ServiceArtifactServers(yaml.YAMLObject):
    yaml_tag = '!Hostname'

    def __init__(self, projectKey, repoSlug):
        self.harnessApiVersion = '1.0'
        self.type = 'DOCKER'
        self.imageName = f'docker-local-virtual/{projectKey}/{repoSlug}'
        self.serverName = 'UWM Docker - Artifactory'

def CreateServiceArtifactServers(projectKey, repoSlug):
    yamlData = CreateArtifactServiceYaml(projectKey,repoSlug)
    path = statics.pathBuilder(statics.MakeDirList.serviceArtifactPath)
    filename = f'docker-local-virtual_{projectKey}_{repoSlug}.yaml'
    statics.CreateFullFile(path,yamlData,filename)

def CreateArtifactServiceYaml(projectKey,repoSlug):
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(ServiceArtifactServers(projectKey,repoSlug),sort_keys=False)