import bpy
from bpy.props import BoolProperty
from .. utils import MACHIN3 as m3


# TODO: the mirror stuff

class Focus(bpy.types.Operator):
    bl_idname = "machin3.focus"
    bl_label = "MACHIN3: Focus"
    bl_options = {'REGISTER', 'UNDO'}

    view_selected: BoolProperty(name="View Selcted", default=True)

    def draw(self, context):
        layout = self.layout

        column = layout.column()

        column.prop(self, "view_selected")

    def execute(self, context):
        history = context.scene.M3.focus_history

        sel = m3.selected_objects()

        if sel:
            self.focus(context, sel, history)


        elif history:
            self.unfocus(context, history)

        # for epoch in history:
            # print(epoch.name, ": ", [obj.name for obj in epoch.objects])

        return {'FINISHED'}

    def focus(self, context, sel, history):
        hidden = []

        for obj in context.view_layer.objects:
            if not obj.hide_viewport and obj not in sel:
                hidden.append(obj)
                obj.hide_viewport = True

        if hidden:
            epoch = history.add()
            epoch.name = "Epoch %d" % (len(history) - 1)

            for obj in hidden:
                entry = epoch.objects.add()
                entry.obj = obj
                entry.name = obj.name

        if self.view_selected:
            bpy.ops.view3d.view_selected()

    def unfocus(self, context, history):
        if self.view_selected:
            selected = []

            for obj in context.view_layer.objects:
                if not obj.hide_viewport:
                    obj.select_set(True)
                    selected.append(obj)

        last_epoch = history[-1]

        for entry in last_epoch.objects:
            entry.obj.hide_viewport = False

            if self.view_selected:
                entry.obj.select_set(True)
                selected.append(entry.obj)

        idx = history.keys().index(last_epoch.name)

        history.remove(idx)

        if self.view_selected:
            bpy.ops.view3d.view_selected()

            for obj in selected:
                obj.select_set(False)
