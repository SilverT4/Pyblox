__doc__ = """Common application data. Contains data about packages, etc."""
from types import MappingProxyType
from .._pyutils.path import tools, JoinPaths
class CommonAppData:
    _commonMap = MappingProxyType({
        "Libraries.zip": "",
        "redist.zip": "",
        "shaders.zip": "shaders/",
        "ssl.zip": "ssl/",
        "WebView2.zip": "",
        "WebView2RuntimeInstaller.zip": "WebView2RuntimeInstaller/",
        "content-avatar.zip": "content/avatar/",
        "content-configs.zip": "content/configs/",
        "content-fonts.zip": "content/fonts/",
        "content-sky.zip": "content/sky/",
        "content-sounds.zip": "content/sounds/",
        "content-textures2.zip": "content/textures/",
        "content-models.zip": "content/models/",
        "content-textures3.zip": "PlatformContent/pc/textures/",
        "content-terrain.zip": "PlatformContent/pc/terrain/",
        "content-platform-fonts.zip": "PlatformContent/pc/fonts/",
        "content-platform-dictionaries.zip": "PlatformContent/pc/shared_compression_dictionaries/",
        "extracontent-luapackages.zip": "ExtraContent/LuaPackages/",
        "extracontent-translations.zip": "ExtraContent/translations/",
        "extracontent-models.zip": "ExtraContent/models/",
        "extracontent-textures.zip": "ExtraContent/textures",
        "extracontent-places.zip": "ExtraContent/places/"
    })

    @property
    def ExecutableName(self) -> str:
        raise NotImplementedError("This value must be overridden by subclasses.")
    
    Directory = JoinPaths(tools.BaseDirectory, "Roblox", "Player")
    ExecutablePath = JoinPaths(Directory, ExecutableName)

    PackageDirectoryMap = None
    def __init__(self):
        if self.PackageDirectoryMap is None:
            self.PackageDirectoryMap = self._commonMap
            return
        merged = {}

        for key, value in self._commonMap.items():
            merged[key] = value
        
        for key, value in self.PackageDirectoryMap.items():
            merged[key] = value

        self.PackageDirectoryMap = merged