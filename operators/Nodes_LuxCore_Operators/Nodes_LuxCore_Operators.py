import bpy
from ..Master_op.master_op import MASTER_OT_Transform



############################################################### -- Materials -- 16 Itens

# LC MAterial Disney
class LUXCORE_OT_MaterialDisney_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_disney_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatDisney")
        return {"FINISHED"}

# LC MAterial Mix
class LUXCORE_OT_MaterialMix_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_mix_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatMix")
        return {"FINISHED"}

# LC MAterial Matte
class LUXCORE_OT_MaterialMatte_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_matte_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatMatte")
        return {"FINISHED"}

# LC MAterial Matte Translucent
class LUXCORE_OT_MaterialMatteTranslucent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_matte_translucent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatMatteTranslucent")
        return {"FINISHED"}

# LC MAterial Metal
class LUXCORE_OT_MaterialMetal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_metal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatMetal")
        return {"FINISHED"}

# LC MAterial Mirror
class LUXCORE_OT_MaterialMirror_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_mirror_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatMirror")
        return {"FINISHED"}

# LC MAterial Glossy
class LUXCORE_OT_MaterialGlossy_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_glossy_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatGlossy2")
        return {"FINISHED"}

# LC MAterial Glossy Translucent
class LUXCORE_OT_MaterialGlossyTranslucent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_glossy_translucent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatGlossyTranslucent")
        return {"FINISHED"}

# LC MAterial Glossy Coating
class LUXCORE_OT_MaterialGlossyCoating_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_glossy_coating_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatGlossyCoating")
        return {"FINISHED"}

# LC MAterial Glass
class LUXCORE_OT_MaterialGlass_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_glass_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatGlass")
        return {"FINISHED"}

# LC MAterial Null (Transparent)
class LUXCORE_OT_MaterialNull_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_null_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatNull")
        return {"FINISHED"}

# LC MAterial Carpaint
class LUXCORE_OT_MaterialCarpaint_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_carpaint_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatCarpaint")
        return {"FINISHED"}

# LC MAterial Cloth
class LUXCORE_OT_MaterialCloth_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_cloth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatCloth")
        return {"FINISHED"}

# LC MAterial Velvet
class LUXCORE_OT_MaterialVelvet_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_velvet_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatVelvet")
        return {"FINISHED"}

# LC MAterial Two Sided
class LUXCORE_OT_MaterialTwoSided_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_two_sided_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatTwoSided")
        return {"FINISHED"}

# LC MAterial Front/Back Opacity
class LUXCORE_OT_MaterialFrontBackOpacity_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_material_front_back_op_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatFrontBackOpacity")
        return {"FINISHED"}


############################################################### -- Volume -- 3 Itens


# LC Volume Volume Clear
class LUXCORE_OT_VolumeClear_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_volume_clear_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeVolClear")
        return {"FINISHED"}

# LC Volume Volume Homogeneous
class LUXCORE_OT_VolumeHomogeneous_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_volume_homogeneous_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeVolHomogeneous")
        return {"FINISHED"}

# LC Volume Heterogeneous
class LUXCORE_OT_VolumeHeterogeneous_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_volume_heterogeneous_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeVolHeterogeneous")
        return {"FINISHED"}


############################################################### -- Texture -- 14 Itens

'''# LC Texture Multiple Images
class LUXCORE_OT_TextureMultipleImages_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_multiple_images_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.luxcore.import_multiple_images()
        return {"FINISHED"}
'''

# LC Texture Image Map
class LUXCORE_OT_TextureImageMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_image_map_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexImagemap")
        return {"FINISHED"}

# LC Texture Brick
class LUXCORE_OT_TextureBrick_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_brick_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBrick")
        return {"FINISHED"}

# LC Texture Wireframe
class LUXCORE_OT_TextureWireframe_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_wireframe_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexWireframe")
        return {"FINISHED"}

# LC Texture Dots
class LUXCORE_OT_TextureDots_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_dots_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexDots")
        return {"FINISHED"}

# LC Texture fBM
class LUXCORE_OT_TexturefBM_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_fbm_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexfBM")
        return {"FINISHED"}

# LC Texture Checkerboard2D
class LUXCORE_OT_TextureCheckerboard2D_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_checkerboard2d_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexCheckerboard2D")
        return {"FINISHED"}

# LC Texture Checkerboard3D
class LUXCORE_OT_TextureCheckerboard3D_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_checkerboard3d_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexCheckerboard3D")
        return {"FINISHED"}

# LC Texture Marble
class LUXCORE_OT_TextureMarble_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_marble_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexMarble")
        return {"FINISHED"}

# LC Texture Wrinkled
class LUXCORE_OT_TextureWrinkled_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_wrinkled_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexWrinkled")
        return {"FINISHED"}

# LC Texture Hitpoint
class LUXCORE_OT_TextureHitpoint_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_hitpoint_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexHitpoint")
        return {"FINISHED"}

# LC Texture Smoke
class LUXCORE_OT_TextureSmoke_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_smoke_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexSmoke")
        return {"FINISHED"}

# LC Texture OpenVDB
class LUXCORE_OT_TextureOpenVDB_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_open_vdb_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexOpenVDB")
        return {"FINISHED"}

# LC Texture Fresnel
class LUXCORE_OT_TextureFresnel_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_texture_fresnel_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexFresnel")
        return {"FINISHED"}



############################################################### -- Texure Blender -- 10 Itens

# LC Blender Texture Blend
class LUXCORE_OT_BTextureBlend_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_blend_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderBlend")
        return {"FINISHED"}

# LC Blender Texture Clouds
class LUXCORE_OT_BTextureClouds_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_clouds_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderClouds")
        return {"FINISHED"}

# LC Blender Texture DistortedNoise
class LUXCORE_OT_BTextureDistortedNoise_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_distorted_noise_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderDistortedNoise")
        return {"FINISHED"}

# LC Blender Texture Magic
class LUXCORE_OT_BTextureMagic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_magic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderMagic")
        return {"FINISHED"}

# LC Blender Texture Marble
class LUXCORE_OT_BTextureMarble_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_marble_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderMarble")
        return {"FINISHED"}

# LC Blender Texture Musgrave
class LUXCORE_OT_BTextureMusgrave_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_musgrave_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderMusgrave")
        return {"FINISHED"}

# LC Blender Texture Noise
class LUXCORE_OT_BTextureNoise_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_noise_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderNoise")
        return {"FINISHED"}

# LC Blender Texture Stucci
class LUXCORE_OT_BTextureStucci_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_stucci_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderStucci")
        return {"FINISHED"}

# LC Blender Texture Wood
class LUXCORE_OT_BTextureWood_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_wood_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderWood")
        return {"FINISHED"}

# LC Blender Texture Voronoi
class LUXCORE_OT_BTextureVoronoi_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_btexture_voronoi_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlenderVoronoi")
        return {"FINISHED"}

############################################################### -- Math -- 7 Itens

# LC  Math Math 
class LUXCORE_OT_MathMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_math_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexMath")
        return {"FINISHED"}

# LC  Math Mix Color 
class LUXCORE_OT_MathMixColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_mix_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexColorMix")
        return {"FINISHED"}

# LC  Math Vector Math 
class LUXCORE_OT_MathVectorMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_vector_math_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexVectorMath")
        return {"FINISHED"}

# LC  Math Dot Product 
class LUXCORE_OT_MathDotProduct_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_dot_product_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexDotProduct")
        return {"FINISHED"}

# LC  Math Split Float 
class LUXCORE_OT_MathSplitFloat_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_split_float_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexSplitFloat3")
        return {"FINISHED"}

# LC  Math Make Float 
class LUXCORE_OT_MathMakeFloat_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_make_float_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexMakeFloat3")
        return {"FINISHED"}

# LC  Math Texture Remap 
class LUXCORE_OT_MathTextureRemap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_math_texture_remap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexRemap")
        return {"FINISHED"}

############################################################### -- Utils -- 17 Itens

# LC  Math Texture Bump 
class LUXCORE_OT_UtilsTextureBump_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_bump_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBump")
        return {"FINISHED"}

# LC  Math Texture Band 
class LUXCORE_OT_UtilsTextureBand_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_band_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBand")
        return {"FINISHED"}

# LC  Math Texture Distort 
class LUXCORE_OT_UtilsTextureDistort_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_distort_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexDistort")
        return {"FINISHED"}

# LC  Math Texture HSV 
class LUXCORE_OT_UtilsTextureHSV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_hsv_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexHSV")
        return {"FINISHED"}

# LC  Math Texture BrightContrast 
class LUXCORE_OT_UtilsTextureBrightContrast_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_bright_contrast_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBrightContrast")
        return {"FINISHED"}

# LC  Math Texture Invert 
class LUXCORE_OT_UtilsTextureInvert_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_invert_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexInvert")
        return {"FINISHED"}

# LC  Math Texture Constfloat1 
class LUXCORE_OT_UtilsTexturConstfloat1_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_contant_value_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexConstfloat1")
        return {"FINISHED"}

# LC  Math Texture Constfloat3 
class LUXCORE_OT_UtilsTextureConstfloat3_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_contant_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexConstfloat3")
        return {"FINISHED"}

# LC  Math Texture IORPreset 
class LUXCORE_OT_UtilsTextureIORPreset_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_ior_preset_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexIORPreset")
        return {"FINISHED"}

# LC  Math Texture HitpointInfo 
class LUXCORE_OT_UtilsTextureHitpointInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_hitpoint_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexHitpointInfo")
        return {"FINISHED"}

# LC  Math Texture Pointiness 
class LUXCORE_OT_UtilsTexturePointiness_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_pointness_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexPointiness")
        return {"FINISHED"}

# LC  Math Texture ObjectID 
class LUXCORE_OT_UtilsTextureObjectID_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_object_id_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexObjectID")
        return {"FINISHED"}

# LC  Math Texture RandomPerIsland 
class LUXCORE_OT_UtilsTextureRandomPerIsland_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_random_per_island_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexRandomPerIsland")
        return {"FINISHED"}

# LC  Math Texture TimeInfo 
class LUXCORE_OT_UtilsTextureTimeInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_time_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexTimeInfo")
        return {"FINISHED"}

# LC  Math Texture UV 
class LUXCORE_OT_UtilsTextureUV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_uv_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexUV")
        return {"FINISHED"}

# LC  Math Texture Random 
class LUXCORE_OT_UtilsTextureRandom_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_random_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexRandom")
        return {"FINISHED"}

# LC  Math Texture Bombing 
class LUXCORE_OT_UtilsTextureBombing_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_utils_texture_bombing_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBombing")
        return {"FINISHED"}


############################################################### -- Mapping -- 5 Itens

# LC  Mapping Mapping2D 
class LUXCORE_OT_MappingMapping2D_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_mapping_2d_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexMapping2D")
        return {"FINISHED"}

# LC  Mapping Mapping3D 
class LUXCORE_OT_MappingMapping3D_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_mapping_3d_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexMapping3D")
        return {"FINISHED"}

# LC  Mapping Triplanar 
class LUXCORE_OT_MappingTriplanar_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_mapping_triplanar_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexTriplanar")
        return {"FINISHED"}

# LC  Mapping Triplanar Bump 
class LUXCORE_OT_MappingTriplanarBump_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_mapping_triplanar_bump_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexTriplanarBump")
        return {"FINISHED"}

# LC  Mapping Triplanar Normalmap 
class LUXCORE_OT_MappingTriplanarNormalmap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_mapping_triplanar_normalmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexTriplanarNormalmap")
        return {"FINISHED"}

############################################################### -- Light -- 4 Itens

# LC  Light Emission 
class LUXCORE_OT_LightEmission_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_light_emission_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatEmission")
        return {"FINISHED"}

# LC  Light LampSpectrum 
class LUXCORE_OT_LightLampSpectrum_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_light_lamp_spectrum_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexLampSpectrum")
        return {"FINISHED"}

# LC  Light Blackbody 
class LUXCORE_OT_LightBlackbody_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_light_blackbody_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexBlackbody")
        return {"FINISHED"}

# LC  Light IrregularData
class LUXCORE_OT_LightIrregularDat_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_light_irregular_data_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTexIrregularData")
        return {"FINISHED"}

############################################################### -- Modifiers -- 5 Itens

# LC  Modifiers ShapeSubdiv
class LUXCORE_OT_ModifiersShapeSubdiv_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_modifier_shapesubdiv_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeShapeSubdiv")
        return {"FINISHED"}

# LC  Modifiers HeightDisplacement
class LUXCORE_OT_ModifiersHeightDisplacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_modifier_height_displacement_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeShapeHeightDisplacement")
        return {"FINISHED"}

# LC  Modifiers VectorDisplacement
class LUXCORE_OT_ModifiersVectorDisplacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_modifier_vector_displacement_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeShapeVectorDisplacement")
        return {"FINISHED"}

# LC  Modifiers Simplify
class LUXCORE_OT_ModifiersSimplify_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_modifier_simplify_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeShapeSimplify")
        return {"FINISHED"}

# LC  Modifiers Harlequin
class LUXCORE_OT_ModifiersHarlequin_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_modifier_harlequin_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeShapeHarlequin")
        return {"FINISHED"}

############################################################### -- Pointer -- 1 Item

# LC  Tree Pointer
class LUXCORE_OT_PointerTree_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_pointer_tree_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeTreePointer")
        return {"FINISHED"}

############################################################### -- Pointer -- 1 Item

# LC  Output
class LUXCORE_OT_Output_Add(MASTER_OT_Transform):
    bl_idname = "nodes.lc_output_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="LuxCoreNodeMatOutput")
        return {"FINISHED"}




classes_LC_OT = [
# Materials
LUXCORE_OT_MaterialDisney_Add,
LUXCORE_OT_MaterialMix_Add,
LUXCORE_OT_MaterialMatte_Add,
LUXCORE_OT_MaterialMatteTranslucent_Add,
LUXCORE_OT_MaterialMetal_Add,
LUXCORE_OT_MaterialMirror_Add,
LUXCORE_OT_MaterialGlossy_Add,
LUXCORE_OT_MaterialGlossyTranslucent_Add,
LUXCORE_OT_MaterialGlossyCoating_Add,
LUXCORE_OT_MaterialGlass_Add,
LUXCORE_OT_MaterialNull_Add,
LUXCORE_OT_MaterialCarpaint_Add,
LUXCORE_OT_MaterialCloth_Add,
LUXCORE_OT_MaterialVelvet_Add,
LUXCORE_OT_MaterialTwoSided_Add,
LUXCORE_OT_MaterialFrontBackOpacity_Add,
# Volume
LUXCORE_OT_VolumeClear_Add,
LUXCORE_OT_VolumeHomogeneous_Add,
LUXCORE_OT_VolumeHeterogeneous_Add,
# Texture
LUXCORE_OT_TextureImageMap_Add,
LUXCORE_OT_TextureBrick_Add,
LUXCORE_OT_TextureWireframe_Add,
LUXCORE_OT_TextureDots_Add,
LUXCORE_OT_TexturefBM_Add,
LUXCORE_OT_TextureCheckerboard2D_Add,
LUXCORE_OT_TextureCheckerboard3D_Add,
LUXCORE_OT_TextureMarble_Add,
LUXCORE_OT_TextureWrinkled_Add,
LUXCORE_OT_TextureHitpoint_Add,
LUXCORE_OT_TextureSmoke_Add,
LUXCORE_OT_TextureOpenVDB_Add,
LUXCORE_OT_TextureFresnel_Add,
# Blender Texture
LUXCORE_OT_BTextureBlend_Add,
LUXCORE_OT_BTextureClouds_Add,
LUXCORE_OT_BTextureDistortedNoise_Add,
LUXCORE_OT_BTextureMagic_Add,
LUXCORE_OT_BTextureMarble_Add,
LUXCORE_OT_BTextureMusgrave_Add,
LUXCORE_OT_BTextureNoise_Add,
LUXCORE_OT_BTextureStucci_Add,
LUXCORE_OT_BTextureWood_Add,
LUXCORE_OT_BTextureVoronoi_Add,
# Math
LUXCORE_OT_MathMath_Add,
LUXCORE_OT_MathMixColor_Add,
LUXCORE_OT_MathVectorMath_Add,
LUXCORE_OT_MathDotProduct_Add,
LUXCORE_OT_MathSplitFloat_Add,
LUXCORE_OT_MathMakeFloat_Add,
LUXCORE_OT_MathTextureRemap_Add,
# Utils
LUXCORE_OT_UtilsTextureBump_Add,
LUXCORE_OT_UtilsTextureBand_Add,
LUXCORE_OT_UtilsTextureDistort_Add,
LUXCORE_OT_UtilsTextureHSV_Add,
LUXCORE_OT_UtilsTextureBrightContrast_Add,
LUXCORE_OT_UtilsTextureInvert_Add,
LUXCORE_OT_UtilsTexturConstfloat1_Add,
LUXCORE_OT_UtilsTextureConstfloat3_Add,
LUXCORE_OT_UtilsTextureIORPreset_Add,
LUXCORE_OT_UtilsTextureHitpointInfo_Add,
LUXCORE_OT_UtilsTexturePointiness_Add,
LUXCORE_OT_UtilsTextureObjectID_Add,
LUXCORE_OT_UtilsTextureRandomPerIsland_Add,
LUXCORE_OT_UtilsTextureTimeInfo_Add,
LUXCORE_OT_UtilsTextureUV_Add,
LUXCORE_OT_UtilsTextureRandom_Add,
LUXCORE_OT_UtilsTextureBombing_Add,
# Mapping
LUXCORE_OT_MappingMapping2D_Add,
LUXCORE_OT_MappingMapping3D_Add,
LUXCORE_OT_MappingTriplanar_Add,
LUXCORE_OT_MappingTriplanarBump_Add,
LUXCORE_OT_MappingTriplanarNormalmap_Add,
# Light
LUXCORE_OT_LightEmission_Add,
LUXCORE_OT_LightLampSpectrum_Add,
LUXCORE_OT_LightBlackbody_Add,
LUXCORE_OT_LightIrregularDat_Add,
# Modifiers
LUXCORE_OT_ModifiersShapeSubdiv_Add,
LUXCORE_OT_ModifiersHeightDisplacement_Add,
LUXCORE_OT_ModifiersVectorDisplacement_Add,
LUXCORE_OT_ModifiersSimplify_Add,
LUXCORE_OT_ModifiersHarlequin_Add,
# Pointer
LUXCORE_OT_PointerTree_Add,
LUXCORE_OT_Output_Add
]