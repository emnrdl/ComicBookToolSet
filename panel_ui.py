import bpy
from bpy.types import Operator, Panel


class Access_Tool_Panel(Panel):
    bl_idname = 'ACCESS_OBJECT_PT_eToolSet'
    bl_label = 'Access'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EMNrdl Tool Set'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('open.workdir',text='Opens the work directory',icon='HOME')      


class Selection_Tool_Panel(Panel):
    bl_idname = 'SELECT_OBJECT_PT_eToolSet'
    bl_label = 'Selection'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EMNrdl Tool Set'
    
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
    bl_category = 'EMNrdl Tool Set'
    
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
    bl_category = 'EMNrdl Tool Set'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('set.linerender',text='Set Render Settings',icon='RESTRICT_RENDER_OFF')

        row = layout.row()
        row.operator('create.cameratoview',text='Create Camera from view',icon='RESTRICT_SELECT_OFF')

        row = layout.row()
        row.operator('set.cameraactive',text='Set Active Camera',icon='OUTLINER_OB_CAMERA')

        row = layout.row()
        row.operator('create.outline',text='Create GP Outline',icon='OUTLINER_OB_GREASEPENCIL')


class Property_Tool_Panel(Panel):
    bl_idname = 'PROPERTY_OBJECT_PT_eToolSet'
    bl_label = 'Property'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EMNrdl Tool Set'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('add.camres',text='Add Resolution to Camera',icon='OUTLINER_OB_CAMERA')

        row = layout.row()
        row.operator('add.cacheable',text='Add Cacheable Property',icon='RNA_ADD')

class Export_Tool_Panel(Panel):
    bl_idname = 'EXPORT_OBJECT_PT_eToolSet'
    bl_label = 'Export'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EMNrdl Tool Set'
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator('export.camera',text='Export Cameras',icon='CON_CAMERASOLVER')

        row = layout.row()
        row.operator('export.cacheable',text='Export Cacheable',icon='RNA_ADD')

class Test_Tool_Panel(Panel):
    bl_idname = 'TEST_OBJECT_PT_eToolSet'
    bl_label = 'Export'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EMNrdl Tool Set'
    
    def draw(self, context):

        layout = self.layout

        scn = context.scene
        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        print(scn.my_tool.path)