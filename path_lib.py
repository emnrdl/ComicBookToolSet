import bpy
import re

class get_path(object):

    @classmethod
    def file_name(cls):
        
        filepath= ''

        if bpy.data.is_saved:
            
            #Delete version number end file extention in filename
            filepath = bpy.data.filepath
            basefilename = bpy.path.basename(filepath)

            try:
                version = re.findall('v[0-9][0-9][0-9]' , basefilename)
                filename = basefilename.replace('_'+version[0]+'.blend','')
            except IndexError as eror:
                filename = 'unsaved'

        return(filename)
    
    @classmethod
    def file_path(cls):
        
        filepath= ''
        
        if bpy.data.is_saved:
            #Delete version number end file extention in filpath and add output directory path
            filepath = bpy.data.filepath
            basefilename = bpy.path.basename(filepath)
            filepath = filepath.replace('\\','/')
            filepath = filepath.replace(basefilename, 'Outputs/' )
        
        return(filepath)
        
    @classmethod
    def fullname(cls):

        filepath= ''

        if bpy.data.is_saved:
            try:
                filepath = bpy.data.filepath
                basefilename = bpy.path.basename(filepath)
                filename = basefilename.replace('.blend','')
            except IndexError as eror:
                filename = 'unsaved'

        return(filename)