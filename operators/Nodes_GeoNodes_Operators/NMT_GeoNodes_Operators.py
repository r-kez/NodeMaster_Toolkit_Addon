import bpy
from ..Master_op.master_op import MASTER_OT_Transform




######################################################################
#                             Attribute                              #
######################################################################

# Geo Nodes Attribute Start

# Attribute Statistic
class GEONODES_OT_AttStatistic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_statistic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeAttributeStatistic")
        return {"FINISHED"}

# Attribute Domain Size
class GEONODES_OT_AttDomainSize_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_domain_size_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeAttributeDomainSize")
        return {"FINISHED"}

# Attribute Blur
class GEONODES_OT_AttBlur_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_blur_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeBlurAttribute")
        return {"FINISHED"}    

# Attribute Capture Named Attribute
class GEONODES_OT_AttCapture_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_capture_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCaptureAttribute")
        return {"FINISHED"}    

# Attribute Remove
class GEONODES_OT_AttRemove_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_remove_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRemoveAttribute")
        return {"FINISHED"}


# Attribute Remove
class GEONODES_OT_AttStoreNamed_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_store_named_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeStoreNamedAttribute")
        return {"FINISHED"}


######################################################################
#                             Curve                                  #
######################################################################

############################## Curve -- Read ####################################

# Curve Handle Positions
class GEONODES_OT_CurveHandlePositions_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_handle_positions_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputCurveHandlePositions")
        return {"FINISHED"}

# Curve Length
class GEONODES_OT_CurveLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveLength")
        return {"FINISHED"}

# Curve Tangent
class GEONODES_OT_CurveTangent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_tangent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputTangent")
        return {"FINISHED"}

# Curve Tilt
class GEONODES_OT_CurveTilt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_tilt_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputCurveTilt")
        return {"FINISHED"}

# Curve End Point Selection
class GEONODES_OT_CurveEndPointSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_end_point_selection__add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveEndpointSelection")
        return {"FINISHED"}

# Curve Handle Type Selection
class GEONODES_OT_CurveHandleTypeSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_handle_type_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveHandleTypeSelection")
        return {"FINISHED"}

# Curve Spline Cyclic
class GEONODES_OT_CurveSplineCyclic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_cyclic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputSplineCyclic")
        return {"FINISHED"}

# Curve Spline Length
class GEONODES_OT_CurveSplineLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSplineLength")
        return {"FINISHED"}

# Curve Spline Parameter
class GEONODES_OT_CurveSplineParameter_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_parameter_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSplineParameter")
        return {"FINISHED"}

# Curve Spline Resolution
class GEONODES_OT_CurveSplineResolution_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_resolution_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputSplineResolution")
        return {"FINISHED"}

############################## Curve -- Sample ####################################

# Curve Spline Resolution
class GEONODES_OT_CurveSample_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_sample_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleCurve")
        return {"FINISHED"}

############################## Curve -- Sample ####################################

# Curve Set Curve Normal
class GEONODES_OT_CurveSetCurveNormal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_curve_normal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveNormal")
        return {"FINISHED"}

# Curve Set Curve Radius
class GEONODES_OT_CurveSetCurveRadius_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_curve_radius_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveRadius")
        return {"FINISHED"}

# Curve Set Curve Tilt
class GEONODES_OT_CurveSetCurveTilt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_curve_tilt_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveTilt")
        return {"FINISHED"}

# Curve Set Curve Handle Positions
class GEONODES_OT_CurveSetCurveHandlePositions_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_handle_positions_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveHandlePositions")
        return {"FINISHED"}

# Curve Set Handles
class GEONODES_OT_CurveSetHandleType_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_handle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveSetHandles")
        return {"FINISHED"}

# Curve Set Spline Cyclic
class GEONODES_OT_CurveSetSplineCyclic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_spline_cyclic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetSplineCyclic")
        return {"FINISHED"}

# Curve Set Spline Resolution
class GEONODES_OT_CurveSetSplineResolution_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_spline_resolution_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetSplineResolution")
        return {"FINISHED"}

# Curve Set Spline Type
class GEONODES_OT_CurveSetSplineType_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_spline_type_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveSplineType")
        return {"FINISHED"}

############################## Curve -- Operations ####################################

# Curve To Mesh
class GEONODES_OT_CurveToMesh_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_to_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveToMesh")
        return {"FINISHED"}

# Curve Curve To Points
class GEONODES_OT_CurveCurveToPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_to_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveToPoints")
        return {"FINISHED"}

# Curve Deform Curves On Surface
class GEONODES_OT_CurveDeformCurvesOnSurface_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_deform_curves_on_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDeformCurvesOnSurface")
        return {"FINISHED"}

# Curve Fill Curve
class GEONODES_OT_CurveFillCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_fill_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFillCurve")
        return {"FINISHED"}

# Curve Fillet Curve
class GEONODES_OT_CurveFilletCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_fillet_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFilletCurve")
        return {"FINISHED"}

# Curve Interpolate Curves
class GEONODES_OT_CurveInterpolateCurves_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_interpolate_curves_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInterpolateCurves")
        return {"FINISHED"}

# Curve Resample Curve
class GEONODES_OT_CurveResampleCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_resample_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeResampleCurve")
        return {"FINISHED"}

# Curve Reverse Curve
class GEONODES_OT_CurveReverseCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_reverse_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeReverseCurve")
        return {"FINISHED"}

# Curve Subdvide Curve
class GEONODES_OT_CurveSubdvideCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_subdivide_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSubdivideCurve")
        return {"FINISHED"}

# Curve Trim Curve
class GEONODES_OT_CurveTrimCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_trim_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTrimCurve")
        return {"FINISHED"}

############################## Curve -- Primitives ####################################

# Curve Arc
class GEONODES_OT_CurveArc_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_arc_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveArc")
        return {"FINISHED"}

# Curve Bezier Segment
class GEONODES_OT_CurveBezierSegment_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_curve_bezier_segment_type_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveBezierSegment")
        return {"FINISHED"}

# Curve Circle
class GEONODES_OT_CurveCircle_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_curve_circle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveCircle")
        return {"FINISHED"}

# Curve Line
class GEONODES_OT_CurveLine_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_line_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveLine")
        return {"FINISHED"}

# Curve Spiral
class GEONODES_OT_CurveSpiral_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spiral_type_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveSpiral")
        return {"FINISHED"}

# Curve Quadratic Bezier
class GEONODES_OT_CurveQuadraticBezier_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_quadratic_bezier_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveQuadraticBezier")
        return {"FINISHED"}

# Curve Quadrilateral
class GEONODES_OT_CurveQuadrilateral_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_quadrilateral_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveQuadrilateral")
        return {"FINISHED"}

# Curve Curve Star
class GEONODES_OT_CurveCurveStar_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_curve_star_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveStar")
        return {"FINISHED"}

############################## Curve -- Topology ####################################

# Curve Curve of Point
class GEONODES_OT_CurveCurveofPoint_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_of_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveOfPoint")
        return {"FINISHED"}

# Curve Offset Point in Curve
class GEONODES_OT_CurveOffsetPointinCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_offset_point_in_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeOffsetPointInCurve")
        return {"FINISHED"}

# Curve Points of Curve
class GEONODES_OT_CurvePointsofCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_points_in_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodePointsOfCurve")
        return {"FINISHED"}


######################################################################
#                             Geometry                               #
######################################################################

############################## Main ####################################

# Geometry to Distance
class GEONODES_OT_GeometryGeometryToDistance_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_to_distance_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeGeometryToInstance")
        return {"FINISHED"}

# Geometry Join Geometry
class GEONODES_OT_GeometryJoinGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_join_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeJoinGeometry")
        return {"FINISHED"}

############################## Read ####################################

# Geometry ID
class GEONODES_OT_GeometryID_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_id_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputID")
        return {"FINISHED"}

# Geometry Index
class GEONODES_OT_GeometryIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputIndex")
        return {"FINISHED"}

# Geometry Named Attribute
class GEONODES_OT_GeometryAttribute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_attribute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputNamedAttribute")
        return {"FINISHED"}

# Geometry Normal
class GEONODES_OT_GeometryNormal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_normal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputNormal")
        return {"FINISHED"}

# Geometry Position
class GEONODES_OT_GeometryPosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_position_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputPosition")
        return {"FINISHED"}

# Geometry Radius
class GEONODES_OT_GeometryRadious_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_radius_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputRadius")
        return {"FINISHED"}

# Geometry Selection
class GEONODES_OT_GeometrySelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeToolSelection")
        return {"FINISHED"}

############################## Sample ####################################

# Geometry Proximity
class GEONODES_OT_GeometryProximity_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_proximity_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeProximity")
        return {"FINISHED"}

# Geometry Index of Nearest
class GEONODES_OT_GeometryNearest_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_index_nearest_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeIndexOfNearest")
        return {"FINISHED"}

# Geometry Raycast
class GEONODES_OT_GeometryRaycast_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_raycast_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRaycast")
        return {"FINISHED"}

# Geometry Sample Index
class GEONODES_OT_GeometrySampleIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_sample_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleIndex")
        return {"FINISHED"}

# Geometry Sample Nearest
class GEONODES_OT_GeometrySampleNearest_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_sample_nearest_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleNearest")
        return {"FINISHED"}

############################## Write ####################################

# Geometry Sample Nearest
class GEONODES_OT_GeometrySetIDt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_set_id_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = 'NODE'
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetID")
        return {"FINISHED"}


# Geometry Sample Nearest
class GEONODES_OT_GeometrySetPosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_set_position_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = 'NODE'
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetPosition")
        return {"FINISHED"}

# Geometry Set Selection
class GEONODES_OT_GeometrySetSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_set_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = 'NODE'
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeToolSetSelection")
        return {"FINISHED"}

############################## Operations ####################################

# Geometry Bounding Box
class GEONODES_OT_GeometryBoundBox_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_bound_box_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeBoundBox")
        return {"FINISHED"}

# Geometry Convex Hull
class GEONODES_OT_GeometryConvexHUll_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_convex_hull_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeConvexHull")
        return {"FINISHED"}

# Geometry Delete Geometry
class GEONODES_OT_GeometryDeleteGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_delete_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDeleteGeometry")
        return {"FINISHED"}

# Geometry Duplicate Elements
class GEONODES_OT_GeometryDuplicateElements_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_duplicate_elements_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDuplicateElements")
        return {"FINISHED"}

# Geometry Merge by Distance
class GEONODES_OT_GeometryMergeByDistance_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_merge_by_distance_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMergeByDistance")
        return {"FINISHED"}

# Geometry Transform
class GEONODES_OT_GeometryTransform_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_transform_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTransform")
        return {"FINISHED"}

# Geometry Separate Geometry
class GEONODES_OT_GeometrySeparateComponents_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_separate_components_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSeparateComponents")
        return {"FINISHED"}

# Geometry Separate Geometry
class GEONODES_OT_GeometrySeparateGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_separate_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSeparateGeometry")
        return {"FINISHED"}


######################################################################
#                             Input                                  #
######################################################################

################## Constant ##################

# Input Bool
class GEONODES_OT_InputBool_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_bool_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputBool")
        return {"FINISHED"}

# Input Color
class GEONODES_OT_InputColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputColor")
        return {"FINISHED"}

# Input Image
class GEONODES_OT_InputImage_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_image_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputImage")
        return {"FINISHED"}

# Input Integer
class GEONODES_OT_InputIntegerd_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_integer_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputInt")
        return {"FINISHED"}

# Input Material
class GEONODES_OT_InputMateriald_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_material_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMaterial")
        return {"FINISHED"}

# Input String
class GEONODES_OT_InputString_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_string_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputString")
        return {"FINISHED"}

# Input Value
class GEONODES_OT_Inputvalue_Add(MASTER_OT_Transform):
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
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeValue")
        return {"FINISHED"}

# Input Store Named Attribute
class GEONODES_OT_InputStoreNamedAttribute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_store_named_attribute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeStoreNamedAttribute")
        return {"FINISHED"}

################## Input Group ###############

'''# Input Group
class GEONODES_OT_InputGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeGroupInput")
        return {"FINISHED"}
'''
##################### Scene ##################

class GEONODES_OT_3DCursor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_3d_cursor_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTool3DCursor")
        return {"FINISHED"}

class GEONODES_OT_InputColInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_col_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCollectionInfo")
        return {"FINISHED"}

class GEONODES_OT_InputCollectionInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_collection_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCollectionInfo")
        return {"FINISHED"}

class GEONODES_OT_InputImageInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_image_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeImageInfo")
        return {"FINISHED"}

class GEONODES_OT_InputIsViewport_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_is_viewport_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeIsViewport")
        return {"FINISHED"}

class GEONODES_OT_InputObjectInfo_Add(MASTER_OT_Transform):
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
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeObjectInfo")
        return {"FINISHED"}

class GEONODES_OT_InputSceneTime_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_scene_time_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputSceneTime")
        return {"FINISHED"}

class GEONODES_OT_InputSelfObject_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_self_object_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSelfObject")
        return {"FINISHED"}


######################################################################
#                             Instances                              #
######################################################################


# Instances On Points
class GEONODES_OT_InstancesOnPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_on_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInstanceOnPoints")
        return {"FINISHED"}

# Instances To Points
class GEONODES_OT_InstancesToPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_to_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInstancesToPoints")
        return {"FINISHED"}

# Instances Realize Instances
class GEONODES_OT_InstancesRealizeInstances_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_realize_insances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRealizeInstances")
        return {"FINISHED"}

# Instances Rotate Instances
class GEONODES_OT_InstancesRotateInstances_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instance_rotate_instances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRotateInstances")
        return {"FINISHED"}

# Instances Scale Instances
class GEONODES_OT_InstancesScaleInstances_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_scale_instances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeScaleInstances")
        return {"FINISHED"}

# Instances Translate Instances
class GEONODES_OT_InstancesTranslateInstancess_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_translate_instances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTranslateInstances")
        return {"FINISHED"}

# Instances Input Instance Rotaion
class GEONODES_OT_InstancesInputInstanceRotaion_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_input_instance_rotation_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputInstanceRotation")
        return {"FINISHED"}

# Instances Input Instance Scale
class GEONODES_OT_InstancesInputInstanceScale_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_input_instance_scale_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputInstanceScale")
        return {"FINISHED"}


######################################################################
#                             Materials                              #
######################################################################


# Material Replace Material
class GEONODES_OT_MaterialReplaceMaterial_Add(MASTER_OT_Transform):
    bl_idname = "nodes.material_replace_material_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeReplaceMaterial")
        return {"FINISHED"}

# Material Material Index
class GEONODES_OT_MaterialIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.material_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMaterialIndex")
        return {"FINISHED"}

# Material Material Selection
class GEONODES_OT_MaterialSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.material_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMaterialSelection")
        return {"FINISHED"}

# Material Material
class GEONODES_OT_Material_Add(MASTER_OT_Transform):
    bl_idname = "nodes.material_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetMaterial")
        return {"FINISHED"}

# Material Set MaterialI ndex
class GEONODES_OT_MaterialSetMaterialIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.set_material_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetMaterialIndex")
        return {"FINISHED"}


######################################################################
#                             Mesh                                   #
######################################################################


#################### READ #######################

# Mesh On Points
class GEONODES_OT_MeshEdgeAngle_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_angle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshEdgeAngle")
        return {"FINISHED"}

# Mesh Edge Neighbors
class GEONODES_OT_MeshEdgeNeighbors_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_neigbors_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshEdgeNeighbors")
        return {"FINISHED"}

# Mesh Edge Vertices
class GEONODES_OT_MeshEdgeVertices_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_vertices_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshEdgeVertices")
        return {"FINISHED"}

# Mesh Edge To Face Group
class GEONODES_OT_MeshEdgeToFaceGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_to_face_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgesToFaceGroups")
        return {"FINISHED"}

# Mesh Face Area
class GEONODES_OT_MeshFaceArea_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_area_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshFaceArea")
        return {"FINISHED"}

# Mesh Face Set Boundaries
class GEONODES_OT_MeshFaceSetBoundaries_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_set_boundaries_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshFaceSetBoundaries")
        return {"FINISHED"}

# Mesh Face Neighbors
class GEONODES_OT_MeshFaceNeighbors_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_neighbors_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshFaceNeighbors")
        return {"FINISHED"}

# Mesh Face Set
class GEONODES_OT_MesFacehSet_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_set_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeToolFaceSet")
        return {"FINISHED"}

# Mesh FaceIs Planar
class GEONODES_OT_MeshFaceIsPlanar_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_is_planar_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshFaceIsPlanar")
        return {"FINISHED"}

# Mesh Is Shade Smooth
class GEONODES_OT_MeshIsShadeSmooth_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_is_shade_smooth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputShadeSmooth")
        return {"FINISHED"}

# Mesh Is Edge Smooth
class GEONODES_OT_MeshIsEdgeSmooth_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_is_edge_smooth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputEdgeSmooth")
        return {"FINISHED"}

# Mesh Island
class GEONODES_OT_MeshIsland_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_island_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshIsland")
        return {"FINISHED"}

# Mesh Shortest Edge Paths
class GEONODES_OT_MeshShortestEdgePaths_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_shortest_edges_paths_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputShortestEdgePaths")
        return {"FINISHED"}

# Mesh Vertex Neighbors
class GEONODES_OT_MeshVertexNeighbors_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_vertex_neighbors_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshVertexNeighbors")
        return {"FINISHED"}

#################### SAMPLE #######################
# Mesh Sample Nearest Surface
class GEONODES_OT_MeshSampleNearestSurface_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_sample_nearest_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleNearestSurface")
        return {"FINISHED"}

# Mesh Sample UV Surface
class GEONODES_OT_MeshSampleUVSurface_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_saple_uv_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleUVSurface")
        return {"FINISHED"}

#################### Write #######################

# Mesh Write Set Shade Smooth
class GEONODES_OT_MesWriteSetShadeSmooth_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_write_set_shade_smooth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetShadeSmooth")
        return {"FINISHED"}

# Mesh Write Set Shade Smooth
class GEONODES_OT_MesWriteSetFaceSet_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_write_set_face_set_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeToolSetFaceSet")
        return {"FINISHED"}

#################### Operations #######################

# Mesh Operations Dual Mesh
class GEONODES_OT_MeshOperationsDualMesh_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_dual_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDualMesh")
        return {"FINISHED"}

# Mesh Operations Edge Paths To Curves
class GEONODES_OT_MeshOperationsEdgePathsToCurves_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_edge_paths_to_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgePathsToCurves")
        return {"FINISHED"}

# Mesh Operations Edge Paths To Selection
class GEONODES_OT_MeshOperationsEdgePathsToSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_edge_paths_to_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgePathsToSelection")
        return {"FINISHED"}

# Mesh Operations Extrude Mesh
class GEONODES_OT_MeshOperationsExtrudeMesh_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_extrude_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeExtrudeMesh")
        return {"FINISHED"}

# Mesh Operations Flip Faces
class GEONODES_OT_MeshOperationsFlipFaces_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_flip_faces_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFlipFaces")
        return {"FINISHED"}

# Mesh Operations Mesh Boolean
class GEONODES_OT_MeshOperationsMeshBoolean_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_mesh_boolean_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshBoolean")
        return {"FINISHED"}

# Mesh Operations Mesh To Curve
class GEONODES_OT_MeshOperationsMeshToCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_mesh_to_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshToCurve")
        return {"FINISHED"}

# Mesh Operations Mesh To Points
class GEONODES_OT_MeshOperationsMeshToPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_mesh_to_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshToPoints")
        return {"FINISHED"}

# Mesh Operations Mesh To Volume
class GEONODES_OT_MeshOperationsMeshToVolume_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_mesh_to_volume_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshToVolume")
        return {"FINISHED"}

# Mesh Operations Scale Elements
class GEONODES_OT_MeshVOperationsScaleElements_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_scale_elements_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeScaleElements")
        return {"FINISHED"}

# Mesh Operations Split Edges
class GEONODES_OT_MeshOperationsSplitEdges_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_split_edges_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSplitEdges")
        return {"FINISHED"}

# Mesh Operations Subdivide Mesh
class GEONODES_OT_MeshOperationsSubdivideMesh_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_subdivide_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSubdivideMesh")
        return {"FINISHED"}

# Mesh Operations Subdivision Surface
class GEONODES_OT_MeshOperationsSubdivisionSurface_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_subdivision_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSubdivisionSurface")
        return {"FINISHED"}

# Mesh Operations Triangulate
class GEONODES_OT_MeshOperationsTriangulate_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_op_triangulate_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTriangulate")
        return {"FINISHED"}

#################### Primitives #######################

# Mesh Primitives Cone
class GEONODES_OT_MeshPrimitivesCone_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_cone_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCone")
        return {"FINISHED"}

# Mesh Primitives Cube
class GEONODES_OT_MeshPrimitivesCube_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_cube_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCube")
        return {"FINISHED"}

# Mesh Primitives Cylinder
class GEONODES_OT_MeshPrimitivesCylinder_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_cylinder_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCylinder")
        return {"FINISHED"}

# Mesh Primitives Grid
class GEONODES_OT_MeshPrimitivesGrid_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_grid_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshGrid")
        return {"FINISHED"}

# Mesh Primitives IcoSphere
class GEONODES_OT_MeshPrimitivesIcoSphere_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_ico_sphere_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshIcoSphere")
        return {"FINISHED"}

# Mesh Primitives Circle
class GEONODES_OT_MeshPrimitivesCircle_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_circle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCircle")
        return {"FINISHED"}

# Mesh Primitives Line
class GEONODES_OT_MeshPrimitivesLine_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_mesh_line_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshLine")
        return {"FINISHED"}

# Mesh Primitives UVSphere
class GEONODES_OT_MeshPrimitivesUVSphere_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_primitive_uv_sphere_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshUVSphere")
        return {"FINISHED"}

#################### Topology #######################

# Mesh Topology Corners Of Edge
class GEONODES_OT_MeshTopologyCornersOfEdge_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_corners_of_edge_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCornersOfEdge")
        return {"FINISHED"}

# Mesh Topology Corners Of Face
class GEONODES_OT_MeshTopologyCornersOfFace_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_corner_of_face_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCornersOfFace")
        return {"FINISHED"}

# Mesh Topology Corners Of Vertex
class GEONODES_OT_MeshTopologyCornersOfVertex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_corner_of_vertex_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCornersOfVertex")
        return {"FINISHED"}

# Mesh Topology Edges Of Corner
class GEONODES_OT_MeshTopologyEdgesOfCorner_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_edges_of_corner_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgesOfCorner")
        return {"FINISHED"}

# Mesh Topology Edges Of Vertex
class GEONODES_OT_MeshTopologyEdgeOfVertex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_edges_of_vertex_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgesOfVertex")
        return {"FINISHED"}

# Mesh Topology Face Of Corner
class GEONODES_OT_MeshTopologyFaceOfCorner_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_face_of_corner_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFaceOfCorner")
        return {"FINISHED"}

# Mesh Topology Offset Corner In Face
class GEONODES_OT_MeshTopologyOffsetCornerInFace_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_offset_corner_in_face_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeOffsetCornerInFace")
        return {"FINISHED"}

# Mesh Topology Vertex Of Corner
class GEONODES_OT_MeshTopologyVertexOfCorner_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_topo_vertex_of_corner_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeVertexOfCorner")
        return {"FINISHED"}

#################### UV #######################

# Mesh UV Pack Islands
class GEONODES_OT_MeshUVPackIslands_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_uv_pack_island_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeUVPackIslands")
        return {"FINISHED"}

# Mesh UV Unwrap
class GEONODES_OT_MeshUVUnwrap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_uv_unwrap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeUVUnwrap")
        return {"FINISHED"}


######################################################################
#                             Output                                 #
######################################################################


#### Constant

# Group Output
class GEONODES_OT_InputGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geo_input_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeGroupInput")
        return {"FINISHED"}


# Group Output
class GEONODES_OT_OutputGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.output_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeGroupOutput")
        return {"FINISHED"}

# Viewer Node
class GEONODES_OT_OutputViewer_Add(MASTER_OT_Transform):
    bl_idname = "nodes.output_viewer_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeViewer")
        return {"FINISHED"}


######################################################################
#                             Point                                  #
######################################################################


# Point Distribute Points In Volume
class GEONODES_OT_PointDistributePointsInVolume_Add(MASTER_OT_Transform):
    bl_idname = "nodes.points_distribute_points_in_volume_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDistributePointsInVolume")
        return {"FINISHED"}

# Point Distribute Points On Faces
class GEONODES_OT_PointDistributePointsOnFaces_Add(MASTER_OT_Transform):
    bl_idname = "nodes.points_distribute_points_on_faces_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDistributePointsOnFaces")
        return {"FINISHED"}

# Point Points
class GEONODES_OT_PointPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.points_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodePoints")
        return {"FINISHED"}

# Point Points To Curves
class GEONODES_OT_PointPointsToCurves_Add(MASTER_OT_Transform):
    bl_idname = "nodes.points_to_curves_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodePointsToCurves")
        return {"FINISHED"}

# Point Points To Vertices
class GEONODES_OT_PointPointsToVertices_Add(MASTER_OT_Transform):
    bl_idname = "nodes.points_to_vertices_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodePointsToVertices")
        return {"FINISHED"}

# Point Points To Volume
class GEONODES_OTPointPointsToVolume_Add(MASTER_OT_Transform):
    bl_idname = "nodes.points_to_volume_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodePointsToVolume")
        return {"FINISHED"}

# Point Point Radius
class GEONODES_OT_PointPointRadius_Add(MASTER_OT_Transform):
    bl_idname = "nodes.point_radius_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetPointRadius")
        return {"FINISHED"}


######################################################################
#                           Simulation Zone                          #
######################################################################

# Simulation Zone
class GEONODES_OT_SimulationZone_Add(MASTER_OT_Transform):
    bl_idname = "nodes.simulation_zone_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_simulation_zone(use_transform=self.use_transform)
        return {"FINISHED"}


######################################################################
#                           Texture                                  #
######################################################################


# Texture
class GEONODES_OT_TextureImage_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geo_image_texture_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeImageTexture")
        return {"FINISHED"}


######################################################################
#                           Utilities                                #
######################################################################

################# UTILITIES -- 6 Lists + 3 Itens #################
#################      Color -- 5 Itens          #################

# Utilities Color Ramp
class GEONODES_OT_UtilitiesColorRamp_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_color_ramp_add"
    bl_label = "Node Add Tool"
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

# Utilities RGBCurve
class GEONODES_OT_UtilitiesRGBCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_rgb_curve_add"
    bl_label = "Node Add Tool"
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

# Utilities CombineColor
class GEONODES_OT_UtilitiesCombineColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_combine_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeCombineColor")
        return {"FINISHED"}

# Utilities Mix Color
class GEONODES_OT_UtilitiesMixColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_mix_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, settings=[{"name":"data_type", "value":"'RGBA'"}], type="ShaderNodeMix")
        return {"FINISHED"}

# Utilities SeparateColor
class GEONODES_OT_UtilitiesSeparateColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_separate_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeSeparateColor")
        return {"FINISHED"}

################# Text -- 7 Itens #################

# Utilities StringJoin
class GEONODES_OT_UtilitiesStringJoin_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_string_join_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeStringJoin")
        return {"FINISHED"}

# Utilities ReplaceString
class GEONODES_OT_UtilitiesReplaceString_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_replace_string_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeReplaceString")
        return {"FINISHED"}

# Utilities SliceString
class GEONODES_OT_UtilitiesSliceString_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_slice_string_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeSliceString")
        return {"FINISHED"}

# Utilities StringLength
class GEONODES_OT_UtilitiesStringLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_string_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeStringLength")
        return {"FINISHED"}

# Utilities StringToCurves
class GEONODES_OT_UtilitiesStringToCurves_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_string_to_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeStringToCurves")
        return {"FINISHED"}

# Utilities ValueToString
class GEONODES_OT_UtilitiesValueToString_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_value_to_string_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeValueToString")
        return {"FINISHED"}

# Utilities SpecialCharacters
class GEONODES_OT_UtilitiesSpecialCharacters_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_special_characters_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputSpecialCharacters")
        return {"FINISHED"}

################# Vector -- 6 Itens #################

# Utilities VectorCurve
class GEONODES_OT_UtilitiesVectorCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_vector_curve_add"
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

# Utilities VectorMath
class GEONODES_OT_UtilitiesVectorMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_vector_math_add"
    bl_label = "Node Add Tool"
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

# Utilities Rotate
class GEONODES_OT_UtilitiesVectorRotate_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_vector_rotate_add"
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

# Utilities CombineXYZ
class GEONODES_OT_UtilitiesCombineXYZ_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_combine_xyz_add"
    bl_label = "Node Add Tool"
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

# Utilities Mix
class GEONODES_OT_UtilitiesVectorMix_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_vector_mix_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, settings=[{"name":"data_type", "value":"'VECTOR'"}], type="ShaderNodeMix")
        return {"FINISHED"}

# Utilities SeparateXYZ
class GEONODES_OT_UtilitiesSeparateXYZ_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_separate_xyz_add"
    bl_label = "Node Add Tool"
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

################# Field -- 3 Itens #################

# Utilities AccumulateField
class GEONODES_OT_UtilitiesAccumulateField_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_accumulate_field_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeAccumulateField")
        return {"FINISHED"}

# Utilities FieldAtIndex
class GEONODES_OT_UtilitiesFieldAtIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_field_at_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFieldAtIndex")
        return {"FINISHED"}

# Utilities FieldOnDomain
class GEONODES_OT_UtilitiesFieldOnDomain_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_field_on_domain_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFieldOnDomain")
        return {"FINISHED"}

################# Math -- 8 Itens #################  !! 5 Are the same as Shader Nodes

# Utilities BooleanMath
class GEONODES_OT_UtilitiesBooleanMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_boolean_math_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeBooleanMath")
        return {"FINISHED"}

# Utilities Compare
class GEONODES_OT_UtilitiesCompare_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_compare_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeCompare")
        return {"FINISHED"}

# Utilities FloatToInt
class GEONODES_OT_UtilitiesFloatToInt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_float_to_int_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeFloatToInt")
        return {"FINISHED"}

################# Rotation -- 10 Itens #################

# Utilities AlignEulerToVector
class GEONODES_OT_UtilitiesAlignEulerToVector_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_align_euler_to_vector_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeAlignEulerToVector")
        return {"FINISHED"}

# Utilities AxisAngleToRotation
class GEONODES_OT_UtilitiesAxisAngleToRotation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_axis_angle_to_rotation_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeAxisAngleToRotation")
        return {"FINISHED"}

# Utilities EulerToRotation
class GEONODES_OT_UtilitiesEulerToRotation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_euler_to_rotation_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeEulerToRotation")
        return {"FINISHED"}

# Utilities InvertRotation
class GEONODES_OT_UtilitiesInvertRotation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_invert_rotation_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInvertRotation")
        return {"FINISHED"}

# Utilities RotateEuler
class GEONODES_OT_UtilitiesRotateEuler_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_rotate_euler_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeRotateEuler")
        return {"FINISHED"}

# Utilities RotateVector
class GEONODES_OT_UtilitiesRotateVector_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_rotate_vector_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeRotateVector")
        return {"FINISHED"}

# Utilities RotationToAxisAngle
class GEONODES_OT_UtilitiesRotationToAxisAngle_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_rotation_to_axis_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeRotationToAxisAngle")
        return {"FINISHED"}

# Utilities RotationToEuler
class GEONODES_OT_UtilitiesRotationToEuler_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_rotation_to_euler_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeRotationToEuler")
        return {"FINISHED"}

# Utilities RotationToQuaternion
class GEONODES_OT_UtilitiesRotationToQuaternion_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_rotation_to_quaternion_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeRotationToQuaternion")
        return {"FINISHED"}

# Utilities QuaternionToRotation
class GEONODES_OT_UtilitiesQuaternionToRotation_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_quaternion_to_rotation_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeQuaternionToRotation")
        return {"FINISHED"}

################# Stand Alone -- 3 Itens #################

# Utilities RandomValue
class GEONODES_OT_UtilitiesRandomValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_random_value_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeRandomValue")
        return {"FINISHED"}

# Utilities repeat_zone
class GEONODES_OT_UtilitiesRepeatZone_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_repeat_zone_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_repeat_zone(use_transform=True)
        return {"FINISHED"}

# Utilities Switch
class GEONODES_OT_UtilitiesSwitch_Add(MASTER_OT_Transform):
    bl_idname = "nodes.utilities_switch_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSwitch")
        return {"FINISHED"}


######################################################################
#                           Volume                                   #
######################################################################


# Volume Cube
class GEONODES_OT_VolumeCube_Add(MASTER_OT_Transform):
    bl_idname = "nodes.volume_cube_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeVolumeCube")
        return {"FINISHED"}

# Volume to Mesh
class GEONODES_OT_VolumeToMesh_Add(MASTER_OT_Transform):
    bl_idname = "nodes.volume_to_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeVolumeToMesh")
        return {"FINISHED"}


######################################################################
#                           End So Far                               #
######################################################################



classes_geo_volume_OT = [
GEONODES_OT_VolumeCube_Add,
GEONODES_OT_VolumeToMesh_Add
]

classes_geo_utilities_OT = [
# Color
GEONODES_OT_UtilitiesColorRamp_Add,
GEONODES_OT_UtilitiesRGBCurve_Add,
GEONODES_OT_UtilitiesCombineColor_Add,
GEONODES_OT_UtilitiesMixColor_Add,
GEONODES_OT_UtilitiesSeparateColor_Add,
# Text
GEONODES_OT_UtilitiesStringJoin_Add,
GEONODES_OT_UtilitiesReplaceString_Add,
GEONODES_OT_UtilitiesSliceString_Add,
GEONODES_OT_UtilitiesStringLength_Add,
GEONODES_OT_UtilitiesStringToCurves_Add,
GEONODES_OT_UtilitiesValueToString_Add,
GEONODES_OT_UtilitiesSpecialCharacters_Add,
# Vector
GEONODES_OT_UtilitiesVectorCurve_Add,
GEONODES_OT_UtilitiesVectorMath_Add,
GEONODES_OT_UtilitiesVectorRotate_Add,
GEONODES_OT_UtilitiesCombineXYZ_Add,
GEONODES_OT_UtilitiesVectorMix_Add,
GEONODES_OT_UtilitiesSeparateXYZ_Add,
# Field
GEONODES_OT_UtilitiesAccumulateField_Add,
GEONODES_OT_UtilitiesFieldAtIndex_Add,
GEONODES_OT_UtilitiesFieldOnDomain_Add,
# Math
GEONODES_OT_UtilitiesBooleanMath_Add,
GEONODES_OT_UtilitiesCompare_Add,
GEONODES_OT_UtilitiesFloatToInt_Add,
# Rotation
GEONODES_OT_UtilitiesAlignEulerToVector_Add,
GEONODES_OT_UtilitiesAxisAngleToRotation_Add,
GEONODES_OT_UtilitiesEulerToRotation_Add,
GEONODES_OT_UtilitiesInvertRotation_Add,
GEONODES_OT_UtilitiesRotateEuler_Add,
GEONODES_OT_UtilitiesRotateVector_Add,
GEONODES_OT_UtilitiesRotationToAxisAngle_Add,
GEONODES_OT_UtilitiesRotationToEuler_Add,
GEONODES_OT_UtilitiesRotationToQuaternion_Add,
GEONODES_OT_UtilitiesQuaternionToRotation_Add,
GEONODES_OT_UtilitiesRandomValue_Add,
GEONODES_OT_UtilitiesRepeatZone_Add,
GEONODES_OT_UtilitiesSwitch_Add
]

classes_geo_texture_OT = [
GEONODES_OT_TextureImage_Add
]

classes_geo_simlulation_OT = [
GEONODES_OT_SimulationZone_Add
]

classes_geo_point_OT = [
GEONODES_OT_PointDistributePointsInVolume_Add,
GEONODES_OT_PointDistributePointsOnFaces_Add,
GEONODES_OT_PointPoints_Add,
GEONODES_OT_PointPointsToCurves_Add,
GEONODES_OT_PointPointsToVertices_Add,
GEONODES_OTPointPointsToVolume_Add,
GEONODES_OT_PointPointRadius_Add
]

classes_geo_output_OT = [
#GEONODES_OT_InputGroup_Add,
GEONODES_OT_OutputGroup_Add,
GEONODES_OT_OutputViewer_Add
]

classes_geo_mesh_OT = [
# Read
GEONODES_OT_MeshEdgeAngle_Add,
GEONODES_OT_MeshEdgeNeighbors_Add,
GEONODES_OT_MeshEdgeVertices_Add,
GEONODES_OT_MeshEdgeToFaceGroup_Add,
GEONODES_OT_MeshFaceArea_Add,
GEONODES_OT_MeshFaceSetBoundaries_Add,
GEONODES_OT_MeshFaceNeighbors_Add,
GEONODES_OT_MesFacehSet_Add,
GEONODES_OT_MeshFaceIsPlanar_Add,
GEONODES_OT_MeshIsShadeSmooth_Add,
GEONODES_OT_MeshIsEdgeSmooth_Add,
GEONODES_OT_MeshIsland_Add,
GEONODES_OT_MeshShortestEdgePaths_Add,
GEONODES_OT_MeshVertexNeighbors_Add,
# Sample
GEONODES_OT_MeshSampleNearestSurface_Add,
GEONODES_OT_MeshSampleUVSurface_Add,
# Write
GEONODES_OT_MesWriteSetShadeSmooth_Add,
GEONODES_OT_MesWriteSetFaceSet_Add,
# Operations
GEONODES_OT_MeshOperationsDualMesh_Add,
GEONODES_OT_MeshOperationsEdgePathsToCurves_Add,
GEONODES_OT_MeshOperationsEdgePathsToSelection_Add,
GEONODES_OT_MeshOperationsExtrudeMesh_Add,
GEONODES_OT_MeshOperationsFlipFaces_Add,
GEONODES_OT_MeshOperationsMeshBoolean_Add,
GEONODES_OT_MeshOperationsMeshToCurve_Add,
GEONODES_OT_MeshOperationsMeshToPoints_Add,
GEONODES_OT_MeshOperationsMeshToVolume_Add,
GEONODES_OT_MeshVOperationsScaleElements_Add,
GEONODES_OT_MeshOperationsSplitEdges_Add,
GEONODES_OT_MeshOperationsSubdivideMesh_Add,
GEONODES_OT_MeshOperationsSubdivisionSurface_Add,
GEONODES_OT_MeshOperationsTriangulate_Add,
# Primitives
GEONODES_OT_MeshPrimitivesCone_Add,
GEONODES_OT_MeshPrimitivesCube_Add,
GEONODES_OT_MeshPrimitivesCylinder_Add,
GEONODES_OT_MeshPrimitivesGrid_Add,
GEONODES_OT_MeshPrimitivesIcoSphere_Add,
GEONODES_OT_MeshPrimitivesCircle_Add,
GEONODES_OT_MeshPrimitivesLine_Add,
GEONODES_OT_MeshPrimitivesUVSphere_Add,
# Topology
GEONODES_OT_MeshTopologyCornersOfEdge_Add,
GEONODES_OT_MeshTopologyCornersOfFace_Add,
GEONODES_OT_MeshTopologyCornersOfVertex_Add,
GEONODES_OT_MeshTopologyEdgesOfCorner_Add,
GEONODES_OT_MeshTopologyEdgeOfVertex_Add,
GEONODES_OT_MeshTopologyFaceOfCorner_Add,
GEONODES_OT_MeshTopologyOffsetCornerInFace_Add,
GEONODES_OT_MeshTopologyVertexOfCorner_Add,
# UV
GEONODES_OT_MeshUVPackIslands_Add,
GEONODES_OT_MeshUVUnwrap_Add
]

classes_geo_instances_OT = [
GEONODES_OT_InstancesOnPoints_Add,
GEONODES_OT_InstancesToPoints_Add,
GEONODES_OT_InstancesRealizeInstances_Add,
GEONODES_OT_InstancesRotateInstances_Add,
GEONODES_OT_InstancesScaleInstances_Add,
GEONODES_OT_InstancesTranslateInstancess_Add,
GEONODES_OT_InstancesInputInstanceRotaion_Add,
GEONODES_OT_InstancesInputInstanceScale_Add,
]

classes_geo_materials_OT = [
GEONODES_OT_MaterialReplaceMaterial_Add,
GEONODES_OT_MaterialIndex_Add,
GEONODES_OT_MaterialSelection_Add,
GEONODES_OT_Material_Add,
GEONODES_OT_MaterialSetMaterialIndex_Add,
]

classes_geo_input_OT = [
#Constant
GEONODES_OT_InputBool_Add,
GEONODES_OT_InputColor_Add,
GEONODES_OT_InputImage_Add,
GEONODES_OT_InputIntegerd_Add,
GEONODES_OT_InputMateriald_Add,
GEONODES_OT_InputString_Add,
GEONODES_OT_Inputvalue_Add,
GEONODES_OT_InputStoreNamedAttribute_Add,
#Group
GEONODES_OT_InputGroup_Add,
#Scene
GEONODES_OT_3DCursor_Add,
GEONODES_OT_InputCollectionInfo_Add,
GEONODES_OT_InputColInfo_Add,
GEONODES_OT_InputImageInfo_Add,
GEONODES_OT_InputIsViewport_Add,
GEONODES_OT_InputObjectInfo_Add,
GEONODES_OT_InputSceneTime_Add,
GEONODES_OT_InputSelfObject_Add
]

classes_geo_geometry_OT = [
GEONODES_OT_GeometryGeometryToDistance_Add,
GEONODES_OT_GeometryJoinGeometry_Add,
GEONODES_OT_GeometryID_Add,
GEONODES_OT_GeometryIndex_Add,
GEONODES_OT_GeometryAttribute_Add,
GEONODES_OT_GeometryNormal_Add,
GEONODES_OT_GeometryPosition_Add,
GEONODES_OT_GeometryRadious_Add,
GEONODES_OT_GeometrySelection_Add,
GEONODES_OT_GeometryProximity_Add,
GEONODES_OT_GeometryNearest_Add,
GEONODES_OT_GeometryRaycast_Add,
GEONODES_OT_GeometrySampleIndex_Add,
GEONODES_OT_GeometrySampleNearest_Add,
GEONODES_OT_GeometrySetSelection_Add,
GEONODES_OT_GeometrySetIDt_Add,
GEONODES_OT_GeometrySetPosition_Add,
GEONODES_OT_GeometryBoundBox_Add,
GEONODES_OT_GeometryConvexHUll_Add,
GEONODES_OT_GeometryDeleteGeometry_Add,
GEONODES_OT_GeometryDuplicateElements_Add,  
GEONODES_OT_GeometryMergeByDistance_Add,
GEONODES_OT_GeometryTransform_Add,
GEONODES_OT_GeometrySeparateComponents_Add,
GEONODES_OT_GeometrySeparateGeometry_Add
]

classes_geo_curve_OT = [
GEONODES_OT_CurveHandlePositions_Add, 
GEONODES_OT_CurveLength_Add,    
GEONODES_OT_CurveTangent_Add,
GEONODES_OT_CurveTilt_Add,
GEONODES_OT_CurveEndPointSelection_Add,
GEONODES_OT_CurveHandleTypeSelection_Add,
GEONODES_OT_CurveSplineCyclic_Add,
GEONODES_OT_CurveSplineLength_Add,
GEONODES_OT_CurveSplineParameter_Add,
GEONODES_OT_CurveSplineResolution_Add,
GEONODES_OT_CurveSetCurveNormal_Add,
GEONODES_OT_CurveSetCurveRadius_Add,
GEONODES_OT_CurveSetCurveTilt_Add,
GEONODES_OT_CurveSetCurveHandlePositions_Add,
GEONODES_OT_CurveSetHandleType_Add,
GEONODES_OT_CurveSetSplineCyclic_Add,
GEONODES_OT_CurveSetSplineResolution_Add,
GEONODES_OT_CurveSetSplineType_Add,
# Curve -- Operations
GEONODES_OT_CurveToMesh_Add,
GEONODES_OT_CurveCurveToPoints_Add,
GEONODES_OT_CurveDeformCurvesOnSurface_Add,
GEONODES_OT_CurveFillCurve_Add,
GEONODES_OT_CurveFilletCurve_Add,
GEONODES_OT_CurveInterpolateCurves_Add,
GEONODES_OT_CurveResampleCurve_Add,
GEONODES_OT_CurveReverseCurve_Add,
GEONODES_OT_CurveSubdvideCurve_Add,
GEONODES_OT_CurveTrimCurve_Add,
# Primitives
GEONODES_OT_CurveArc_Add, 
GEONODES_OT_CurveBezierSegment_Add, 
GEONODES_OT_CurveCircle_Add, 
GEONODES_OT_CurveLine_Add, 
GEONODES_OT_CurveSpiral_Add, 
GEONODES_OT_CurveQuadraticBezier_Add, 
GEONODES_OT_CurveQuadrilateral_Add, 
GEONODES_OT_CurveCurveStar_Add, 
# Topology
GEONODES_OT_CurveCurveofPoint_Add, 
GEONODES_OT_CurveOffsetPointinCurve_Add, 
GEONODES_OT_CurvePointsofCurve_Add
]

classes_geo_attribute_OT = [
GEONODES_OT_AttStatistic_Add,
GEONODES_OT_AttDomainSize_Add,
GEONODES_OT_AttBlur_Add,
GEONODES_OT_AttCapture_Add, 
GEONODES_OT_AttRemove_Add,
GEONODES_OT_AttStoreNamed_Add
]


classes_GeoNodes_All = (
    classes_geo_volume_OT +
    classes_geo_utilities_OT +
    classes_geo_texture_OT +
    classes_geo_simlulation_OT +
    classes_geo_point_OT +
    classes_geo_output_OT +
    classes_geo_mesh_OT +
    classes_geo_instances_OT +
    classes_geo_materials_OT +
    classes_geo_input_OT +
    classes_geo_geometry_OT +
    classes_geo_curve_OT +
    classes_geo_attribute_OT
)
