from database import TestGeometry
from database import session


def create_test_data():
    local_session = session()

    # 카카오 판교 오피스 테스트
    test_data = TestGeometry(point="POINT(37.4021 127.1086)")

    local_session.add(test_data)
    local_session.commit()
    local_session.close()


def check_test_data():

    local_session = session()

    test_data = local_session.query(TestGeometry).first()

    from shapely import wkb

    wkb_data = wkb.loads(bytes(test_data.point))

    print(wkb_data.x, wkb_data.y)


create_test_data()
check_test_data()
