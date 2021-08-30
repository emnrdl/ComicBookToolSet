import bpy
from . exlib import ShowMessageBox
from bpy.types import Operator


class add_bbox_OT_Operator(Operator):
    
    bl_idname = 'add.bbox'
    bl_label = 'Add BBOX'
    bl_description = 'Create a bounding box for selected meshes'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):


        return{'FINISHED'}