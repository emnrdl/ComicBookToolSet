import bpy
from bpy.types import Operator, Panel


class MyProperties(bpy.types.PropertyGroup):

    my_enum : bpy.props.EnumProperty(
        name = 'Enum',
        description='items',
        items = [('OP1','option 1'),
                 ('OP2','option 2')

        ] 
    )


class Tool_Panel(Panel):
    bl_idname = 'OBJECT_PT_eToolSet'
    bl_label = 'EMNrdl Tool Set'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EMNrdl Tool Set'

    def draw(self, context):
        layout = self.layout
        placeholder = bpy.context.scene

        layout.label(text="Access:")

        row = layout.row()
        row.operator('open.workdir',text='Opens the work directory',icon='HOME')      

        layout.label(text="Selection:")

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

        layout.label(text="Editing:")

        row = layout.row()
        row.operator('copy.objects',text='Copy to Objects',icon='CON_TRACKTO')

        row = layout.row()
        row.operator('copy.anddel',text='Copy and Delete',icon='CON_TRACKTO')

        row = layout.row()
        row.operator('add.bbox',text='Create BBOX from Selected',icon='CUBE')

        layout.label(text="Render:")

        row = layout.row()
        row.operator('set.linerender',text='Set Render Settings',icon='RESTRICT_RENDER_OFF')

        row = layout.row()
        row.operator('set.cameraactive',text='Set Active Camera',icon='OUTLINER_OB_CAMERA')

        row = layout.row()
        row.operator('create.outline',text='Create GP Outline',icon='OUTLINER_OB_GREASEPENCIL')

        layout.label(text="Property:")

        row = layout.row()
        row.operator('add.camres',text='Add Resolution to Camera',icon='OUTLINER_OB_CAMERA')

        row = layout.row()
        row.operator('add.cacheable',text='Add Cacheable Property',icon='RNA_ADD')

        layout.label(text="Export:")

        row = layout.row()
        row.operator('export.camera',text='Export Cameras',icon='CON_CAMERASOLVER')

        row = layout.row()
        row.operator('export.cacheable',text='Export Cacheable',icon='RNA_ADD')

