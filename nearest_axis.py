# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_nearest_axis

import bpy
from bpy_extras import view3d_utils
from mathutils import Vector


class NearestAxis:

    _base_axis = (
        (Vector((1.0, 0.0, 0.0)), 'LEFT'),
        (Vector((-1.0, 0.0, 0.0)), 'RIGHT'),
        (Vector((0.0, 1.0, 0.0)), 'FRONT'),
        (Vector((0.0, -1.0, 0.0)), 'BACK'),
        (Vector((0.0, 0.0, 1.0)), 'BOTTOM'),
        (Vector((0.0, 0.0, -1.0)), 'TOP')
    )

    @classmethod
    def align_nearest(cls, context):
        # align 3D viewport to the nearest base axis
        region = next((reg for reg in context.area.regions if reg.type == 'WINDOW'), None)
        if region:
            # get viewport view direction vector
            viewport_view_direction = view3d_utils.region_2d_to_vector_3d(
                region,
                region.data,
                (region.width / 2.0, region.height / 2.0)
            )
            # find nearest base axis - with what base axis viewport direction has minimum angle
            angles = tuple(map(lambda _axis: _axis[0].angle(viewport_view_direction), cls._base_axis))
            min_angle_ids = angles.index(min(angles))
            nearest_axis = cls._base_axis[min_angle_ids]
            # align 3D Viewport to the nearest axis
            bpy.ops.view3d.view_axis('INVOKE_DEFAULT', type=nearest_axis[1])
