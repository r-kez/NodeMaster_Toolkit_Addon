'''Cropped Resolution took from Amaranth Addon built-in in Blender'''

import bpy
import os





class RENDER_PT_resolutionHelper(bpy.types.Panel):
    bl_idname = "RENDER_PT_resolutionHelper"
    bl_label = "Resolution Helper"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "NodeMaster Toolkit"

    def draw(self, context):
        rd = context.scene.render
        #Define Information
        res_percentage = context.scene.render.resolution_percentage
        res_x = context.scene.render.resolution_x 
        res_y = context.scene.render.resolution_y  
        render_settings = context.scene.render
        final_res_x = int(res_x * (res_percentage/100))
        final_res_y = int(res_y * (res_percentage/100))
        final_res_x_border = round((final_res_x * (rd.border_max_x - rd.border_min_x)))
        final_res_y_border = round((final_res_y * (rd.border_max_y - rd.border_min_y)))

        #Draw UI Grid

        layout = self.layout
        layout.label(text="Render Resolution")

        #Define Grid Size
        grid = layout.grid_flow(row_major=True, columns=2)

        #Display Render Resolution
        grid.label(text="Resolution X:")
        grid.prop(render_settings, "resolution_x", text="")
        grid.label(text="Resolution Y:")
        grid.prop(render_settings, "resolution_y", text="")


        grid = layout.grid_flow(row_major=True, columns=1)

        grid.operator("render.res_flip", text="Flip Resolution")

        #Display Percentage Slider
        grid.prop(render_settings, "resolution_percentage", text="Percentage")

        grid = layout.grid_flow(row_major=True, columns=2, align=True)

        #Show Final Resolution
        grid.label(text="Final Resolution:")
        grid.label(text=f"{final_res_x} x {final_res_y}")     
        if rd.use_border:
            grid.label(text="Cropped Resolution:")
            grid.label(text=f"{final_res_x_border} x {final_res_y_border}")

#Get Image Information

class OBJECT_PT_CollectionPanel(bpy.types.Panel):
    bl_label = "Object Collection Panel"
    bl_idname = "OBJECT_PT_collection_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}    
    bl_category = 'NodeMaster Toolkit'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Select Move and Unorganized Objects")

        #row = layout.row()
        grid = layout.grid_flow(row_major=True, columns=2, align=True)
        grid.operator("object.move_and_select_unorganized_mesh", text="Mesh")
        grid.operator("object.move_and_select_unorganized_lights", text="Lights")
        grid.operator("object.move_empty", text="Empty")
        grid.operator("object.move_camera", text="Camera")
        grid.operator("object.move_text", text="Text")
        grid.operator("object.move_curve", text="Curve")

## Indice na frente do nome da imagem
'''class IMAGE_UL_items(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor=0.2)
        split.label(text=str(index))
        split.prop(item, "name", text="", emboss=False, icon_value=icon)
        
'''
## Sem Indice junto ao nome da imagem
'''class IMAGE_UL_items(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name", text="", emboss=False, icon_value=icon)'''

class IMAGE_UL_items(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if item:
            row = layout.row(align=True)
            row.prop(item, "name", text="", emboss=False, icon_value=icon)
            row.template_icon_view(item, "image", scale_x=4, scale_y=4)


class IMAGE_PT_ImageListsPanel(bpy.types.Panel):
    bl_idname = "IMAGE_PT_ImageListsPanel"
    bl_label = "Current File Images"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'DEFAULT_CLOSED'}    
    bl_category = "NodeMaster Toolkit"


    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Set World Texture Node Name: ")
        layout.prop(scene, "world_hdri_texture_node", text="")
        layout.label(text="Image List:")

        layout.template_list("IMAGE_UL_items", "", scene, "image_list", scene, "image_list_index", rows=5)
        
        if bpy.context.scene.image_list:
            selected_image = bpy.context.scene.image_list[bpy.context.scene.image_list_index]
            layout.label(text=f"Selected: {selected_image.name}")
        else:
            layout.label(text="No images found.")

        grid = layout.grid_flow(row_major=True, columns=2)
        grid.operator("object.open_image_file_browser", text="Browse")
        grid.operator("object.update_image_list", text="Update")
        grid = layout.grid_flow(row_major=True, columns=1)
        grid.operator("object.link_to_environment", text="Link to World")

class IMAGE_PT_LoadDir(bpy.types.Panel):
    bl_idname = "IMAGE_PT_LoadDir"
    bl_label = "Load Directory"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "NodeMaster Toolkit"
    bl_options = {'DEFAULT_CLOSED'}    


    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        row = layout.row()
        row.prop(wm, "my_previews_dir")
        row = layout.row()
        row.template_icon_view(wm, "my_previews")
        row = layout.row()
        row.prop(wm, "my_previews", text="")
        layout.label(text="Set World Texture Node Name: ")
        layout.prop(context.scene, "world_hdri_texture_node", text="")
        layout.operator("object.find_node_by_name_in_group", text="Link to World")
        selected_image_name = bpy.context.window_manager.my_previews
        directory_path = bpy.context.window_manager.my_previews_dir
        selected_image_path = os.path.join(directory_path, selected_image_name)
        layout.label(text="Path: " + selected_image_path)        



classes_view_3d_PT = [
RENDER_PT_resolutionHelper,
OBJECT_PT_CollectionPanel,
IMAGE_PT_ImageListsPanel,
IMAGE_UL_items,
IMAGE_PT_LoadDir
]