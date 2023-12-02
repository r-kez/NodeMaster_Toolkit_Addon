
import bpy

#
#____ Shader Panels ____
#

# General Toogle for split column in 2
Break_Col: bpy.props.BoolProperty(default=False)

Panel_Row_Major_Switch: bpy.props.BoolProperty(default=False, description='True = Complete line First | False = Complete Column First')
RowMajorRes = False


#General Panel List

class NODE_PT_Shader_Utilities_Panel(bpy.types.Panel):
    bl_idname = "NODE_PT_Shader_Utilities_Panel"
    bl_label = "Utilities"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'        


    # Draw Dropdown Menu
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Default Blender Nodes")

        grid = layout.grid_flow(row_major=True, columns=2, align=True)        
        grid.prop(scene, "Break_Col", text="Break Column")
        grid.prop(scene, "Panel_Row_Major_Switch", text="Row Major")


        # Add Boolean Button
        #layout.operator("node.add_boolean_socket", text="Add Boolean Button - NoWorking")

        # Add Integer Button
        #layout.operator("node.add_integer_socket", text="Add Integer Button - NoWorking")

        return None


class NODES_PT_ListPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_ListPanel"
    bl_label = "Shader Nodes List"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_order = 0

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine in {'CYCLES', 'BLENDER_EEVEE'} and context.area.ui_type == "ShaderNodeTree"    
        

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        
        row.operator("nodes.tex_image_add", text="TESTE")

#  Sub Panels Start

# Input Attributes 
class NODES_PT_InputPanelAttributes(bpy.types.Panel):
    bl_idname = "NODES_PT_InputPanelAttributes"
    bl_label = "Attributes"
    bl_context = "object"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_InputPanel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 1

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

        grid.operator("nodes.input_select_poly_add", text=".select_poly")           # select_poly        
        grid.operator("nodes.input_vs_uvmap_add", text=".vs.UVMap")                 #.vs.UVMap        
        grid.operator("nodes.input_corner_edge_add", text=".corner_edge")           #.corner_edge        
        grid.operator("nodes.input_select_vert_add", text=".select_vert")           #.select_vert        
        grid.operator("nodes.input_corner_vert_add", text=".corner_vert")           #.corner_vert        
        grid.operator("nodes.input_position_add", text="position")                  #position        
        grid.operator("nodes.input_es_uvmap_add", text=".es.UVMap")                 #.es.UVMap        
        grid.operator("nodes.input_select_edge_add", text=".select_edge")           #.select_edge        
        grid.operator("nodes.input_edge_verts_add", text=".edge_verts")             #.edge_verts        
        grid.operator("nodes.input_att_uvmap_add", text="UVMap")                    #UVMap

        return None

# Input Panel 
class NODES_PT_InputPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_InputPanel"
    bl_label = "Input"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 2

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
        # 
        grid.operator("nodes.input_ao_add", text="Amient Occlusion")                # Amient Occlusion
        grid.operator("nodes.input_attribute_add", text="Attribute")                # Attribute
        grid.operator("nodes.input_bevel_add", text="Bevel")                        # Bevel
        grid.operator("nodes.input_camera_data_add", text="Camera Data")            # Camera Data  
        grid.operator("nodes.input_vertex_color_add", text="Vertex Color")          # Vertex Color   
        grid.operator("nodes.input_curve_info_add", text="Curve Info")              # urve Info 
        grid.operator("nodes.input_fresnel_add", text="Fresnel")                    # Fresnel
        grid.operator("nodes.input_geometry_add", text="Geometry")                  # Geometry
        grid.operator("nodes.input_layer_weight_add", text="Layer Weight")          # Layer Weight
        grid.operator("nodes.input_light_path_add", text="Light Path")              # Light Path
        grid.operator("nodes.input_object_info_add", text="Object Info")            # Object Info
        grid.operator("nodes.input_particle_info_add", text="Particle Info")        # Particle Info
        grid.operator("nodes.input_point_info_add", text="Point Info")              # Point Info
        grid.operator("nodes.input_rgb_add", text="RGB")                            # RGB
        grid.operator("nodes.input_tangent_add", text="Tangent")                    # Tangent
        grid.operator("nodes.input_tex_coord_add", text="Texture Coordinates")      # Texture Coordnates     
        grid.operator("nodes.input_uv_map_add", text="UV Map")                      # UV Map
        grid.operator("nodes.input_value_add", text="Value")                        # Value
        grid.operator("nodes.input_volume_info_add", text="Volume Info")            # Volume Info
        grid.operator("nodes.input_wireframe_add", text="Wireframe")                # Wireframe

        return None

# Output SUBPANEL 
class NODES_PT_OutputPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_OutputPanel"
    bl_label = "Output"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 3
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False


        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)
        
        grid.operator("nodes.outout_aov_add", text="AOV Output")                       # AOV Output  
        grid.operator("nodes.outout_light_add", text="Light Output")                   # Light Output 
        grid.operator("nodes.outout_material_add", text="Material Output")             # Material Output

        if scene.Break_Col:
            # Null Operator for dont have empty space on the box layout
            grid.operator("null.operator_type", text="")

        else:
            return None

# COLOR SUBPANEL 
class NODES_PT_ColorPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_ColorPanel"
    bl_label = "Color"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 4

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
        
        grid.operator("nodes.color_bc_add", text="Brightness / Contrast")                   # Brightness/ Contrast        
        grid.operator("nodes.color_gamma_add", text="Gamma")                                # Gamma            
        grid.operator("nodes.color_hsv_add", text="Hue Sat. Val.")                          # Hue Saturation Value        
        grid.operator("nodes.color_invert_add", text="Invert Color")                        # Invert Color        
        grid.operator("nodes.color_light_falloff_add", text="Light Fall Off")               # Light Fall Off        
        grid.operator("nodes.color_mix_add", text="Mix Color")                              #Mix Color        
        grid.operator("nodes.color_rgb_curve_add", text="RGB Curve")                        # RGB Curve
        
        if scene.Break_Col:
            # Null Operator for dont have empty space on the box layout
            grid.operator("null.operator_type", text="")

        else:
            return None

# CONVERTER SUBPANEL 
class NODES_PT_ConvPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_ConvPanel"
    bl_label = "Converter"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 5


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "ConverterBreakTo2Col", text="Break Column")

        if scene.Panel_Row_Major_Switch:
            RowMajorRes = True
        else:
            RowMajorRes = False

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        # grid layout
        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)
        
        grid.operator("nodes.conv_blackbody_add", text="Blackbody")                 # Blackbody        
        grid.operator("nodes.conv_clamp_add", text="Clamp")                         # Clamp        
        grid.operator("nodes.conv_ramp_add", text="Color Ramp")                     # Color Ramp        
        grid.operator("nodes.conv_comb_color_add", text="Combine Color")            # Combine Color        
        grid.operator("nodes.conv_comb_xyx_add", text="Combine XYZ")                # Combine XY        
        grid.operator("nodes.conv_float_curve_add", text="Float Curve")             # Float Curve        
        grid.operator("nodes.conv_map_range_add", text="Map Range")                 # Map Range        
        grid.operator("nodes.conv_math_add", text="Math")                           # Math        
        grid.operator("nodes.conv_mix_add", text="Mix")                             # Mix        
        grid.operator("nodes.conv_rgb_to_bw_add", text="RGB to Black & White")      # RGB to Black & White        
        grid.operator("nodes.conv_separate_color_add", text="Separate Color")       # Separate Color        
        grid.operator("nodes.conv_separate_xyz_add", text="Separate XYZ")           # Separate XYZ        
        grid.operator("nodes.conv_vector_math_add", text="Vector Math")             # Vector Math        
        grid.operator("nodes.conv_wave_length_add", text="Wave Length")             # Wave Length
        grid.operator("nodes.separate_plus_combine_color", text="Separate + Combine Color")                        # RGB Curve


        return None

# Shader 
class NODES_PT_AddShaderPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_ShaderPanel"
    bl_label = "Shader"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 6

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
        
        grid.operator("nodes.shader_add_add", text="Add Shader")                            # Add Shader
        grid.operator("nodes.shader_anisotropic_add", text="Anisotropic")                   # Anisotropic
        grid.operator("nodes.shader_diff_add", text="Diffuse")                              # Diffuse
        grid.operator("nodes.shader_emission_add", text="Emission")                         # Emission
        grid.operator("nodes.shader_glass_add", text="Glass")                               # Glass
        grid.operator("nodes.shader_glossy_add", text="Glossy")                             # Glossy
        grid.operator("nodes.shader_hair_add", text="Hair")                                 # Hair
        grid.operator("nodes.shader_holdout_add", text="Holdout")                           # Holdout
        grid.operator("nodes.shader_mix_add", text="Mix Shader")                            # Mix Shader
        grid.operator("nodes.shader_principled_add", text="Principled BSDF")                # Principled BSDF
        grid.operator("nodes.shader_hair_principled_add", text="Principled Hair BSDF")      # Principled Hair BSDF
        grid.operator("nodes.shader_principled_volume_add", text="Principled Volume")       # Volume Principled
        grid.operator("nodes.shader_refraction_add", text="Refraction BSDF")                # Refraction BSDF
        grid.operator("nodes.shader_sheen_add", text="Sheen")                               # Sheen
        grid.operator("nodes.shader_sub_surf_add", text="Subsurface Scattering")            # Subsurface Scattering
        grid.operator("nodes.shader_toon_add", text="Toon")                                 # Toon
        grid.operator("nodes.shader_translucent_add", text="Translucent")                   # Translucent
        grid.operator("nodes.shader_transparent_add", text="Transparent")                   # Transparent
        grid.operator("nodes.shader_vol_abs_add", text="Volume Absorption")                 # Volume Absorptio
        grid.operator("nodes.shader_vol_scattering_add", text="Volume Scattering")          # Volume Scattering

        return None

# TEXTURE SUBPANEL 
class NODES_PT_TexturePanel(bpy.types.Panel):
    bl_idname = "NODES_PT_TexturePanel"
    bl_label = "Texture"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 7
    

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

        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        grid.operator("nodes.texture_brick_add", text="Brick")                      # Brick Texture  
        grid.operator("nodes.texture_checker_add", text="Checker")                  # Checker Texture        
        grid.operator("nodes.texture_environment_add", text="Environment")          # Environment Texture      
        grid.operator("nodes.texture_gradient_add", text="Gradient")                # Gradient Texture        
        grid.operator("nodes.texture_ies_add", text="IES")                          # IES Texture      
        grid.operator("nodes.texture_image_add", text="Image")                      # Image Texture      
        grid.operator("nodes.texture_magic_add", text="Magic")                      # Magic Texture     
        grid.operator("nodes.texture_musgrave_add", text="Musgrave")                # Musgrave Texture       
        grid.operator("nodes.texture_noise_add", text="Noise")                      # Noise Texture   
        grid.operator("nodes.texture_point_density_add", text="Point Density")      # Point Density Texture        
        grid.operator("nodes.texture_sky_add", text="Sky")                          # Sky Texture     
        grid.operator("nodes.texture_voronoi_add", text="Voronoi")                  # Voronoi Texture         
        grid.operator("nodes.texture_wave_add", text="Wave")                        # Wave Texture     
        grid.operator("nodes.texture_white_noise_add", text="White Noise")          # White Noise Texture

        return None  

# Vector SUBPANEL 
class NODES_PT_VectorPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_VectorPanel"
    bl_label = "Vector"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 8

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

        grid = layout.grid_flow(row_major=RowMajorRes, columns=BoolRes, align=True)

        grid.operator("nodes.vector_bump_add", text="Bump")                         # Bumpt
        grid.operator("nodes.displacement_add", text="Displacement")                # Displacement
        grid.operator("nodes.vector_mapping_add", text="Mapping")                   # Mapping
        grid.operator("nodes.vector_normal_add", text="Normal")                     # Normal
        grid.operator("nodes.vector_normal_map_add", text="Normal Map")             # Normal Map
        grid.operator("nodes.vector_curve_add", text="Vector Curves")               # Vector Curves
        grid.operator("nodes.vector_displacement_add", text="Vector Displacement")  # Vector Displacement
        grid.operator("nodes.vector_rotate_add", text="Vector Rotate")              # Vector Rotate
        grid.operator("nodes.vector_transform_add", text="Vector Transform")        # Vector Transform

        if scene.Break_Col:
            grid.operator("null.operator_type", text="")

        else:
            return None

# Script SUBPANEL 
class NODES_PT_ScriptNodePanel(bpy.types.Panel):
    bl_idname = "NODES_PT_ScriptNodePanel"
    bl_label = "Script"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 9
    
    def draw(self, context):
        layout = self.layout        

        layout.operator("nodes.script_add", text="Script")      # Script Add

        return None


# Layout SUBPANEL 
class NODES_PT_LayoutPanel(bpy.types.Panel):
    bl_idname = "NODES_PT_LayoutPanel"
    bl_label = "Layout"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "NODES_PT_ListPanel"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 9
    
    def draw(self, context):
        layout = self.layout

        grid = layout.grid_flow(row_major=RowMajorRes, columns=1, align=True)

        grid.operator("nodes.layout_frame_add", text="Frame")                         # Frame Add     
        grid.operator("nodes.layout_reroute_add", text="Reroute")                     # Reroute Add

        return None 



classes_Native_Nodes_PT = [
NODE_PT_Shader_Utilities_Panel,
NODES_PT_ListPanel,
NODES_PT_InputPanel,
NODES_PT_InputPanelAttributes,
NODES_PT_OutputPanel,
NODES_PT_ColorPanel,
NODES_PT_ConvPanel,
NODES_PT_AddShaderPanel,
NODES_PT_TexturePanel,
NODES_PT_VectorPanel,
NODES_PT_ScriptNodePanel,
NODES_PT_LayoutPanel
]

