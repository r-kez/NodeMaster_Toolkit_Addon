import bpy



Break_Col: bpy.props.BoolProperty(default=False, description='Split layout in 2 columns')
Panel_Row_Major_Switch: bpy.props.BoolProperty(default=False, description='True = Complete line First | False = Complete Column First')
RowMajorRes = False


class LUXCORE_PT_Shader_Utilities_Panel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_Shader_Utilities_Panel"
    bl_label = "Utilities"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    

    # Draw Dropdown Menu
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Lux Core Material Nodes")
        grid = layout.grid_flow(row_major=True, columns=2, align=True)        
        grid.prop(scene, "Break_Col", text="Break Column")
        grid.prop(scene, "Panel_Row_Major_Switch", text="Row Major")

        return None


# LC Materials Main 
class LUXCORE_PT_GeneralPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_GeneralPanel"
    bl_label = "LuxCore Shading Nodes"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"

    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 1

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    

    def draw(self, context):
        layout = self.layout

        return None

# LC Materials Main 
class LUXCORE_PT_MaterialsPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_MaterialsPanel"
    bl_label = "Materials"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 2

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False


        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        grid.operator('nodes.lc_material_disney_add', text="Disney")           
        grid.operator('nodes.lc_material_mix_add', text="Material Mix")           
        grid.operator('nodes.lc_material_matte_add', text="Matte")           
        grid.operator('nodes.lc_material_matte_translucent_add', text="Matte Translucent")           
        grid.operator('nodes.lc_material_metal_add', text="Metal")           
        grid.operator('nodes.lc_material_mirror_add', text="Mirror")           
        grid.operator('nodes.lc_material_glossy_add', text="Glossy")           
        grid.operator('nodes.lc_material_glossy_translucent_add', text="Glossy Translucent")           
        grid.operator('nodes.lc_material_glossy_coating_add', text="Glossy Coating")           
        grid.operator('nodes.lc_material_glass_add', text="Glass")           
        grid.operator('nodes.lc_material_null_add', text="Null (Transparent)")           
        grid.operator('nodes.lc_material_carpaint_add', text="Carpaint")           
        grid.operator('nodes.lc_material_cloth_add', text="Cloth")           
        grid.operator('nodes.lc_material_velvet_add', text="Velvet")           
        grid.operator('nodes.lc_material_two_sided_add', text="Two Sided")           
        grid.operator('nodes.lc_material_front_back_op_add', text="Front/Back Opacity")           


        return None

# LC Volume Main 
class LUXCORE_PT_VolumePanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_VolumePanel"
    bl_label = "Volume"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 3

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        grid.operator('nodes.lc_volume_clear_add', text="Volume Clear")           
        grid.operator('nodes.lc_volume_homogeneous_add', text="Volume Homogeneous")           
        grid.operator('nodes.lc_volume_heterogeneous_add', text="Volume Heterogeneous")           
        
        if scene.Break_Col:        
            grid.operator('null.operator_type', text="")           
        
        return None

# LC Texture Main 
class LUXCORE_PT_TexturePanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_TexturePanel"
    bl_label = "Texture"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 5

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        #grid.operator('nodes.lc_texture_multiple_images_add', text="Multiple Images")           
        grid.operator('nodes.lc_texture_image_map_add', text="Image Map")           
        grid.operator('nodes.lc_texture_brick_add', text="Brick")           
        grid.operator('nodes.lc_texture_wireframe_add', text="Wireframe")           
        grid.operator('nodes.lc_texture_dots_add', text="Dots")           
        grid.operator('nodes.lc_texture_fbm_add', text="fBM")           
        grid.operator('nodes.lc_texture_checkerboard2d_add', text="2D Checkerboard")           
        grid.operator('nodes.lc_texture_checkerboard3d_add', text="3D Checkerboard")           
        grid.operator('nodes.lc_texture_marble_add', text="Marble")           
        grid.operator('nodes.lc_texture_wrinkled_add', text="Wrinkled")           
        grid.operator('nodes.lc_texture_hitpoint_add', text="Vertex Color")           
        grid.operator('nodes.lc_texture_smoke_add', text="Smoke")           
        grid.operator('nodes.lc_texture_open_vdb_add', text="OpenVDB")           
        grid.operator('nodes.lc_texture_fresnel_add', text="Fresnel")           
        if scene.Break_Col:
            grid.operator('null.operator_type', text="")


        return None

# LC Blender Texture Main 
class LUXCORE_PT_BlenderTexturePanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_BlenderTexturePanel"
    bl_label = "Blender Texture"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 6

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        #grid.operator('nodes.lc_texture_multiple_images_add', text="Multiple Images")           
        grid.operator('nodes.lc_btexture_blend_add', text="Blend")           
        grid.operator('nodes.lc_btexture_clouds_add', text="Clouds")           
        grid.operator('nodes.lc_btexture_distorted_noise_add', text="Distorted Noise")           
        grid.operator('nodes.lc_btexture_magic_add', text="Magic")           
        grid.operator('nodes.lc_btexture_marble_add', text="Marble")           
        grid.operator('nodes.lc_btexture_musgrave_add', text="Musgrave")           
        grid.operator('nodes.lc_btexture_noise_add', text="Noise")           
        grid.operator('nodes.lc_btexture_stucci_add', text="Stucci")           
        grid.operator('nodes.lc_btexture_wood_add', text="Wood")           
        grid.operator('nodes.lc_btexture_voronoi_add', text="Voronoi")           

        return None

# LC Math Main 
class LUXCORE_PT_MathPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_MathPanel"
    bl_label = "Math"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 7

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        #grid.operator('nodes.lc_texture_multiple_images_add', text="Multiple Images")           
        grid.operator('nodes.lc_math_math_add', text="Math")           
        grid.operator('nodes.lc_math_mix_color_add', text="Mix Color")           
        grid.operator('nodes.lc_math_vector_math_add', text="Vector Math")           
        grid.operator('nodes.lc_math_dot_product_add', text="Dot Product")           
        grid.operator('nodes.lc_math_split_float_add', text="Split RGB")           
        grid.operator('nodes.lc_math_make_float_add', text="Combine Float")           
        grid.operator('nodes.lc_math_texture_remap_add', text="Texture Remap")           
        if scene.Break_Col:
            grid.operator('null.operator_type', text="")

        return None

# LC Utils Main 
class LUXCORE_PT_UtilsPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_UtilsPanel"
    bl_label = "Utils"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 8

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        #grid.operator('nodes.lc_texture_multiple_images_add', text="Multiple Images")           
        grid.operator('nodes.lc_utils_texture_bump_add', text="Bump")           
        grid.operator('nodes.lc_utils_texture_band_add', text="Color Ramp")           
        grid.operator('nodes.lc_utils_texture_distort_add', text="Distort")           
        grid.operator('nodes.lc_utils_texture_hsv_add', text="Hue Saturation Value")           
        grid.operator('nodes.lc_utils_texture_bright_contrast_add', text="Brightness / Contrast")           
        grid.operator('nodes.lc_utils_texture_invert_add', text="Invert")           
        grid.operator('nodes.lc_utils_texture_contant_value_add', text="Constant Value")           
        grid.operator('nodes.lc_utils_texture_contant_color_add', text="Constant Color")           
        grid.operator('nodes.lc_utils_texture_ior_preset_add', text="IOR Preset")           
        grid.operator('nodes.lc_utils_texture_hitpoint_info_add', text="Hitpoint Info")           
        grid.operator('nodes.lc_utils_texture_pointness_add', text="Pointiness")           
        grid.operator('nodes.lc_utils_texture_object_id_add', text="Object ID")           
        grid.operator('nodes.lc_utils_texture_random_per_island_add', text="Random Per Island")           
        grid.operator('nodes.lc_utils_texture_time_info_add', text="Time Info")           
        grid.operator('nodes.lc_utils_texture_uv_add', text="Texture UV Test")           
        grid.operator('nodes.lc_utils_texture_random_add', text="Random")           
        grid.operator('nodes.lc_utils_texture_bombing_add', text="Bombing")           
        if scene.Break_Col:
            grid.operator('null.operator_type', text="")

        return None

# LC Mapping Main 
class LUXCORE_PT_MappingPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_MappingPanel"
    bl_label = "Mapping"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 9

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        #grid.operator('nodes.lc_texture_multiple_images_add', text="Multiple Images")           
        grid.operator('nodes.lc_mapping_2d_add', text="Mapping 2D")           
        grid.operator('nodes.lc_mapping_3d_add', text="Mapping 3D")           
        grid.operator('nodes.lc_mapping_triplanar_add', text="Triplanar")           
        grid.operator('nodes.lc_mapping_triplanar_bump_add', text="Triplanar Bump")           
        grid.operator('nodes.lc_mapping_triplanar_normalmap_add', text="Triplanar Normalmap")           
        
        if scene.Break_Col:
            grid.operator('null.operator_type', text="")

        return None

# LC Light Main 
class LUXCORE_PT_LightPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_LightPanel"
    bl_label = "Light"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 10

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        #grid.operator('nodes.lc_texture_multiple_images_add', text="Multiple Images")           
        grid.operator('nodes.lc_light_emission_add', text="Emission")           
        grid.operator('nodes.lc_light_lamp_spectrum_add', text="Lamp Spectrum")           
        grid.operator('nodes.lc_light_blackbody_add', text="Blackbody")           
        grid.operator('nodes.lc_light_irregular_data_add', text="Irregular Data")           

        return None

# LC Shape Modifiers Main 
class LUXCORE_PT_ModifiersPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_ModifiersPanel"
    bl_label = "Shape Modifiers"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 11

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)
        
        grid.operator('nodes.lc_modifier_shapesubdiv_add', text="Subdivision")           
        grid.operator('nodes.lc_modifier_height_displacement_add', text="Height Displacement")           
        grid.operator('nodes.lc_modifier_vector_displacement_add', text="Vector Displacement")           
        grid.operator('nodes.lc_modifier_simplify_add', text="Simplify")           
        grid.operator('nodes.lc_modifier_harlequin_add', text="Harlequin")           

        return None

# LC Tree Pointer Main 
class LUXCORE_PT_PointerPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_PointerPanel"
    bl_label = "Pointer"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 12

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)
        
        grid.operator('nodes.lc_pointer_tree_add', text="Pointer")           

        return None

# LC Output Main 
class LUXCORE_PT_OutputPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_OutputPanel"
    bl_label = "Output"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "LUXCORE_PT_GeneralPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 13

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "luxcore_material_nodes"    


    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        #col = box.column_flow(columns=1, align=True)
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)
        
        grid.operator('nodes.lc_output_add', text="Output")           

        return None



class LUXCORE_PT_LayoutPanel(bpy.types.Panel):
    bl_idname = "LUXCORE_PT_GeneralPanel"
    bl_label = "Layout"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 14

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False


        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        # grid layout
        grid = layout.grid_flow(row_major=MajorRowRes, columns=BoolRes, align=True)

        grid.operator("nodes.layout_frame_add", text="Frame")            # Frame
        grid.operator("nodes.layout_reroute_add", text="Reroute")        # Reroute

        return None



classes_LC_PT = [
LUXCORE_PT_Shader_Utilities_Panel,
LUXCORE_PT_GeneralPanel,
LUXCORE_PT_MaterialsPanel,
LUXCORE_PT_VolumePanel,
LUXCORE_PT_TexturePanel,
LUXCORE_PT_BlenderTexturePanel,
LUXCORE_PT_MathPanel,
LUXCORE_PT_UtilsPanel,
LUXCORE_PT_MappingPanel,
LUXCORE_PT_LightPanel,
LUXCORE_PT_ModifiersPanel,
LUXCORE_PT_PointerPanel,
LUXCORE_PT_OutputPanel,
LUXCORE_PT_LayoutPanel



]