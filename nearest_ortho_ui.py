# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_ortho

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class NEAREST_ORTHO_PT_panel(Panel):
    bl_idname = 'NEAREST_ORTHO_PT_panel'
    bl_label = 'Nearest Ortho'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Nearest Ortho'

    def draw(self, context):
        self.layout.operator('nearest_ortho.main', icon='BLENDER', text='nearest_ortho execute')


def register():
    register_class(NEAREST_ORTHO_PT_panel)


def unregister():
    unregister_class(NEAREST_ORTHO_PT_panel)
