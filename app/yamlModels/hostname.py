import yaml
from .. import statics
class Hostname(yaml.YAMLObject):
    yaml_tag = '!Hostname'

    def __init__(self,infrastructureKey, projectKey, serviceName):
        self.harnessApiVersion = '1.0'
        self.type = 'INFRA_DEFINITION'
        self.cloudProviderType = 'KUBERNETES_CLUSTER'
        self.deploymentType = 'KUBERNETES'
        self.infrastructure = self.infrastructure(infrastructureKey, projectKey, serviceName)

    class infrastructure(yaml.YAMLObject):
        def __init__(self, infrastructureName, projectKey, serviceName):
            self.type = 'DIRECT_KUBERNETES'
            self.cloudProviderName: infrastructureName
            self.namespace = f'uwm-{projectKey}'
            self.releaseName = f'{serviceName}'

def CreateHostname(hostname, infrastructureName, projectKey, serviceName):
    yamlData = CreateHostnameYaml(infrastructureName, projectKey, serviceName)
    path = statics.pathBuilder(statics.MakeDirList.infDefPath)
    filename = f'{hostname}.yaml'
    statics.CreateFullFile(path,yamlData,filename)


def CreateHostnameYaml(infrastructureName, projectKey, serviceName):
    yaml.emitter.Emitter.process_tag = statics.noopToRemoveOutput
    return yaml.dump(Hostname(infrastructureName, projectKey, serviceName),sort_keys=False)