import bpy







# Geometry Nodes -- Attribute Main -- 6 Itens
class EXTRANODES_PT_ExtraNodesPanel(bpy.types.Panel):
    bl_idname = "EXTRANODES_PT_ExtraNodesPanel"
    bl_label = "Extra Nodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "NMT - Nodes"
    bl_context = "object"
    bl_description = "All nodes in a easy way to access."
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "ShaderNodeTree"    


    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Shader Editor Editor Extra Nodes:")
        #layout.label(text="Issues: \nIt will add the new group \n only outside of the current group.")
        grid = layout.grid_flow(row_major=True, columns=1, align=True)        

        grid.operator('import.node_extra_nodes_bool_group', text="Boolean")
        grid.operator('import.node_extra_nodes_integer_group', text="Interger")
        grid.operator('import.node_extra_nodes_color_mix_five_group', text="Color Mixer 5 Slots")
        grid.operator('import.node_extra_nodes_color_mix_ten_group', text="Color Mixer 10 Slots")
        grid.operator('import.node_extra_nodes_shader_mix_five_group', text="Shader Mixer 5 Slots")
        grid.operator('import.node_extra_nodes_shader_mix_ten_group', text="Shader Mixer 10 Slots")
        grid.operator('import.node_extra_nodes_blur_group', text="Blur")

        return None


classes_ExtraNodes_PT = [
    EXTRANODES_PT_ExtraNodesPanel,
]    