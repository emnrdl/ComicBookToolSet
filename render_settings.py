import bpy
from bpy.types import Operator
from . path_lib  import get_path
from . exlib import ShowMessageBox, create_dir


class Set_Render_Settings_OT_Operator(Operator):
    
    bl_idname = 'set.rendersettings'
    bl_label = 'Set render settingsg'
    bl_description = 'Set render settings'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        scene = bpy.data.scenes['Scene']    

        scene.render.film_transparent = True
        scene.render.image_settings.compression = 0
        
        export_path = ''
        if bpy.data.is_saved:
            name = get_path.fullname() 
            path = get_path.file_path() + 'render'
            path = path.replace('/','\\')
            export_path = path +'\\'+ name +'.exr'
            scene.render.filepath = export_path
        else:
            ShowMessageBox('Please Save the File','ERROR','ERROR')

        #data
        bpy.context.scene.view_layers["View Layer"].use_pass_combined = True
        bpy.context.scene.view_layers["View Layer"].use_pass_z = True
        bpy.context.scene.view_layers["View Layer"].use_pass_normal = True
        bpy.context.scene.view_layers["View Layer"].use_pass_vector = True
        #light
        bpy.context.scene.view_layers["View Layer"].use_pass_diffuse_color = True
        bpy.context.scene.view_layers["View Layer"].use_pass_emit = True
        bpy.context.scene.view_layers["View Layer"].use_pass_shadow = True
        bpy.context.scene.view_layers["View Layer"].use_pass_ambient_occlusion = True
        #cryptomatte
        bpy.context.scene.view_layers["View Layer"].use_pass_cryptomatte_object = True
        bpy.context.scene.view_layers["View Layer"].use_pass_cryptomatte_material = True

        #file format
        bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'

        #Compositor node setup
        bpy.context.scene.use_nodes = True
        tree = bpy.context.scene.node_tree

        # clear default nodes
        for node in tree.nodes:
            tree.nodes.remove(node)

        # create input image node
        image_node = tree.nodes.new(type='CompositorNodeRLayers')
        image_node.location = 0,0

        # create output node
        comp_node = tree.nodes.new('CompositorNodeComposite')   
        comp_node.location = 800,200

        links = tree.links
        link = links.new(image_node.outputs[0], comp_node.inputs[0])
        
        #-------------------------------File Outputs--------------------------------

        #image output
        image_output = tree.nodes.new('CompositorNodeOutputFile')
        image_output.location = 800,50
        if bpy.data.is_saved:
            image_output.base_path = path +'\\'+ name + '_' + bpy.context.scene.camera.name + '_frame_'
        else:
            ShowMessageBox('Please Save the File','ERROR','ERROR')

        for count, outputs in enumerate(image_node.outputs, start=0):
            if (outputs.enabled == True):
                if(count == 0):
                    links.new(image_node.outputs[count], image_output.inputs[count])
                else:    
                    image_output.file_slots.new(outputs.identifier)
                    links.new(image_node.outputs[count], image_output.inputs[count])

            if outputs.identifier == 'Depth':
                normalize_node = tree.nodes.new('CompositorNodeNormalize')
                normalize_node.location  = 400, -400
                links.new(image_node.outputs[count], normalize_node.inputs[0])
                links.new(normalize_node.outputs[0],image_output.inputs[count])
                print(outputs.identifier)
        
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


class Create_Camera_OT_Operator(Operator):

    bl_idname = 'create.cameratoview' 
    bl_label = 'Create to view'
    bl_description = 'Create to view'
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        scn = bpy.context.scene
        dta = bpy.data
        camera_data = dta.cameras.new(name = 'Camera')
        camera_object = dta.objects.new('Camera',camera_data)
        scn.collection.objects.link(camera_object)

        bpy.context.scene.camera = camera_object
        bpy.ops.view3d.camera_to_view()
        
        return{'FINISHED'}

#code from stored view addon
class SetSceneCamera(Operator):
    bl_idname = "cameraselector.set_scene_camera"
    bl_label = "Set Scene Camera"
    bl_description = "Set chosen camera as the scene's active camera"

    hide_others = False

    def execute(self, context):
        chosen_camera = context.active_object
        scene = context.scene

        if self.hide_others:
            for c in [o for o in scene.objects if o.type == 'CAMERA']:
                c.hide = (c != chosen_camera)
        scene.camera = chosen_camera
        bpy.ops.object.select_all(action ='DESELECT')
        chosen_camera.select_set(True)
        return {'FINISHED'}

    def invoke(self, context, event):
        if event.ctrl:
            self.hide_others = True

        return self.execute(context)

class PreviewSceneCamera(Operator):
    bl_idname = "cameraselector.preview_scene_camera"
    bl_label = "Preview Camera"
    bl_description = "Preview chosen camera and make scene's active camera"

    def execute(self, context):
        chosen_camera = context.active_object
        bpy.ops.view3d.object_as_camera()
        bpy.ops.object.select_all(action="DESELECT")
        chosen_camera.select_set(True)
        return {'FINISHED'}

#-----------------------------------------------------------