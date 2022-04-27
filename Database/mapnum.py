from Database.emoji import *
keyword_mapnum = {
    0: ['edelstein', '에델슈타인'],
    1: ['victoria_island', '빅토리아 아일랜드'],
    2: ['nihal_desert', '니할 사막'],
    3: ['aqua_road', '아쿠아로드'],
    4: ['elnath_mts', '엘나스 산맥'],
    5: ['ludus_lake', '루더스 호수'],
    6: ['ereb', '에레브'],
    7: ['temple_of_time', '시간의 신전'],
    8: ['rien', '리엔'],
    9: ['kritias', '크리티아스'],
    10: ['minar_forest', '미나르 숲'],
    11: ['mureung_garden', '무릉도원'],
    12: ['mechanical_grave', '기계무덤'],
    13: ['maple_world', '메이플 월드'],
    14: ['sleepy_wood', '슬리피우드'],
    15: ['ellinia', '엘리니아'],
    16: ['henesys', '헤네시스'],
    17: ['kerning_city', '커닝시티'],
    18: ['perion', '페리온'],
    19: ['root_abyss', '루타비스'],
    20: ['fallen_world_tree', '타락한 세계수'],
    21: ['folkvillage', '아랫마을'],
    22: ['deep_mine', '폐광'],
    23: ['lion_castle', '사자왕의 성'],
    24: ['fantastic_theme_park', '판타스틱 테마파크'],
    25: ['ellin_forest', '엘린 숲'],
    26: ['omega_sector', '지구방위본부'],
    27: ['clock_tower_lower_floor', '시계탑 최하층'],
    28: ['gate_of_future', '미래의 문'],
    29: ['arcane_river', '아케인 리버'],
    30: ['road_of_vanishing', '소멸의 여로'],
    31: ['reverse_city', '리버스 시티'],
    32: ['chew_chew_island', '츄츄 아일랜드'],
    33: ['yum_yum_island', '얌얌 아일랜드'],
    34: ['lacheln', '꿈의 도시 레헬른'],
    35: ['arcana', '신비의 숲 아르카나'],
    36: ['morass', '기억의 늪 모라스'],
    37: ['esfera', '태초의 바다 에스페라'],
    38: ['sellas', '셀라스, 별이 잠긴 곳'],
    39: ['tenebris', '테네브리스'],
    40: ['moonbridge', '문브릿지'],
    41: ['labyrinth_of_suffering', '고통의 미궁'],
    42: ['limen', '리멘'],
    43: ['riena_strait', '리에나 해협'],
    44: ['colossus_the_giant', '암벽거인 콜로서스'],
    45: ['golden_temple', '황금사원'],
    46: ['grandis', '그란디스'],
    47: ['pantheon', '판테온'],
    48: ['helisium', '헬리시움'],
    49: ['citadel_of_tyrant', '폭군의 성채'],
    50: ['pointy_ear_fox_village', '뾰족귀 여우마을'],
    51: ['fox_valley', '여우 골짜기'],
    52: ['savage_terminal', '새비지 터미널'],
    53: ['verdel', '베르딜'],
    54: ['asylum', '아쉴롬'],
    55: ['cheongungol', '청운골'],
    56: ['ristonia', '리스토니아'],
    57: ['toolen_city', '툴렌시티'],
    58: ['cernium', '신의 도시 세르니움'],
    59: ['burning_cernium', '불타는 세르니움'],
    60: ['hotel_arcs', '호텔 아르크스'],
    61: ['fairy_academy_elinel', '요정 학원 엘리넬'],
    62: ['gold_beach', '골드비치'],
    63: ['secret_forest_elodin', '비밀의 숲 엘로딘'],
    64: ['mushroom_castle', '버섯의 성'],
    65: ['partem', '파르템'],
    66: ['kerning_tower', '커닝 타워'],
    67: ['ancient_city_aswan', '고대도시 아스완'],
    68: ['narin', '나린'],
    69: ['karotte', '멈추지 않는 탑, 카로테']
}

icon_mapnum = {
    edelstein : 0,
    victoria_island : 1,
    nihal_desert : 2,
    aqua_road : 3,
    elnath_mts : 4,
    ludus_lake : 5,
    ereb : 6,
    temple_of_time : 7,
    rien : 8,
    kritias : 9,
    minar_forest : 10,
    mureung_garden : 11,
    mechanical_grave : 12,
    maple_world : 13,
    sleepy_wood : 14,
    ellinia : 15,
    henesys : 16,
    kerning_city : 17,
    perion : 18,
    root_abyss : 19,
    fallen_world_tree : 20,
    folkvillage : 21,
    deep_mine : 22,
    lion_castle : 23,
    fantastic_theme_park : 24,
    ellin_forest : 25,
    omega_sector : 26,
    clock_tower_lower_floor : 27,
    gate_of_future : 28,
    arcane_river : 29,
    road_of_vanishing : 30,
    reverse_city : 31,
    chew_chew_island : 32,
    yum_yum_island : 33,
    lacheln : 34,
    arcana : 35,
    morass : 36,
    esfera : 37,
    sellas : 38,
    tenebris : 39,
    moonbridge : 40,
    labyrinth_of_suffering : 41,
    limen : 42,
    riena_strait : 43,
    colossus_the_giant : 44,
    golden_temple : 45,
    grandis : 46,
    pantheon : 47,
    helisium : 48,
    citadel_of_tyrant : 49,
    pointy_ear_fox_village : 50,
    fox_valley : 51,
    savage_terminal : 52,
    verdel : 53,
    asylum : 54,
    cheongungol : 55,
    ristonia : 56,
    toolen_city : 57,
    cernium : 58,
    burning_cernium : 59,
    hotel_arcs : 60,
    fairy_academy_elinel : 61,
    gold_beach : 62,
    secret_forest_elodin : 63,
    mushroom_castle : 64,
    partem : 65,
    kerning_tower : 66,
    ancient_city_aswan : 67,
    narin : 68,
    karotte : 69
}

linked_map = {
    0: [maple_world, mechanical_grave], # 에델슈타인
    1: [maple_world, grandis, sleepy_wood, fairy_academy_elinel, gold_beach, secret_forest_elodin, mushroom_castle, partem, kerning_tower], # 빅토리아 아일랜드
    2: [maple_world, ancient_city_aswan], # 니할 사막
    3: [maple_world, folkvillage, elnath_mts], # 아쿠아 로드
    4: [maple_world, aqua_road, deep_mine], # 엘나스 사막
    5: [maple_world, folkvillage, fantastic_theme_park, ellin_forest, omega_sector, clock_tower_lower_floor], # 루더스 호수
    6: [maple_world, victoria_island, elnath_mts, tenebris], # 에레브
    7: [maple_world, minar_forest, gate_of_future, arcane_river], # 시간의 신전
    8: [maple_world, riena_strait], # 리엔
    9: [maple_world, minar_forest], # 크리티아스
    10: [maple_world, colossus_the_giant, kritias, temple_of_time], # 미나르 숲
    11: [maple_world, golden_temple], # 무릉 도원
    12: [edelstein], # 기계무덤
    13: [victoria_island, edelstein, nihal_desert, aqua_road, elnath_mts, ludus_lake, ereb, temple_of_time, rien, kritias, minar_forest, mureung_garden], # 메이플 월드
    14: [victoria_island, root_abyss, fallen_world_tree], # 슬리피우드
    15: [], # 엘리니아
    16: [], # 헤네시스
    17: [], # 커닝시티
    18: [], # 페리온
    19: [sleepy_wood], # 루타비스
    20: [sleepy_wood], # 타락한 세계수
    21: [aqua_road, ludus_lake], # 아랫마을
    22: [elnath_mts, lion_castle], # 폐광
    23: [deep_mine], # 사자왕의 성
    24: [ludus_lake], # 판타스틱 테마파크
    25: [ludus_lake], # 엘린 숲
    26: [ludus_lake], # 지구방위본부
    27: [ludus_lake], # 시계탑 최하층
    28: [temple_of_time], # 미래의 문
    29: [temple_of_time, road_of_vanishing, chew_chew_island, lacheln, arcana, morass, esfera, tenebris], # 아케인 리버
    30: [arcane_river, temple_of_time, reverse_city, chew_chew_island], # 소멸의 여로
    31: [road_of_vanishing], # 리버스 시티
    32: [arcane_river, road_of_vanishing, yum_yum_island, lacheln], # 츄츄 아일랜드
    33: [chew_chew_island], # 얌얌 아일랜드
    34: [arcane_river, chew_chew_island, arcana], # 꿈의 도시 레헬른
    35: [arcane_river, lacheln, morass], # 신비의 숲 아르카나
    36: [arcane_river, arcana, esfera], # 기억의 늪 모라스
    37: [arcane_river, morass, sellas], # 태초의 바다 에스페라
    38: [esfera], # 셀라스, 별이 잠긴 곳
    39: [arcane_river, ereb, moonbridge], # 테네브리스
    40: [tenebris, labyrinth_of_suffering], # 문브릿지
    41: [moonbridge, limen], # 고통의 미궁
    42: [labyrinth_of_suffering], # 리멘
    43: [rien], # 리에나 해협
    44: [minar_forest], # 암벽거인 콜로서스
    45: [mureung_garden], # 황금 사원
    46: [victoria_island, pantheon, helisium, pointy_ear_fox_village, savage_terminal, verdel, cheongungol, ristonia, narin, cernium, hotel_arcs], # 그란디스
    47: [grandis, helisium], # 판테온
    48: [grandis, pantheon, citadel_of_tyrant], # 헬리시움
    49: [helisium], # 폭군의 성채
    50: [grandis, fox_valley], # 뾰족귀 여우마을
    51: [pointy_ear_fox_village], # 여우 골짜기
    52: [grandis, toolen_city, asylum], # 새비지 터미널
    53: [grandis], # 베르딜
    54: [savage_terminal], # 아쉴롬
    55: [grandis], # 청운골
    56: [grandis], # 라스토니아
    57: [savage_terminal], # 툴렌 시티
    58: [grandis, burning_cernium], # 세르니움
    59: [grandis, cernium], # 불타는 세르니움
    60: [grandis, karotte], # 호텔 아르크스
    61: [victoria_island], # 요정학원 엘리넬
    62: [victoria_island], # 골드비치
    63: [victoria_island], # 비밀의 숲 엘로딘
    64: [victoria_island], # 버섯의 성
    65: [victoria_island], # 파르템
    66: [victoria_island], # 커닝 타워
    67: [nihal_desert], # 고대도시 아스완
    68: [grandis], # 나린
    69: [hotel_arcs] # 멈추지 않는 탑, 카로테
}