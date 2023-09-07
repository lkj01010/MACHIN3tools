import bpy
from bpy.props import StringProperty, BoolProperty


class SetTransformPreset(bpy.types.Operator):
    bl_idname = "machin3.set_transform_preset"
    bl_label = "MACHIN3: Set Transform Preset"
    bl_description = "Set Transform Pivot and Orientation at the same time."
    bl_options = {'REGISTER', 'UNDO'}

    pivot: StringProperty(name="Transform Pivot")
    orientation: StringProperty(name="Transform Orientation")
    create_orientation: BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout
        column = layout.column()

    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'VIEW_3D'

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = self.pivot
        context.scene.transform_orientation_slots[0].type = self.orientation

        if self.create_orientation:
            bpy.ops.transform.create_orientation(use=True)

        return {'FINISHED'}

# mid:
class DeleteOrientations(bpy.types.Operator):
    bl_idname = "machin3.delete_orientations"
    bl_label = "Delete Customs"
    bl_description = "Delete Custom Orientations"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        column = layout.column()

    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'VIEW_3D'

    def execute(self, context):
        # bpy.context.scene.transform_orientation_slots[0].type = ""

        # 1. 清除自定义的坐标系
        # Try to set transform orientation and catch error message
        try:
            bpy.context.scene.transform_orientation_slots[0].type = ""
        except Exception as inst:
            # Extract custom orientations from error message
            transforms_str = str(inst).split("not found in")[1]
            transform_list = transforms_str.split(
                "(")[1].split(")")[0].split(",")

            # Execlude first 7 "default" transform orientation
            # default_orientations = ['GLOBAL', 'LOCAL', 'NORMAL', 'GIMBAL', 'VIEW', 'CURSOR', 'PARENT']

            for type in transform_list[7:]:
                # for type in transform_list:
                type = type[2:len(type)-1]
                # if type not in default_orientations:
                bpy.context.scene.transform_orientation_slots[0].type = type
                bpy.ops.transform.delete_orientation()

        return {'FINISHED'}
