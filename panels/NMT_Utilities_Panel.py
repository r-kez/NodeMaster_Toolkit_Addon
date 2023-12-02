
import bpy
import os
import json
import re
from bpy.types import Menu
import bpy.utils.previews



######################################################################
#                          Favorites                                 #
######################################################################


config_path = bpy.utils.resource_path('USER') + '/config/'
json_file_path = config_path + 'NodeMasterToolkit_Favorites.json'

favorites_data = {
    "ShaderNodes": [],
    "GeometryNodes": []
}

def execute(self, context):
    current_context = context.area.ui_type
    
    return current_context

class MoveOperatorUpOperator(bpy.types.Operator):
    bl_idname = "script.move_operator_up"
    bl_label = "Move Operator Up"
    bl_description = "Move the selected operator up in the list"

    node_information: bpy.props.StringProperty()  # Add property here
    file_path = json_file_path

    def execute(self, context):
        node_information = self.node_information
        selected_info = bpy.context.window_manager.node_information.split('\n')
        selected_info = [info for info in selected_info if info]

        index = selected_info.index(node_information)

        if index > 0:
            selected_info[index], selected_info[index - 1] = selected_info[index - 1], selected_info[index]

            bpy.context.window_manager.node_information = '\n'.join(selected_info)
            self.update_json_file(selected_info)

        return {'FINISHED'}

    def update_json_file(self, data):
        favorites_data = {}
        current_context = bpy.context.area.ui_type

        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as file:
                favorites_data = json.load(file)

        favorites_data[current_context] = data

        with open(json_file_path, 'w') as file:
            json.dump(favorites_data, file)

class MoveOperatorDownOperator(bpy.types.Operator):
    bl_idname = "script.move_operator_down"
    bl_label = "Move Operator Down"
    bl_description = "Move the selected operator down in the list"

    node_information: bpy.props.StringProperty()  # Add property here
    file_path = json_file_path

    def execute(self, context):
        node_information = self.node_information
        selected_info = bpy.context.window_manager.node_information.split('\n')
        selected_info = [info for info in selected_info if info]

        index = selected_info.index(node_information)

        if index < len(selected_info) - 1:
            selected_info[index], selected_info[index + 1] = selected_info[index + 1], selected_info[index]

            bpy.context.window_manager.node_information = '\n'.join(selected_info)
            self.update_json_file(selected_info)

        return {'FINISHED'}

    def update_json_file(self, data):
        favorites_data = {}
        current_context = bpy.context.area.ui_type

        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as file:
                favorites_data = json.load(file)

        favorites_data[current_context] = data

        with open(json_file_path, 'w') as file:
            json.dump(favorites_data, file)

# Property to set the favorite list display count
set_fav_display: bpy.props.IntProperty(
    name="Favorite List Display",
    description="Set the number of nodes to be shown on the favorite list",
    default=10,
    min=1,
    max=20
)

# Path to Blender's configuration folder
config_path = bpy.utils.resource_path('USER') + '/config/'

class UpdateListOperator(bpy.types.Operator):
    bl_idname = "script.update_list"
    bl_label = "Force Update List"
    bl_description = "Update the displayed list"

    def execute(self, context):
        # Reading information from the .json file
        file_path = config_path + 'NodeMasterToolkit_Favorites.json'
        information = []
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                current_context = context.area.ui_type
                
                # Check if the current_context exists in the data dictionary
                if current_context in data:
                    information = data[current_context]

        # Updating the list in the Blender window
        bpy.context.window_manager.node_information = '\n'.join(information)

        # Forcing panel redraw
        bpy.context.area.tag_redraw()

        self.report({'INFO'}, "List updated")
        return {'FINISHED'}

# Operator to save information to a .json file
class SaveInfoOperator(bpy.types.Operator):
    bl_idname = "script.save_info"
    bl_label = "Save Information"
    bl_description = "Save information about the selected node"
    
    def execute(self, context):
        # Getting the selected node
        current_node = bpy.context.active_node
        
        # Getting node information
        node_name = current_node.name
        node_type = current_node.bl_idname
        
        # Removing numerical variations from the node name
        base_node_name = re.sub(r'\.\d+', '', node_name)
        
        # Creating content to save in the file
        content = f"{base_node_name}:{node_type}"
        
        # Checking if the configuration folder exists
        if not os.path.exists(config_path):
            os.makedirs(config_path)

        # Carregando os dados existentes do arquivo JSON
        file_path = config_path + 'NodeMasterToolkit_Favorites.json'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            data = {}  # Inicializa um dicionário vazio se o arquivo não existir

        # Obtendo o contexto atual (Shader Node Editor, Geometry Nodes etc.)
        current_context = context.area.ui_type

        # Criando uma lista vazia se o contexto não existir no arquivo JSON
        if current_context not in data:
            data[current_context] = []

        # Verificando se a informação do nó já está na lista
        if content not in data[current_context]:
            # Adicionando informação do nó à lista
            data[current_context].append(content)

            # Salvando informações no arquivo JSON
            with open(file_path, 'w') as file:
                json.dump(data, file)

            # Atualizando a lista na janela do Blender
            bpy.context.window_manager.node_information = '\n'.join(data[current_context])

            self.report({'INFO'}, "Node information saved successfully!")
        else:
            self.report({'WARNING'}, "Node information is already in the list")

        return {'FINISHED'}

# Operator to create custom operators
class CreateOperatorOperator(bpy.types.Operator):
    bl_idname = "script.create_operator"
    bl_label = "Create Operator"
    bl_description = "Create a new operator based on node information"
    
    
    node_information: bpy.props.StringProperty()

    def execute(self, context):
        # Splitting node information into parts
        info_parts = self.node_information.split(':')
        
        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False
        
        # Checking if there is enough information
        if len(info_parts) >= 2:
            # Here you can use the information to create new operators or perform other desired actions
            node_name = info_parts[0]
            node_type = info_parts[1]
            
            # Example: Adding a node of the same type as the node associated with the operator
            tree = bpy.context.space_data.node_tree
            node = tree.nodes.new(node_type)
            
            # Positioning the new node relative to the mouse cursor
            

            node.location = context.space_data.cursor_location
            
            bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
            
            self.report({'INFO'}, f"Node '{node_name}' added")
        else:
            self.report({'WARNING'}, "Incomplete information to add the node")
        
        return {'FINISHED'}

# Operator to remove the node from the list
class RemoveNodeOperator(bpy.types.Operator):
    bl_idname = "script.remove_node"
    bl_label = "Remove Node"
    bl_description = "Remove node information from the list"
    bl_options = {'REGISTER', 'UNDO'}    
    
    
    node_information: bpy.props.StringProperty()
    force_update: bpy.props.BoolProperty(default=False)  # Property to force panel update

    def execute(self, context):
        # Getting the node list
        information = bpy.context.window_manager.node_information.split('\n')
        
        # Removing the node from the list
        information.remove(self.node_information)
        
        # Saving information to a .json file in the configuration folder
        file_path = config_path + 'NodeMasterToolkit_Favorites.json'
        with open(file_path, 'w') as file:
            json.dump(information, file)
        
        # Updating the list in the Blender window
        bpy.context.window_manager.node_information = '\n'.join(information)
        
        # Forcing panel redraw
        if self.force_update:
            bpy.context.area.tag_redraw()

        self.report({'INFO'}, "Node removed from the list")
        return {'FINISHED'}

class CUSTOMPANEL_PT_Favorites(bpy.types.Panel):
    bl_label = "Favorites"
    bl_idname = "CUSTOMPANEL_PT_Favorites"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'NMT - Extras'
    bl_description = "Custom panel for managing node information"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0

    # Only draw the panel on Shader Node Editor
    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'


    def draw(self, context):
        layout = self.layout

        grid = layout.grid_flow(row_major=True, columns=1, align=True)
        grid.prop(context.scene, "set_fav_display")  # Integer Input
        grid.operator("script.update_list", text="Force Update List")
        grid.operator("script.save_info", text="Add Node to Favorite")

        box = layout.box()
        buttons_grid = box.grid_flow(row_major=True, columns=1, align=True)  # Renomeie esta variável

        displayed_node_count = context.scene.set_fav_display
        information = bpy.context.window_manager.node_information.split('\n')
        information = [info for info in information if info]
        information = information[:displayed_node_count]

        for info in information:
            op_row = buttons_grid.row(align=True)

            op = op_row.operator("script.create_operator", text=info.split(':')[0])
            op.node_information = info

            remover_op = op_row.operator("script.remove_node", text="", icon='X')
            remover_op.node_information = info
            
            remover_op.force_update = True  # Property to force panel update
            
            op_up = op_row.operator("script.move_operator_up", icon='TRIA_UP', text="")
            op_up.node_information = info

            op_down = op_row.operator("script.move_operator_down", icon='TRIA_DOWN', text="")
            op_down.node_information = info

def draw_menu(self, context):
    self.layout.operator("script.save_info", text="Add to Favorite")

# Verifica se o nó ativo é do tipo desejado e adiciona o menu se for o caso
def draw_node_menu(self, context):
    if context.active_node and isinstance(context.active_node, bpy.types.ShaderNodeTexImage):
        self.layout.separator()
        self.layout.append("NODE_PT_my_node_menu", text="Add to Favorites")



######################################################################
#                 Most Used Nodes - ShaderNodeTree                   #
######################################################################


def clean_node_name(node_name):
    if len(node_name) >= 4 and node_name[-4] == "." and node_name[-3:].isdigit():
        return node_name[:-4]
    else:
        return node_name

def find_most_used_nodes():
    nodes_count = {}
    for material in bpy.data.materials:
        if material.use_nodes:
            for node in material.node_tree.nodes:
                node_name = clean_node_name(node.name)
                if node_name in nodes_count:
                    nodes_count[node_name][0] += 1
                else:
                    nodes_count[node_name] = [1, node.name, node.bl_idname]  # Adding the operator name

    most_used_nodes = sorted(nodes_count.items(), key=lambda x: x[1][0], reverse=True)[:20]
    return most_used_nodes

# New operator to add the selected node to favorites
class NODE_OT_AddSelectedNodeToFavorites(bpy.types.Operator):
    bl_idname = "node.add_selected_node_to_favorites"
    bl_label = "Add Selected Node to Favorites"

    def execute(self, context):
        selected_node = context.active_node
        if selected_node:
            toggle_favorite(selected_node.name)  # Add the node name to favorites

        return {'FINISHED'}

def write_nodes_to_file(nodes):
    filepath = bpy.utils.user_resource('CONFIG')
    filepath = os.path.join(filepath, "NMT_ShaderNodeTree_Most_Used_Nodes.txt")
    
    existing_nodes = {}
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                parts = line.split(':')
                if len(parts) == 4:
                    node_type, count, operator_name, operator_id = parts
                    existing_nodes[node_type] = [int(count), operator_name, operator_id]

    with open(filepath, 'w') as file:
        for node_type, data in nodes:
            if node_type in existing_nodes:
                pass
            else:
                existing_nodes[node_type] = data

        for node_type, data in existing_nodes.items():
            file.write(f"{node_type}:{data[0]}:{data[1]}:{data[2]}\n")

    return existing_nodes

def find_four_most_used_nodes(input_int_most_used):
    filepath = bpy.utils.user_resource('CONFIG')
    filepath = os.path.join(filepath, "NMT_ShaderNodeTree_Most_Used_Nodes.txt")

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            nodes_list = file.read().splitlines()

        nodes_dict = {}
        for line in nodes_list:
            node_type, count, operator_name, operator_id = line.split(':')
            nodes_dict[node_type] = [int(count), operator_name, operator_id]

        four_most_used_nodes = sorted(nodes_dict.items(), key=lambda x: x[1][0], reverse=True)[:input_int_most_used]

        return four_most_used_nodes
    else:
        return []

class NODE_OT_CallNodeOperator(bpy.types.Operator):
    bl_idname = "node.call_node"
    bl_label = "Call Node"
    
    node_type: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.node.add_node(type=self.node_type)
        bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        return {'FINISHED'}

def display_nodes_panel(self, context):
    layout = self.layout
    input_int_most_used = context.scene.input_int_most_used
    four_most_used_nodes = find_four_most_used_nodes(input_int_most_used)
    
    grid = layout.grid_flow(row_major=True, columns=1, align=True)
    
    for node_type, data in four_most_used_nodes:
        count, operator_name, operator_id = data
        op = grid.operator(NODE_OT_CallNodeOperator.bl_idname, text=f"{node_type} - {count}x")
        op.node_type = operator_id  # Associating the operator ID
        
    #layout.separator()        
    #layout.operator("node.update_node_list", text="Update Node List")

class NODE_PT_MostUsedNativePanel(bpy.types.Panel):
    bl_label = "Most Used Nodes"
    bl_idname = "NODE_PT_MostUsedNativePanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'NMT - Extras'
    bl_options = {'DEFAULT_CLOSED'}    
    bl_order = 0

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "ShaderNodeTree"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "input_int_most_used")
        layout.operator("node.update_node_list", text="Update List")
        layout.separator()
        display_nodes_panel(self, context)

class NODE_OT_UpdateNodeListOperator(bpy.types.Operator):
    bl_idname = "node.update_node_list"
    bl_label = "Update Node List"
    
    def execute(self, context):
        most_used_nodes = find_most_used_nodes()
        write_nodes_to_file(most_used_nodes)
        return {'FINISHED'}


######################################################################
#                      Current Nodes in Scene                        #
######################################################################


class NODE_OT_AddSelectedNode(bpy.types.Operator):
    bl_idname = "node.add_selected_node"
    bl_label = "Add Selected Node"
    bl_description = "Add the selected node to the node tree"
    
    node_type: bpy.props.StringProperty(description="Node type to be added")  # Property to store the node type

    def execute(self, context):
        # Add the selected node to the node tree
        node_tree = bpy.context.space_data.node_tree

        # Deselect all nodes in the tree
        for node in node_tree.nodes:
            node.select = False
            
        node_group = context.space_data.node_tree
        selected_node = node_group.nodes.new(self.node_type)
        selected_node.location = context.space_data.cursor_location  # Set the node location
        bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        return {'FINISHED'}

# Define the panel in the Node Editor UI
class NODE_PT_EditorNodesList(bpy.types.Panel):
    bl_label = "Nodes in Scene"
    bl_idname = "NODE_PT_custom_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'NMT - Extras'
    bl_order = 0
    bl_description = "Add nodes dynamically to the node tree"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        layout = self.layout
        
        grid = layout.grid_flow(row_major=True, columns=1, align=True)
        
        grid.label(text="Available Nodes in current shader:")
        
        nodes = context.space_data.node_tree.nodes if context.space_data.node_tree else None
        added_nodes = set()  # Set to store already added nodes

        # List all available nodes to add
        if nodes:
            for node_type in nodes:
                if node_type.bl_idname not in added_nodes:
                    
                    grid.operator("node.add_selected_node", text=node_type.bl_label).node_type = node_type.bl_idname
                    added_nodes.add(node_type.bl_idname)  # Add the node to the set of added nodes


######################################################################
#                      Pie Menu for Favorites                        #
######################################################################


class NodeEditorPieMenu(Menu):
    bl_idname = "NODE_MT_pie_node_editor"
    bl_label = "Node Editor Pie Menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Carregar os dados do arquivo JSON
        config_path = bpy.utils.resource_path('USER') + '/config/'
        json_file_path = config_path + 'NodeMasterToolkit_Favorites.json'

        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as file:
                favorites_data = json.load(file)
        else:
            favorites_data = {}

        current_context = context.area.ui_type
        if current_context in favorites_data:
            nodes = favorites_data[current_context]
        else:
            nodes = []

        displayed_node_count = context.scene.set_fav_display
        nodes = nodes[:displayed_node_count]

        # Dividir os itens em submenus de, por exemplo, 4 itens cada
        for i in range(0, len(nodes), 4):
            submenu = pie.column()
            for node_info in nodes[i:i+4]:
                node_name, operator_name = node_info.split(':')
                submenu.operator("node.add_dynamic_node", text=node_name).node_operator = operator_name

        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as file:
                favorites_data = json.load(file)
                print("Favorites Data:", favorites_data)
        else:
            favorites_data = {}
            print("File not found:", json_file_path)

class NodeAddDynamicOperator(bpy.types.Operator):
    bl_idname = "node.add_dynamic_node"
    bl_label = "Add Node"
    
    node_operator: bpy.props.StringProperty()
    

    def execute(self, context):
                # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False
        
        # Adicionar o nó ao editor de nós
        try:
            node_tree = context.space_data.node_tree
            node = node_tree.nodes.new(type=self.node_operator)
            node.location = context.space_data.cursor_location
            bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

        except Exception as e:
            self.report({'ERROR'}, f"Failed to add node: {e}")
            return {'CANCELLED'}
        return {'FINISHED'}



######################################################################
#                      Frame All Node Editor                         #
######################################################################


class FrameAll_OT(bpy.types.Operator):
    bl_idname = "nodes.frame_all"
    bl_label = "Frame entire node tree"
    
    def execute(self, context):
        bpy.ops.node.view_all()
        return {"FINISHED"}
        
        
class NODE_PT_FrameAllPanel(bpy.types.Panel):
    bl_label = "Utilities"
    bl_idname = "NODE_PT_FrameAllPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'NMT - Extras'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}    

    def draw(self, context):
        layout = self.layout
        layout.operator("nodes.frame_all", text="Frame All", icon="MESH_PLANE") 


classes_Utilities_PT_OP =[
    # Frame All Node Editor
    NODE_PT_FrameAllPanel,
    FrameAll_OT,
    # Favorites
    CUSTOMPANEL_PT_Favorites,
    SaveInfoOperator,
    MoveOperatorUpOperator,
    MoveOperatorDownOperator,
    CreateOperatorOperator,
    RemoveNodeOperator,
    UpdateListOperator,
    # Most Used Nodes
    NODE_OT_CallNodeOperator,
    NODE_PT_MostUsedNativePanel,
    NODE_OT_UpdateNodeListOperator,
    # Current Nodes in Scene
    NODE_OT_AddSelectedNode,
    NODE_PT_EditorNodesList,
    # Pie Menu For Favorites
    NodeEditorPieMenu,
    NodeAddDynamicOperator
]
