import bpy
import os
import json
import numpy as np
from bpy_types import Operator
from . path_lib  import get_path
from . exlib import ShowMessageBox, create_dir


class export_all_camera_OT_Operator(Operator):

    bl_idname = 'export.camera'
    bl_label = 'Export all cameras as alembic'
    bl_description = 'Export all cameras as alembic in current frame'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        if bpy.data.is_saved:
            bpy.ops.object.select_all(action='DESELECT')
            
            for obj in bpy.context.scene.objects:
                if obj.type == 'CAMERA':
                    obj.select_set(True)

            selected = bpy.context.selected_objects
            if len(selected) == 0:
            
                ShowMessageBox('There is no camera in the scene','ERROR','ERROR')
            
            else:                            
                
                #path and naming create

                version = 1
                name = get_path.fullname() 
                path = get_path.file_path()
                dir = path + 'camera' + '/' + 'Cams_' + 'v00' + str(version)
   
                
                while os.path.isdir(dir):
                    version += 1 
                    dir = path + 'camera' + '/' + 'Cams_' + 'v00' + str(version) 

                jsonpath = dir + '/' + name + '_' + 'cameras' + '.json'
                export_path = dir + '/' + name + '_' + 'cameras' + ".abc"               
                #---------------------------------------------------                
                
                #dict create
                cams = []
                nonrescams_name = []
                nonrescams = []
                camprops = {}

                for cam in selected:
                    camname = cam.name
                    
                    if 'Resolution_X' and 'Resolution_Y' in cam:
                        
                        resolutionX = cam['Resolution_X']
                        resolutionY = cam['Resolution_Y']
                        transform = np.array(cam.matrix_world)
                        
                        #cam property dict
                        
                        camprops = {
                        'name': camname,
                        'transform': transform.tolist(),
                        'resolutionX': resolutionX,
                        'resolutionY': resolutionY
                    }

                        cams.append(camprops)

                    else:
                        nonrescams_name.append(camname)
                        nonrescams.append(cam)
                #---------------------------------------------------

                #Export
                if len(nonrescams) == 0:

                    create_dir(dir)
                    
                    #Export as a json file in output directory
                    with open(jsonpath, 'w', encoding='utf-8') as  outfile:
                        json.dump(cams, outfile, sort_keys=True, indent=4)

                    #Export as a Alembic file in output directory
                    bpy.ops.wm.alembic_export(filepath=export_path,
                                            selected=True, 
                                            global_scale=1.0, 
                                            flatten=True, 
                                            export_custom_properties=True,
                                            start=1,
                                            end=1
                                            )
                    

                else:
                    bpy.ops.object.select_all(action='DESELECT')

                    for cam in nonrescams:
                        cam.select_set(True)

                    ShowMessageBox('Please Add Resolution this Cameras ' + str(nonrescams_name) ,'ERROR','ERROR')
                    print(nonrescams_name)


        else:
            ShowMessageBox('Please Save the File','ERROR','ERROR')
        return{'FINISHED'}