import bpy

class BlenderButton(bpy.types.Panel):
    bl_label = "Gazebo2Blender"
    bl_idname = "OBJECT_PT_log"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.label(text="Export:")

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("bpy.ops.")


def register():
    bpy.utils.register_class(BlenderButton)

def unregister():
    bpy.utils.unregister_class(BlenderButton)

if __name__ == "__main__":
    register()