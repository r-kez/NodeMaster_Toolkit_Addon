import bpy
import os
import urllib.parse



# Add Boolean Group
class OPERATOR_ImportBooleanNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_bool_group"
    bl_label = "Import Node Group"
    bl_description = "Import a Boolean Node Group"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='Boolean')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    # Verifica se o Node Group já existe na cena
                    existing_group = bpy.data.node_groups.get(ng.name)
                    if existing_group:
                        # Cria um novo nó dentro do Node Group atual
                        new_node = node_tree.nodes.new('ShaderNodeGroup')
                        new_node.node_tree = existing_group

                        # Posiciona o novo nó na localização do cursor, dentro do Node Group ativo
                        new_node.parent = context.active_node  # Define o novo nó como filho do nó ativo
                        new_node.location = context.space_data.cursor_location  # Posiciona com base na localização do cursor

                        bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
                    else:
                        self.report({'ERROR'}, f"Node Group '{ng.name}' não encontrado no arquivo.")

        return {'FINISHED'}

# Add Interger Group
class OPERATOR_ImportIntergerNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_integer_group"
    bl_label = "Import Node Group"
    bl_description = "Import a Integer Node Group"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='Integer')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    bpy.data.node_groups.new(ng.name, 'ShaderNodeTree')
                    new_node = context.space_data.node_tree.nodes.new('ShaderNodeGroup')
                    new_node.node_tree = ng

                    # Posiciona o novo nó na localização do cursor
                    new_node.location = context.space_data.cursor_location
                    bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        else:
            print(f"O arquivo '{file_path}' não foi encontrado.")

        return {'FINISHED'}

# Add Color Mixer 5 Group
class OPERATOR_ImportColorMixFiveNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_color_mix_five_group"
    bl_label = "Import Node Group"
    bl_description = "Color Mixer wwith 5 Slots"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='ColorMixer5')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    bpy.data.node_groups.new(ng.name, 'ShaderNodeTree')
                    new_node = context.space_data.node_tree.nodes.new('ShaderNodeGroup')
                    new_node.node_tree = ng

                    # Posiciona o novo nó na localização do cursor
                    new_node.location = context.space_data.cursor_location
                    bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        else:
            print(f"O arquivo '{file_path}' não foi encontrado.")

        return {'FINISHED'}

# Add Color Mixer 10 Group
class OPERATOR_ImportColorMixTenNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_color_mix_ten_group"
    bl_label = "Import Node Group"
    bl_description = "Color Mixer wwith 5 Slots"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='ColorMixer10')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    bpy.data.node_groups.new(ng.name, 'ShaderNodeTree')
                    new_node = context.space_data.node_tree.nodes.new('ShaderNodeGroup')
                    new_node.node_tree = ng

                    # Posiciona o novo nó na localização do cursor
                    new_node.location = context.space_data.cursor_location
                    bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        else:
            print(f"O arquivo '{file_path}' não foi encontrado.")

        return {'FINISHED'}

# Add Shader Mixer 5 Group
class OPERATOR_ImportShaderMixFiveNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_shader_mix_five_group"
    bl_label = "Import Node Group"
    bl_description = "Color Mixer wwith 5 Slots"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='ShaderMixer5')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    bpy.data.node_groups.new(ng.name, 'ShaderNodeTree')
                    new_node = context.space_data.node_tree.nodes.new('ShaderNodeGroup')
                    new_node.node_tree = ng

                    # Posiciona o novo nó na localização do cursor
                    new_node.location = context.space_data.cursor_location
                    bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        else:
            print(f"O arquivo '{file_path}' não foi encontrado.")

        return {'FINISHED'}

# Add Shader Mixer 5 Group
class OPERATOR_ImportShaderMixTenNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_shader_mix_ten_group"
    bl_label = "Import Node Group"
    bl_description = "Color Mixer wwith 5 Slots"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='ShaderMixer10')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    bpy.data.node_groups.new(ng.name, 'ShaderNodeTree')
                    new_node = context.space_data.node_tree.nodes.new('ShaderNodeGroup')
                    new_node.node_tree = ng

                    # Posiciona o novo nó na localização do cursor
                    new_node.location = context.space_data.cursor_location
                    bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        else:
            print(f"O arquivo '{file_path}' não foi encontrado.")

        return {'FINISHED'}

# Add Blur Group
class OPERATOR_ImportBlurNodeGroup(bpy.types.Operator):
    bl_idname = "import.node_extra_nodes_blur_group"
    bl_label = "Import Node Group"
    bl_description = "Color Mixer wwith 5 Slots"

    file_path: bpy.props.StringProperty(
        default='NMT_Extra_Nodes.blend'
    )  # Caminho relativo ao arquivo .blend que contém o Node Group
    node_group_name: bpy.props.StringProperty(default='Blur')  # Nome do Node Group a ser importado

    def execute(self, context):
        # Diretório do arquivo do addon
        addon_dir = os.path.dirname(os.path.realpath(__file__))

        # Caminho completo para o arquivo .blend
        file_path = os.path.join(addon_dir, self.file_path)

        # Obtém a árvore de nodos ativa
        node_tree = bpy.context.space_data.node_tree

        # Percorre todos os nodos na árvore e deseleciona-os
        for node in node_tree.nodes:
            node.select = False

        # Verifica se o arquivo .blend existe no caminho especificado
        if os.path.exists(file_path):
            print("Arquivo encontrado!")

            # Verifica se estamos em um contexto de shader
            if context.space_data is None or context.space_data.tree_type != 'ShaderNodeTree':
                self.report({'ERROR'}, "This operation is only available in Shader Node Editor.")
                return {'CANCELLED'}

            # Carrega o arquivo .blend
            with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
                data_to.node_groups = [self.node_group_name]
        
            # Adiciona o Node Group carregado à coleção de Node Groups da cena atual
            for ng in data_to.node_groups:
                if ng is not None:
                    bpy.data.node_groups.new(ng.name, 'ShaderNodeTree')
                    new_node = context.space_data.node_tree.nodes.new('ShaderNodeGroup')
                    new_node.node_tree = ng

                    # Posiciona o novo nó na localização do cursor
                    new_node.location = context.space_data.cursor_location
                    bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')


        else:
            print(f"O arquivo '{file_path}' não foi encontrado.")

        return {'FINISHED'}


classes_ExtraNodes_OT = [
    OPERATOR_ImportBooleanNodeGroup,
    OPERATOR_ImportIntergerNodeGroup,
    OPERATOR_ImportColorMixFiveNodeGroup,
    OPERATOR_ImportColorMixTenNodeGroup,
    OPERATOR_ImportShaderMixFiveNodeGroup,
    OPERATOR_ImportShaderMixTenNodeGroup,
    OPERATOR_ImportBlurNodeGroup,
]
