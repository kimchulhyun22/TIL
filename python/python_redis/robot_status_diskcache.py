from diskcache import Cache


class RobotStatusDiskCache:
    ROBOT_POSE = 'robot_pose'

    def __init__(self):
        self.__diskcache = Cache()

    def set_robot_pose(self, position_x: float, position_y: float, position_z: float,
                       orientation_x: float, orientation_y: float, orientation_z: float, orientation_w: float):
        try:
            self.__diskcache[RobotStatusDiskCache.ROBOT_POSE] = {
                'position_x': position_x,
                'position_y': position_y,
                'position_z': position_z,
                'orientation_x': orientation_x,
                'orientation_y': orientation_y,
                'orientation_z': orientation_z,
                'orientation_w': orientation_w
            }
        except Exception as error:
            print('error = ', error)

    def get_robot_pose(self):
        return (self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['position_x'],
                self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['position_y'],
                self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['position_z'],
                self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['orientation_x'],
                self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['orientation_y'],
                self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['orientation_z'],
                self.__diskcache[RobotStatusDiskCache.ROBOT_POSE]['orientation_w'])
