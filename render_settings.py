import bpy
from . exlib import ShowMessageBox
from bpy.types import Operator


class set_line_render_OT_Operator(Operator):
    
    bl_idname = 'set.linerender'
    bl_label = 'Set render settings for Line Shading'
    bl_description = 'Set render settings for Line Shading'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        scene = bpy.data.scenes['Scene']    
        active = bpy.context.active_object

        if bpy.context.active_object.type == 'CAMERA':
            bpy.context.scene.camera = active

        scene.render.resolution_x = 4096
        scene.render.resolution_y = 2048
        scene.render.film_transparent = True

        return{'FINISHED'}


class set_camera_active_OT_Operator(Operator):

    bl_idname = 'set.cameraactive'
    bl_label = 'Set active to selected camera'
    bl_description = 'Set active to selected camera'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
           
        active = bpy.context.active_object
        scene = bpy.data.scenes['Scene']

        if bpy.context.active_object.type == 'CAMERA':
            bpy.context.scene.camera = active
            if 'Resolution_X' in active:
                scene.render.resolution_x = active['Resolution_X']
                scene.render.resolution_y = active['Resolution_Y']
        else:
            ShowMessageBox("Select 'Camera' type object","ERROR",'ERROR')


        return{'FINISHED'}

class add_camera_resolution_OT_Operator(Operator):

    bl_idname = 'add.camres'
    bl_label = 'Add current resolution to camera property'
    bl_description = 'Add current resolution to camera property'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
           
        active = bpy.context.active_object
        scene = bpy.data.scenes['Scene']

        if bpy.context.active_object.type == 'CAMERA':
            active['Resolution_X'] = scene.render.resolution_x
            active['Resolution_Y'] = scene.render.resolution_y
        else:
            ShowMessageBox("Select 'Camera' type object","ERROR",'ERROR')


        return{'FINISHED'}
    

class create_outline_OT_Operator(Operator):

    bl_idname = 'create.outline'
    bl_label = 'Create Outline'
    bl_description = 'Create Gpencil object and add Line Art modifier for hole scene'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if 'Outline_Render' in bpy.context.view_layer.objects:
            ShowMessageBox("Outline Object Already Exist","ERROR",'ERROR')
        else:

            bpy.ops.object.select_all(action='DESELECT')
            gp_data = bpy.data.grease_pencils.new("Outline_Render_layer")
            gp_ob = bpy.data.objects.new("Outline_Render", gp_data)
            bpy.context.scene.collection.objects.link(gp_ob)
            gp_ob.select_set(True)
            bpy.context.view_layer.objects.active = gp_ob
            gp_ob = bpy.context.active_object

            # Create grease pencil Layer
            bpy.ops.gpencil.layer_add()


            # Create material for grease pencil
            if "line_material" in bpy.data.materials.keys():
                gp_mat = bpy.data.materials["line_material"]
            else:
                gp_mat = bpy.data.materials.new("line_material")

            if not gp_mat.is_grease_pencil:
                bpy.data.materials.create_gpencil_data(gp_mat)

            gp_data.materials.append(gp_mat)


            # Add Line Art modifier and set settings

            bpy.ops.object.gpencil_modifier_add(type='GP_LINEART')
            gp_ob.grease_pencil_modifiers["Line Art"].source_type = 'SCENE'
            gp_ob.grease_pencil_modifiers["Line Art"].target_layer = 'GP_Layer'
            gp_ob.grease_pencil_modifiers["Line Art"].target_material = gp_mat
            bpy.ops.object.select_all(action='DESELECT')

        return{'FINISHED'}


class create_indoor_lighting_setup_OT_Operator(Operator):

    bl_idname = 'create.indoorlighting' 
    bl_label = 'Create In-door Lighting'
    bl_description = 'Create in-door lighting'
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        
        

        
        
        return{'FINISHED'}

class create_outdoor_lighting_setup_OT_Operator(Operator):

    bl_idname = 'create.outdoorlighting' 
    bl_label = 'Create Out-Door Lighting'
    bl_description = 'Create out-door lighting'
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        
        # create light datablock, set attributes
        light_data = bpy.data.lights.new(name="Sun_Light", type='SUN')
        light_data.energy = 30

        # create new object with our light datablock
        light_object = bpy.data.objects.new(name="Sun_Light", object_data=light_data)

        # link light object
        bpy.context.collection.objects.link(light_object)

        # make it active 
        bpy.context.view_layer.objects.active = light_object

        #change location
        light_object.location = (0, 0, 0)
        
        
        return{'FINISHED'}