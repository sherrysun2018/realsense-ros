# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch realsense2_camera node without rviz2."""
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('realsense2_camera'),
        'config',
        'd435i.yaml'
        )

    return LaunchDescription([
        # Realsense
        launch_ros.actions.Node(
            package='realsense2_node', 
            node_namespace='t265',
            node_executable='realsense2_node',
            parameters = [{
                           'device_type': 't265',
                           'enable_fisheye1': False,
                           'enable_fisheye2': False,
                           'topic_odom_in': 'odom_in',
                           'calib_odom_file': '',
                           }],
            output='screen',
            emulate_tty=True,
            ),
        launch_ros.actions.Node(
            package='realsense2_node', 
            node_namespace='d400',
            node_executable='realsense2_node',
            parameters = [{
                           'device_type': 'd4.5',
                           'align_depth': True,
                           'enable_pointcloud': True,
                           'color_width': 640,
                           'color_height': 480,
                           'depth_width': 640,
                           'depth_height': 480,
                           'clip_distance': -2.0,
                           }],
            output='screen',
            emulate_tty=True,
            ),
    ])