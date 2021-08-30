import bpy
from bpy.types import Operator
from . exlib import ShowMessageBox
import os


class open_work_dir_OT_Operator(Operator):

    bl_idname = 'open.workdir'
    bl_label = 'Opens the work directory'
    bl_description = 'Opens the work directory'

    def execute(self, context):
        
        if bpy.data.is_saved:

            #Delete version number end file extention in filpath
            filepath = bpy.data.filepath
            basefilename = bpy.path.basename(filepath)
            filepath = filepath.replace('\\','/')
            filepath = filepath.replace(basefilename, '' )

            filepath = os.path.realpath(filepath)
            if os.name == 'posix':
                os.system('xdg-open "%s" ' % filepath)
            else:
                os.startfile(filepath)

        else:
            ShowMessageBox('Please Save the File','ERROR','ERROR')
        return{'FINISHED'}