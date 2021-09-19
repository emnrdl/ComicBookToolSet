import bpy
from bpy.types import Operator, Panel


class Access_Tool_Panel(Panel):
    bl_idname = 'ACCESS_OBJECT_PT_eToolSet'
    bl_label = 'Access'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('open.workdir',text='Opens the work directory',icon='HOME')      


class Selection_Tool_Panel(Panel):
    bl_idname = 'SELECT_OBJECT_PT_eToolSet'
    bl_label = 'Selection'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('select.meshs',text='Select Meshs',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('select.cameras',text='Select Cameras',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('select.emptys',text='Select Emptys',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('select.lights',text='Select Lights',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('select.parentedmeshes',text='Select Parented Meshes',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('select.parented',text='Select Parented',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('select.cacheable',text='Select Cacheable',icon='RESTRICT_SELECT_OFF')


class Editing_Tool_Panel(Panel):
    bl_idname = 'EDITING_OBJECT_PT_eToolSet'
    bl_label = 'Editing'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('copy.objects',text='Copy to Objects',icon='CON_TRACKTO')

        row = layout.row()
        row.operator('copy.anddel',text='Copy and Delete',icon='CON_TRACKTO')

        row = layout.row()
        row.operator('add.bbox',text='Create BBOX from Selected',icon='CUBE')

class Render_Tool_Panel(Panel):
    bl_idname = 'RENDER_OBJECT_PT_eToolSet'
    bl_label = 'Render'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('set.rendersettings',text='Set Render Settings',icon='RESTRICT_RENDER_OFF')

        row = layout.row()
        row.operator('create.outline',text='Create GP Outline',icon='OUTLINER_OB_GREASEPENCIL')

class Camera_Panel(Panel):
    bl_parent_id = 'RENDER_OBJECT_PT_eToolSet'
    bl_idname = 'CAMERA_OBJECT_PT_eToolSet'
    bl_label = 'Camera'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):
        
        layout = self.layout

        row = layout.row()
        row.operator('set.cameraactive',text='Set Selected Camera Active',icon='OUTLINER_OB_CAMERA')

        row = layout.row()
        row.operator('create.cameratoview',text='Create Camera from view',icon='RESTRICT_SELECT_OFF')

        #code from stored view addon
        scene = context.scene
        layout.label(text="Camera Selector")
        cameras = sorted([o for o in scene.objects if o.type == 'CAMERA'],
                         key=lambda o: o.name)

        if len(cameras) > 0:
            for camera in cameras:
                row = layout.row(align=True)
                row.context_pointer_set("active_object", camera)
                row.operator("cameraselector.set_scene_camera",
                                   text=camera.name, icon='OUTLINER_DATA_CAMERA')
                row.operator("cameraselector.preview_scene_camera",
                                   text='', icon='RESTRICT_VIEW_OFF')
        else:
            layout.label(text="No cameras in this scene")
        
        #----------------------------------------------------------
class Property_Tool_Panel(Panel):
    bl_idname = 'PROPERTY_OBJECT_PT_eToolSet'
    bl_label = 'Property'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('add.camres',text='Add Resolution to Camera',icon='OUTLINER_OB_CAMERA')

        row = layout.row()
        row.operator('add.cacheable',text='Add Cacheable Property',icon='RNA_ADD')

class Import_Tool_Panel(Panel):
    bl_idname = 'IMPORT_OBJECT_PT_eToolSet'
    bl_label = 'Import'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('import.camerawithjson',text='Import Cameras',icon='CON_CAMERASOLVER')
class Export_Tool_Panel(Panel):
    bl_idname = 'EXPORT_OBJECT_PT_eToolSet'
    bl_label = 'Export'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('export.camera',text='Export Cameras',icon='CON_CAMERASOLVER')

        row = layout.row()
        row.operator('export.cacheable',text='Export Cacheable',icon='RNA_ADD')

class Character_Tool_Panel(Panel):
    bl_idname = 'CHAR_OBJECT_PT_eToolSet'
    bl_label = 'Character'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('char.ref',text='Referances Base Character',icon='RNA_ADD')


class Test_Tool_Panel(Panel):
    bl_idname = 'TEST_OBJECT_PT_eToolSet'
    bl_label = 'Test'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ComicBookToolSet'
    
    def draw(self, context):

        layout = self.layout

        scn = context.scene
        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")