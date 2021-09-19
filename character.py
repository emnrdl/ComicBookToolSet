import bpy
from bpy.types import Operator

class char_ref_OT_Opertator(Operator):

    bl_idname = 'char.ref'
    bl_label = 'Referances base character'
    bl_description = 'Referances base character'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        



        return {'FINISHED'}