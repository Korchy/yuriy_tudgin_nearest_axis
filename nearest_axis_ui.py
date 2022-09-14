# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_axis

import bpy
from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class NEAREST_AXIS_PT_panel(Panel):
    bl_idname = 'NEAREST_AXIS_PT_panel'
    bl_label = 'Nearest Axis'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Nearest Axis'

    def draw(self, context):
        self.layout.operator(
            operator='nearest_axis.align',
            icon='ORIENTATION_LOCAL'
        )


def register():
    register_class(NEAREST_AXIS_PT_panel)


def unregister():
    if hasattr(bpy.types, 'NEAREST_AXIS_PT_panel'):
        unregister_class(NEAREST_AXIS_PT_panel)
