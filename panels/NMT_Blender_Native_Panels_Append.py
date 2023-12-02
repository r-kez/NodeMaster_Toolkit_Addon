import bpy

from ..operators.View3D_Operators.View_3D_Utils_Operators import RENDER_OT_Res_Flip

def FlipResolutionAppend(self, context):
    layout = self.layout

    layout.operator("render.res_flip", text="Flip Resolution")

