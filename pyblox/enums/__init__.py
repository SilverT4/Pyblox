__doc__ = """Contains all the Enums as Python equivalents of Bloxstrap's C# enums."""
from enum import Enum
from . import FlagPresets
class Theme(Enum):
    Default = 0
    Light = 1
    Dark = 2

class NextAction(Enum):
    Terminate = 0
    LaunchSettings = 1
    LaunchRoblox = 2
    LaunchRobloxStudio = 3

class ServerType(Enum):
    Public = 0
    Private = 1
    Reserved = 2

class CursorType(Enum):
    Default = 1
    From2006 = 3
    From2013 = 2

class ErrorCode(Enum):
    # https://learn.microsoft.com/en-us/windows/win32/msi/error-codes
    # https://i-logic.com/serial/errorcodes.htm
    # https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/705fb797-2175-4a90-b5a3-3918024b10b8
    # just the ones that we're interested in
    ERROR_SUCCESS = 0
    ERROR_INVALID_FUNCTION = 1
    ERROR_FILE_NOT_FOUND = 2
    ERROR_CANCELLED = 1223
    ERROR_INSTALL_USEREXIT = 1602
    ERROR_INSTALL_FAILURE = 1603
    CO_E_APPNOTFOUND = -2147221003

class GenericTriState(Enum):
    Successful = 0
    Failed = 1
    Unknown = 2

class VersionComparison(Enum):
    LessThan = -1
    Equal = 0
    GreaterThan = 1

class LaunchMode(Enum):
    None_ = 0
    Player = 1
    Studio = 2
    StudioAuth = 3

class EmojiType(Enum):
    Default = 0
    Catmoji = 1
    Windows11 = 2
    Windows10 = 3
    Windows8 = 4

class BootstrapperIcon(Enum):
    IconPyblox = 0
    Icon2008 = 1
    Icon2011 = 2
    IconEarly2015 = 3
    IconLate2015 = 4
    Icon2017 = 5
    Icon2019 = 6
    Icon2022 = 7
    IconCustom = 8

class BootstrapperStyle(Enum):
    VistaDialog = 0
    LegacyDialog2008 = 1
    LegacyDialog2011 = 2
    ProgressDialog = 3
    ClassicFluentDialog = 4
    ByfronDialog = 5
    FluentDialog = 6
    FluentAeroDialog = 7

