from .yamlModels import hostname as hostnameImport
from .yamlModels import environmentIndex as environmentImport
from .yamlModels import repoSlugIndex as repoSlugImport
from .yamlModels import repoSlugValues as repoSlugValuesImport
from .yamlModels import serviceIndex as serviceIndexImport
from .yamlModels import serviceArtifactServers as serviceArtifactImport
from .yamlModels import serviceManifestIndex as serviceManifestImport
from .yamlModels import valuesIndex as valuesIndexImport
from .yamlModels import apiServiceValues as apiServiceValuesImport
from .yamlModels import valuesValues as valuesValuesImport

def CreateAllFiles(data):
    hostnameImport.CreateHostname(data.hostname, data.infrastructureName, data.projectKey, data.serviceName)
    environmentImport.CreateEnvironmentIndex()
    repoSlugImport.CreateRepoSlugIndex()
    repoSlugValuesImport.CreateRepoSlugValues(data.commonName, data.env)
    serviceIndexImport.CreateServiceIndex()
    serviceArtifactImport.CreateServiceArtifactServers(data.projectKey, data.repoSlug)
    serviceManifestImport.CreateServiceManifestIndex()
    valuesIndexImport.CreateValuesIndex()
    if(data.typeOfApp == 'api'):
        apiServiceValuesImport.CreateApiServiceValues(data.commonName,data.certSecretName,data.artifactMetadataImage,data.envName)
    elif(data.typeOfApp == 'webui'):
        valuesValuesImport.CreateValuesValues(data.commonName,data.certSecretName,data.artifactMetadataImage,data.envName)