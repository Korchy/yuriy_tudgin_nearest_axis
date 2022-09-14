# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_ortho

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .nearest_ortho import NearestOrtho


class NEAREST_ORTHO_OT_main(Operator):
    bl_idname = 'nearest_ortho.main'
    bl_label = 'nearest_ortho: main'
    bl_description = 'nearest_ortho - main operator'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        NearestOrtho.nearest_ortho(
           context=context
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(NEAREST_ORTHO_OT_main)


def unregister():
    unregister_class(NEAREST_ORTHO_OT_main)
