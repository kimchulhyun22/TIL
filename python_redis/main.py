import robot_status_redis
import robot_status_diskcache
import datetime

if __name__ == '__main__':
    try:

        # Redis
        start = datetime.datetime.now()

        rs = robot_status_redis.RobotStatusRedis()
        rs.set_robot_pose(0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0)
        print(rs.get_robot_pose())

        end = datetime.datetime.now()

        print('redis = ', (end-start).microseconds, 'microseconds')

        # DiskCache
        start = datetime.datetime.now()

        rs = robot_status_diskcache.RobotStatusDiskCache()
        rs.set_robot_pose(0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0)
        print(rs.get_robot_pose())

        end = datetime.datetime.now()

        print('diskcache = ', (end - start).microseconds, 'microseconds')

    except Exception as error:
        print(error)