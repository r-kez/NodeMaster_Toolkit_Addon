bl_info = {
    "name": "NodeMaster Toolkit - Node Editor",
    "description": "Some helpful features for your workflow",
    "author": "Robert Kezives",
    "version": (1, 2),
    "blender": (3, 6, 0),
    "location": "3D View & Node Editor > N-Panel",
    "warning": "", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/r-kez/Custom_Panel_Addon",
    "tracker_url": "https://github.com/r-kez/Custom_Panel_Addon",
    "support": "COMMUNITY",
    "category": "UI Utilities",
}

import os
import bpy
from bpy.types import WindowManager
from bpy.props import (StringProperty, EnumProperty,)
from bpy.types import WindowManager

########### Master Operator ###########
from .operators.Master_op.master_op import classes_master_OT

########### Preferences ###########
from .panels.NMT_Preferences_Panel import classes_Preferences

########### Extra Nodes Operators ###########
from .operators.Nodes_ExtraNodes_Operators.NMT_ExtraNodes import classes_ExtraNodes_OT

########### Utilities Panels and Operators ###########
from .panels.NMT_Utilities_Panel import classes_Utilities_PT_OP

########### Extra Nodes Panels ###########
from .panels.NMT_ExtraNodes_Panel import classes_ExtraNodes_PT

########### Native Shading Nodes ###########
from .operators.Nodes_Blender_Native_Nodes_Operators.NMT_Blender_Native_Nodes_Operator import classes_Native_Nodes_All

########### Geometry Nodes ###########
from .operators.Nodes_GeoNodes_Operators.NMT_GeoNodes_Operators import classes_GeoNodes_All

########### LuxCore ###########
from .operators.Nodes_LuxCore_Operators.Nodes_LuxCore_Operators import classes_LC_OT

########### View 3D Operators ###########
from .operators.View3D_Operators.View_3D_Utils_Operators import classes_view_3d_OT, IMAGE_PT_ImageInfo 

########### Octane Operators ###########
from .operators.Nodes_Octane_Operators.Octane_Operators import classes_Octane_OT

########### PANELS ###########
# NMT_Blender_Native_Nodes_Panel
from .panels.NMT_Blender_Native_Nodes_Panel import classes_Native_Nodes_PT 

# NMT_GeoNodes_Panel
from .panels.NMT_GeoNodes_Panel import classes_GeoNodes_PT

# NMT_View3d_Panel
from .panels.NMT_View3d_Panel import classes_view_3d_PT

# NMT_Blender_Native-Panels_Append
from .panels.NMT_Blender_Native_Panels_Append import FlipResolutionAppend

# NMT_LuxCore_Panel
from .panels.NMT_LuxCore_Panel import classes_LC_PT

# NMT_OctanePaenl
from .panels.NMT_Octane_Panel import classes_OCTANE_PT


#__Classes_List__#

all_classes = (
    classes_Preferences +
    classes_Utilities_PT_OP +
    classes_ExtraNodes_OT + 
    classes_ExtraNodes_PT +
    classes_master_OT + 
    classes_Native_Nodes_All + 
    classes_GeoNodes_All + 
    classes_view_3d_OT +   
    classes_Native_Nodes_PT + 
    classes_GeoNodes_PT + 
    classes_view_3d_PT +  
    classes_LC_PT +  
    classes_LC_OT +
    classes_Octane_OT +
    classes_OCTANE_PT
)

#__Register__#

preview_collections = {}

def enum_previews_from_directory_items(self, context):
    """EnumProperty callback"""
    enum_items = []

    if context is None:
        return enum_items

    wm = context.window_manager
    directory = wm.my_previews_dir

    # Get the preview collection (defined in register func).
    pcoll = preview_collections["main"]

    if directory == pcoll.my_previews_dir:
        return pcoll.my_previews

    print("Scanning directory: %s" % directory)

    if directory and os.path.exists(directory):
        # Scan the directory for png files
        image_paths = []
        for fn in os.listdir(directory):
            if fn.lower().endswith((".png", ".exr", ".hdr", ".jpg")):
                image_paths.append(fn)

        for i, name in enumerate(image_paths):
            # generates a thumbnail preview for a file.
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            if not icon:
                thumb = pcoll.load(name, filepath, 'IMAGE')
            else:
                thumb = pcoll[name]
            enum_items.append((name, name, "", thumb.icon_id, i))

    pcoll.my_previews = enum_items
    pcoll.my_previews_dir = directory
    return pcoll.my_previews



class CustomMostUsedNodes(bpy.types.PropertyGroup):
    nodes_data: bpy.props.StringProperty()


def register():

    WindowManager.my_previews_dir = StringProperty(name="Folder Path", subtype='DIR_PATH', default="")
    WindowManager.my_previews = EnumProperty(items=enum_previews_from_directory_items,)
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()
    pcoll.my_previews_dir = ""
    pcoll.my_previews = ()
    preview_collections["main"] = pcoll

    #### View 3D
    bpy.utils.register_class(IMAGE_PT_ImageInfo)
    bpy.types.Scene.image_list = bpy.props.CollectionProperty(type=IMAGE_PT_ImageInfo)
    bpy.types.Scene.filter_image_type = bpy.props.BoolProperty(name="Filter Image Type", description="Enable image filtering by type", default=False)
    bpy.types.Scene.world_hdri_texture_node = bpy.props.StringProperty(default="Environment Texture", description="FOR NODE IN GROUP ONLY!")
    bpy.types.Scene.image_list_index = bpy.props.IntProperty()
    bpy.types.Scene.filter_image_button = bpy.props.BoolProperty()
    bpy.types.Scene.Break_Col = bpy.props.BoolProperty(default=False, description='Split layout in 2 columns')
    bpy.types.Scene.Panel_Row_Major_Switch = bpy.props.BoolProperty(default=False, description='True = Complete line fist | False = Complete Column First')
    bpy.types.RENDER_PT_format.append(FlipResolutionAppend)
    
    #### Favorites
    bpy.types.WindowManager.node_information = bpy.props.StringProperty(name="Node Information", default="")
    bpy.types.Scene.set_fav_display = bpy.props.IntProperty(name="Favorite List Display", description="Set the number of nodes to be shown on the favorite list", default=10, min=1, max=20)
    #### Most Used Nodes
    bpy.utils.register_class(CustomMostUsedNodes)    
    bpy.types.Scene.custom_most_used_nodes = bpy.props.CollectionProperty(type=CustomMostUsedNodes)
    bpy.types.WindowManager.custom_most_used_nodes = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    bpy.types.Scene.input_int_most_used = bpy.props.IntProperty(name="Display Amount", description="Set the amount of nodes to be shown on the list", default=10, min=1, max=20)
    #### Favorites Pie Menu
    # Adicione um atalho de teclado para o Pie Menu no Node Editor
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.get('Node Editor')
        if not km:
            km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'E', 'PRESS')
        kmi.properties.name = "NODE_MT_pie_node_editor"

    ## Register Panels And Operators
    for cls in all_classes:
        bpy.utils.register_class(cls)


def unregister():

    del WindowManager.my_previews
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

        #### View 3D
    bpy.utils.unregister_class(IMAGE_PT_ImageInfo)
    del bpy.types.Scene.image_list
    del bpy.types.Scene.filter_image_type
    del bpy.types.Scene.world_hdri_texture_node
    del bpy.types.Scene.image_list_index  
    del bpy.types.Scene.filter_image_button
    del bpy.types.Scene.Break_Col
    del bpy.types.Scene.Panel_Row_Major_Switch
    #### Unregister filter image button
    bpy.types.RENDER_PT_format.remove(FlipResolutionAppend)

    #### Favorites
    del bpy.types.WindowManager.node_information
    del bpy.types.Scene.set_fav_display
    #### Most Used Nodes
    bpy.utils.unregister_class(CustomMostUsedNodes)
    del bpy.types.Scene.custom_most_used_nodes
    del bpy.types.Scene.input_int_most_used
    del bpy.types.WindowManager.custom_most_used_nodes
    #### Favorites Pie Menu
    # Remova o atalho de teclado ao desregistrar
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.get('Node Editor')
        if km:
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie' and kmi.properties.name == "NODE_MT_pie_node_editor":
                    km.keymap_items.remove(kmi)
                    break


    ## Unregister Panels And Operators
    for cls in all_classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()


