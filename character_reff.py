import bpy
import os
from bpy.types import Operator

class char_append_OT_Opertator(Operator):

    bl_idname = 'char.append'
    bl_label = 'Append base character'
    bl_description = 'Append base character'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        active = bpy.context.active_object
        selected = bpy.context.selected_objects

        selected_char = str(bpy.context.scene.my_tool.charlist)
        file_path = str(bpy.utils.user_resource('SCRIPTS')) + '\\addons\\ComicBookToolSet\\baseChar\\Base_Male_A\\Base_Male_A.blend'
        inner_path = 'Collection'
        object_name = 'Male_Rig'
        print(selected_char)

        if selected_char == 'OP1':
            
            object_name = 'Male_Rig'
            print('aaa')
            bpy.ops.wm.append(
            filepath=os.path.join(file_path, inner_path, object_name),
            directory=os.path.join(file_path, inner_path),
            filename=object_name

            )
        if selected_char == 'OP2':
            file_path = str(bpy.utils.user_resource('SCRIPTS')) + '\\addons\\ComicBookToolSet\\baseChar\\Base_Female_A\\Base_Female_A.blend'
            object_name = 'Female_Rig'
            
            bpy.ops.wm.append(
            filepath=os.path.join(file_path, inner_path, object_name),
            directory=os.path.join(file_path, inner_path),
            filename=object_name
            
            )



        return {'FINISHED'}