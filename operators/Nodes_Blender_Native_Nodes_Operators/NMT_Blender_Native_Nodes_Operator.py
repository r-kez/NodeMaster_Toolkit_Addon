import bpy
from ..Master_op.master_op import MASTER_OT_Transform

######################################################################
#                             Color                                  #
######################################################################

#Brightness / Contrast
class NODES_OT_ColorBC_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_bc_add"
    bl_label = "Brightness / Contrast"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBrightContrast")
        return {"FINISHED"}

#Gamma
class NODES_OT_Gamma_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_gamma_add"
    bl_label = "Gamma"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeGamma")
        return {"FINISHED"}

# Hue Saturation Value
class NODES_OT_HSV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_hsv_add"
    bl_label = "Hue Saturation Value"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeHueSaturation")
        return {"FINISHED"}

# Invert Color
class NODES_OT_INVERT_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_invert_add"
    bl_label = "Invert Color"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeInvert")
        return {"FINISHED"}

# Light FallOff
class NODES_OT_LightFallOff_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_light_falloff_add"
    bl_label = "Light FallOff"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeLightFalloff")
        return {"FINISHED"}

# Mix Color
class NODES_OT_MixColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_mix_add"
    bl_label = "Mix Color"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, settings=[{"name":"data_type", "value":"'RGBA'"}], type="ShaderNodeMix")
        return {"FINISHED"}

# Mix Color
class NODES_OT_RGBCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_rgb_curve_add"
    bl_label = "RGB Curve"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeRGBCurve")
        return {"FINISHED"}


######################################################################
#                             Converter                              #
######################################################################


# Converter Blackbody
class NODES_OT_ConvBackbody_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_blackbody_add"
    bl_label = "Blackbody"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBlackbody")
        return {"FINISHED"}

# Clamp 
class NODES_OT_ConvClamp_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_clamp_add"
    bl_label = "Clamp"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeClamp")
        return {"FINISHED"}

# Converter Color Ramp 
class NODES_OT_ConvRamp_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_ramp_add"
    bl_label = "Color Ramp"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeValToRGB")
        return {"FINISHED"}    

# Converter Combine Color 
class NODES_OT_ConvCombColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_comb_color_add"
    bl_label = "Combine Color"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeCombineColor")
        return {"FINISHED"}

# Converter Combine XYZ 
class NODES_OT_ConvCombXYZ_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_comb_xyx_add"
    bl_label = "Combine XYZ"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeCombineXYZ")
        return {"FINISHED"}

# Converter Float Curve
class NODES_OT_ConvFloatCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_float_curve_add"
    bl_label = "Float Curve"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeFloatCurve")
        return {"FINISHED"}

# Converter Map Range
class NODES_OT_ConvMapRange_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_map_range_add"
    bl_label = "Map Range"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMapRange")
        return {"FINISHED"}

# Converter Math
class NODES_OT_ConvMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_math_add"
    bl_label = "Math"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMath")
        return {"FINISHED"}

# Converter Mix
class NODES_OT_ConvMix_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_mix_add"
    bl_label = "Mix"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMix")
        return {"FINISHED"}

# Converter RGB to BW
class NODES_OT_ConvRGBToBw_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_rgb_to_bw_add"
    bl_label = "RGB to BW"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeRGBToBW")
        return {"FINISHED"}

# Converter Separate Color
class NODES_OT_ConvSeparateColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_separate_color_add"
    bl_label = "Separate Color"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeSeparateColor")
        return {"FINISHED"}

# Converter Separate XYZ
class NODES_OT_ConvSeparateXYZ_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_separate_xyz_add"
    bl_label = "Separate XYZ"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeSeparateXYZ")
        return {"FINISHED"}

# Converter Vector Math
class NODES_OT_ConvVectorMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_vector_math_add"
    bl_label = "Vector Math"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorMath")
        return {"FINISHED"}

# Converter Wave Length
class NODES_OT_ConvWaveLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_wave_length_add"
    bl_label = "Wave Length"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeWavelength")
        return {"FINISHED"}

# Converter Wave Length
class NODES_OT_ConvWaveLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_wave_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeWavelength")
        return {"FINISHED"}


######################################################################
#                             Input                                  #
######################################################################


## Attribute Input ##

# .select_poly
class NODES_OT_InputSelectPoly_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_select_poly_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".select_poly")
        return {"FINISHED"}

# .vs.UVMap
class NODES_OT_InputVSUVMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_vs_uvmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".vs.UVMap")
        return {"FINISHED"}    

# .corner_edge
class NODES_OT_InputCornerEdge_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_corner_edge_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".corner_edge")
        return {"FINISHED"}     

# .select_vert
class NODES_OT_InputSelectVert_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_select_vert_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".select_vert")
        return {"FINISHED"} 

# .corner_vert
class NODES_OT_InputCornertVert_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_corner_vert_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".corner_vert")
        return {"FINISHED"}

# position
class NODES_OT_InputPosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_position_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name="position")
        return {"FINISHED"} 

# .es.UVMap
class NODES_OT_InputEsUvMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_es_uvmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".es.UVMap")
        return {"FINISHED"}     

# .select_edge
class NODES_OT_InputSelectEdge_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_select_edge_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".select_edge")
        return {"FINISHED"}     

# .edge_verts
class NODES_OT_InputEdgeVerts_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_edge_verts_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".edge_verts")
        return {"FINISHED"}  

# UVMap att
class NODES_OT_InputUVMapAtt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_att_uvmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name="UVMap")
        return {"FINISHED"}     

## Input Operators START ## 

# Ambient Occlusion
class NODES_OT_InputAO_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_ao_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeAmbientOcclusion") 
        return {"FINISHED"}     
# Attribute
class NODES_OT_InputAttribute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_attribute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeAttribute") 
        return {"FINISHED"}     
# Bevel
class NODES_OT_InputBevel_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_bevel_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeBevel") 
        return {"FINISHED"}     
# Camera Data
class NODES_OT_InputCameraData_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_camera_data_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeCameraData") 
        return {"FINISHED"}     
# Vertex Color
class NODES_OT_InputVertexColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_vertex_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeVertexColor") 
        return {"FINISHED"}                     

# Curve Info
class NODES_OT_InputCurveInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_curve_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeHairInfo") 
        return {"FINISHED"}                     

# Curve Info
class NODES_OT_InputFresnel_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_fresnel_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeFresnel") 
        return {"FINISHED"}                     

# Geometry
class NODES_OT_InputGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeNewGeometry") 
        return {"FINISHED"}                     

# Geometry
class NODES_OT_InputLayerWeight_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_layer_weight_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeLayerWeight") 
        return {"FINISHED"}                     

# Object Info
class NODES_OT_InputLightPath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_light_path_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeLightPath") 
        return {"FINISHED"}                     

# Object Info
class NODES_OT_InputObjectInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_object_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeObjectInfo") 
        return {"FINISHED"}                     

# Particle Info
class NODES_OT_InputParticleInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_particle_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeParticleInfo") 
        return {"FINISHED"}                     

# Point Info
class NODES_OT_InputPointInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_point_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodePointInfo") 
        return {"FINISHED"}                     

# RGB
class NODES_OT_InputRGB_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_rgb_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeRGB") 
        return {"FINISHED"}                     

# Tangent
class NODES_OT_InputTangent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_tangent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeTangent") 
        return {"FINISHED"}                     

# Texture Coordenates
class NODES_OT_InputTexCoord_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_tex_coord_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeTexCoord") 
        return {"FINISHED"}                     

# UV Map
class NODES_OT_InputUVMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_uv_map_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeUVMap") 
        return {"FINISHED"}     

# Value 
class NODES_OT_InputValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_value_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeValue") 
        return {"FINISHED"}     

# Volume Info
class NODES_OT_InputVolumeInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_volume_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeVolumeInfo") 
        return {"FINISHED"}     

# Wireframe
class NODES_OT_InputWireframe_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_wireframe_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeWireframe") 
        return {"FINISHED"}  


######################################################################
#                             Layout                                 #
######################################################################


# Node Frame
class NODES_OT_LayoutFrame_Add(MASTER_OT_Transform):
    bl_idname = "nodes.layout_frame_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeFrame")
        return {"FINISHED"}

# Reroute
class NODES_OT_LayoutReroute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.layout_reroute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeReroute")
        return {"FINISHED"}    


######################################################################
#                             Output                                 #
######################################################################



# AOV Output
class NODES_OT_OutAOV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.outout_aov_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeOutputAOV")
        return {"FINISHED"}

# Output Light
class NODES_OT_OutLight_Add(MASTER_OT_Transform):
    bl_idname = "nodes.outout_light_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeOutputLight")
        return {"FINISHED"}

# Output Material
class NODES_OT_OutMaterial_Add(MASTER_OT_Transform):
    bl_idname = "nodes.outout_material_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeOutputMaterial")
        return {"FINISHED"}


######################################################################
#                             Script                                 #
######################################################################


# Script
class NODES_OT_Script_Add(MASTER_OT_Transform):
    bl_idname = "nodes.script_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeScript")
        return {"FINISHED"}


######################################################################
#                             Shader                                 #
######################################################################



# Add Shader
class NODES_OT_ShaderrAdd_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_add_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeAddShader")
        return {"FINISHED"}

# BSDF Anisotropic
class NODES_OT_ShaderAniso_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_anisotropic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfAnisotropic")
        return {"FINISHED"}

# BSDF Diffuse
class NODES_OT_ShaderDiff_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_diff_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfDiffuse")
        return {"FINISHED"}

# Emission
class NODES_OT_ShaderEmission_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_emission_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeEmission")
        return {"FINISHED"}

# BSDF Glass
class NODES_OT_ShaderGlass_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_glass_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfGlass")
        return {"FINISHED"}

# BSDF Glossy
class NODES_OT_ShaderGlossy_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_glossy_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfGlossy")
        return {"FINISHED"}

# BSDF Hair
class NODES_OT_ShaderHair_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_hair_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfHair")
        return {"FINISHED"}

# Holdout
class NODES_OT_ShaderHold_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_holdout_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeHoldout")
        return {"FINISHED"}

# Mix Shader
class NODES_OT_ShaderMix_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_mix_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMixShader")
        return {"FINISHED"}

# BSDF Principled
class NODES_OT_ShaderPrincipled_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_principled_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfPrincipled")
        return {"FINISHED"}

# BSDF Principled Hair
class NODES_OT_ShaderPrincipledHair_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_hair_principled_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfHairPrincipled")
        return {"FINISHED"}

# Volume Principled
class NODES_OT_ShaderPrincipledVolume_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_principled_volume_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVolumePrincipled")
        return {"FINISHED"}

# BSDF Refraction
class NODES_OT_ShaderRefraction_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_refraction_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfRefraction")
        return {"FINISHED"}

# BSDF Sheen
class NODES_OT_ShaderSheen_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_sheen_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfSheen")
        return {"FINISHED"}

# Subsurface Scattering
class NODES_OT_ShaderSubSurf_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_sub_surf_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeSubsurfaceScattering")
        return {"FINISHED"}

# BSDF Toon
class NODES_OT_ShaderToon_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_toon_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfToon")
        return {"FINISHED"}

# BSDF Translucent
class NODES_OT_ShaderTranslucent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_translucent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfTranslucent")
        return {"FINISHED"}

# BSDF Transparent
class NODES_OT_ShaderTransparent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_transparent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfTransparent")
        return {"FINISHED"}

# Volume Absorption
class NODES_OT_ShaderVolAbsorption_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_vol_abs_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVolumeAbsorption")
        return {"FINISHED"}

# Volume Scattering
class NODES_OT_VolScattering_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_vol_scattering_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVolumeScatter")
        return {"FINISHED"}


######################################################################
#                             Texture                                #
######################################################################



# Brick Texture
class NODES_OT_TexBrick_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_brick_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexBrick")
        return {"FINISHED"}

# Checker Texture
class NODES_OT_TexCheck_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_checker_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexChecker")
        return {"FINISHED"}

# Environment Texture
class NODES_OT_TexEnvironment_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_environment_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexEnvironment")
        return {"FINISHED"}

# Environment Texture
class NODES_OT_TexGradient_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_gradient_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexGradient")
        return {"FINISHED"}

# IES Texture
class NODES_OT_TexIES_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_ies_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexIES")
        return {"FINISHED"}

# Image Texture
class NODES_OT_TexImage_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_image_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexImage")
        return {"FINISHED"}

# Magic Texture
class NODES_OT_TexMagic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_magic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexMagic")
        return {"FINISHED"}

# Musgrave Texture
class NODES_OT_TexMusgrave_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_musgrave_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexMusgrave")
        return {"FINISHED"}

# Noise Texture
class NODES_OT_TexNoise_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_noise_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexNoise")
        return {"FINISHED"}

# Point Density Texture
class NODES_OT_TexPointDensity_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_point_density_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexPointDensity")
        return {"FINISHED"}

# Sky Texture
class NODES_OT_TexSky_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_sky_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexSky")
        return {"FINISHED"}

# Voronoi Texture
class NODES_OT_TexVoronoi_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_voronoi_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexVoronoi")
        return {"FINISHED"}

# Wave Texture
class NODES_OT_TexWave_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_wave_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexWave")
        return {"FINISHED"}

# Wave Texture
class NODES_OT_TexWhiteNoise_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_white_noise_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexWhiteNoise")
        return {"FINISHED"}


######################################################################
#                             Vector                                 #
######################################################################



# Bump
class NODES_OT_VectorBump_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_bump_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "BANANA"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBump")
        return {"FINISHED"}

# Displacement
class NODES_OT_Displacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.displacement_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeDisplacement")
        return {"FINISHED"}

# Mapping
class NODES_OT_VectorMapping_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_mapping_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMapping")
        return {"FINISHED"}

# Normal
class NODES_OT_VectorNormal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_normal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeNormal")
        return {"FINISHED"}

# Normal Map
class NODES_OT_VectorNormalMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_normal_map_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeNormalMap")
        return {"FINISHED"}

# Vector Curves
class NODES_OT_VectorCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorCurve")
        return {"FINISHED"}

# Vector Displacement
class NODES_OT_VectorDisplacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_displacement_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorDisplacement")
        return {"FINISHED"}

# Vector Rotate
class NODES_OT_VectorRotate_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_rotate_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorRotate")
        return {"FINISHED"}

# Vector Transform
class NODES_OT_VectorTransform_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_transform_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorTransform")
        return {"FINISHED"}


classes_Native_Nodes_All = [
# Color    
NODES_OT_ColorBC_Add,
NODES_OT_Gamma_Add,
NODES_OT_HSV_Add,
NODES_OT_INVERT_Add,
NODES_OT_LightFallOff_Add,
NODES_OT_MixColor_Add,
NODES_OT_RGBCurve_Add,
# Converter
NODES_OT_ConvBackbody_Add,
NODES_OT_ConvClamp_Add,
NODES_OT_ConvRamp_Add,
NODES_OT_ConvCombColor_Add,
NODES_OT_ConvCombXYZ_Add,
NODES_OT_ConvFloatCurve_Add,
NODES_OT_ConvMapRange_Add,
NODES_OT_ConvMath_Add,
NODES_OT_ConvMix_Add,
NODES_OT_ConvRGBToBw_Add,
NODES_OT_ConvSeparateColor_Add,
NODES_OT_ConvSeparateXYZ_Add,
NODES_OT_ConvVectorMath_Add,
NODES_OT_ConvWaveLength_Add,    
# Input
NODES_OT_InputSelectPoly_Add,
NODES_OT_InputVSUVMap_Add,
NODES_OT_InputCornerEdge_Add,
NODES_OT_InputSelectVert_Add,
NODES_OT_InputCornertVert_Add,
NODES_OT_InputPosition_Add,
NODES_OT_InputEsUvMap_Add,
NODES_OT_InputSelectEdge_Add,
NODES_OT_InputEdgeVerts_Add,
NODES_OT_InputUVMapAtt_Add,
# Input Operators
NODES_OT_InputAO_Add,
NODES_OT_InputAttribute_Add,
NODES_OT_InputBevel_Add,
NODES_OT_InputCameraData_Add,
NODES_OT_InputVertexColor_Add,
NODES_OT_InputCurveInfo_Add,
NODES_OT_InputFresnel_Add,
NODES_OT_InputGeometry_Add,
NODES_OT_InputLayerWeight_Add,
NODES_OT_InputLightPath_Add,
NODES_OT_InputObjectInfo_Add,
NODES_OT_InputParticleInfo_Add,
NODES_OT_InputPointInfo_Add,
NODES_OT_InputRGB_Add,
NODES_OT_InputTangent_Add,
NODES_OT_InputTexCoord_Add,
NODES_OT_InputUVMap_Add,
NODES_OT_InputValue_Add,
NODES_OT_InputVolumeInfo_Add,
NODES_OT_InputWireframe_Add,  
# Layout
NODES_OT_LayoutFrame_Add, 
NODES_OT_LayoutReroute_Add,
# Output
NODES_OT_OutAOV_Add,
NODES_OT_OutLight_Add, 
NODES_OT_OutMaterial_Add,   
# Script
NODES_OT_Script_Add,   
# Shader
NODES_OT_ShaderrAdd_Add,
NODES_OT_ShaderAniso_Add,
NODES_OT_ShaderDiff_Add,
NODES_OT_ShaderEmission_Add,
NODES_OT_ShaderGlass_Add,
NODES_OT_ShaderGlossy_Add,
NODES_OT_ShaderHair_Add,
NODES_OT_ShaderHold_Add,
NODES_OT_ShaderMix_Add,
NODES_OT_ShaderPrincipled_Add,
NODES_OT_ShaderPrincipledHair_Add,
NODES_OT_ShaderPrincipledVolume_Add,
NODES_OT_ShaderRefraction_Add,
NODES_OT_ShaderSheen_Add,
NODES_OT_ShaderSubSurf_Add,
NODES_OT_ShaderToon_Add,
NODES_OT_ShaderTranslucent_Add,
NODES_OT_ShaderTransparent_Add,
NODES_OT_ShaderVolAbsorption_Add,
NODES_OT_VolScattering_Add,   
# TExture
NODES_OT_TexBrick_Add,
NODES_OT_TexCheck_Add,
NODES_OT_TexEnvironment_Add,
NODES_OT_TexGradient_Add,
NODES_OT_TexIES_Add,
NODES_OT_TexImage_Add,
NODES_OT_TexMagic_Add,
NODES_OT_TexMusgrave_Add,
NODES_OT_TexNoise_Add,
NODES_OT_TexPointDensity_Add,
NODES_OT_TexSky_Add,
NODES_OT_TexVoronoi_Add,
NODES_OT_TexWave_Add,
NODES_OT_TexWhiteNoise_Add,
# Vector
NODES_OT_VectorBump_Add,
NODES_OT_Displacement_Add,
NODES_OT_VectorMapping_Add,
NODES_OT_VectorNormal_Add,
NODES_OT_VectorNormalMap_Add,
NODES_OT_VectorCurve_Add,
NODES_OT_VectorDisplacement_Add,
NODES_OT_VectorRotate_Add,
NODES_OT_VectorTransform_Add  
]