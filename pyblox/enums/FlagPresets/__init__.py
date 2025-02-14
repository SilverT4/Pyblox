from enum import Enum

class InGameMenuVersion(Enum):
    Default = 0
    V1 = 1
    V2 = 2
    V4 = 3
    V4Chrome = 4

class LightingMode(Enum):
    Default = 0
    Voxel = 1
    ShadowMap = 2
    Future = 3

class MSAAMode(Enum):
    Default = 0
    x1 = 1
    x2 = 2
    x4 = 3

class RenderingMode(Enum):
    Default = 0
    D3D11 = 1
    D3D10 = 2

class TextureQuality(Enum):
    Default = 0
    Level0 = 1
    Level1 = 2
    Level2 = 3
    Level3 = 4

