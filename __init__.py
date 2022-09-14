# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_ortho

from . import nearest_ortho_ops
from . import nearest_ortho_ui
from .addon import Addon


bl_info = {
    'name': 'Nearest Ortho',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport',
    'wiki_url': 'https://b3d.interplanety.org/en/',
    'tracker_url': 'https://b3d.interplanety.org/en/',
    'description': 'Align the 3D Viewport window to the nearest ortho axis'
}


def register():
    if not Addon.dev_mode():
        nearest_ortho_ops.register()
        nearest_ortho_ui.register()
    else:
        print('It seems you are trying to use the dev version of the '
           + bl_info['name']
           + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        nearest_ortho_ui.unregister()
        nearest_ortho_ops.unregister()


if __name__ == '__main__':
    register()
