import bpy








#OCTANE General Panel List

class OCTANE_PT_Shader_Utilities_Panel(bpy.types.Panel):
    bl_idname = "OCTANE_PT_Shader_Utilities_Panel"
    bl_label = "Utilities"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "ShaderNodeTree"    


    # Draw Dropdown Menu
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Default Blender Nodes")

        grid = layout.grid_flow(row_major=True, columns=2, align=True)        
        grid.prop(scene, "Break_Col", text="Break Column")
        grid.prop(scene, "Panel_Row_Major_Switch", text="Row Major")

        return None

class OCTANE_PT_MainPanel(bpy.types.Panel):
    bl_idname = "OCTANE_PT_MainPanel"
    bl_label = "Octane Nodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"

    @classmethod
    def poll(self, context):
        return context.scene.render.engine in {'octane'} and context.area.ui_type in {'ShaderNodeTree', 'octane_render_aov_nodes'}   


    # Draw Dropdown Menu
    def draw(self, context):
        layout = self.layout

        return None


# Output 
class OCTANE_PT_OutputPanel(bpy.types.Panel):
    bl_idname = "OCTANE_PT_OutputPanel"
    bl_label = "Output"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "OCTANE_PT_MainPanel"
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
        
        grid.operator("nodes.octane_output_aov_group_output_node_add", text="AOV Group Output")                            # Add Shader

        return None

# Advanced Tools 
class OCTANE_PT_AdvancedToolsPanel(bpy.types.Panel):
    bl_idname = "OCTANE_PT_AdvancedToolsPanel"
    bl_label = "Advanced Tools"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "OCTANE_PT_MainPanel"
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
        
        grid.operator("nodes.octane_object_data_add", text="Camera Data")                            
        grid.operator("nodes.octane_object_data_add", text="Object Data")                   

        return None

# Render Settings
class OCTANE_PT_RenderSettingsPanel(bpy.types.Panel):
    bl_idname = "OCTANE_PT_RenderSettingsPanel"
    bl_label = "Advanced Tools"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_parent_id = "OCTANE_PT_MainPanel"
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
        
        grid.operator("nodes.octane_camera_imager_add", text="Camera Imager")                               
        grid.operator("nodes.octane_ocio_color_space_add", text="OCIO Color Space")                             
                                

        return None


classes_OCTANE_PT = [
    #OCTANE_PT_Shader_Utilities_Panel,
    OCTANE_PT_MainPanel,
    OCTANE_PT_OutputPanel,
    OCTANE_PT_AdvancedToolsPanel,
    OCTANE_PT_RenderSettingsPanel
]
