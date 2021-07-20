from . import statics
from . import createFiles
from . import InputData
import sys

def main():
    if(len(sys.argv) > 2):
        data = InputData.GetInputDataFromArguments(sys.argv)
    else:
        data = InputData.GetInputDataFromJson()

    statics.setGlobals(data.envName, data.repoSlug)
    createFiles.CreateAllFiles(data)