from enum import Enum
import os


#Statics that never change
basePath = 'TemplateFolder'
environmentsPath = 'Environments'
infrastructureDefinitionsPath = 'Infrastructure Definitions'
servicesPath = 'Services'
serviceArtifactServers = 'Artifact Servers'
serviceManifests = 'Manifests'
valuesPath = 'Values'
indexFilename = 'Index.yaml'
valuesFilename = 'values.yaml'
environmentName = ''
repoSlug = ''

def setGlobals(environment, slug):
    global environmentName
    global repoSlug
    environmentName = environment
    repoSlug = slug


#Used by all the models to remove the output in the yaml
def noopToRemoveOutput(self, *args, **kw):
    pass

def pathBuilder(makeDirEnum):
    enumVal = makeDirEnum.value
    if(enumVal == MakeDirList.envDefPath.value):
        return f'{basePath}/{environmentsPath}/{environmentName}'
    elif(enumVal == MakeDirList.envRepoSlugPath.value):
        return f'{basePath}/{environmentsPath}/{environmentName}/{valuesPath}/{servicesPath}/{repoSlug}'
    elif(enumVal == MakeDirList.infDefPath.value):
        return f'{basePath}/{environmentsPath}/{environmentName}/{infrastructureDefinitionsPath}'
    elif(enumVal == MakeDirList.serviceBasePath.value):
        return f'{basePath}/{servicesPath}/{repoSlug}'
    elif(enumVal == MakeDirList.serviceArtifactPath.value):
        return f'{basePath}/{servicesPath}/{repoSlug}/{serviceArtifactServers}'
    elif(enumVal == MakeDirList.serviceManifestPath.value):
        return f'{basePath}/{servicesPath}/{repoSlug}/{serviceManifests}'
    elif(enumVal == MakeDirList.serviceValuesPath.value):
        return f'{basePath}/{servicesPath}/{repoSlug}/{valuesPath}'

#Enum to reference when you are making your path
class MakeDirList(Enum):
    envDefPath = 0
    envRepoSlugPath = 1
    infDefPath = 2
    serviceBasePath = 3
    serviceArtifactPath = 4 
    serviceManifestPath = 5
    serviceValuesPath = 6

def CreateFullFile(path, yamlData, filename):
    CreateDirectory(path)
    CreateFile(yamlData,path,filename)

def CreateFile(yamlDataToWrite, pathToWrite, filename):
    with open(f'{pathToWrite}/{filename}', "w+") as file:
        file.write(yamlDataToWrite)

def CreateDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)
