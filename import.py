import bpy
import json
from . exlib import ShowMessageBox

class open_work_dir_OT_Operator(Operator):

    bl_idname = 'import.'
    bl_label = 'Opens the work directory'
    bl_description = 'Opens the work directory'

    def execute(self, context):
        
        
        return{'FINISHED'}