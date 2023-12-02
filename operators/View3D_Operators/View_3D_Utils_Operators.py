import bpy
import os







# Filter Image Property Gropup
filter_image_type = bpy.props.BoolProperty(name="Filter Image Type", description="Enable image filtering by type", default=False)

####### FLIP RESOLUTION START

class RENDER_OT_Res_Flip(bpy.types.Operator):
    bl_idname = "render.res_flip"
    bl_label = "Flip render resolution"
    bl_options = {'UNDO'}
    bl_description = "Flip Current Resolution"

    def execute(self, context):

        res_x = context.scene.render.resolution_x 
        res_y = context.scene.render.resolution_y    

        context.scene.render.resolution_x = res_y
        context.scene.render.resolution_y = res_x

        return ({'FINISHED'})

class RENDER_OT_Percentage(bpy.types.Operator):
    bl_idname = "render.percentage_operator"
    bl_label = "Display Render Final Resolution"
    
    def execute(self, context):

        res_percentage = context.scene.render.resolution_percentage
        res_x = context.scene.render.resolution_x
        res_y = context.scene.render.resolution_y



####### Image List OPERATOR START

if not hasattr(bpy.types.Scene, "filter_image_type"):
    bpy.types.Scene.filter_image_type = bpy.props.BoolProperty(
        name="Filter Image Type",
        description="Enable image filtering by type",
        default=False
    )

class OpenImageFileBrowserOperator(bpy.types.Operator):
    bl_idname = "object.open_image_file_browser"
    bl_label = "Open Image File Browser"
    bl_options = {'UNDO'}
    bl_description = "Open File Browser"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        # Carrega a imagem selecionada no Blender
        bpy.ops.image.open(filepath=self.filepath, relative_path=True, filter_image=True)
        return {'FINISHED'}

    def invoke(self, context, event):
        # Configurações para filtrar apenas arquivos de imagem
        context.window_manager.fileselect_add(self)

        return {'RUNNING_MODAL'}

class UpdateImageListOperator(bpy.types.Operator):
    bl_idname = "object.update_image_list"
    bl_label = "Update Image List"
    bl_options = {'UNDO'}
    bl_description = "Update Image List"
    
    def execute(self, context):
        # Atualiza a lista de imagens na cena
        scene = context.scene
        scene.image_list.clear()
        for image in bpy.data.images:
            item = scene.image_list.add()
            item.name = image.name
            item.width = image.size[0]
            item.height = image.size[1]
        return {'FINISHED'}

class IMAGE_OT_LinkToWorld(bpy.types.Operator):
    bl_idname = "object.link_to_environment"
    bl_label = "Link Selected Image to Environment Node"
    bl_options = {'UNDO'}
    bl_description = "Link selected image to World Node"


    def find_node_by_name_in_group(self, node_group, node_name):
        for node in node_group.nodes:
            if node.name == node_name:
                return node
        return None

    def execute(self, context):
        selected_image = context.scene.image_list[context.scene.image_list_index]

        # Obtém o nome do nó a partir da variável da cena
        node_name = context.scene.world_hdri_texture_node

        # Percorre todos os grupos no Shader Editor
        for node_group in bpy.data.node_groups:
            hdri_texture_node = self.find_node_by_name_in_group(node_group, node_name)
            if hdri_texture_node:
                # Tenta encontrar a imagem pelo nome
                image = bpy.data.images.get(selected_image.name)

                # Conecta a imagem ao nó especificado pelo nome
                if image:
                    hdri_texture_node.image = image
                    self.report({'INFO'}, f"Imagem '{selected_image.name}' vinculada ao nó '{node_name}' no grupo '{node_group.name}'.")
                    return {'FINISHED'}
                else:
                    self.report({'ERROR'}, f"Imagem '{selected_image.name}' não encontrada.")
                    return {'CANCELLED'}

        self.report({'ERROR'}, f"Nenhum nó com o nome '{node_name}' encontrado em nenhum grupo.")
        return {'CANCELLED'}


class FindNodeByNameInGroupOperator(bpy.types.Operator):
    bl_idname = "object.find_node_by_name_in_group"
    bl_label = "Find Node by Name in Group"

    def find_node_by_name_in_group(self, node_group, node_name):
        for node in node_group.nodes:
            if node.name == node_name:
                return node
        return None

    def execute(self, context):
        wm = context.window_manager

        # Obtendo o caminho completo da imagem selecionada
        selected_image_name = wm.my_previews
        directory_path = wm.my_previews_dir
        selected_image_path = os.path.join(directory_path, selected_image_name)

        node_name = context.scene.world_hdri_texture_node

        # Lógica para encontrar o nó pelo nome no grupo
        for node_group in bpy.data.node_groups:
            hdri_texture_node = self.find_node_by_name_in_group(node_group, node_name)
            if hdri_texture_node:
                # Conectar a imagem ao nó encontrado
                image = bpy.data.images.load(selected_image_path)
                if image:
                    hdri_texture_node.image = image
                    self.report({'INFO'}, f"Imagem '{selected_image_name}' vinculada ao nó '{node_name}' no grupo '{node_group.name}'.")
                    return {'FINISHED'}
                else:
                    self.report({'ERROR'}, f"Erro ao carregar a imagem '{selected_image_name}'.")
                    return {'CANCELLED'}
        
        self.report({'ERROR'}, f"Nenhum nó com o nome '{node_name}' encontrado em nenhum grupo.")
        return {'CANCELLED'}

####### Image List OPERATOR START

class IMAGE_OT_SelectFromList(bpy.types.Operator):
    bl_idname = "object.select_image_from_list"
    bl_label = "Select Image"
    bl_description = "Select image to be added to World Node"
    
    
    index: bpy.props.IntProperty()  # Defina o atributo como uma anotação de tipo
    
    def execute(self, context):
        context.scene.image_list_index = self.index
        return {"FINISHED"}


"""-------------------------------------------------------------------------------------"""

####### Define Selected OPERATOR START CHAT GPT    

class selectedButton(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    selected = bpy.props.BoolProperty(default=False)

"""-------------------------------------------------------------------------------------"""    


class IMAGE_PT_ImageInfo(bpy.types.PropertyGroup):

    name = bpy.props.StringProperty()   #Store Image Name
    width = bpy.props.IntProperty()     #Store Image width 
    height = bpy.props.IntProperty()    #Store Image height


"""-------------------------------------------------------------------------------------"""    

####### Filter OPERATOR START CHAT GPT      

class IMAGE_OT_FilterImageButton(bpy.types.Operator):
    bl_idname = "object.filter_image_button"
    bl_label = "Simple Operator"

    filter_image_button: bpy.props.BoolProperty()

    def execute(self, context):
        if self.filter_image_button:
            self.report({'INFO'}, 'Boolean ativado!')
        else:
            self.report({'INFO'}, 'Boolean desativado!')
        return {'FINISHED'}


def move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names):
    # Verifica se a coleção alvo existe, se não, cria
    if target_collection_name not in bpy.data.collections:
        target_collection = bpy.data.collections.new(target_collection_name)
        bpy.context.scene.collection.children.link(target_collection)
    else:
        target_collection = bpy.data.collections[target_collection_name]

    # Limpa a seleção atual
    bpy.ops.object.select_all(action='DESELECT')

    # Lista para armazenar os objetos organizados
    organized_objects = []

    # Lista todos os objetos do tipo específico na cena
    for obj in bpy.context.scene.objects:
        if obj.type == obj_type:
            # Verifica se o objeto está em alguma coleção excluída
            in_excluded_collection = False
            for col in obj.users_collection:
                if col.name in excluded_collection_names:
                    in_excluded_collection = True
                    break
            
            if in_excluded_collection:
                organized_objects.append(obj)
            else:
                # Desvincula o objeto de suas coleções atuais
                for other_col in obj.users_collection:
                    other_col.objects.unlink(obj)

                # Move o objeto para a coleção alvo
                if obj.name not in target_collection.objects:
                    target_collection.objects.link(obj)
                # Seleciona o objeto
                obj.select_set(True)

    # Retorna a lista de objetos organizados
    return organized_objects

# Object Collection Panel Operator
class MOVE_OT_Mesh(bpy.types.Operator):
    bl_idname = "object.move_and_select_unorganized_mesh"
    bl_label = "Move and Select Unorganized Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Nome da coleção para onde os objetos devem ser movidos
        target_collection_name = "Mesh"
        obj_type = 'MESH'

        # Nomes das coleções que serão excluídas da seleção e movimento
        excluded_collection_names = ["_LCA", "_Trash", "_ShaderBalls", "_Backdrop", "_Lights", "_3_point_light_grp", "_ring_light_grp", 
        "_projector_light_grp", "_single_light_grp", "_WorldOrigin", "_Camera", "_SizeRef", "_ExcludeThisCollection"]

        # Chama a função para mover objetos para a coleção e selecionar os não organizados
        move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names)
        return {'FINISHED'}

# Object Collection Panel Operator
class MOVE_OT_Lights(bpy.types.Operator):
    bl_idname = "object.move_and_select_unorganized_lights"
    bl_label = "Move and Select Unorganized Lights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Nome da coleção para onde os objetos devem ser movidos
        target_collection_name = "Lights"
        obj_type = 'LIGHT'

        # Nomes das coleções que serão excluídas da seleção e movimento
        excluded_collection_names = ["_LCA", "_Trash", "_ShaderBalls", "_Backdrop", "_Lights", "_3_point_light_grp", "_ring_light_grp", 
        "_projector_light_grp", "_single_light_grp", "_WorldOrigin", "_Camera", "_SizeRef", "_ExcludeThisCollection"]

        # Chama a função para mover objetos para a coleção e selecionar os não organizados
        move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names)
        return {'FINISHED'}

# Object Collection Panel Operator
class MOVE_OT_Empty(bpy.types.Operator):
    bl_idname = "object.move_empty"
    bl_label = "Move and Select Unorganized Lights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Nome da coleção para onde os objetos devem ser movidos
        target_collection_name = "Empty"
        obj_type = 'EMPTY'

        # Nomes das coleções que serão excluídas da seleção e movimento
        excluded_collection_names = ["_LCA", "_Trash", "_ShaderBalls", "_Backdrop", "_Lights", "_3_point_light_grp", "_ring_light_grp", 
        "_projector_light_grp", "_single_light_grp", "_WorldOrigin", "_Camera", "_SizeRef", "_ExcludeThisCollection"]

        # Chama a função para mover objetos para a coleção e selecionar os não organizados
        move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names)
        return {'FINISHED'}

# Object Collection Panel Operator
class MOVE_OT_Camera(bpy.types.Operator):
    bl_idname = "object.move_camera"
    bl_label = "Move and Select Unorganized Lights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Nome da coleção para onde os objetos devem ser movidos
        target_collection_name = "Camera"
        obj_type = 'CAMERA'

        # Nomes das coleções que serão excluídas da seleção e movimento
        excluded_collection_names = ["_LCA", "_Trash", "_ShaderBalls", "_Backdrop", "_Lights", "_3_point_light_grp", "_ring_light_grp", 
        "_projector_light_grp", "_single_light_grp", "_WorldOrigin", "_Camera", "_SizeRef", "_ExcludeThisCollection"]

        # Chama a função para mover objetos para a coleção e selecionar os não organizados
        move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names)
        return {'FINISHED'}

# Object Collection Panel Operator
class MOVE_OT_Text(bpy.types.Operator):
    bl_idname = "object.move_text"
    bl_label = "Move and Select Unorganized Lights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Nome da coleção para onde os objetos devem ser movidos
        target_collection_name = "Text"
        obj_type = 'FONT'

        # Nomes das coleções que serão excluídas da seleção e movimento
        excluded_collection_names = ["_LCA", "_Trash", "_ShaderBalls", "_Backdrop", "_Lights", "_3_point_light_grp", "_ring_light_grp", 
        "_projector_light_grp", "_single_light_grp", "_WorldOrigin", "_Camera", "_SizeRef", "_ExcludeThisCollection"]

        # Chama a função para mover objetos para a coleção e selecionar os não organizados
        move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names)
        return {'FINISHED'}

# Object Collection Panel Operator
class MOVE_OT_Curve(bpy.types.Operator):
    bl_idname = "object.move_curve"
    bl_label = "Move and Select Unorganized Lights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Nome da coleção para onde os objetos devem ser movidos
        target_collection_name = "Curve"
        obj_type = 'CURVE'

        # Nomes das coleções que serão excluídas da seleção e movimento
        excluded_collection_names = ["_LCA", "_Trash", "_ShaderBalls", "_Backdrop", "_Lights", "_3_point_light_grp", "_ring_light_grp", 
        "_projector_light_grp", "_single_light_grp", "_WorldOrigin", "_Camera", "_SizeRef", "_ExcludeThisCollection"]

        # Chama a função para mover objetos para a coleção e selecionar os não organizados
        move_and_select_unorganized_objects(target_collection_name, obj_type, excluded_collection_names)
        return {'FINISHED'}




classes_view_3d_OT = [
FindNodeByNameInGroupOperator,
RENDER_OT_Res_Flip,   
RENDER_OT_Percentage,
OpenImageFileBrowserOperator,
UpdateImageListOperator,
IMAGE_OT_LinkToWorld,
IMAGE_OT_SelectFromList,
selectedButton,
IMAGE_OT_FilterImageButton,
MOVE_OT_Mesh,
MOVE_OT_Lights,
MOVE_OT_Empty,
MOVE_OT_Camera,
MOVE_OT_Text,
MOVE_OT_Curve
]

