import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty


######################################################################
#                      ADDON PREFERENCES                             #
######################################################################



class ExampleAddonPreferences(AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    filepath: StringProperty(
        name="Example File Path",
        subtype='FILE_PATH',
    )
    number: IntProperty(
        name="Example Number",
        default=4,
    )
    boolean: BoolProperty(
        name="Example Boolean",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        #layout.label(text="This is a preferences view for our add-on")
        #layout.prop(self, "filepath")
        #layout.prop(self, "number")
        #layout.prop(self, "boolean")

        layout.label(text="This is still an addon under development.")
        layout.label(text="If you have criticisms or suggestions for improvements feel free to get in touch")
        
        Contact = "https://linktr.ee/rkezives"
        row = layout.row(align=True)
        row.operator("wm.url_open", text="Contact").url = Contact



class OBJECT_OT_addon_prefs_example(Operator):
    """Display example preferences"""
    bl_idname = "object.addon_prefs_example"
    bl_label = "Add-on Preferences Example"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        info = ("Path: %s, Number: %d, Boolean %r" %
                (addon_prefs.filepath, addon_prefs.number, addon_prefs.boolean))

        self.report({'INFO'}, info)
        print(info)

        return {'FINISHED'}



classes_Preferences = [
    ExampleAddonPreferences,
    OBJECT_OT_addon_prefs_example
]