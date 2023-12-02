import bpy






# General Toogle for Break panels in 2 Columns

#class My_settings(bpy.types.PropertyGroup):
    #Break_Col: bpy.props.BoolProperty(name='Boolean Checkbox', default=False )


Break_Col: bpy.props.BoolProperty(default=False )
Panel_Row_Major_Switch: bpy.props.BoolProperty(default=False, description='True = Complete line First | False = Complete Column First')

#Break_Col: bpy.props.BoolProperty(default=False) 

# Geometry Nodes -- Attribute Main -- 6 Itens
class GEONODES_PT_UtilitiesPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesPanel"
    bl_label = "Utilities"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    
    
    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene
        # Bool Button for Activate Break Columns
        layout.label(text="Geometry Nodes Panel")
        grid = layout.grid_flow(row_major=True, columns=2, align=True)        
        grid.prop(scene, "Break_Col", text="Break Column")
        grid.prop(scene, "Panel_Row_Major_Switch", text="Row Major")

        return None


# Geometry Nodes -- Attribute Main -- 6 Itens
class GEONODES_PT_AttributePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_AttributePanel"
    bl_label = "Attribute"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0

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
        
        grid.operator("nodes.att_statistic_add", text="Attribute Statistic")                # Attribute Statistic
        grid.operator("nodes.att_domain_size_add", text="Domain Size")                      # Domain Size 
        grid.operator("nodes.att_blur_add", text="Blur Attribute")                          # Blur Attribute 
        grid.operator("nodes.att_capture_add", text="Capture Attribute")                    # Capture Attribute 
        grid.operator("nodes.att_remove_add", text="Remove Named Attribute")                # Remove Named Attribute 
        grid.operator("nodes.att_store_named_add", text="Store Named Attribute")            # Store Named Attribute        

        return None

# Geometry Nodes -- Input Main -- 3 subpanels --- 15 Itens
class GEONODES_PT_InputPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_InputPanel"
    bl_label = "Input"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 1

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    


    def draw(self, context):
        layout = self.layout

        return None

# Geometry Nodes -- Input Subpanel -- Constant --- 8 Items
class GEONODES_PT_InputConstantPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_InputConstantPanel"
    bl_label = "Constant"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_InputPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 2

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
        
        grid.operator("nodes.input_bool_add", text="Boolean")                                       # Boolean
        grid.operator("nodes.input_color_add", text="Color")                                        # Color 
        grid.operator("nodes.input_image_add", text="Image")                                        # Image 
        grid.operator("nodes.input_integer_add", text="Integer")                                    # Integer 
        grid.operator("nodes.input_material_add", text="Material")                                  # Material
        grid.operator("nodes.input_string_add", text="String")                                      # String  
        grid.operator("nodes.input_value_add", text="Value")                                    # Value 
        grid.operator("nodes.input_store_named_attribute_add", text="Store Named Attribute")        # Vector        

        return None

# Geometry Nodes -- Input Subpanel -- Group --- 1 Item
class GEONODES_PT_InputGroupPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_InputGroupPanel"
    bl_label = "Group Input"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_InputPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 3

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        if scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False


        # grid layout
        grid = layout.grid_flow(row_major=MajorRowRes, columns=1, align=True)
        
        grid.operator("nodes.input_group_add", text="Group Input")                # Group Input

        return None

# Geometry Nodes -- Input Subpanel -- Scene --- 6 Itens
class GEONODES_PT_InputScenePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_InputScenePanel"
    bl_label = "Scene"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_InputPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 4

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
        
        if context.space_data.geometry_nodes_type == 'TOOL':
            grid.operator("nodes.input_3d_cursor_add", text="3D Cursor")                 # 3D Cursor TOOL EXCLUSIVE
            grid.operator("nodes.input_collection_info_add", text="Collection Info")     # Collection Info
            grid.operator("nodes.input_image_info_add", text="Image Info")               # Image Info
            grid.operator("nodes.input_is_viewport_add", text="Is Viewport")             # Is Viewport 
            grid.operator("nodes.input_object_info_add", text="Object Info")             # Object Info 
            grid.operator("nodes.input_scene_time_add", text="Scene Time")               # Scene Time 
            grid.operator("nodes.input_self_object_add", text="Self Object")             # Self Object
            if scene.Break_Col:
                grid.operator("null.operator_type", text="")              # Add A New Empty Slot for Equal Distribution

        else:
            grid.operator("nodes.input_image_info_add", text="Image Info")               # Image Info
            grid.operator("nodes.input_collection_info_add", text="Collection Info")     # Collection Info            
            grid.operator("nodes.input_is_viewport_add", text="Is Viewport")             # Is Viewport 
            grid.operator("nodes.input_object_info_add", text="Object Info")             # Object Info 
            grid.operator("nodes.input_scene_time_add", text="Scene Time")               # Scene Time 
            grid.operator("nodes.input_self_object_add", text="Self Object")             # Self Object

        return None

# Geometry Nodes -- Output -- 2 Itens
class GEONODES_PT_OutputPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_OutputPanel"
    bl_label = "Output"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    #bl_parent_id = ""
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 5

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    
    
    def draw(self, context):
        layout = self.layout
        
        if context.scene.Break_Col:
            BoolRes = 2
        else:
            BoolRes = 1

        if context.scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False


        grid = layout.grid_flow(row_major=MajorRowRes, columns=BoolRes, align=True)

        grid.operator("nodes.output_group_add", text="Group Output")               # Group Output
        grid.operator("nodes.output_viewer_add", text="Viewer")             # Viewer

        return None

############################## Geometry Main Panel ####################################

# Geometry Nodes -- Geometry -- Main -- 4 Listas and 2 Itens
class GEONODES_PT_GeometryPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_GeometryPanel"
    bl_label = "Geometry"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    #bl_parent_id = ""
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 6

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    


    def draw(self, context):
        layout = self.layout

        if context.scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False

        
        if context.scene.Break_Col:
            BoolRes = 2
        else:
            BoolRes = 1

        grid = layout.grid_flow(row_major=MajorRowRes, columns=BoolRes, align=True)

        grid.operator("nodes.geometry_to_distance_add", text="Geometry to Distance")      # Geometry to Distance
        grid.operator("nodes.geometry_join_geometry_add", text="Join Geometry")           # Join Geometry


        return None   


# Geometry Nodes -- Geometry Subpanel -- Read --- 6 Itens
class GEONODES_PT_GeometryReadPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_GeometryReadPanel"
    bl_label = "Read"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_GeometryPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 7

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    ReadBreakTo2Col: bpy.props.BoolProperty(default=False)  

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
        if context.space_data.geometry_nodes_type == 'TOOL':
            grid.operator("nodes.geometry_id_add", text="Geometry ID")
            grid.operator("nodes.geometry_index_add", text="Geometry Index")
            grid.operator("nodes.geometry_attribute_add", text="Geometry Attribute")
            grid.operator("nodes.geometry_normal_add", text="Normal")
            grid.operator("nodes.geometry_position_add", text="Position")                   
            grid.operator("nodes.geometry_radius_add", text="Radius")                       
            grid.operator("nodes.geometry_selection_add", text="Selection") # Tool Exclusive
            if scene.Break_Col:
                grid.operator("null.operator_type", text="")
        else:
            grid.operator("nodes.geometry_id_add", text="Geometry ID")
            grid.operator("nodes.geometry_index_add", text="Geometry Index")
            grid.operator("nodes.geometry_attribute_add", text="Geometry Attribute")
            grid.operator("nodes.geometry_normal_add", text="Normal")
            grid.operator("nodes.geometry_position_add", text="Position")                   
            grid.operator("nodes.geometry_radius_add", text="Radius")                       


        return None


# Geometry Nodes -- Geometry Subpanel -- Sample --- 5 Itens
class GEONODES_PT_GeometrySamplePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_GeometrySamplePanel"
    bl_label = "Sample"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_GeometryPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 8

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    GeoSampleBreakTo2Col: bpy.props.BoolProperty(default=False)

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
        
        grid.operator("nodes.geometry_proximity_add", text="Geometry Proximity")            # Geometry Proximity
        grid.operator("nodes.geometry_index_nearest_add", text="Index of Nearest")          # Index of Nearest 
        grid.operator("nodes.geometry_raycast_add", text="Raycast")                         # Raycast 
        grid.operator("nodes.geometry_sample_index_add", text="Sample Index")               # Sample Index 
        grid.operator("nodes.geometry_sample_nearest_add", text="Sample Nearest")           # Sample Nearest


        if scene.Break_Col:
            grid.operator("null.operator_type", text="")              # Add A New Empty Slot for Equal Distribution

        return None


# Geometry Nodes -- Geometry Subpanel -- Write --- 5 Itens
class GEONODES_PT_GeometryWritePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_GeometryWritePanel"
    bl_label = "Write"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_GeometryPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 9

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    def draw(self, context):
        layout = self.layout
        
        if context.scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False


        if context.scene.Break_Col:
            BoolRes = 2
        else:
            BoolRes = 1

        grid = layout.grid_flow(row_major=MajorRowRes, columns=BoolRes, align=True)
        
        if context.space_data.geometry_nodes_type == 'TOOL':
            grid.operator("nodes.geometry_set_id_add", text="Set ID")                     # Set ID
            grid.operator("nodes.geometry_set_position_add", text="Set Position")         # Set Position
            grid.operator("nodes.geometry_set_selection_add", text="Set Selection")         # Set Position
            if context.scene.Break_Col:
                grid.operator("null.operator_type", text="")              # Add A New Empty Slot for Equal Distribution

        else:
            grid.operator("nodes.geometry_set_id_add", text="Set ID")                     # Set ID
            grid.operator("nodes.geometry_set_position_add", text="Set Position")         # Set Position
        

        return None


# Geometry Nodes -- Geometry Subpanel -- Operations --- 5 Itens
class GEONODES_PT_GeometryOperationsPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_GeometryOperationsPanel"
    bl_label = "Operation"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_GeometryPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 10

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
        
        grid.operator("nodes.geometry_bound_box_add", text="Bounding Box")                             # Bound Bo
        grid.operator("nodes.geometry_convex_hull_add", text="Convex Hull")                         # Convex Hull 
        grid.operator("nodes.geometry_delete_geometry_add", text="Delete Geometry")                 # Delete Geometry 
        grid.operator("nodes.geometry_duplicate_elements_add", text="Duplicate Elements")           # Duplicate Elements 
        grid.operator("nodes.geometry_merge_by_distance_add", text="Merge by Distance")             # Merge by Distance
        grid.operator("nodes.geometry_transform_add", text="Transform Geometry")                    # Transform Geometry
        grid.operator("nodes.geometry_separate_components_add", text="Separate Componets")          # Separate Componets
        grid.operator("nodes.geometry_separate_geometry_add", text="Separate Geometry")             # Separate Geometry

        return None

############################## Curve Main Panel ####################################

# Geometry Nodes -- Curve Main Panel
class GEONODES_PT_CurvePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurvePanel"
    bl_label = "Curve"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    #bl_parent_id = "GEONODES_PT_GeometryPanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 11

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    


    def draw(self, context):

        return None

# Geometry Nodes -- Curve Subpanel -- Read --- 10 Itens
class GEONODES_PT_CurveReadPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurveReadPanel"
    bl_label = "Read"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_CurvePanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 12

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    def draw(self, context):
        layout = self.layout

        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        if scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False


        # grid layout
        grid = layout.grid_flow(row_major=MajorRowRes, columns=BoolRes, align=True)
        
        grid.operator("nodes.curve_handle_positions_add", text="Handle Position")                           # Handle Position
        grid.operator("nodes.curve_length_add", text="Curve Length")                                        # Curve Length" 
        grid.operator("nodes.curve_tangent_add", text="Curve Tangent")                                      # Curve Tangent 
        grid.operator("nodes.curve_tilt_add", text="Curve Tilt")                                            # Curve Tilt 
        grid.operator("nodes.curve_end_point_selection__add", text="Endpoint Selection")                    # End Point Selection
        grid.operator("nodes.curve_handle_type_selection_add", text="Handle Type Selection")                # Handle Type Selection
        grid.operator("nodes.curve_spline_cyclic_add", text="Spline Cyclic")                                # Spline Cyclic
        grid.operator("nodes.curve_spline_length_add", text="Spline Length")                                # Spline Length
        grid.operator("nodes.curve_spline_parameter_add", text="Spline Parameter")                          # Spline Parameter
        grid.operator("nodes.curve_spline_resolution_add", text="Spline Resolution")                        # Spline Resolution

        return None

# Geometry Nodes -- Curve Subpanel -- Read --- 10 Itens
class GEONODES_PT_CurveSamplePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurveSamplePanel"
    bl_label = "Sample"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_CurvePanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 12

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    def draw(self, context):
        layout = self.layout

        if context.scene.Panel_Row_Major_Switch:
            MajorRowRes = True
        else:
            MajorRowRes = False


        # Boolean Button to Split the column in 2
        scene = context.scene

        if scene.Break_Col:
            BoolRes = 2        
        else:
            BoolRes = 1

        # grid layout
        grid = layout.grid_flow(row_major=MajorRowRes, columns=BoolRes, align=True)
        
        grid.operator("nodes.curve_handle_positions_add", text="Handle Position")                           # Handle Position
        grid.operator("nodes.curve_length_add", text="Curve Length")                                        # Curve Length" 
        grid.operator("nodes.curve_tangent_add", text="Curve Tangent")                                      # Curve Tangent 
        grid.operator("nodes.curve_tilt_add", text="Curve Tilt")                                            # Curve Tilt 
        grid.operator("nodes.curve_end_point_selection__add", text="Endpoint Selection")                    # End Point Selection
        grid.operator("nodes.curve_handle_type_selection_add", text="Handle Type Selection")                # Handle Type Selection
        grid.operator("nodes.curve_spline_cyclic_add", text="Spline Cyclic")                                # Spline Cyclic
        grid.operator("nodes.curve_spline_length_add", text="Spline Length")                                # Spline Length
        grid.operator("nodes.curve_spline_parameter_add", text="Spline Parameter")                          # Spline Parameter
        grid.operator("nodes.curve_spline_resolution_add", text="Spline Resolution")                        # Spline Resolution

        return None

# Geometry Nodes -- Curve Subpanel -- Write --- 8 Itens
class GEONODES_PT_CurveWritePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurveWritePanel"
    bl_label = "Write"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_CurvePanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 13

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
        
        grid.operator("nodes.curve_set_curve_normal_add", text="Set Curve Normal")                              # Set Curve Normal
        grid.operator("nodes.curve_set_curve_radius_add", text="Set Curve Radius")                              # Set Curve Radius" 
        grid.operator("nodes.curve_set_curve_tilt_add", text="Set Curve Tilt")                                  # Set Curve Tilt 
        grid.operator("nodes.curve_set_handle_positions_add", text="Set Handle Position")                          # Set Curve Handle Type 
        grid.operator("nodes.curve_set_handle_add", text="Set Handle Type")                                         # Set Handles
        grid.operator("nodes.curve_set_spline_cyclic_add", text="Set Spline Cyclic")                            # Set Spline Cyclic
        grid.operator("nodes.curve_set_spline_resolution_add", text="Set Spline Resolution")                    # Set Spline Resolution
        grid.operator("nodes.curve_set_spline_type_add", text="Set Spline Type")                                # Set Spline Type

        return None

# Geometry Nodes -- Curve Subpanel -- Operations --- 10 Itens
class GEONODES_PT_CurveOperationsPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurveOperationsPanel"
    bl_label = "Operations"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_CurvePanel"
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

        grid.operator("nodes.curve_to_mesh_add", text="Curve to Mesh")                                          # Curve to Mesh
        grid.operator("nodes.curve_to_points_add", text="Curve to Points")                                      # Curve to Points
        grid.operator("nodes.curve_deform_curves_on_surface_add", text="Deform Curves on Surface")              # Deform Curves on Surface  
        grid.operator("nodes.curve_fill_curve_add", text="Fill Curve")                                          # Fill Curve 
        grid.operator("nodes.curve_fillet_curve_add", text="Fillet Curve")                                      # Fillet Curve
        grid.operator("nodes.curve_interpolate_curves_add", text="Interpolate Curves")                          # Interpolate Curves
        grid.operator("nodes.curve_resample_curve_add", text="Resample Curves")                                 # Resample Curves
        grid.operator("nodes.curve_reverse_curve_add", text="Reverse Curve")                                   # Reverse Curves
        grid.operator("nodes.curve_subdivide_curve_add", text="Subdivide Curve")                                # Subdivide Curve
        grid.operator("nodes.curve_trim_curve_add", text="Trim Curve")                                          # Trim Curve

        return None

# Geometry Nodes -- Curve Subpanel -- Operations --- 10 Itens
class GEONODES_PT_CurvePrimitivesPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurvePrimitivesPanel"
    bl_label = "Primitives"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_CurvePanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 15

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

        grid.operator("nodes.curve_arc_add", text="Arc")                                            # Arc
        grid.operator("nodes.curve_curve_bezier_segment_type_add", text="Bezier Segment")           # Bezier Segment
        grid.operator("nodes.curve_curve_circle_add", text="Circle")                                # Circle  
        grid.operator("nodes.curve_line_add", text="Line")                                          # Line
        grid.operator("nodes.curve_spiral_type_add", text="Spiral")                                 # Spiral
        grid.operator("nodes.curve_quadratic_bezier_add", text="Quadratic")                         # Quadratic
        grid.operator("nodes.curve_quadrilateral_add", text="Quradrilateral")                       # Quradrilateral
        grid.operator("nodes.curve_curve_star_add", text="Star")                                    # Star

        return None

# Geometry Nodes -- Curve Subpanel -- Topology --- 8 Itens
class GEONODES_PT_CurveTopologyPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_CurveTopologyPanel"
    bl_label = "Topology"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "GEONODES_PT_CurvePanel"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 16

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

        grid.operator("nodes.curve_of_points_add", text="Curve of Points")                              # Curve of Points
        grid.operator("nodes.curve_offset_point_in_curve_add", text="Offset Points in Curve")           # Offset Points in Curve
        grid.operator("nodes.curve_points_in_curve_add", text="Points in Curve")                        # Points in Curve  
        
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")              # Add A New Empty Slot for Equal Distribution
        else:

            return None

# Geometry Nodes -- Curve Subpanel -- Instances --- 10 Itens
class GEONODES_PT_InstancesPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_InstancesPanel"
    bl_label = "Instances"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 17

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

        grid.operator("nodes.instances_on_points_add", text="Instance on Points")                                   # Instance on Points
        grid.operator("nodes.instances_to_points_add", text="Instances To Points")                                  # Instances To Points
        grid.operator("nodes.instances_realize_insances_add", text="Realize Instances")                             # Realize Instances  
        grid.operator("nodes.instance_rotate_instances_add", text="Rotate Instances")                               # Rotate Instances
        grid.operator("nodes.instances_scale_instances_add", text="Scale Instances")                                # Scale Instances
        grid.operator("nodes.instances_translate_instances_add", text="Translate Instances")                        # Translate Instances  
        grid.operator("nodes.instances_input_instance_rotation_add", text="Input Instance Rotation")                # Input Instance Rotation
        grid.operator("nodes.instances_input_instance_scale_add", text="Input Instance Scale")                      # Input Instance Scale  

        return None

############################## Mesh Panel ####################################

# Geometry Nodes -- Mesh -- Main --- 7 Lists
class GEONODES_PT_MeshMainPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshMainPanel"
    bl_label = "Mesh"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 18

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "GeometryNodeTree"    

    def draw(self, context):
        layout = self.layout

        return None


# Geometry Nodes -- Mesh Subpanel -- Read --- 13 Itens
class GEONODES_PT_MeshReadPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshReadPanel"
    bl_label = "Read"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 19

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

        if context.space_data.geometry_nodes_type == 'TOOL':
            grid.operator("nodes.mesh_edge_angle_add", text="Edge Angle")
            grid.operator("nodes.mesh_edge_neigbors_add", text="Edge Neighbors")
            grid.operator("nodes.mesh_edge_vertices_add", text="Edge Vertices")
            grid.operator("nodes.mesh_edge_to_face_group_add", text="Edge To Face Groups")             
            grid.operator("nodes.mesh_face_area_add", text="Face Area")                                 
            grid.operator("nodes.mesh_face_set_boundaries_add", text="Face Group Boundaries")           
            grid.operator("nodes.mesh_face_neighbors_add", text="Face Neighbors")
            grid.operator("nodes.mesh_face_set_add", text="Face Set")                                   # Face Set TOOL EXCLUSIVE
            grid.operator("nodes.mesh_face_is_planar_add", text="Is Face is Planar")
            grid.operator("nodes.mesh_is_shade_smooth_add", text="Is Shade Smooth")
            grid.operator("nodes.mesh_is_edge_smooth_add", text="Is Edge Smooth")
            grid.operator("nodes.mesh_island_add", text="Mesh Island") 
            grid.operator("nodes.mesh_shortest_edges_paths_add", text="Shortest Edge Path")
            grid.operator("nodes.mesh_vertex_neighbors_add", text="Vertex Neighbors") 
        else:
            grid.operator("nodes.mesh_edge_angle_add", text="Edge Angle")
            grid.operator("nodes.mesh_edge_neigbors_add", text="Edge Neighbors")
            grid.operator("nodes.mesh_edge_vertices_add", text="Edge Vertices")
            grid.operator("nodes.mesh_edge_to_face_group_add", text="Edge To Face Groups")
            grid.operator("nodes.mesh_face_area_add", text="Face Area")
            grid.operator("nodes.mesh_face_set_boundaries_add", text="Face Group Boundaries")
            grid.operator("nodes.mesh_face_neighbors_add", text="Face Neighbors")
            grid.operator("nodes.mesh_face_is_planar_add", text="Is Face is Planar")
            grid.operator("nodes.mesh_is_shade_smooth_add", text="Is Shade Smooth")
            grid.operator("nodes.mesh_is_edge_smooth_add", text="Is Edge Smooth")
            grid.operator("nodes.mesh_island_add", text="Mesh Island") 
            grid.operator("nodes.mesh_shortest_edges_paths_add", text="Shortest Edge Path")
            grid.operator("nodes.mesh_vertex_neighbors_add", text="Vertex Neighbors")  
            if scene.Break_Col:
                grid.operator("null.operator_type", text="")

        return None

# Geometry Nodes -- Mesh Subpanel -- Sample --- 2 Itens
class GEONODES_PT_MeshSamplePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshSamplePanel"
    bl_label = "Sample"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 20

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

        grid.operator("nodes.mesh_sample_nearest_surface_add", text="Sample Nearest Surface")                       # Sample Nearest Surface
        grid.operator("nodes.mesh_saple_uv_surface_add", text="Sample UV Surface")                                  # Sample UV Surface

        return None

# Geometry Nodes -- Mesh Subpanel -- Write --- 1 Item
class GEONODES_PT_MeshWritePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshWritePanel"
    bl_label = "Write"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 20

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

        if context.space_data.geometry_nodes_type == 'TOOL':
            grid.operator("nodes.mesh_write_set_shade_smooth_add", text="Set Shade Smooth")                                   # Set Shade Smooth
            grid.operator("nodes.mesh_write_set_face_set_add", text="Set Face Set")
        else:  
            grid.operator("nodes.mesh_write_set_shade_smooth_add", text="Set Shade Smooth")                                   # Set Shade Smooth

        return None

# Geometry Nodes -- Mesh Subpanel -- Operations --- 14 Itens
class GEONODES_PT_MeshOperationsPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshOperationsPanel"
    bl_label = "Operations"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 21

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

        grid.operator("nodes.mesh_op_dual_mesh_add", text="Dual Mesh")                                      # Dual Mesh
        grid.operator("nodes.mesh_op_edge_paths_to_curve_add", text="Edge Paths to Curves")                  # Edge Paths to Curve
        grid.operator("nodes.mesh_op_edge_paths_to_selection_add", text="Edge Paths To Selection")          # Edge Paths To Selection
        grid.operator("nodes.mesh_op_extrude_mesh_add", text="Extrude Mesh")                                # Extrude Mesh
        grid.operator("nodes.mesh_op_flip_faces_add", text="Flip Faces")                                    # Flip Faces
        grid.operator("nodes.mesh_op_mesh_boolean_add", text="Mesh Boolean")                                # Mesh Boolean
        grid.operator("nodes.mesh_op_mesh_to_curve_add", text="Mesh To Curve")                              # Mesh To Curve
        grid.operator("nodes.mesh_op_mesh_to_points_add", text="Mesh To Points")                            # Mesh To Points
        grid.operator("nodes.mesh_op_mesh_to_volume_add", text="Mesh To Volume")                            # Mesh To Volume
        grid.operator("nodes.mesh_op_scale_elements_add", text="Scale Elements")                            # Scale Elements
        grid.operator("nodes.mesh_op_split_edges_add", text="Split Edges")                                  # Split Edges
        grid.operator("nodes.mesh_op_subdivide_mesh_add", text="Subdivide Mesh")                            # Subdivide Mesh
        grid.operator("nodes.mesh_op_subdivision_surface_add", text="Subdivision Surface")                  # Subdivision Surface
        grid.operator("nodes.mesh_op_triangulate_add", text="Triangulate")                                  # Triangulate                


        return None

# Geometry Nodes -- Mesh Subpanel -- Primitives --- 8 Itens
class GEONODES_PT_MeshPrimitivesPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshPrimitivesPanel"
    bl_label = "Primitives"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 22

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

        grid.operator("nodes.mesh_primitive_cone_add", text="Cone")                                   # Cone
        grid.operator("nodes.mesh_primitive_cube_add", text="Cube")                                   # Cube
        grid.operator("nodes.mesh_primitive_cylinder_add", text="Cylinder")                           # Cylinder
        grid.operator("nodes.mesh_primitive_grid_add", text="Grid")                                   # Grid
        grid.operator("nodes.mesh_primitive_ico_sphere_add", text="Ico Sphere")                       # Ico Sphere
        grid.operator("nodes.mesh_primitive_circle_add", text="Circle")                               # Circle
        grid.operator("nodes.mesh_primitive_mesh_line_add", text="Mesh Line")                         # Mesh Line
        grid.operator("nodes.mesh_primitive_uv_sphere_add", text="UV Sphere")                         # UV Sphere


        return None

# Geometry Nodes -- Mesh Subpanel -- Topology --- 8 Itens
class GEONODES_PT_MeshTopologyPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshTopologyPanel"
    bl_label = "Topology"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 23

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

        grid.operator("nodes.mesh_topo_corners_of_edge_add", text="Corners of Edge")                                    # Corners of Edge
        grid.operator("nodes.mesh_topo_corner_of_face_add", text="Corner of Face")                                      # Corner of Face
        grid.operator("nodes.mesh_topo_corner_of_vertex_add", text="Corner of Vertex")                                  # Corner of Vertex
        grid.operator("nodes.mesh_topo_edges_of_corner_add", text="Edges of Corner")                                    # Edges of Corner
        grid.operator("nodes.mesh_topo_edges_of_vertex_add", text="Edges of Vertex")                                    # Edges of Vertex
        grid.operator("nodes.mesh_topo_face_of_corner_add", text="Face of Corners")                                     # Face of Corners
        grid.operator("nodes.mesh_topo_offset_corner_in_face_add", text="Offset Corner in Face")                        # Offset Corner in Face
        grid.operator("nodes.mesh_topo_vertex_of_corner_add", text="Vertex of Corner")                                  # Vertex of Corner

        return None

# Geometry Nodes -- Mesh Subpanel -- UV --- 2 Itens
class GEONODES_PT_MeshUVPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MeshUVPanel"
    bl_label = "UV"
    bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 24

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

        grid.operator("nodes.mesh_uv_pack_island_add", text="Pack Islands")                           # Pack Islands
        grid.operator("nodes.mesh_uv_unwrap_add", text="UV Unwrap")                                   # UV Unwrap

        return None

# Geometry Nodes -- Points -- Main --- 7 Itens
class GEONODES_PT_PointsPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_PointsPanel"
    bl_label = "Points"
    #bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 25

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

        grid.operator("nodes.points_distribute_points_in_volume_add", text="Dist. Points in Volume")               # Distribute Points in Volume
        grid.operator("nodes.points_distribute_points_on_faces_add", text="Dist. Points on Faces")                 # Distribute Points on Faces
        grid.operator("nodes.points_points_add", text="Points")                                                         # Points
        grid.operator("nodes.points_to_curves_add", text="Points to Curves")                                            # Points to Curves
        grid.operator("nodes.points_to_vertices_add", text="Points to Vertives")                                        # Points to Vertives
        grid.operator("nodes.points_to_volume_add", text="Points to Volume")                                            # Points to Volume
        grid.operator("nodes.point_radius_add", text="Set Point Radius")                                                    # Point Radius
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")

            return None

# Geometry Nodes -- Volume -- Main --- 2 Items
class GEONODES_PT_VolumePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_VolumePanel"
    bl_label = "Volume"
    #bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 26

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

        grid.operator("nodes.volume_cube_add", text="Volume Cube")               # Volume Cube
        grid.operator("nodes.volume_to_mesh_add", text="Volume to Mesh")         # Volume to Mesh

        return None

# Geometry Nodes -- Simulation -- Main --- 1 Item
class GEONODES_PT_SimulationPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_SimulationPanel"
    bl_label = "Simulation"
    #bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 27

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

        grid.operator("nodes.simulation_zone_add", text="Simulation Zone")               # Simulation Zone


        return None

# Geometry Nodes -- Material -- Main --- 5 Itens
class GEONODES_PT_MaterialPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_MaterialPanel"
    bl_label = "Material"
    #bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 28

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

        grid.operator("nodes.material_replace_material_add", text="Replace Material")               # Replace Material
        grid.operator("nodes.material_index_add", text="Material Index")                            # Material Index
        grid.operator("nodes.material_selection_add", text="Material Selection")                    # Material Selection
        grid.operator("nodes.material_add", text="Set Material")                                    # Set Material
        grid.operator("nodes.set_material_index_add", text="Material Index")                        # Material Index
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")

            return None

# Geometry Nodes -- Material -- Main --- 5 Itens
class GEONODES_PT_TexturePanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_TexturePanel"
    bl_label = "Texture"
    #bl_parent_id = "GEONODES_PT_MeshMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 29

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

        grid.operator("nodes.texture_brick_add", text="Brick Texture")               # Brick Texture
        grid.operator("nodes.texture_checker_add", text="Checker Texture")           # Checker Texture
        grid.operator("nodes.texture_gradient_add", text="Gradient")                 # Gradient
        grid.operator("nodes.geo_image_texture_add", text="Image Texture")           # Image Texture
        grid.operator("nodes.texture_magic_add", text="Magic Texture")               # Magic Texture
        grid.operator("nodes.texture_musgrave_add", text="Musgrave")                 # Musgrave
        grid.operator("nodes.texture_noise_add", text="Noise Texture")               # Noise Texture
        grid.operator("nodes.texture_voronoi_add", text="Voronoi")                   # Voronoi
        grid.operator("nodes.texture_wave_add", text="Wave Texture")                 # Wave Texture
        grid.operator("nodes.texture_white_noise_add", text="White Noise")           # White Noise

        return None

################# UTILITIES -- 6 Lists + 3 Itens #################

# Geometry Nodes -- Utilities -- Main --- 3 Itens
class GEONODES_PT_UtilitiesMainPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesMainPanel"
    bl_label = "Utilities"
    #bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 30

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

        grid.operator("nodes.utilities_random_value_add", text="Random Value")         # Random Value
        grid.operator("nodes.utilities_repeat_zone_add", text="Repeat Zone")           # Repeat Zone
        grid.operator("nodes.utilities_switch_add", text="Switch")                     # Switch
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")
        return None


################# Color -- 5 Itens #################

# Geometry Nodes -- Utilities -- Color --- 5 Itens
class GEONODES_PT_UtilitiesColorPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesColorPanel"
    bl_label = "Color"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 31

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

        grid.operator("nodes.utilities_color_ramp_add", text="Color Ramp")               # Color Ramp
        grid.operator("nodes.utilities_rgb_curve_add", text="RGB Curve")                 # RGB Curve
        grid.operator("nodes.utilities_combine_color_add", text="Combine Color")         # Combine Color
        grid.operator("nodes.utilities_mix_color_add", text="Mix Color")                 # Mix Color
        grid.operator("nodes.texture_gradient_add", text="Separate Color")               # Separate Color
        
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")
        return None

################# Text -- 7 Itens #################

# Geometry Nodes -- Utilities -- Text --- 5 Itens
class GEONODES_PT_UtilitiesTextPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesTextPanel"
    bl_label = "Text"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 32

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

        grid.operator("nodes.utilities_string_join_add", text="String Join")                        # String Join
        grid.operator("nodes.utilities_replace_string_add", text="Replace String")                  # Replace String
        grid.operator("nodes.utilities_slice_string_add", text="Slice String")                      # Slice String
        grid.operator("nodes.utilities_string_length_add", text="String Length")                    # String Length
        grid.operator("nodes.utilities_string_to_curve_add", text="String To Curves")               # String To Curves
        grid.operator("nodes.utilities_value_to_string_add", text="Value To String")                # Value To String
        grid.operator("nodes.utilities_special_characters_add", text="Special Characters")          # Special Characters
        
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")
        return None

################# Vector -- 6 Itens #################

# Geometry Nodes -- Utilities -- Vector --- 6 Itens
class GEONODES_PT_UtilitiesVectorPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesVectorPanel"
    bl_label = "Vector"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 32

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

        grid.operator("nodes.utilities_vector_curve_add", text="Vector Curve")             # Vector Curve
        grid.operator("nodes.utilities_vector_math_add", text="Vector Math")               # Vector Math
        grid.operator("nodes.utilities_vector_rotate_add", text="Vector Rotate")           # Vector Rotate
        grid.operator("nodes.utilities_combine_xyz_add", text="Combine XYZ")               # Combine XYZ
        grid.operator("nodes.utilities_vector_mix_add", text="Vector Mix")                 # Vector Mix
        grid.operator("nodes.utilities_separate_xyz_add", text="Separate XYZ")             # Separate XYZ
        
        return None

################# Field -- 3 Itens #################

# Geometry Nodes -- Utilities -- Field --- 3 Itens
class GEONODES_PT_UtilitiesFieldPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesFieldPanel"
    bl_label = "Field"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 33

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

        grid.operator("nodes.utilities_accumulate_field_add", text="Accumulate Field")       # Accumulate Field
        grid.operator("nodes.utilities_field_at_index_add", text="Field At Index")           # Field At Index
        grid.operator("nodes.utilities_field_on_domain_add", text="Field On Domain")         # Field On Domain
        
        if scene.Break_Col:
            grid.operator("null.operator_type", text="")
        
        return None

################# Math -- 8 Itens #################  !! 5 Are the same as Shader Nodes

# Geometry Nodes -- Utilities -- Math --- 8 Itens
class GEONODES_PT_UtilitiesMathPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesMathPanel"
    bl_label = "Math"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 34

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

        grid.operator("nodes.utilities_boolean_math_add", text="Boolean Math")      # Boolean Math
        grid.operator("nodes.conv_clamp_add", text="Clamp")                         # Clamp
        grid.operator("nodes.utilities_compare_add", text="Compare")                # Compare
        grid.operator("nodes.conv_float_curve_add", text="Float Curve")             # Float Curve
        grid.operator("nodes.utilities_float_to_int_add", text="Float To Integer")  # Float To Int
        grid.operator("nodes.conv_map_range_add", text="Map Range")                 # Map Range
        grid.operator("nodes.conv_math_add", text="Math")                           # Math
        grid.operator("nodes.conv_mix_add", text="Mix")                             # Gradient

        return None

################# Rotation -- 10 Itens #################

# Geometry Nodes -- Utilities -- Rotation --- 10 Itens

class GEONODES_PT_UtilitiesRotationPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_UtilitiesRotationPanel"
    bl_label = "Rotation"
    bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 35

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

        grid.operator("nodes.utilities_align_euler_to_vector_add", text="Align Euler to Vector")            # Align Euler to Vector
        grid.operator("nodes.utilities_axis_angle_to_rotation_add", text="Axis Angle to Rotation")          # Axis Angle to Rotation
        grid.operator("nodes.utilities_euler_to_rotation_add", text="Euler to Rotation")                    # Euler to Rotation
        grid.operator("nodes.utilities_invert_rotation_add", text="Invert Rotation")                        # Invert Rotation
        grid.operator("nodes.utilities_rotate_euler_add", text="Rotate Euler")                              # Rotate Euler
        grid.operator("nodes.utilities_rotate_vector_add", text="Rotate Vector")                            # Rotate Vector
        grid.operator("nodes.utilities_rotation_to_axis_add", text="Rotation to Axis Angle")                # Rotation to Axis Angle
        grid.operator("nodes.utilities_rotation_to_euler_add", text="Rotation to Euler")                    # Rotation to Euler
        grid.operator("nodes.utilities_rotation_to_quaternion_add", text="Rotation to Quaternion")          # Rotation to Quaternion
        grid.operator("nodes.utilities_quaternion_to_rotation_add", text="Quaternion to Rotation")          # Quaternion to Rotation
        
        return None

######################## Group ########################

# Geometry Nodes -- Group -- Main --- 2 Itens

class GEONODES_PT_GroupPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_GroupPanel"
    bl_label = "Group"
    #bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 36

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

        grid.operator("nodes.geo_input_group_add", text="Group Input")       # Group Input
        grid.operator("nodes.output_group_add", text="Group Output")          # Group Output

        return None


######################## Layout ########################

#Geometry Nodes -- Layout -- Main --- 2 Itens

class GEONODES_PT_LayoutPanel(bpy.types.Panel):
    bl_idname = "GEONODES_PT_LayoutPanel"
    bl_label = "Layout"
    #bl_parent_id = "GEONODES_PT_UtilitiesMainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 37

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







classes_GeoNodes_PT = [
GEONODES_PT_UtilitiesPanel,
GEONODES_PT_AttributePanel,
# Input
GEONODES_PT_InputPanel, 
GEONODES_PT_InputConstantPanel,
GEONODES_PT_InputGroupPanel,
GEONODES_PT_InputScenePanel,
# Output
GEONODES_PT_OutputPanel,
# Geometry
GEONODES_PT_GeometryPanel, 
GEONODES_PT_GeometryReadPanel,
GEONODES_PT_GeometrySamplePanel,
GEONODES_PT_GeometryWritePanel,
GEONODES_PT_GeometryOperationsPanel,
# Curve
GEONODES_PT_CurvePanel,
GEONODES_PT_CurveReadPanel,
GEONODES_PT_CurveSamplePanel,
GEONODES_PT_CurveWritePanel,
GEONODES_PT_CurveOperationsPanel,
GEONODES_PT_CurvePrimitivesPanel,
GEONODES_PT_CurveTopologyPanel,
# Instances
GEONODES_PT_InstancesPanel,
# Mesh
GEONODES_PT_MeshMainPanel,
GEONODES_PT_MeshReadPanel,
GEONODES_PT_MeshSamplePanel,
GEONODES_PT_MeshWritePanel,
GEONODES_PT_MeshOperationsPanel,
GEONODES_PT_MeshPrimitivesPanel,
GEONODES_PT_MeshTopologyPanel,
GEONODES_PT_MeshUVPanel,
# Points
GEONODES_PT_PointsPanel,
# Volume
GEONODES_PT_VolumePanel,
# Simulation Zone
GEONODES_PT_SimulationPanel,
# Material
GEONODES_PT_MaterialPanel,
# Texture
GEONODES_PT_TexturePanel,
# Utilities
GEONODES_PT_UtilitiesMainPanel,
GEONODES_PT_UtilitiesColorPanel,
GEONODES_PT_UtilitiesTextPanel,
GEONODES_PT_UtilitiesVectorPanel,
GEONODES_PT_UtilitiesFieldPanel,
GEONODES_PT_UtilitiesMathPanel,
GEONODES_PT_UtilitiesRotationPanel,
# Group
GEONODES_PT_GroupPanel,
# Layout 
GEONODES_PT_LayoutPanel,
]       

