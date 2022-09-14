# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_axis

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .nearest_axis import NearestAxis


class NEAREST_AXIS_OT_align(Operator):
    bl_idname = 'nearest_axis.align'
    bl_label = 'Align'
    bl_description = 'Align the 3D Viewport to the nearest axis'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        NearestAxis.align_nearest(
           context=context
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(NEAREST_AXIS_OT_align)


def unregister():
    unregister_class(NEAREST_AXIS_OT_align)
