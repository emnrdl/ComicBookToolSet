import bpy
from bpy.props import (
    StringProperty,
    BoolProperty,
    IntProperty,
    FloatProperty,
    EnumProperty
)
from bpy.types import (
    Panel,
    Operator,
    AddonPreferences,
    PropertyGroup
)


class MyProperties(PropertyGroup):

    path : StringProperty(
        name="Dir Path",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='FILE_PATH')
