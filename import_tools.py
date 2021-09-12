import bpy
from bpy.types import Operator
import json
from . exlib import ShowMessageBox
import os, fnmatch

class Import_Camera_With_JSON_OT_Operator(Operator):

    bl_idname = 'import.camerawithjson'
    bl_label = 'Import camera with json '
    bl_description = 'Import camera with json '

    def execute(self, context):
        
        path = str(bpy.context.scene.my_tool.path)

        f = open(path)
        data = json.load(f)


        for cam in data:
            
            cam_name  = cam['name']
            camera_data = bpy.data.cameras.new(name=cam_name)
            camera_object = bpy.data.objects.new(cam_name, camera_data)
            bpy.context.scene.collection.objects.link(camera_object)

            camera_object['Resolution_X'] = cam['resolutionX']            
            camera_object['Resolution_Y'] = cam['resolutionY']

            camera_object.matrix_world = cam['transform']


#        bpy.ops.wm.alembic_import(filepath=alembic_file[0], 
#            scale=1.0, set_frame_range=True,
#            as_background_job=False)

        f.close()

        return{'FINISHED'}