"""Dragonfly Energy plugin for Pollination."""
from pollination_dsl.common import get_docker_image_from_dependency

# set the version for docker image dynamically based on dragonfly-energy version
# in dependencies
image_id = get_docker_image_from_dependency(
    __package__, 'dragonfly-energy', 'ladybugtools'
)

__pollination__ = {
    'config': {
        'docker': {
            'image': image_id,
            'workdir': '/home/ladybugbot/run'
        }
    }
}
