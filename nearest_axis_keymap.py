# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_axis

import bpy


class NEAREST_AXIS_KeyMap:

    _keymaps = []

    @classmethod
    def register(cls, context):
        # add keys
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
            # add keys
            keymap_item = keymap.keymap_items.new('nearest_axis.align', 'EQUAL', 'PRESS')
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        # clear keys
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    NEAREST_AXIS_KeyMap.register(context=bpy.context)


def unregister():
    NEAREST_AXIS_KeyMap.unregister()
