Yaml generator for harness
Can take in cli params for them, or can also have a json file to read them from

Build the app by running pyinstaller harnessYamlGenerator.py --onefile
Note, to create a windows.exe you will run pyinstaller in powershell, and for a linux executable you will run
pyinstaller on linux.  pyinstaller is not cross-compilable, so it builds the executable based on which you run.

For powershell, pyinstaller is probably not in your python path, so either add it or run pyinstaller from the
proper directory
C:\Users\%USERNAME%\AppData\Roaming\Python\Python39\Scripts\pyinstaller.exe