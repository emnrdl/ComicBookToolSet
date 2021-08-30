
import bpy
from . exlib import ShowMessageBox
from bpy.types import Operator

class select_meshes_OT_Operator(Operator):
    
    bl_idname = 'select.meshs' 
    bl_label = 'Select Meshs'
    bl_description = 'Select all Mesh Type Objects in the Scene'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                obj.select_set(True)

        return {'FINISHED'}

class select_cameras_OT_Operator(Operator):

    bl_idname = 'select.cameras' 
    bl_label = 'Select Cameras'
    bl_description = 'Select all Camera Type Objects in the Scene'
    bl_options = {'REGISTER', 'UNDO'}        

    def execute(self, context):
        
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.context.scene.objects:
            if obj.type == 'CAMERA':
                obj.select_set(True)

    
        return {'FINISHED'}

class select_emptys_OT_Operator(Operator):
    
    bl_idname = 'select.emptys' 
    bl_label = 'Select Emptys'
    bl_description = 'Select all Empty Type Objects in the Scene'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.context.scene.objects:
            if obj.type == 'EMPTY':
                obj.select_set(True)


        return {'FINISHED'}

class select_lights_OT_Operator(Operator):

    bl_idname = 'select.lights' 
    bl_label = 'Select Lights'
    bl_description = 'Select all Light Type Objects in the Scene'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.context.scene.objects:
            if obj.type == 'LIGHT':
                obj.select_set(True)

        return {'FINISHED'}

class select_allparented_OT_Operator(Operator):

    bl_idname = 'select.parented' 
    bl_label = 'Select Parented'
    bl_description = 'Select all objects under the root bone'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        
        selected = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')

        for objects in selected:
            for child in objects.children:
                child.select_set(True)


        return {'FINISHED'}

class select_parentedmeshes_OT_Operator(Operator):

    bl_idname = 'select.parentedmeshes' 
    bl_label = 'Select Parented Meshes'
    bl_description = 'Select all mesh type objects under the root bone'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        selected = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')

        for objects in selected:
            for child in objects.children:
                if child.type == 'MESH':
                    child.select_set(True)

        
        return {'FINISHED'}
