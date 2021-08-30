import bpy
from bpy.types import Operator, Space, SpaceOutliner

class show_outliner_OT_Operator(Operator):

    bl_idname = 'show.outliner' 
    bl_label = 'Show Outliner'
    bl_description = 'Shows selected mesh in outliner'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        objname = bpy.context.active_object.name

        bpy.types.SpaceOutliner.filter_text = objname
        
        return {'FINISHED'}