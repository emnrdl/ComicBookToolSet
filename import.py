import bpy
from bpy.types import Operator
import json
from . exlib import ShowMessageBox

class Import_Camera_With_JSON_OT_Operator(Operator):

    bl_idname = 'import.camerawithjson'
    bl_label = 'Import camera with json '
    bl_description = 'Import camera with json '

    def execute(self, context):
        
        
        return{'FINISHED'}