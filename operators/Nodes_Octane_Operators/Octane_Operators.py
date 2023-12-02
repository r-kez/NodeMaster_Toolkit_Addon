import bpy
from ..Master_op.master_op import MASTER_OT_Transform


############################################################
#                     GENERAL NODES                        #
############################################################
# Output - 1 Item
class NODES_OT_OctaneOutputAOVGroupOutputNode_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_output_aov_group_output_node_add"
    bl_label = "Octane Render AOV Output"
    bl_description = "Add Octane Render AOV Output Node"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneRenderAOVOutputNode")
        return {"FINISHED"}

# Octane Advanced Tools - 4 Itens
class NODES_OT_OctaneCameraData_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_camera_data_add"
    bl_label = "Octane Camera Data"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )


    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneCameraData")
        return {"FINISHED"}

class NODES_OT_OctaneObjectData_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_object_data_add"
    bl_label = "Octane Object Data"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneObjectData")
        return {"FINISHED"}


class NODES_OT_OctaneProxy_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_proxy_add"
    bl_label = "Octane Proxy"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneProxy")
        return {"FINISHED"}    

# Octane Render Settings - 2 Itens
class NODES_OT_OctaneCameraImager_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_camera_imager_add"
    bl_label = "Octane Camera Imager"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneCameraImager")
        return {"FINISHED"}

class NODES_OT_OctaneOCIOColorSpace_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_ocio_color_space_add"
    bl_label = "Octane OCIO Color Space"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOCIOColorSpace")
        return {"FINISHED"}    

###############################################################

## VALUES 25 Itens - No SubPanels
class NODES_OT_OctaneBoolValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_bool_value_add"
    bl_label = "Octane Bool Value"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneBoolValue")
        return {"FINISHED"}

class NODES_OT_OctaneIntValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_int_value_add"
    bl_label = "Octane Int Value"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneIntValue")
        return {"FINISHED"}

class NODES_OT_OctaneFloatValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_float_value_add"
    bl_label = "Octane Float Value"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneFloatValue")
        return {"FINISHED"}

class NODES_OT_OctaneStringValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_string_value_add"
    bl_label = "Octane String Value"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneStringValue")
        return {"FINISHED"}

class NODES_OT_OctaneLightIDBitValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_light_id_bit_value_add"
    bl_label = "Octane Light ID Bit Value"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneLightIDBitValue")
        return {"FINISHED"}

class NODES_OT_OctaneSunDirection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_sun_direction_add"
    bl_label = "Octane Sun Direction"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneSunDirection")
        return {"FINISHED"}

# Converter
class NODES_OT_OctaneConverterFloatToInt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_converter_float_to_int_add"
    bl_label = "Octane Converter Float to Int"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneConverterFloatToInt")
        return {"FINISHED"}

class NODES_OT_OctaneConverterIntToFloat_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_converter_int_to_float_add"
    bl_label = "Octane Converter Int to Float"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneConverterIntToFloat")
        return {"FINISHED"}

# Operators
class NODES_OT_OctaneOperatorBinaryMathOperation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_binary_math_operation_add"
    bl_label = "Octane Operator Binary Math Operation"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorBinaryMathOperation")
        return {"FINISHED"}

class NODES_OT_OctaneOperatorBooleanLogicOperator_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_boolean_logic_operator_add"
    bl_label = "Octane Operator Boolean Logic Operator"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorBooleanLogicOperator")
        return {"FINISHED"}

class NODES_OT_OctaneOperatorFloatRelationalOperator_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_float_relational_operator_add"
    bl_label = "Octane Operator Float Relational Operator"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorFloatRelationalOperator")
        return {"FINISHED"}

class NODES_OT_OctaneOperatorIntRelationalOperator_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_int_relational_operator_add"
    bl_label = "Octane Operator Int Relational Operator"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorIntRelationalOperator")
        return {"FINISHED"}

class NODES_OT_OctaneOperatorRange_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_range_add"
    bl_label = "Octane Operator Range"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorRange")
        return {"FINISHED"}

class NODES_OT_OctaneOperatorRotate_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_rotate_add"
    bl_label = "Octane Operator Rotate"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorRotate")
        return {"FINISHED"}

class NODES_OT_OctaneOperatorUnaryMathOperation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_operator_unary_math_operation_add"
    bl_label = "Octane Operator Unary Math Operation"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOperatorUnaryMathOperation")
        return {"FINISHED"}

class NODES_OT_OctaneBoolSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_bool_switch_add"
    bl_label = "Octane Bool Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneBoolSwitch")
        return {"FINISHED"}

class NODES_OT_OctaneFloatSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_float_switch_add"
    bl_label = "Octane Float Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneFloatSwitch")
        return {"FINISHED"}

class NODES_OT_OctaneIntSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_int_switch_add"
    bl_label = "Octane Int Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneIntSwitch")
        return {"FINISHED"}

class NODES_OT_OctaneStringSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_string_switch_add"
    bl_label = "Octane String Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneStringSwitch")
        return {"FINISHED"}

class NODES_OT_OctaneUtilityFloatComponentPicker_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_utility_float_component_picker_add"
    bl_label = "Octane Utility Float Component Picker"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneUtilityFloatComponentPicker")
        return {"FINISHED"}

class NODES_OT_OctaneUtilityFloatIf_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_utility_float_if_add"
    bl_label = "Octane Utility Float If"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneUtilityFloatIf")
        return {"FINISHED"}

class NODES_OT_OctaneUtilityFloatMerger_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_utility_float_merger_add"
    bl_label = "Octane Utility Float Merger"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneUtilityFloatMerger")
        return {"FINISHED"}

class NODES_OT_OctaneUtilityIntComponentPicker_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_utility_int_component_picker_add"
    bl_label = "Octane Utility Int Component Picker"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneUtilityIntComponentPicker")
        return {"FINISHED"}

class NODES_OT_OctaneUtilityIntIf_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_utility_int_if_add"
    bl_label = "Octane Utility Int If"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneUtilityIntIf")
        return {"FINISHED"}


###################################################################################    


# Octane Displacement - 4 Itens
class NODES_OT_OctaneTextureDisplacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_texture_displacement_add"
    bl_label = "Octane Texture Displacement"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneTextureDisplacement")
        return {"FINISHED"}

class NODES_OT_OctaneVertexDisplacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_vertex_displacement_add"
    bl_label = "Octane Vertex Displacement"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVertexDisplacement")
        return {"FINISHED"}

class NODES_OT_OctaneVertexDisplacementMixer_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_vertex_displacement_mixer_add"
    bl_label = "Octane Vertex Displacement Mixer"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVertexDisplacementMixer")
        return {"FINISHED"}

class NODES_OT_OctaneDisplacementSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_displacement_switch_add"
    bl_label = "Octane Displacement Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDisplacementSwitch")
        return {"FINISHED"}

# PROJECTION 15 ITENS
class NODES_OT_OctaneBox_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_box_add"
    bl_label = "Octane Box"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneBox")
        return {"FINISHED"}

class NODES_OT_OctaneColorToUVW_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_color_to_uvw_add"
    bl_label = "Octane Color To UVW"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneColorToUVW")
        return {"FINISHED"}

class NODES_OT_OctaneCylindrical_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_cylindrical_add"
    bl_label = "Octane Cylindrical"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneCylindrical")
        return {"FINISHED"}

class NODES_OT_OctaneDistortedMeshUV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_distorted_mesh_uv_add"
    bl_label = "Octane Distorted Mesh UV"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDistortedMeshUV")
        return {"FINISHED"}

class NODES_OT_OctaneInstancePosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_instance_position_add"
    bl_label = "Octane Instance Position"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneInstancePosition")
        return {"FINISHED"}

class NODES_OT_OctaneMatCap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_matcap_add"
    bl_label = "Octane MatCap"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneMatCap")
        return {"FINISHED"}

class NODES_OT_OctaneMeshUVProjection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_mesh_uv_projection_add"
    bl_label = "Octane Mesh UV Projection"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneMeshUVProjection")
        return {"FINISHED"}

class NODES_OT_OctaneOSLDelayedUV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_osl_delayed_uv_add"
    bl_label = "Octane OSL Delayed UV"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOSLDelayedUV")
        return {"FINISHED"}

class NODES_OT_OctaneOSLProjection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_osl_projection_add"
    bl_label = "Octane OSL Projection"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOSLProjection")
        return {"FINISHED"}

class NODES_OT_OctanePerspective_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_perspective_add"
    bl_label = "Octane Perspective"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctanePerspective")
        return {"FINISHED"}

class NODES_OT_OctaneSamplePosToUV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_sample_pos_to_uv_add"
    bl_label = "Octane Sample Pos To UV"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneSamplePosToUV")
        return {"FINISHED"}

class NODES_OT_OctaneSpherical_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_spherical_add"
    bl_label = "Octane Spherical"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneSpherical")
        return {"FINISHED"}

class NODES_OT_OctaneTriplanar_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_triplanar_add"
    bl_label = "Octane Triplanar"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneTriplanar")
        return {"FINISHED"}

class NODES_OT_OctaneXYZToUVW_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_xyz_to_uvw_add"
    bl_label = "Octane XYZ To UVW"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneXYZToUVW")
        return {"FINISHED"}

class NODES_OT_OctaneProjectionSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_projection_switch_add"
    bl_label = "Octane Projection Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneProjectionSwitch")
        return {"FINISHED"}

##################################################################################

# TRANSFORM 7 Itens
class NODES_OT_Octane2DTransformation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_2d_transformation_add"
    bl_label = "Octane 2D Transformation"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="Octane2DTransformation")
        return {"FINISHED"}

class NODES_OT_Octane3DTransformation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_3d_transformation_add"
    bl_label = "Octane 3D Transformation"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="Octane3DTransformation")
        return {"FINISHED"}

class NODES_OT_OctaneConverterLookAtTransform_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_converter_look_at_transform_add"
    bl_label = "Octane Converter Look At Transform"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneConverterLookAtTransform")
        return {"FINISHED"}

class NODES_OT_OctaneRotation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_rotation_add"
    bl_label = "Octane Rotation"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneRotation")
        return {"FINISHED"}

class NODES_OT_OctaneScale_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_scale_add"
    bl_label = "Octane Scale"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneScale")
        return {"FINISHED"}

class NODES_OT_OctaneTransformValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_transform_value_add"
    bl_label = "Octane Transform Value"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneTransformValue")
        return {"FINISHED"}

class NODES_OT_OctaneTransformSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.octane_transform_switch_add"
    bl_label = "Octane Transform Switch"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneTransformSwitch")
        return {"FINISHED"}

##########################################################################################
#                                  COMPOSITE EXCLUSIVE                                   #
##########################################################################################

# Octane Blending Settings
class OctaneBlendingSettingsOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_blending_settings"
    bl_label = "Octane Blending Settings"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneBlendingSettings")
        return {'FINISHED'}

# Octane Output AOVs Output AOV
class OctaneOutputAOVsOutputAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_output_aov"
    bl_label = "Octane Output AOVs Output AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsOutputAOV")
        return {'FINISHED'}

# Octane Output AOVs Output AOV Group
class OctaneOutputAOVsOutputAOVGroupOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_output_aov_group"
    bl_label = "Octane Output AOVs Output AOV Group"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsOutputAOVGroup")
        return {'FINISHED'}

class OctaneOutputAOVsImageFileOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_image_file"
    bl_label = "Octane Output AOVs Image File"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsImageFile")
        return {'FINISHED'}

class OctaneOutputAOVsLayerGroupOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_layer_group"
    bl_label = "Octane Output AOVs Layer Group"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsLayerGroup")
        return {'FINISHED'}

class OctaneOutputAOVsRenderAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_render_aov"
    bl_label = "Octane Output AOVs Render AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsRenderAOV")
        return {'FINISHED'}

class OctaneOutputAOVsSolidColorOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_solid_color"
    bl_label = "Octane Output AOVs Solid Color"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsSolidColor")
        return {'FINISHED'}

class OctaneOutputAOVsAdjustBrightnessOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_adjust_brightness"
    bl_label = "Octane Output AOVs Adjust Brightness"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAdjustBrightness")
        return {'FINISHED'}

class OctaneOutputAOVsAdjustContrastSDROnlyOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_adjust_contrast_sdr_only"
    bl_label = "Octane Output AOVs Adjust Contrast SDR Only"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAdjustContrastSDROnly")
        return {'FINISHED'}

class OctaneOutputAOVsAdjustHueOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_adjust_hue"
    bl_label = "Octane Output AOVs Adjust Hue"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAdjustHue")
        return {'FINISHED'}

class OctaneOutputAOVsAdjustSaturationOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_adjust_saturation"
    bl_label = "Octane Output AOVs Adjust Saturation"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAdjustSaturation")
        return {'FINISHED'}

class OctaneOutputAOVsAdjustWhiteBalanceOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_adjust_white_balance"
    bl_label = "Octane Output AOVs Adjust White Balance"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAdjustWhiteBalance")
        return {'FINISHED'}

class OctaneOutputAOVsApplyCameraResponseCurveSDROnlyOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_apply_camera_response_curve_sdr_only"
    bl_label = "Octane Output AOVs Apply Camera Response Curve SDR Only"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsApplyCameraResponseCurveSDROnly")
        return {'FINISHED'}

class OctaneOutputAOVsApplyCustomCurveOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_apply_custom_curve"
    bl_label = "Octane Output AOVs Apply Custom Curve"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsApplyCustomCurve")
        return {'FINISHED'}

class OctaneOutputAOVsApplyGammaCurveSDROnlyOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_apply_gamma_curve_sdr_only"
    bl_label = "Octane Output AOVs Apply Gamma Curve SDR Only"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsApplyGammaCurveSDROnly")
        return {'FINISHED'}

class OctaneOutputAOVsApplyLUTOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_apply_lut"
    bl_label = "Octane Output AOVs Apply LUT"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsApplyLUT")
        return {'FINISHED'}

class OctaneOutputAOVsApplyOCIOLookOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_apply_ocio_look"
    bl_label = "Octane Output AOVs Apply OCIO Look"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsApplyOCIOLook")
        return {'FINISHED'}

class OctaneOutputAOVsChannelClampOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_channel_clamp"
    bl_label = "Octane Output AOVs Channel Clamp"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsChannelClamp")
        return {'FINISHED'}

class OctaneOutputAOVsChannelInvertSDROnlyOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_channel_invert_sdr_only"
    bl_label = "Octane Output AOVs Channel Invert SDR Only"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsChannelInvertSDROnly")
        return {'FINISHED'}

class OctaneOutputAOVsChannelMapRangeOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_channel_map_range"
    bl_label = "Octane Output AOVs Channel Map Range"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsChannelMapRange")
        return {'FINISHED'}

# Effects - Display -- 5 Itens
class OctaneOutputAOVsConvertForSDRDisplayACESOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_convert_for_sdr_display_aces"
    bl_label = "Octane Output AOVs Convert for SDR Display ACES"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsConvertForSDRDisplayACES")
        return {'FINISHED'}

class OctaneOutputAOVsConvertForSDRDisplayAgXOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_convert_for_sdr_display_agx"
    bl_label = "Octane Output AOVs Convert for SDR Display AgX"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsConvertForSDRDisplayAgX")
        return {'FINISHED'}

class OctaneOutputAOVsConvertForSDRDisplayBasicOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_convert_for_sdr_display_basic"
    bl_label = "Octane Output AOVs Convert for SDR Display Basic"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsConvertForSDRDisplayBasic")
        return {'FINISHED'}

class OctaneOutputAOVsConvertForSDRDisplayOCIOOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_convert_for_sdr_display_ocio"
    bl_label = "Octane Output AOVs Convert for SDR Display OCIO"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsConvertForSDRDisplayOCIO")
        return {'FINISHED'}

class OctaneOutputAOVsConvertForSDRDisplaySmoothOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_convert_for_sdr_display_smooth"
    bl_label = "Octane Output AOVs Convert for SDR Display Smooth"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsConvertForSDRDisplaySmooth")
        return {'FINISHED'}

## Effects - Opacity -- 3 Itens
class OctaneOutputAOVsAdjustOpacityOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_adjust_opacity"
    bl_label = "Octane Output AOVs Adjust Opacity"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAdjustOpacity")
        return {'FINISHED'}

class OctaneOutputAOVsMaskWithCryptomatteOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_mask_with_cryptomatte"
    bl_label = "Octane Output AOVs Mask with Cryptomatte"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsMaskWithCryptomatte")
        return {'FINISHED'}

class OctaneOutputAOVsMaskWithLayerGroupOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_mask_with_layer_group"
    bl_label = "Octane Output AOVs Mask with Layer Group"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsMaskWithLayerGroup")
        return {'FINISHED'}

## Effects - Processing -- 7 Itens

class OctaneOutputAOVsAddBloomOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_add_bloom"
    bl_label = "Octane Output AOVs Add Bloom"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAddBloom")
        return {'FINISHED'}

class OctaneOutputAOVsAddChromaticAberrationOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_add_chromatic_aberration"
    bl_label = "Octane Output AOVs Add Chromatic Aberration"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAddChromaticAberration")
        return {'FINISHED'}

class OctaneOutputAOVsAddGlareOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_add_glare"
    bl_label = "Octane Output AOVs Add Glare"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAddGlare")
        return {'FINISHED'}

class OctaneOutputAOVsAddLensFlareOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_add_lens_flare"
    bl_label = "Octane Output AOVs Add Lens Flare"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAddLensFlare")
        return {'FINISHED'}

class OctaneOutputAOVsAddVignetteOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_add_vignette"
    bl_label = "Octane Output AOVs Add Vignette"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsAddVignette")
        return {'FINISHED'}

class OctaneOutputAOVsBlurOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_blur"
    bl_label = "Octane Output AOVs Blur"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsBlur")
        return {'FINISHED'}

class OctaneOutputAOVsRemoveHotPixelsOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_remove_hot_pixels"
    bl_label = "Octane Output AOVs Remove Hot Pixels"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsRemoveHotPixels")
        return {'FINISHED'}

## Legacy -- 1 Item
class OctaneOutputAOVsLightMixerOutputAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_light_mixer_output_aov"
    bl_label = "Octane Output AOVs Light Mixer Output AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsLightMixerOutputAOV")
        return {'FINISHED'}


class OctaneBlendingSettingsSwitchOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_blending_settings_switch"
    bl_label = "Octane Blending Settings Switch"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneBlendingSettingsSwitch")
        return {'FINISHED'}

class OctaneOutputAOVGroupSwitchOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aov_group_switch"
    bl_label = "Octane Output AOV Group Switch"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVGroupSwitch")
        return {'FINISHED'}

class OctaneOutputAOVLayerSwitchOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aov_layer_switch"
    bl_label = "Octane Output AOV Layer Switch"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVLayerSwitch")
        return {'FINISHED'}

class OctaneOutputAOVSwitchOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aov_switch"
    bl_label = "Octane Output AOV Switch"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVSwitch")
        return {'FINISHED'}

class OctaneOutputAOVsLayerGroupPassThroughOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_output_aovs_layer_group_pass_through"
    bl_label = "Octane Output AOVs Layer Group Pass Through"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneOutputAOVsLayerGroupPassThrough")
        return {'FINISHED'}

######################################################################################
####      bpy.context.area.ui_type = 'octane_render_aov_nodes' EXCLUSIVE         #####
######################################################################################

# Render AOV -- 2 Itens + 8 Lists
class OctaneRenderAOVGroupOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_render_aov_group"
    bl_label = "Octane Render AOV Group"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneRenderAOVGroup")
        return {'FINISHED'}

class OctaneRenderAOVSwitchOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_render_aov_switch"
    bl_label = "Octane Render AOV Switch"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneRenderAOVSwitch")
        return {'FINISHED'}

class OctaneCryptomatteAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_cryptomatte_aov"
    bl_label = "Octane Cryptomatte AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneCryptomatteAOV")
        return {'FINISHED'}

class OctaneIrradianceAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_irradiance_aov"
    bl_label = "Octane Irradiance AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneIrradianceAOV")
        return {'FINISHED'}

class OctaneLightDirectionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_light_direction_aov"
    bl_label = "Octane Light Direction AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneLightDirectionAOV")
        return {'FINISHED'}

class OctaneNoiseAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_noise_aov"
    bl_label = "Octane Noise AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneNoiseAOV")
        return {'FINISHED'}

class OctanePostProcessingAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_post_processing_aov"
    bl_label = "Octane Post Processing AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctanePostProcessingAOV")
        return {'FINISHED'}

class OctanePostfxMediaAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_postfx_media_aov"
    bl_label = "Octane Postfx Media AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctanePostfxMediaAOV")
        return {'FINISHED'}

class OctaneShadowAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_shadow_aov"
    bl_label = "Octane Shadow AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneShadowAOV")
        return {'FINISHED'}

## Beauty surfaces
class OctaneDiffuseAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_diffuse_aov"
    bl_label = "Octane Diffuse AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDiffuseAOV")
        return {'FINISHED'}

class OctaneDiffuseDirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_diffuse_direct_aov"
    bl_label = "Octane Diffuse Direct AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDiffuseDirectAOV")
        return {'FINISHED'}

class OctaneDiffuseFilterBeautyAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_diffuse_filter_beauty_aov"
    bl_label = "Octane Diffuse Filter (Beauty) AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDiffuseFilterBeautyAOV")
        return {'FINISHED'}

class OctaneDiffuseIndirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_diffuse_indirect_aov"
    bl_label = "Octane Diffuse Indirect AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDiffuseIndirectAOV")
        return {'FINISHED'}

class OctaneEmittersAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_emitters_aov"
    bl_label = "Octane Emitters AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneEmittersAOV")
        return {'FINISHED'}

class OctaneEnvironmentAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_environment_aov"
    bl_label = "Octane Environment AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneEnvironmentAOV")
        return {'FINISHED'}

class OctaneReflectionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_reflection_aov"
    bl_label = "Octane Reflection AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneReflectionAOV")
        return {'FINISHED'}

class OctaneReflectionDirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_reflection_direct_aov"
    bl_label = "Octane Reflection Direct AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneReflectionDirectAOV")
        return {'FINISHED'}

class OctaneReflectionFilterBeautyAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_reflection_filter_beauty_aov"
    bl_label = "Octane Reflection Filter (Beauty) AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneReflectionFilterBeautyAOV")
        return {'FINISHED'}

class OctaneReflectionIndirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_reflection_indirect_aov"
    bl_label = "Octane Reflection Indirect AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneReflectionIndirectAOV")
        return {'FINISHED'}

class OctaneRefractionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_refraction_aov"
    bl_label = "Octane Refraction AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneRefractionAOV")
        return {'FINISHED'}

class OctaneRefractionFilterBeautyAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_refraction_filter_beauty_aov"
    bl_label = "Octane Refraction Filter (Beauty) AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneRefractionFilterBeautyAOV")
        return {'FINISHED'}

class OctaneSubsurfaceScatteringAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_subsurface_scattering_aov"
    bl_label = "Octane Subsurface Scattering AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneSubsurfaceScatteringAOV")
        return {'FINISHED'}

class OctaneTransmissionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_transmission_aov"
    bl_label = "Octane Transmission AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneTransmissionAOV")
        return {'FINISHED'}

class OctaneTransmissionFilterBeautyAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_transmission_filter_beauty_aov"
    bl_label = "Octane Transmission Filter (Beauty) AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneTransmissionFilterBeautyAOV")
        return {'FINISHED'}

## Beauty volumes
class OctaneVolumeAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_volume_aov"
    bl_label = "Octane Volume AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVolumeAOV")
        return {'FINISHED'}

class OctaneVolumeEmissionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_volume_emission_aov"
    bl_label = "Octane Volume Emission AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVolumeEmissionAOV")
        return {'FINISHED'}

class OctaneVolumeMaskAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_volume_mask_aov"
    bl_label = "Octane Volume Mask AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVolumeMaskAOV")
        return {'FINISHED'}

class OctaneVolumeZDepthBackAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_volume_zdepth_back_aov"
    bl_label = "Octane Volume Z-Depth Back AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVolumeZDepthBackAOV")
        return {'FINISHED'}

class OctaneVolumeZDepthFrontAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_volume_zdepth_front_aov"
    bl_label = "Octane Volume Z-Depth Front AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneVolumeZDepthFrontAOV")
        return {'FINISHED'}

## Custom
class OctaneCustomAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_custom_aov"
    bl_label = "Octane Custom AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneCustomAOV")
        return {'FINISHED'}

class OctaneGlobalTextureAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_global_texture_aov"
    bl_label = "Octane Global Texture AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneGlobalTextureAOV")
        return {'FINISHED'}

## Denoised
class OctaneDenoisedDiffuseDirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_diffuse_direct_aov"
    bl_label = "Octane Denoised Diffuse Direct AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedDiffuseDirectAOV")
        return {'FINISHED'}

class OctaneDenoisedDiffuseIndirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_diffuse_indirect_aov"
    bl_label = "Octane Denoised Diffuse Indirect AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedDiffuseIndirectAOV")
        return {'FINISHED'}

class OctaneDenoisedEmissionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_emission_aov"
    bl_label = "Octane Denoised Emission AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedEmissionAOV")
        return {'FINISHED'}

class OctaneDenoisedReflectionDirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_reflection_direct_aov"
    bl_label = "Octane Denoised Reflection Direct AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedReflectionDirectAOV")
        return {'FINISHED'}

class OctaneDenoisedReflectionIndirectAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_reflection_indirect_aov"
    bl_label = "Octane Denoised Reflection Indirect AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedReflectionIndirectAOV")
        return {'FINISHED'}

class OctaneDenoisedRemainderAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_remainder_aov"
    bl_label = "Octane Denoised Remainder AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedRemainderAOV")
        return {'FINISHED'}

class OctaneDenoisedVolumeAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_volume_aov"
    bl_label = "Octane Denoised Volume AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedVolumeAOV")
        return {'FINISHED'}

class OctaneDenoisedVolumeEmissionAOVOperator(MASTER_OT_Transform):
    bl_idname = "node.octane_denoised_volume_emission_aov"
    bl_label = "Octane Denoised Volume Emission AOV"
    
    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="OctaneDenoisedVolumeEmissionAOV")
        return {'FINISHED'}

classes_Octane_OT = [
    OctaneDiffuseAOVOperator,
    OctaneDiffuseDirectAOVOperator,
    OctaneDiffuseFilterBeautyAOVOperator,
    OctaneDiffuseIndirectAOVOperator,
    OctaneEmittersAOVOperator,
    OctaneEnvironmentAOVOperator,
    OctaneReflectionAOVOperator,
    OctaneCryptomatteAOVOperator,
    OctaneIrradianceAOVOperator,
    OctaneLightDirectionAOVOperator,
    OctaneNoiseAOVOperator,
    OctanePostProcessingAOVOperator,
    OctanePostfxMediaAOVOperator,
    OctaneShadowAOVOperator,
    OctaneReflectionDirectAOVOperator,
    OctaneReflectionFilterBeautyAOVOperator,
    OctaneReflectionIndirectAOVOperator,
    OctaneRefractionAOVOperator,
    OctaneRefractionFilterBeautyAOVOperator,
    OctaneSubsurfaceScatteringAOVOperator,
    OctaneTransmissionAOVOperator,
    OctaneTransmissionFilterBeautyAOVOperator,
    OctaneVolumeAOVOperator,
    OctaneVolumeEmissionAOVOperator,
    OctaneVolumeMaskAOVOperator,
    OctaneVolumeZDepthBackAOVOperator,
    OctaneVolumeZDepthFrontAOVOperator,
    OctaneCustomAOVOperator,
    OctaneGlobalTextureAOVOperator,
    OctaneBlendingSettingsOperator,
    OctaneOutputAOVsOutputAOVOperator,
    OctaneOutputAOVsOutputAOVGroupOperator,
    OctaneOutputAOVsImageFileOperator,
    OctaneOutputAOVsLayerGroupOperator,
    OctaneOutputAOVsRenderAOVOperator,
    OctaneOutputAOVsSolidColorOperator,
    OctaneOutputAOVsAdjustBrightnessOperator,
    OctaneOutputAOVsAdjustContrastSDROnlyOperator,
    OctaneOutputAOVsAdjustHueOperator,
    OctaneOutputAOVsAdjustSaturationOperator,
    OctaneOutputAOVsAdjustWhiteBalanceOperator,
    OctaneOutputAOVsApplyCameraResponseCurveSDROnlyOperator,
    OctaneOutputAOVsApplyCustomCurveOperator,
    OctaneOutputAOVsApplyGammaCurveSDROnlyOperator,
    OctaneOutputAOVsApplyLUTOperator,
    OctaneOutputAOVsApplyOCIOLookOperator,
    OctaneOutputAOVsChannelClampOperator,
    OctaneOutputAOVsChannelInvertSDROnlyOperator,
    OctaneOutputAOVsChannelMapRangeOperator,
    OctaneOutputAOVsConvertForSDRDisplayACESOperator,
    OctaneOutputAOVsConvertForSDRDisplayAgXOperator,
    OctaneOutputAOVsConvertForSDRDisplayBasicOperator,
    OctaneOutputAOVsConvertForSDRDisplayOCIOOperator,
    OctaneOutputAOVsConvertForSDRDisplaySmoothOperator,
    OctaneOutputAOVsAddBloomOperator,
    OctaneOutputAOVsAddChromaticAberrationOperator,
    OctaneOutputAOVsAddGlareOperator,
    OctaneOutputAOVsAddLensFlareOperator,
    OctaneOutputAOVsAddVignetteOperator,
    OctaneOutputAOVsBlurOperator,
    OctaneOutputAOVsRemoveHotPixelsOperator,
    OctaneOutputAOVsAdjustOpacityOperator,
    OctaneOutputAOVsMaskWithCryptomatteOperator,
    OctaneOutputAOVsMaskWithLayerGroupOperator,
    OctaneOutputAOVsLightMixerOutputAOVOperator,
    OctaneBlendingSettingsSwitchOperator,
    OctaneOutputAOVGroupSwitchOperator,
    OctaneOutputAOVLayerSwitchOperator,
    OctaneOutputAOVSwitchOperator,
    OctaneOutputAOVsLayerGroupPassThroughOperator,
    OctaneRenderAOVGroupOperator,
    OctaneRenderAOVSwitchOperator,
    NODES_OT_OctaneBoolValue_Add,
    NODES_OT_OctaneIntValue_Add,
    NODES_OT_OctaneFloatValue_Add,
    NODES_OT_OctaneStringValue_Add,
    NODES_OT_OctaneLightIDBitValue_Add,
    NODES_OT_OctaneSunDirection_Add,
    NODES_OT_OctaneConverterFloatToInt_Add,
    NODES_OT_OctaneConverterIntToFloat_Add,
    NODES_OT_OctaneOutputAOVGroupOutputNode_Add,
    NODES_OT_OctaneCameraData_Add,
    NODES_OT_OctaneObjectData_Add,
    NODES_OT_OctaneProxy_Add,
    NODES_OT_OctaneCameraImager_Add,
    NODES_OT_OctaneOCIOColorSpace_Add,
    NODES_OT_OctaneOperatorBinaryMathOperation_Add,
    NODES_OT_OctaneOperatorBooleanLogicOperator_Add,
    NODES_OT_OctaneOperatorFloatRelationalOperator_Add,
    NODES_OT_OctaneOperatorIntRelationalOperator_Add,
    NODES_OT_OctaneOperatorRange_Add,
    NODES_OT_OctaneOperatorRotate_Add,
    NODES_OT_OctaneOperatorUnaryMathOperation_Add,
    NODES_OT_OctaneBoolSwitch_Add,
    NODES_OT_OctaneFloatSwitch_Add,
    NODES_OT_OctaneIntSwitch_Add,
    NODES_OT_OctaneStringSwitch_Add,
    NODES_OT_OctaneUtilityFloatComponentPicker_Add,
    NODES_OT_OctaneUtilityFloatIf_Add,
    NODES_OT_OctaneUtilityFloatMerger_Add,
    NODES_OT_OctaneUtilityIntComponentPicker_Add,
    NODES_OT_OctaneUtilityIntIf_Add,
    OctaneDenoisedDiffuseDirectAOVOperator,
    OctaneDenoisedDiffuseIndirectAOVOperator,
    OctaneDenoisedEmissionAOVOperator,
    OctaneDenoisedReflectionDirectAOVOperator,
    OctaneDenoisedReflectionIndirectAOVOperator,
    OctaneDenoisedRemainderAOVOperator,
    OctaneDenoisedVolumeAOVOperator,
    OctaneDenoisedVolumeEmissionAOVOperator,
    NODES_OT_OctaneTextureDisplacement_Add,
    NODES_OT_OctaneVertexDisplacement_Add,
    NODES_OT_OctaneVertexDisplacementMixer_Add,
    NODES_OT_OctaneDisplacementSwitch_Add,
    NODES_OT_OctaneBox_Add,
    NODES_OT_OctaneColorToUVW_Add,
    NODES_OT_OctaneCylindrical_Add,
    NODES_OT_OctaneDistortedMeshUV_Add,
    NODES_OT_OctaneInstancePosition_Add,
    NODES_OT_OctaneMatCap_Add,
    NODES_OT_OctaneMeshUVProjection_Add,
    NODES_OT_OctaneOSLDelayedUV_Add,
    NODES_OT_OctaneOSLProjection_Add,
    NODES_OT_OctanePerspective_Add,
    NODES_OT_OctaneSamplePosToUV_Add,
    NODES_OT_OctaneSpherical_Add,
    NODES_OT_OctaneTriplanar_Add,
    NODES_OT_OctaneXYZToUVW_Add,
    NODES_OT_OctaneProjectionSwitch_Add,
    NODES_OT_Octane2DTransformation_Add,
    NODES_OT_Octane3DTransformation_Add,
    NODES_OT_OctaneConverterLookAtTransform_Add,
    NODES_OT_OctaneRotation_Add,
    NODES_OT_OctaneScale_Add,
    NODES_OT_OctaneTransformValue_Add,
    NODES_OT_OctaneTransformSwitch_Add,
]

# Remover duplicatas
classes_Octane_OT = list(set(classes_Octane_OT))




'''
classes = [
    OctaneDiffuseAOVOperator,
    OctaneDiffuseDirectAOVOperator,
    OctaneDiffuseFilterBeautyAOVOperator,
    OctaneDiffuseIndirectAOVOperator,
    OctaneEmittersAOVOperator,
    OctaneEnvironmentAOVOperator,
    OctaneReflectionAOVOperator,
    OctaneCryptomatteAOVOperator,
    OctaneIrradianceAOVOperator,
    OctaneLightDirectionAOVOperator,
    OctaneNoiseAOVOperator,
    OctanePostProcessingAOVOperator,
    OctanePostfxMediaAOVOperator,
    OctaneShadowAOVOperator, 
    OctaneReflectionDirectAOVOperator,
    OctaneReflectionFilterBeautyAOVOperator,
    OctaneReflectionIndirectAOVOperator,
    OctaneRefractionAOVOperator,
    OctaneRefractionFilterBeautyAOVOperator,
    OctaneSubsurfaceScatteringAOVOperator,
    OctaneTransmissionAOVOperator,
    OctaneTransmissionFilterBeautyAOVOperator,       
    OctaneVolumeAOVOperator,
    OctaneVolumeEmissionAOVOperator,
    OctaneVolumeMaskAOVOperator,
    OctaneVolumeZDepthBackAOVOperator,
    OctaneVolumeZDepthFrontAOVOperator,  
    OctaneCustomAOVOperator,
    OctaneGlobalTextureAOVOperator,   
    OctaneBlendingSettingsOperator,
    OctaneOutputAOVsOutputAOVOperator,
    OctaneOutputAOVsOutputAOVGroupOperator, 
    OctaneOutputAOVsImageFileOperator,
    OctaneOutputAOVsLayerGroupOperator,
    OctaneOutputAOVsRenderAOVOperator,
    OctaneOutputAOVsSolidColorOperator, 
    OctaneOutputAOVsAdjustBrightnessOperator,
    OctaneOutputAOVsAdjustContrastSDROnlyOperator,
    OctaneOutputAOVsAdjustHueOperator,
    OctaneOutputAOVsAdjustSaturationOperator, 
    OctaneOutputAOVsAdjustWhiteBalanceOperator,
    OctaneOutputAOVsApplyCameraResponseCurveSDROnlyOperator,
    OctaneOutputAOVsApplyCustomCurveOperator,
    OctaneOutputAOVsApplyGammaCurveSDROnlyOperator,  
    OctaneOutputAOVsApplyLUTOperator,
    OctaneOutputAOVsApplyOCIOLookOperator,
    OctaneOutputAOVsChannelClampOperator,
    OctaneOutputAOVsChannelInvertSDROnlyOperator,
    OctaneOutputAOVsChannelMapRangeOperator,
    OctaneOutputAOVsConvertForSDRDisplayACESOperator,
    OctaneOutputAOVsConvertForSDRDisplayAgXOperator,
    OctaneOutputAOVsConvertForSDRDisplayBasicOperator,
    OctaneOutputAOVsConvertForSDRDisplayOCIOOperator,
    OctaneOutputAOVsConvertForSDRDisplaySmoothOperator, 
    OctaneOutputAOVsAddBloomOperator,
    OctaneOutputAOVsAddChromaticAberrationOperator,
    OctaneOutputAOVsAddGlareOperator,
    OctaneOutputAOVsAddLensFlareOperator,
    OctaneOutputAOVsAddVignetteOperator,
    OctaneOutputAOVsBlurOperator,
    OctaneOutputAOVsRemoveHotPixelsOperator,  
    OctaneOutputAOVsAdjustOpacityOperator,
    OctaneOutputAOVsMaskWithCryptomatteOperator,
    OctaneOutputAOVsMaskWithLayerGroupOperator,
    OctaneOutputAOVsLightMixerOutputAOVOperator,
    OctaneBlendingSettingsSwitchOperator,
    OctaneOutputAOVGroupSwitchOperator,
    OctaneOutputAOVLayerSwitchOperator,
    OctaneOutputAOVSwitchOperator,
    OctaneOutputAOVsLayerGroupPassThroughOperator,
    OctaneRenderAOVGroupOperator,
    OctaneRenderAOVSwitchOperator,
    NODES_OT_OctaneBoolValue_Add,
    NODES_OT_OctaneIntValue_Add,
    NODES_OT_OctaneFloatValue_Add,
    NODES_OT_OctaneStringValue_Add,
    NODES_OT_OctaneLightIDBitValue_Add,
    NODES_OT_OctaneSunDirection_Add,
    NODES_OT_OctaneConverterFloatToInt_Add,
    NODES_OT_OctaneConverterIntToFloat_Add,
    NODES_OT_OctaneOutputAOVGroupOutputNode_Add,
    NODES_OT_OctaneCameraData_Add,
    NODES_OT_OctaneObjectData_Add,
    NODES_OT_OctaneScriptGraph_Add,
    NODES_OT_OctaneProxy_Add,
    NODES_OT_OctaneCameraImager_Add,
    NODES_OT_OctaneOCIOColorSpace_Add,
    NODES_OT_OctaneOperatorBinaryMathOperation_Add,
    NODES_OT_OctaneOperatorBooleanLogicOperator_Add,
    NODES_OT_OctaneOperatorFloatRelationalOperator_Add,
    NODES_OT_OctaneOperatorIntRelationalOperator_Add,
    NODES_OT_OctaneOperatorRange_Add,
    NODES_OT_OctaneOperatorRotate_Add,
    NODES_OT_OctaneOperatorUnaryMathOperation_Add,    
    NODES_OT_OctaneOperatorRotate_Add,
    NODES_OT_OctaneOperatorUnaryMathOperation_Add,
    NODES_OT_OctaneBoolSwitch_Add,
    NODES_OT_OctaneFloatSwitch_Add,
    NODES_OT_OctaneIntSwitch_Add,
    NODES_OT_OctaneStringSwitch_Add,
    NODES_OT_OctaneUtilityFloatComponentPicker_Add,
    NODES_OT_OctaneUtilityFloatIf_Add,
    NODES_OT_OctaneUtilityFloatMerger_Add,
    NODES_OT_OctaneUtilityIntComponentPicker_Add,
    NODES_OT_OctaneUtilityIntIf_Add,
    OctaneDenoisedDiffuseDirectAOVOperator,
    OctaneDenoisedDiffuseIndirectAOVOperator,
    OctaneDenoisedEmissionAOVOperator,
    OctaneDenoisedReflectionDirectAOVOperator,
    OctaneDenoisedReflectionIndirectAOVOperator,
    OctaneDenoisedRemainderAOVOperator,
    OctaneDenoisedVolumeAOVOperator,
    OctaneDenoisedVolumeEmissionAOVOperator,
    NODES_OT_OctaneTextureDisplacement_Add,
    NODES_OT_OctaneVertexDisplacement_Add,
    NODES_OT_OctaneVertexDisplacementMixer_Add,
    NODES_OT_OctaneDisplacementSwitch_Add,
    NODES_OT_OctaneBox_Add,
    NODES_OT_OctaneColorToUVW_Add,
    NODES_OT_OctaneCylindrical_Add,
    NODES_OT_OctaneDistortedMeshUV_Add,
    NODES_OT_OctaneInstancePosition_Add,
    NODES_OT_OctaneMatCap_Add,  
    NODES_OT_OctaneMeshUVProjection_Add,
    NODES_OT_OctaneOSLDelayedUV_Add,
    NODES_OT_OctaneOSLProjection_Add, 
    NODES_OT_OctanePerspective_Add,
    NODES_OT_OctaneSamplePosToUV_Add,
    NODES_OT_OctaneSpherical_Add, 
    NODES_OT_OctaneTriplanar_Add,
    NODES_OT_OctaneXYZToUVW_Add,
    NODES_OT_OctaneProjectionSwitch_Add,
    NODES_OT_Octane2DTransformation_Add,
    NODES_OT_Octane3DTransformation_Add,
    NODES_OT_OctaneConverterLookAtTransform_Add,
    NODES_OT_OctaneRotation_Add,
    NODES_OT_OctaneScale_Add,
    NODES_OT_OctaneTransformValue_Add,
    NODES_OT_OctaneTransformSwitch_Add,                                                                         
]
'''
















