import enum


class KakaoMapCategory(enum.Enum):
    # 대형마트
    MART = 'MT1'
    # 편의점
    CONVENIENCE_STORE = 'CS2'
    # 어린이집, 유치원
    KINDERGARDEN = 'PS3'
    # 학교
    SCHOOL = 'SC4'
    # 학원
    ACADEMY = 'AC5'
    # 주차장
    PARKING_LOT = 'PK6'
    # 주유소, 충전소
    GAS_STATION = 'OL7'
    # 지하철역
    SUBWAY_STATION = 'SW8'
    # 은행
    BANK = 'BK9'
    # 문화시설
    CULTURE_FACILITY = 'CT1'
    # 중개업소
    BROKERAGE = 'AG2'
    # 공공기관
    PUBLIC_INSTITUTION = 'PO3'
    # 관광명소
    ATTRACTION = 'AT4'
    # 숙박
    ACCOMODATION = 'AD5'
    # 음식점
    RESTAURANT = 'FD6'
    # 카페
    CAFE = 'CE7'
    # 병원
    HOSPITAL = 'HP8'
    # 약국
    PHARMACY = 'PM9'