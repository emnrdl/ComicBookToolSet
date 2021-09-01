# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ComicBookToolSet",
    "author" : "emnrdl",
    "description" : "",
    "blender" : (2, 90, 0),
    "version" : (0, 0, 3),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.props import PointerProperty

from . panel_ui import (
  Access_Tool_Panel, 
  Selection_Tool_Panel, 
  Property_Tool_Panel, 
  Render_Tool_Panel,
  Camera_Panel, 
  Export_Tool_Panel, 
  Editing_Tool_Panel, 
  Test_Tool_Panel
)
from . open_folder import open_work_dir_OT_Operator
from . copy_to_loc import copy_to_objects_OT_Operator
from . copy_and_del import copy_and_del_OT_Operator
from . render_settings import (
  Set_Render_Settings_OT_Operator, 
  create_outline_OT_Operator, 
  set_camera_active_OT_Operator, 
  add_camera_resolution_OT_Operator, 
  Create_Camera_OT_Operator,
  SetSceneCamera,
  PreviewSceneCamera
)
from . mesh_tool import add_bbox_OT_Operator
from . selection_tools import (
  select_meshes_OT_Operator, 
  select_cameras_OT_Operator, 
  select_emptys_OT_Operator, 
  select_lights_OT_Operator, 
  select_allparented_OT_Operator, 
  select_parentedmeshes_OT_Operator
)
from . cacheable import add_cacheable_OT_Operator, select_cacheable_OT_Operator, export_cacheable_OT_Operator
from . navigation import show_outliner_OT_Operator
from . export import export_all_camera_OT_Operator
from . panel_property import MyProperties

classes = (
            open_work_dir_OT_Operator,
            Access_Tool_Panel,
            Selection_Tool_Panel,
            Editing_Tool_Panel,
            Render_Tool_Panel,
            Camera_Panel,
            Property_Tool_Panel,
            Export_Tool_Panel,
            Test_Tool_Panel,
            copy_to_objects_OT_Operator,
            copy_and_del_OT_Operator,
            Set_Render_Settings_OT_Operator,
            create_outline_OT_Operator,
            set_camera_active_OT_Operator,
            add_bbox_OT_Operator,
            select_lights_OT_Operator,
            select_meshes_OT_Operator,
            select_cameras_OT_Operator,
            select_emptys_OT_Operator,
            select_allparented_OT_Operator,
            select_parentedmeshes_OT_Operator,
            add_cacheable_OT_Operator,
            select_cacheable_OT_Operator,
            export_cacheable_OT_Operator,
            show_outliner_OT_Operator,
            add_camera_resolution_OT_Operator,
            export_all_camera_OT_Operator,
            Create_Camera_OT_Operator,
            SetSceneCamera,
            PreviewSceneCamera,
            MyProperties
          )

def register():

  from bpy.utils import register_class
  
  for cls in classes:
    register_class(cls)
  bpy.types.Scene.my_tool = PointerProperty(type = MyProperties)

def unregister():

  from bpy.utils import unregister_class
  
  for cls in reversed(classes):
    unregister_class(cls)
  del bpy.types.Scene.my_tool

if __name__ == "__main__":
  register()