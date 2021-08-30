import bpy
from . exlib import ShowMessageBox
from bpy.types import Operator


class copy_to_objects_OT_Operator(Operator):
    
    bl_idname = 'copy.objects'
    bl_label = 'Copy the last selected objects to selected objects location'
    bl_description = 'Copy the last selected objects to selected objects location'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        active = bpy.context.active_object
        selected = bpy.context.selected_objects
        try:
            selected.remove(active)
            bpy.ops.object.select_all(action='DESELECT')
            for i, obj in enumerate(selected):
                new_obj = active.copy()
                new_obj.data = active.data.copy()
                new_obj.animation_data_clear()
                bpy.context.collection.objects.link(new_obj)
                new_obj.select_set(True)
                new_obj.matrix_world = selected[i].matrix_world
        except:
            ShowMessageBox("Select base object","ERROR",'ERROR')
    
        return{'FINISHED'}