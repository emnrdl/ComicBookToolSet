import bpy
import json
from bpy.types import Operator
from . exlib import ShowMessageBox



class set_camera_active_OT_Operator(Operator):

    bl_idname = 'import.cameprop'
    bl_label = 'Import camera property from json'
    bl_description = 'Import camera property from json'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
           
        active = bpy.context.active_object
        scene = bpy.data.scenes['Scene']

        json.load


        if bpy.context.active_object.type == 'CAMERA':
            bpy.context.scene.camera = active
            if 'Resolution_X' in active:
                scene.render.resolution_x = active['Resolution_X']
                scene.render.resolution_y = active['Resolution_Y']
        else:
            ShowMessageBox("Select 'Camera' type object","ERROR",'ERROR')


        return{'FINISHED'}