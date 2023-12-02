import bpy









class NODE_OT_AddBoolSocket(bpy.types.Operator):
    bl_idname = "node.add_boolean_socket"
    bl_label = "Add a new socket type Boolean"
    bl_options = {'UNDO'}
    
    def execute(self, context):
        
        node = context.active_node

        # Check if the active node is a group or composite node
        if node.type in ('GROUP', 'COMPOSITE'):
            node_group = node.node_tree 
            node_group.nodes.active = node
            input_socket = node_group.new_socket('NodeSocketBool', 'Boolean Input')
            input_socket.default_value = False

        else:

            self.report({'ERROR'}, "Cannot add input to built-in node")

        return {'FINISHED'}


##  tree.interface.new_socket(name="My Input", in_out='INPUT')

##  node -- context.active_node

##  node group -- context.active_node.node_tree

classes_utils_OT = [
NODE_OT_AddBoolSocket    
]

