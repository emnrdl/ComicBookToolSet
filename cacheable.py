import bpy
from bpy.types import Operator
from . exlib import ShowMessageBox
from . path_lib import get_path
import os
from . exlib import create_dir

class add_cacheable_OT_Operator(Operator):

    bl_idname = 'add.cacheable'
    bl_label = 'Add propertie named cacheable'
    bl_description = 'Add propertie named cacheable to selected objects'

    def execute(self, context):

        #Add cacheable and name propertie to selected object
        selectedobj = bpy.context.selected_objects

        if len(selectedobj) == 0: 
            print('Please Select Object')
            ShowMessageBox("Please Select Object","ERROR",'ERROR')

        elif bpy.data.is_saved:

            name = get_path.file_name()
            try:
                name = name.replace('_Rig_Main','')
            except IndexError as eror:
                return(name)
            for obj in selectedobj:
                obj["cacheable"] = 1
                obj["name"] =  name
        
        else:
            ShowMessageBox("Please Save the File","ERROR",'ERROR')



        return{'FINISHED'}


class select_cacheable_OT_Operator(Operator):

    bl_idname = 'select.cacheable'
    bl_label = 'Select all cacheable'
    bl_description = 'Select all cacheable'

    def execute(self, context):

        if bpy.data.is_saved:            
            for obj in bpy.data.objects :                
                if 'cacheable' in obj:
                    obj.select_set(True)
                else:
                    obj.select_set(False)

        selectedobj = bpy.context.selected_objects

        if len(selectedobj) == 0: 
            print('Please Select Object')
            ShowMessageBox("There is no cacheable in the scene","ERROR",'ERROR')
        
        return{'FINISHED'}


class export_cacheable_OT_Operator(Operator):
    
    bl_idname = 'export.cacheable'
    bl_label = 'Export all the cacheable attributes as alembic'
    bl_description = 'Export all the cacheable attributes in the scene as alembic to ../Outputs/alembic directory'

    def execute(self, context):
        

        if bpy.data.is_saved:
            

            for obj in bpy.data.objects :                
                if 'cacheable' in obj:
                    obj.select_set(True)
                else:
                    obj.select_set(False)
            
            allCacheable = bpy.context.selected_objects
            bpy.ops.object.select_all(action='DESELECT')
            
            for obj in allCacheable:
                for child in obj.children: 
                    if child.type == 'MESH':
                        child.select_set(True)
                    
                    else:
                        child.select_set(False)   

               
                
                
                
                name = get_path.fullname() 
                path = get_path.file_path() + '/alembic'
                objname = obj['name']

                scene = bpy.context.scene



                
                export_path = path + '/' + name + '_' + str(scene.frame_start) + '_' + str(scene.frame_end)+'_'+ objname + ".abc"

                i = 0
                while os.path.isfile(export_path):
                    i += 1 
                    export_path = path + '/' + name + '_' + str(scene.frame_start) + '_' + str(scene.frame_end)+'_'+ objname + str(i) + ".abc"

                obj.select_set(False)


                create_dir(path)

                #Export as a Alembic file in output directory

                bpy.ops.wm.alembic_export(filepath=export_path,
                                        selected=True, 
                                        global_scale=100.0, 
                                        flatten=True, 
                                        export_custom_properties=False
                                        )
                
                bpy.ops.object.select_all(action='DESELECT')

        else:
            ShowMessageBox("Please Save the File","ERROR",'ERROR')

        return{'FINISHED'}
