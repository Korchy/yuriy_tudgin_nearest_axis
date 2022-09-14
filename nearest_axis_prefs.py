# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_axis

from bpy.types import AddonPreferences
from bpy.props import BoolProperty
from bpy.utils import register_class, unregister_class
from . import nearest_axis_ui


class NEAREST_AXIS_preferences(AddonPreferences):
    bl_idname = __package__

    panel_viewport: BoolProperty(
        name='Show 3D Viewport panel',
        default=True,
        update=lambda self, context: self._panel_viewport_update(
            self=self
        )
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, property='panel_viewport')

    @staticmethod
    def _panel_viewport_update(self):
        if self.panel_viewport:
            nearest_axis_ui.register()
        else:
            nearest_axis_ui.unregister()


def register():
    register_class(NEAREST_AXIS_preferences)


def unregister():
    unregister_class(NEAREST_AXIS_preferences)
