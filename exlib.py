import bpy
import os

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text = message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

def create_dir(dir_path):

    path = dir_path

    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print('Directory already exist')
