# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_axis

from . import nearest_axis_ops
from . import nearest_axis_ui
from . import nearest_axis_prefs
from . import nearest_axis_keymap
from .addon import Addon
import bpy


bl_info = {
    'name': 'Nearest Axis',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport',
    'wiki_url': 'https://b3d.interplanety.org/en/',
    'tracker_url': 'https://b3d.interplanety.org/en/',
    'description': 'Align the 3D Viewport window to the nearest axis'
}


def register():
    if not Addon.dev_mode():
        nearest_axis_prefs.register()
        nearest_axis_ops.register()
        if bpy.context.preferences.addons[__package__].preferences.panel_viewport:
            nearest_axis_ui.register()
        nearest_axis_keymap.register()
    else:
        print('It seems you are trying to use the dev version of the '
           + bl_info['name']
           + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        nearest_axis_keymap.unregister()
        nearest_axis_ui.unregister()
        nearest_axis_ops.unregister()
        nearest_axis_prefs.unregister()


if __name__ == '__main__':
    register()
