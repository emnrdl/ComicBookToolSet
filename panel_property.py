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


class PG_MyProperties(PropertyGroup):

    path : StringProperty(
        name="Dir Path",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
        )
    
    charlist : EnumProperty(
        name="Character List:",
        description="Apply Data to attribute.",      
        items=[ ('OP1', "Male Character",""),
                ('OP2', "Female Character","")
                ]
        )