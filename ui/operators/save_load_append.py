import bpy
from bpy.props import StringProperty, BoolProperty
from ... utils import MACHIN3 as m3


class SaveIncremental(bpy.types.Operator):
    bl_idname = "machin3.save_incremental"
    bl_label = "Save Incremental"
    bl_description = "Save Incremental"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        print("hello")

        return {'FINISHED'}


class LoadMostRecent(bpy.types.Operator):
    bl_idname = "machin3.load_most_recent"
    bl_label = "Load Most Recent"
    bl_options = {"REGISTER"}

    def execute(self, context):
        recent_path = bpy.utils.user_resource('CONFIG', "recent-files.txt")

        try:
            with open(recent_path) as file:
                recent_files = file.read().splitlines()
        except (IOError, OSError, FileNotFoundError):
            recent_files = []

        most_recent = recent_files[0]

        bpy.ops.wm.open_mainfile(filepath=most_recent)

        return {'FINISHED'}


class AppendWorld(bpy.types.Operator):
    bl_idname = "machin3.append_world"
    bl_label = "Append World"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout

        column = layout.column()


    def execute(self, context):

        print("appending world")

        """
        blendpath = "/home/x/TEMP/blender/Rendering/Materials9.blend"

        fullpath = "%s/%s" % (blendpath, self.appendtype.capitalize())

        # the append ops also unselects for some reason, so we need to get the selection before
        if self.appendtype == "MATERIAL" and self.applymaterial and self.appendname != "ALL":
            sel = m3.selected_objects()

        if self.appendtype == "WORLD":
            bpy.ops.wm.append(directory=fullpath, filename=self.appendname)

            bpy.context.scene.cycles.film_transparent = False

            world = bpy.data.worlds.get(self.appendname)

            bpy.context.scene.world = world

        elif self.appendtype == "MATERIAL":
            if self.appendname == "ALL":
                for name in m3_material_names:
                    if name not in ["", "ALL"]:
                        bpy.ops.wm.append(directory=fullpath, filename=name)
            else:
                bpy.ops.wm.append(directory=fullpath, filename=self.appendname)

                if self.applymaterial:
                    m3.select(sel)
                    bpy.ops.object.apply_material(mat_to_assign=self.appendname)
        """


        return {'FINISHED'}


class AppendMaterial(bpy.types.Operator):
    bl_idname = "machin3.append_material"
    bl_label = "Append Material"
    bl_options = {'REGISTER', 'UNDO'}

    name = StringProperty(name="Append Name")

    applymaterial = BoolProperty(name="Apply Material to Selection", default=True)

    def draw(self, context):
        layout = self.layout

        column = layout.column()

        if self.appendtype == "MATERIAL":
            column.prop(self, "applymaterial")

    def execute(self, context):

        print("appending material:", self.name)

        """
        blendpath = "/home/x/TEMP/blender/Rendering/Materials9.blend"

        fullpath = "%s/%s" % (blendpath, self.appendtype.capitalize())

        # the append ops also unselects for some reason, so we need to get the selection before
        if self.appendtype == "MATERIAL" and self.applymaterial and self.appendname != "ALL":
            sel = m3.selected_objects()

        if self.appendname == "ALL":
            for name in m3_material_names:
                if name not in ["", "ALL"]:
                    bpy.ops.wm.append(directory=fullpath, filename=name)
        else:
            bpy.ops.wm.append(directory=fullpath, filename=self.appendname)

            if self.applymaterial:
                m3.select(sel)
                bpy.ops.object.apply_material(mat_to_assign=self.appendname)
        """


        return {'FINISHED'}
