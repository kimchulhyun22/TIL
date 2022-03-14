import redis_client


class RobotStatusRedis:
    ROBOT_POSE = 'robot_pose'

    def __init__(self):
        self.redis_client = redis_client.RedisClient()

    def set_robot_pose(self, position_x: float, position_y: float, position_z: float,
                       orientation_x: float, orientation_y: float, orientation_z: float, orientation_w: float):
        redis_connection = self.redis_client.get_connection()

        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'position_x', position_x)
        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'position_y', position_y)
        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'position_z', position_z)

        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'orientation_x', orientation_x)
        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'orientation_y', orientation_y)
        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'orientation_z', orientation_z)
        redis_connection.hset(RobotStatusRedis.ROBOT_POSE, 'orientation_w', orientation_w)

    def get_robot_pose(self):
        redis_connection = self.redis_client.get_connection()
        return (float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'position_x')),
                float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'position_y')),
                float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'position_z')),
                float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'orientation_x')),
                float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'orientation_y')),
                float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'orientation_z')),
                float(redis_connection.hget(RobotStatusRedis.ROBOT_POSE, 'orientation_w')))
