__doc__ = """module to deal with joining paths and whatnot"""
from os import getenv, getcwd, path
import sys
from pathlib import Path

GetEnvironmentVariable = getenv

def JoinPaths(path1:str, *path2:str):
    return Path(path1, *path2)

class PathTools:
    def __init__(self, baseDirectory:str):
        self.BaseDirectory = baseDirectory
        self.Downloads = JoinPaths(baseDirectory, "Downloads")
        self.Logs = JoinPaths(baseDirectory, "Logs")
        self.Integrations = JoinPaths(baseDirectory, "Integrations")
        self.Versions = JoinPaths(baseDirectory, "Versions")
        self.Modifications = JoinPaths(baseDirectory, "Modifications")
        self.Application = JoinPaths(baseDirectory, "pyblox.py")
        self.UserProfile = Path("~").expanduser()
        self.LocalAppData = JoinPaths(self.UserProfile, "Local Settings")
        self.Desktop = JoinPaths(self.UserProfile, "Desktop")
        self.WindowsStartMenu = JoinPaths(self.UserProfile, "Application Data", "Microsoft", "Windows", "Start Menu", "Programs")
        self.Temp = JoinPaths(getenv("TEMP"), "Pyblox")
        self.TempUpdates = JoinPaths(self.Temp, "Updates")
        self.TempLogs = JoinPaths(self.Temp, "Logs")
        self.CustomFont = JoinPaths(self.Modifications, "content", "fonts", "CustomFont.ttf")

    @property
    def Process(self):
        return path.abspath(sys.executable)
    
    @Process.getter
    def Process(self):
        return path.abspath(sys.executable)
    
    @Process.setter
    def Process(self, x):
        raise SystemError("Process executable path cannot be changed through running script. To change, please reinstall Python or Pyblox.")
    
    @Process.deleter
    def Process(self):
        raise NotImplementedError("Cannot unset executable path")
    @property
    def isInitialized(self):
        return self.BaseDirectory is not None
    
    @property
    def CurrentDirectory(self):
        """The current working directory. This is equivalent to `os.chdir`"""
        return

    @CurrentDirectory.getter
    def CurrentDirectory(self) -> Path:
        return Path(".").resolve()
    
    @CurrentDirectory.setter
    def CurrentDirectory(self, x):
        raise SystemError(
            f"Current directory must be set using `os.chdir`. Attempting to set CurrentDirectory would not update the current directory as intended."
            )
    
    @CurrentDirectory.deleter
    def CurrentDirectory(self):
        raise SystemError("Current directory variable cannot be deleted.")
    

tools = PathTools(Path("~/Local Settings/Pyblox").expanduser())