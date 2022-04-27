from Database.MobImg import *
from Database.icon import *
class monster:
    def __init__(self, name, damage, hp, meso, exp, world, img, icon):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.meso = meso
        self.exp = exp
        self.world = world
        self.img = img
        self.icon = icon

mob_edel1 = monster("새싹 화분", 5, 100, 10, 20, "에델슈타인", img_edel1, icon_edelstein)
mob_edel2 = monster("나팔꽃 화분", 5, 110, 15, 21, "에델슈타인", img_edel2, icon_edelstein)
mob_edel3 = monster("포도주스병", 6, 115, 15, 23, "에델슈타인", img_edel3, icon_edelstein)
mob_edel4 = monster("순찰로봇", 7, 120, 20, 25, "에델슈타인", img_edel4, icon_edelstein)
mob_edel5 = monster("이상한 이정표", 7, 130, 20, 27, "에델슈타인", img_edel5, icon_edelstein)
mob_edel6 = monster("구렁이", 10, 130, 25, 30, "에델슈타인", img_edel6, icon_edelstein)
mob_edel7 = monster("물 도둑", 15, 140, 25, 33, "에델슈타인", img_edel7, icon_edelstein)
mob_edel8 = monster("더스트 박스", 15, 160, 27, 35, "에델슈타인", img_edel8, icon_edelstein)
mob_edel9 = monster("가로등", 18, 175, 30, 37, "에델슈타인", img_edel9, icon_edelstein)
mob_edel10 = monster("순찰로봇S", 25, 200, 45, 45, "에델슈타인", img_edel10, icon_edelstein)
mob_edel11 = monster("안전제일", 30, 220, 50, 50, "에델슈타인", img_edel11, icon_edelstein)
mob_edel12 = monster("아기 바위베어먹기", 30, 250, 53, 53, "에델슈타인", img_edel12, icon_edelstein)
mob_edel13 = monster("큰 바위베어먹기", 30, 300, 55, 55, "에델슈타인", img_edel13, icon_edelstein)

mob_nihal1 = monster('흰 모래토끼', 1046, 10000, 10359, 15834, '아리안트', img_nihal1, icon_nihal_desert)
mob_nihal2 = monster('갈색 모래토끼', 1046, 10000, 15834, 10359, '아리안트', img_nihal2, icon_nihal_desert)
mob_nihal3 = monster('귀마개 프릴드', 1098, 11750, 13789, 19112, '아리안트', img_nihal3, icon_nihal_desert)
mob_nihal4 = monster('목도리 프릴드', 1098, 11750, 19112, 13789, '아리안트', img_nihal4, icon_nihal_desert)
mob_nihal5 = monster('주니어 카투스', 1129, 12250, 16784, 22512, '아리안트', img_nihal5, icon_nihal_desert)
mob_nihal6 = monster('카투스', 1219, 13385, 17284, 23444, '아리안트', img_nihal6, icon_nihal_desert)
mob_nihal7 = monster('로얄 카투스', 1219, 13385, 23444, 17284, '아리안트', img_nihal7, icon_nihal_desert)
mob_nihal8 = monster('벨라모아', 1300, 14000, 18129, 23125, '아리안트', img_nihal8, icon_nihal_desert)
mob_nihal9 = monster('미요캐츠', 1350, 15185, 18932, 23984, '아리안트', img_nihal9, icon_nihal_desert)
mob_nihal10 = monster('키요', 1500, 17585, 20152, 25284, '아리안트', img_nihal10, icon_nihal_desert)
mob_nihal11 = monster('모래난쟁이', 1625, 19114, 21558, 26042, '아리안트', img_nihal11, icon_nihal_desert)
mob_nihal12 = monster('모래거인', 1700, 20152, 22512, 26939, '아리안트', img_nihal12, icon_nihal_desert)
mob_nihal13 = monster('스콜피언', 1800, 21524, 24015, 28529, '아리안트', img_nihal13, icon_nihal_desert)
mob_nihal14 = monster('모래 두더지', 1900, 23152, 26785, 30000, '아리안트', img_nihal14, icon_nihal_desert)
mob_nihal15 = monster('붉은 모래난쟁이', 2000, 25000, 28152, 31525, '아리안트', img_nihal15, icon_nihal_desert)
mob_nihal16 = monster('큐브슬라임', 2250, 27712, 30124, 35155, '마가티아', img_nihal16, icon_magatia)
mob_nihal17 = monster('루모', 2300, 29145, 33313, 38878, '마가티아', img_nihal17, icon_magatia)
mob_nihal18 = monster('트리플 루모', 2333, 33333, 33333, 40000, '마가티아', img_nihal18, icon_magatia)
mob_nihal19 = monster('호문', 2500, 34512, 35684, 41568, '마가티아', img_nihal19, icon_magatia)
mob_nihal20 = monster('호문쿨루', 2750, 34512, 37774, 44145, '마가티아', img_nihal20, icon_magatia)
mob_nihal21 = monster('호문스큘러', 3000, 36712, 40612, 46152, '마가티아', img_nihal21, icon_magatia)
mob_nihal22 = monster('아이언 뮤테', 3100, 38000, 42600, 48128, '마가티아', img_nihal22, icon_magatia)
mob_nihal23 = monster('강화된 아이언 뮤테', 3300, 41525, 46162, 52451, '마가티아', img_nihal23, icon_magatia)
mob_nihal24 = monster('미스릴 뮤테', 3300, 43312, 48713, 57718, '마가티아', img_nihal24, icon_magatia)
mob_nihal25 = monster('강화된 미스릴 뮤테', 3500, 43312, 49613, 60014, '마가티아', img_nihal25, icon_magatia)
mob_nihal26 = monster('사이티', 3550, 45185, 75763, 80452, '마가티아', img_nihal26, icon_magatia)
mob_nihal27 = monster('로이드', 3700, 47883, 47141, 62384, '마가티아', img_nihal27, icon_magatia)
mob_nihal28 = monster('네오 휴로이드', 4250, 53250, 50358, 65714, '마가티아', img_nihal28, icon_magatia)
mob_nihal29 = monster('D.로이', 4500, 56144, 55313, 69212, '마가티아', img_nihal29, icon_magatia)
mob_nihal30 = monster('자동경비시스템', 5000, 60000, 61156, 73994, '마가티아', img_nihal30, icon_magatia)
mob_nihal31 = monster('데우', 500, 3000000, 3128594, 4154541, '아리안트', img_nihal31, icon_nihal_desert) # 보스
mob_nihal32 = monster('데우', 700, 4000000, 6727412, 8887245, '아리안트', img_nihal32, icon_nihal_desert) # 히든보스
mob_nihal33 = monster('루루모', 650, 4350000, 4377751, 5328231, '마가티아', img_nihal33, icon_magatia) # 보스
mob_nihal34 = monster('루루모모', 800, 6000000, 7658832, 9595952, '마가티아', img_nihal34, icon_magatia) # 히든보스
mob_nihal35 = monster('호문스페큘러', 650, 5000000, 5112882, 5988232, '마가티아', img_nihal35, icon_magatia) # 보스
mob_nihal36 = monster('디트와 로이', 700, 5500000, 5516875, 6362875, '마가티아', img_nihal36, icon_magatia) # 보스
mob_nihal37 = monster('키메라', 750, 6000000, 6278759, 7172793, '마가티아', img_nihal37, icon_magatia) # 보스
mob_nihal38 = monster('키메라', 800, 8000000, 9293938, 10012132, '마가티아', img_nihal38, icon_magatia) # 보스
mob_nihal39 = monster('프랑켄로이드', 800, 8000000, 7272795, 8129384, '마가티아', img_nihal39, icon_magatia) # 보스
mob_nihal40 = monster('화난 프랑켄로이드', 1000, 10000000, 11131726, 14451672, '마가티아', img_nihal40, icon_magatia) # 보스


mob_leben1 = monster("경비로봇", 895, 7754, 6052, 9126, "레벤 광산", img_leben1, icon_leben_mine)
mob_leben2 = monster("경비로봇L", 954, 8012, 6782, 9830, "레벤 광산", img_leben2, icon_leben_mine)
mob_leben3 = monster("빅 스파이더", 1000, 9113, 7074, 10132, "레벤 광산", img_leben3, icon_leben_mine)
mob_leben4 = monster("카트 베어", 20000, 400, 3385, 5872, "레벤 광산", img_leben4, icon_leben_mine)
mob_leben5 = monster("라키", 1152, 9656, 7777, 11111, "레벤 광산", img_leben5, icon_leben_mine)
mob_leben6 = monster("라쿤", 1256, 10152, 8385, 12535, "레벤 광산", img_leben6, icon_leben_mine)
mob_leben7 = monster("라칸", 1256, 10152, 12535, 8385, "레벤 광산", img_leben7, icon_leben_mine)
mob_leben8 = monster("방어 시스템", 1370, 12500, 8753, 14434, "레벤 광산", img_leben8, icon_leben_mine)
mob_leben9 = monster("강화된 방어 시스템", 1500, 13500, 9210, 15323, "레벤 광산", img_leben9, icon_leben_mine)
mob_leben10 = monster("AF형 안드로이드", 3700, 7530, 10874, 16912, "레벤 광산", img_leben10, icon_leben_mine)
mob_leben11 = monster("고장난 DF형 안드로이드", 700, 32050, 21154, 30405, "레벤 광산", img_leben11, icon_leben_mine)
mob_leben12 = monster("광석 이터", 2200, 13245, 18750, 24565, "레벤 광산", img_leben11, icon_leben_mine)


mob_aquaroad1 = monster("씨클", 380, 2984, 1669, 1875, "아쿠아로드", img_aquaroad1, icon_aqua_road)
mob_aquaroad2 = monster("씨코", 415, 3333, 1724, 2400, "아쿠아로드", img_aquaroad2, icon_aqua_road)
mob_aquaroad3 = monster("스쿠버 페페", 433, 3564, 1889, 2492, "아쿠아로드", img_aquaroad3, icon_aqua_road)
mob_aquaroad4 = monster("주니어 씰", 482, 3876, 2059, 2669, "아쿠아로드", img_aquaroad4, icon_aqua_road)
mob_aquaroad5 = monster("핀붐", 506, 4040, 2452, 2830, "아쿠아로드", img_aquaroad5, icon_aqua_road)
mob_aquaroad6 = monster("버블피쉬", 535, 4375, 2122, 3333, "아쿠아로드", img_aquaroad6, icon_aqua_road)
mob_aquaroad7 = monster("플라워 피쉬", 565, 4582, 2444, 3482, "아쿠아로드", img_aquaroad7, icon_aqua_road)
mob_aquaroad8 = monster("마스크피쉬", 582, 4865, 2674, 3612, "아쿠아로드", img_aquaroad8, icon_aqua_road)
mob_aquaroad9 = monster("푸퍼", 600, 5000, 2800, 3700, "아쿠아로드", img_aquaroad9, icon_aqua_road)
mob_aquaroad10 = monster("포이즌 푸퍼", 630, 5000, 2800, 3700, "아쿠아로드", img_aquaroad10, icon_aqua_road)
mob_aquaroad11 = monster("크라피", 650, 5325, 2960, 3885, "아쿠아로드", img_aquaroad11, icon_aqua_road)
mob_aquaroad12 = monster("크립", 650, 5325, 3885, 2960, "아쿠아로드", img_aquaroad12, icon_aqua_road)
mob_aquaroad13 = monster("스파커", 680, 5740, 3174, 4082, "아쿠아로드", img_aquaroad13, icon_aqua_road)
mob_aquaroad14 = monster("프리져", 680, 5740, 4082, 3174, "아쿠아로드", img_aquaroad14, icon_aqua_road)
mob_aquaroad15 = monster("폭렬 망둥이집", 1, 40000, 10092, 11854, "아쿠아로드", img_aquaroad15, icon_aqua_road)
mob_aquaroad16 = monster("망둥이", 230, 2834, 964, 1027, "아쿠아로드", img_aquaroad16, icon_aqua_road)
mob_aquaroad17 = monster("본 피쉬", 735, 6285, 3285, 4484, "아쿠아로드", img_aquaroad17, icon_aqua_road)
mob_aquaroad18 = monster("스퀴드", 777, 6570, 3584, 4692, "아쿠아로드", img_aquaroad18, icon_aqua_road)
mob_aquaroad19 = monster("리셀 스퀴드", 777, 6962, 3584, 4692, "아쿠아로드", img_aquaroad19, icon_aqua_road)
mob_aquaroad20 = monster("샤크", 800, 7000, 3688, 4912, "아쿠아로드", img_aquaroad20, icon_aqua_road)
mob_aquaroad21 = monster("콜드 샤크", 900, 7000, 3698, 5012, "아쿠아로드", img_aquaroad21, icon_aqua_road)
mob_aquaroad22 = monster("블러드붐", 3000, 500, 3082, 3999, "아쿠아로드", img_aquaroad22, icon_aqua_road)
mob_aquaroad23 = monster("세르프", 315, 51250, 32387, 40404, "아쿠아로드", img_aquaroad23, icon_aqua_road) # 보스
mob_aquaroad24 = monster("피아누스", 400, 78250, 50124, 60660, "아쿠아로드", img_aquaroad24, icon_aqua_road) # 보스


mob_luduslake1 = monster("북치는 토끼", 582, 5000, 3012, 3984, "에오스탑", img_luduslake1, icon_ludus_lake)
mob_luduslake2 = monster("브라운테니", 1800, 10000, 9000, 13500, "루디브리엄", img_luduslake2, icon_ludus_lake)
mob_luduslake3 = monster("핑크테니", 1800, 10000, 11000, 10000, "루디브리엄", img_luduslake3, icon_ludus_lake)
mob_luduslake4 = monster("팬더테니", 1800, 10000, 6750, 16785, "루디브리엄", img_luduslake4, icon_ludus_lake)
mob_luduslake5 = monster("더키 패밀리", 2005, 11111, 9374, 18842, "루디브리엄", img_luduslake5, icon_ludus_lake)
mob_luduslake6 = monster("치크세이버", 614, 5262, 3334, 4265, "에오스탑", img_luduslake6, icon_ludus_lake)
mob_luduslake7 = monster("핑크세이버", 614, 5262, 3786, 3512, "에오스탑", img_luduslake7, icon_ludus_lake)
mob_luduslake8 = monster("스카이세이버", 614, 5262, 2952, 4554, "에오스탑", img_luduslake8, icon_ludus_lake)
mob_luduslake9 = monster("처프", 636, 5584, 3692, 4354, "에오스탑", img_luduslake9, icon_ludus_lake)
mob_luduslake10 = monster("트위터", 636, 5584, 4354, 3692, "에오스탑", img_luduslake10, icon_ludus_lake)
mob_luduslake11 = monster("블록퍼스", 666, 5792, 4559, 3884, "에오스탑", img_luduslake11, icon_ludus_lake)
mob_luduslake12 = monster("킹 블록퍼스", 684, 5902, 4802, 4000, "에오스탑", img_luduslake12, icon_ludus_lake)
mob_luduslake13 = monster("블록골렘", 675, 5854, 4672, 3955, "에오스탑", img_luduslake13, icon_ludus_lake)
mob_luduslake14 = monster("킹 블록골렘", 700, 6161, 4884, 4185, "에오스탑", img_luduslake14, icon_ludus_lake)
mob_luduslake15 = monster("라츠", 500, 4289, 2684, 3559, "에오스탑", img_luduslake15, icon_ludus_lake)
mob_luduslake16 = monster("블랙 라츠", 525, 4434, 2772, 3679, "에오스탑", img_luduslake16, icon_ludus_lake)
mob_luduslake17 = monster("장난감 목마", 2222, 12850, 9862, 19775, "루디브리엄", img_luduslake17, icon_ludus_lake)
mob_luduslake18 = monster("로보토이", 2300, 14777, 10000, 20000, "루디브리엄", img_luduslake18, icon_ludus_lake)
mob_luduslake19 = monster("마스터 로보", 2500, 14777, 11111, 21895, "루디브리엄", img_luduslake19, icon_ludus_lake)
mob_luduslake20 = monster("롬바드", 285, 45556, 29876, 36334, "에오스탑", img_luduslake20, icon_ludus_lake) # 보스
mob_luduslake21 = monster("타이머", 500, 99999, 92786, 132524, "루디브리엄", img_luduslake21, icon_ludus_lake) # 보스


mob_orbis1 = monster("스톤볼", 220, 2940, 2284, 2159, "오르비스", img_orbis1, icon_orbis)
mob_orbis2 = monster("아이스 스톤볼", 250, 3100, 2419, 2538, "오르비스", img_orbis2, icon_orbis)
mob_orbis3 = monster("파이어 스톤볼", 250, 3100, 2538, 2419, "오르비스", img_orbis3, icon_orbis)
mob_orbis4 = monster("샐리온", 275, 3405, 2775, 2662, "오르비스", img_orbis4, icon_orbis)
mob_orbis5 = monster("라이오너", 275, 3500, 2862, 2790, "오르비스", img_orbis5, icon_orbis)
mob_orbis6 = monster("그류핀", 275, 3500, 2790, 2862, "오르비스", img_orbis6, icon_orbis)
mob_orbis7 = monster("루이넬", 300, 3800, 3102, 3000, "오르비스", img_orbis7, icon_orbis)
mob_orbis8 = monster("루나픽시", 350, 4000, 3339, 3210, "오르비스", img_orbis8, icon_orbis)
mob_orbis9 = monster("스타픽시", 375, 3750, 3210, 3339, "오르비스", img_orbis9, icon_orbis)
mob_orbis10 = monster("러스터픽시", 350, 4240, 3428, 3352, "오르비스", img_orbis10, icon_orbis)
mob_orbis11 = monster("고스트픽시", 400, 4500, 3500, 3500, "오르비스", img_orbis11, icon_orbis)
mob_orbis12 = monster("네펜데스", 600, 3250, 3814, 3792, "오르비스", img_orbis12, icon_orbis)
mob_orbis13 = monster("다크 네펜데스", 650, 3250, 3972, 3884, "오르비스", img_orbis13, icon_orbis)
mob_orbis14 = monster("골든 스코피", 450, 5000, 4182, 4093, "오르비스", img_orbis14, icon_orbis)
mob_orbis15 = monster("골든 맘무트", 600, 6000, 4451, 4556, "오르비스", img_orbis15, icon_orbis)
mob_orbis16 = monster("크림슨 발록", 315, 55555, 39212, 51800, "오르비스", img_orbis16, icon_orbis) # 보스
mob_orbis17 = monster("엘리쟈", 375, 60101, 41454, 53535, "오르비스", img_orbis17, icon_orbis) # 보스
mob_orbis18 = monster("파파픽시", 400, 68754, 43432, 56112, "오르비스", img_orbis18, icon_orbis) # 보스
mob_orbis19 = monster("크세르크세스", 450, 76390, 49884, 60125, "오르비스", img_orbis19, icon_orbis) # 보스


mob_elnath1 = monster("주니어 예티", 800, 6975, 4682, 6666, "엘나스", img_elnath1, icon_elnath_mts)
mob_elnath2 = monster("다크 주니어 예티", 800, 6975, 6666, 4682, "엘나스", img_elnath2, icon_elnath_mts)
mob_elnath3 = monster("화이트팽", 895, 7377, 4924, 7195, "엘나스", img_elnath3, icon_elnath_mts)
mob_elnath4 = monster("헥터", 895, 7377, 7195, 4924, "엘나스", img_elnath4, icon_elnath_mts)
mob_elnath5 = monster("페페", 938, 7835, 5185, 7377, "엘나스", img_elnath5, icon_elnath_mts)
mob_elnath6 = monster("다크 페페", 938, 7835, 7377, 5185, "엘나스", img_elnath6, icon_elnath_mts)
mob_elnath7 = monster("예티", 1000, 8181, 7803, 5447, "엘나스", img_elnath7, icon_elnath_mts)
mob_elnath8 = monster("다크 예티", 1000, 8181, 5447, 7803, "엘나스", img_elnath8, icon_elnath_mts)
mob_elnath9 = monster("예티와 페페", 1115, 8454, 5755, 8096, "엘나스", img_elnath9, icon_elnath_mts)
mob_elnath10 = monster("다크 예티와 페페", 1115, 8454, 8096, 5755, "엘나스", img_elnath10, icon_elnath_mts)
mob_elnath11 = monster("웨어울프", 1341, 8512, 6084, 8400, "엘나스", img_elnath11, icon_elnath_mts)
mob_elnath12 = monster("라이칸스로프", 1341, 8512, 8400, 6084, "엘나스", img_elnath12, icon_elnath_mts)
mob_elnath13 = monster("호브 헥터", 1350, 8600, 6200, 8400, "엘나스", img_elnath13, icon_elnath_mts)
mob_elnath14 = monster("정예 호브", 1360, 8700, 6300, 8500, "엘나스", img_elnath14, icon_elnath_mts)
mob_elnath15 = monster("컴뱃 호브", 1370, 8800, 6400, 8600, "엘나스", img_elnath15, icon_elnath_mts)
mob_elnath16 = monster("흉폭한 호브", 1400, 9000, 6600, 8800, "엘나스", img_elnath16, icon_elnath_mts)
mob_elnath17 = monster("설산의 마녀", 415, 69118, 106824, 133242, "엘나스", img_elnath17, icon_orbis) # 보스
mob_elnath18 = monster("스노우맨", 420, 70000, 147772, 159932, "엘나스", img_elnath18, icon_orbis) # 보스
mob_elnath19 = monster("리치", 450, 73815, 150504, 161135, "엘나스", img_elnath19, icon_orbis) # 보스
mob_elnath20 = monster("렉스", 485, 80814, 184961, 203816, "엘나스", img_elnath20, icon_orbis) # 보스


mob_minar1 = monster('레쉬', 3300, 48500, 64484, 75310, '미나르숲', img_minar1, icon_minar_forest)
mob_minar2 = monster('다크 레쉬', 3500, 53000, 75994, 81992, '미나르숲', img_minar2, icon_minar_forest)
mob_minar3 = monster('비틀', 3600, 59000, 83220, 85994, '미나르숲', img_minar3, icon_minar_forest)
mob_minar4 = monster('듀얼 비틀', 3800, 62500, 85854, 91259, '미나르숲', img_minar4, icon_minar_forest)
mob_minar5 = monster('호브', 4000, 67782, 91512, 99999, '미나르숲', img_minar5, icon_minar_forest)
mob_minar6 = monster('핀호브', 4300, 71956, 100124, 112154, '미나르숲', img_minar6, icon_minar_forest)
mob_minar7 = monster('가시덤불', 30000, 5000, 51259, 63328, '미나르숲', img_minar7, icon_minar_forest)
mob_minar8 = monster('헹키', 4500, 74494, 121559, 137591, '미나르숲', img_minar8, icon_minar_forest)
mob_minar9 = monster('하프', 4300, 75682, 131135, 166364, '미나르숲', img_minar9, icon_minar_forest)
mob_minar10 = monster('블러드 하프', 4600, 78615, 159163, 181612, '미나르숲', img_minar10, icon_minar_forest)
mob_minar11 = monster('버크', 4800, 81954, 191192, 213654, '미나르숲', img_minar11, icon_minar_forest)
mob_minar12 = monster('듀얼 버크', 5000, 85312, 200102, 231325, '미나르숲', img_minar12, icon_minar_forest)
mob_minar13 = monster('검은 켄타우로스', 5500, 91359, 224289, 266382, '미나르숲', img_minar13, icon_minar_forest)
mob_minar14 = monster('붉은 켄타우로스', 5600, 92152, 231154, 275183, '미나르숲', img_minar14, icon_minar_forest)
mob_minar15 = monster('푸른 켄타우로스', 5700, 93519, 247794, 280505, '미나르숲', img_minar15, icon_minar_forest)
mob_minar16 = monster('블루 드래곤터틀', 6000, 100000, 278754, 318182, '미나르숲', img_minar16, icon_minar_forest)
mob_minar17 = monster('레드 드래곤터틀', 6150, 113584, 309182, 356059, '미나르숲', img_minar17, icon_minar_forest)
mob_minar18 = monster('리스튼', 6400, 135916, 349183, 388672, '미나르숲', img_minar18, icon_minar_forest)
mob_minar19 = monster('브레스튼', 6600, 168285, 360805, 412956, '미나르숲', img_minar19, icon_minar_forest)
mob_minar20 = monster('그린 코니언', 7000, 192165, 401259, 445924, '미나르숲', img_minar20, icon_minar_forest)
mob_minar21 = monster('다크 코니언', 7250, 215632, 434164, 485290, '미나르숲', img_minar21, icon_minar_forest)
mob_minar22 = monster('레드 와이번', 8185, 272652, 512434, 535543, '미나르숲', img_minar22, icon_minar_forest)
mob_minar23 = monster('블루 와이번', 8350, 308372, 554344, 582885, '미나르숲', img_minar23, icon_minar_forest)
mob_minar24 = monster('다크 와이번', 8500, 332385, 572785, 607723, '미나르숲', img_minar24, icon_minar_forest)
mob_minar25 = monster('뉴트주니어', 9000, 350000, 600000, 630000, '미나르숲', img_minar25, icon_minar_forest)
mob_minar26 = monster('네스트골렘', 9500, 382950, 632454, 666364, '미나르숲', img_minar26, icon_minar_forest)
mob_minar27 = monster('스켈레곤', 10000, 442485, 688924, 707572, '미나르숲', img_minar27, icon_minar_forest)
mob_minar28 = monster('스켈로스', 15000, 525920, 828985, 1001012, '미나르숲', img_minar28, icon_minar_forest)
mob_minar29 = monster('마스터 호브', 2000, 63250000, 9042832, 100000000, '미나르숲', img_minar29, icon_minar_forest)
mob_minar30 = monster('마스터 하프', 2250, 78500000, 152395670, 177654389, '미나르숲', img_minar30, icon_minar_forest)
mob_minar31 = monster('마뇽', 2500, 91850000, 232559384, 266774752, '미나르숲', img_minar31, icon_minar_forest)
mob_minar32 = monster('마뇽', 4000, 211532680, 552354695, 75775782, '미나르숲', img_minar32, icon_minar_forest)
mob_minar33 = monster('그리프', 2750, 135916000, 352669384, 400000000, '미나르숲', img_minar33, icon_minar_forest)
mob_minar34 = monster('그리프', 4500, 2529943840, 682395759, 82885624, '미나르숲', img_minar34, icon_minar_forest)
mob_minar35 = monster('켄타우로스 킹', 3000, 161933280, 394287684, 452554564, '미나르숲', img_minar35, icon_minar_forest)
mob_minar36 = monster('레비아탄', 3500, 270538840, 554344984, 588262765, '미나르숲', img_minar36, icon_minar_forest)
mob_minar37 = monster('레비아탄', 5000, 445482965, 1032659335, 1129678540, '미나르숲', img_minar37, icon_minar_forest)
mob_minar38 = monster('드래고니카', 5000, 449825672, 693659380, 708090850, '미나르숲', img_minar38, icon_minar_forest)
mob_minar39 = monster('드래곤라이더', 7500, 612832985, 882852892, 1001012050, '미나르숲', img_minar39, icon_minar_forest)




mob_deepmine1 = monster("플라이 아이", 1550, 9000, 8250, 12054, "폐광", img_deepmine1, icon_deep_mine)
mob_deepmine2 = monster("쿨리 좀비", 1785, 9672, 8894, 12889, "폐광", img_deepmine2, icon_deep_mine)
mob_deepmine3 = monster("마이너 좀비", 1907, 11079, 9584, 14002, "폐광", img_deepmine3, icon_deep_mine)
mob_deepmine4 = monster("불독", 2300, 13000, 10550, 14782, "폐광", img_deepmine4, icon_deep_mine)
mob_deepmine5 = monster("파이어독", 2500, 15000, 11274, 16042, "폐광", img_deepmine5, icon_deep_mine)


mob_lioncastle1 = monster("문지기 크로키", 1350, 8000, 6500, 9000, "사자왕의 성", img_lioncastle1, icon_lion_castle)
mob_lioncastle2 = monster("레인디어", 1400, 8250, 6750, 9300, "사자왕의 성", img_lioncastle2, icon_lion_castle)
mob_lioncastle3 = monster("블러드 레인디어", 1450, 8500, 7000, 9500, "사자왕의 성", img_lioncastle3, icon_lion_castle)
mob_lioncastle4 = monster("베어울프", 1500, 8750, 7250, 10000, "사자왕의 성", img_lioncastle4, icon_lion_castle)
mob_lioncastle5 = monster("그레이 벌쳐", 1550, 9000, 7500, 10500, "사자왕의 성", img_lioncastle5, icon_lion_castle)
mob_lioncastle6 = monster("황금벌", 1600, 9000, 7750, 11000, "사자왕의 성", img_lioncastle6, icon_lion_castle)
mob_lioncastle7 = monster("프로즌 로즈", 1650, 9250, 8000, 11500, "사자왕의 성", img_lioncastle7, icon_lion_castle)
mob_lioncastle8 = monster("가든 골렘", 1700, 9500, 8250, 12000, "사자왕의 성", img_lioncastle8, icon_lion_castle)
mob_lioncastle9 = monster("캐슬 골렘", 1800, 10000, 9000, 13500, "사자왕의 성", img_lioncastle9, icon_lion_castle)
mob_lioncastle10 = monster("킹 캐슬 골렘", 200, 135000, 61805, 74788, "사자왕의 성", img_lioncastle10, icon_lion_castle) # 보스
mob_lioncastle11 = monster("교도관 아니", 615, 82665, 80423, 99872, "사자왕의 성", img_lioncastle11, icon_lion_castle) # 보스


mob_clocktower1 = monster("티키", 3175, 19500, 13672, 18084, "시계탑 최하층", img_clocktower1, icon_ludus_lake)
mob_clocktower2 = monster("틱톡", 3375, 21850, 14449, 18865, "시계탑 최하층", img_clocktower2, icon_ludus_lake)
mob_clocktower3 = monster("크로노스", 3500, 23500, 15692, 19999, "시계탑 최하층", img_clocktower3, icon_ludus_lake)
mob_clocktower4 = monster("플래툰 크로노스", 3750, 25000, 16884, 20000, "시계탑 최하층", img_clocktower4, icon_ludus_lake)
mob_clocktower5 = monster("마스터 크로노스", 4000, 25000, 17982, 20205, "시계탑 최하층", img_clocktower5, icon_ludus_lake)
mob_clocktower6 = monster("버피", 4500, 28990, 19194, 21964, "시계탑 최하층", img_clocktower6, icon_ludus_lake)
mob_clocktower7 = monster("레이지 버피", 4500, 28990, 19562, 23558, "시계탑 최하층", img_clocktower7, icon_ludus_lake)
mob_clocktower8 = monster("버푼", 4700, 30000, 20654, 25872, "시계탑 최하층", img_clocktower8, icon_ludus_lake)
mob_clocktower9 = monster("딥 버푼", 4700, 31950, 22020, 28051, "시계탑 최하층", img_clocktower9, icon_ludus_lake)
mob_clocktower10 = monster("소울테니", 5000, 34000, 23475, 30000, "시계탑 최하층", img_clocktower10, icon_ludus_lake)
mob_clocktower11 = monster("마스터 소울테니", 5000, 36785, 25184, 32981, "시계탑 최하층", img_clocktower11, icon_ludus_lake)
mob_clocktower12 = monster("데스테니", 5325, 38000, 26891, 35008, "시계탑 최하층", img_clocktower12, icon_ludus_lake)
mob_clocktower13 = monster("마스터 데스테니", 5325, 40850, 29012, 37774, "시계탑 최하층", img_clocktower13, icon_ludus_lake)
mob_clocktower14 = monster("파이렛", 5555, 43772, 32095, 40962, "시계탑 최하층", img_clocktower14, icon_ludus_lake)
mob_clocktower15 = monster("듀얼 파이렛", 5555, 45984, 33761, 43563, "시계탑 최하층", img_clocktower15, icon_ludus_lake)
mob_clocktower16 = monster("바이킹", 5810, 48112, 35532, 47272, "시계탑 최하층", img_clocktower16, icon_ludus_lake)
mob_clocktower17 = monster("기간틱 바이킹", 5810, 50234, 38294, 50924, "시계탑 최하층", img_clocktower17, icon_ludus_lake)
mob_clocktower18 = monster("클라크", 6000, 53556, 41986, 54082, "시계탑 최하층", img_clocktower18, icon_ludus_lake)
mob_clocktower19 = monster("다크 클라크", 6000, 57234, 44401, 55586, "시계탑 최하층", img_clocktower19, icon_ludus_lake)
mob_clocktower20 = monster("팬텀워치", 6440, 60000, 46694, 58232, "시계탑 최하층", img_clocktower20, icon_ludus_lake)
mob_clocktower21 = monster("G.팬텀워치", 6440, 64000, 48923, 61115, "시계탑 최하층", img_clocktower21, icon_ludus_lake)
mob_clocktower22 = monster("게이트키퍼", 7000, 70000, 53652, 64285, "시계탑 최하층", img_clocktower22, icon_ludus_lake)
mob_clocktower23 = monster("타나토스", 8250, 82952, 61834, 78245, "시계탑 최하층", img_clocktower23, icon_ludus_lake)
mob_clocktower24 = monster("알리샤르", 2500, 1522950, 550234, 675421, "시계탑 최하층", img_clocktower24, icon_ludus_lake) # 보스


mob_folk1 = monster("삼미호", 7280, 69800, 51872, 64321, "아랫마을", img_folk1, icon_folkvillage)
mob_folk2 = monster("월묘", 8154, 75600, 56900, 69752, "아랫마을", img_folk2, icon_folkvillage)
mob_folk3 = monster("호돌이", 8560, 83000, 63384, 73905, "아랫마을", img_folk3, icon_folkvillage)
mob_folk4 = monster("호걸", 9000, 97500, 71894, 80012, "아랫마을", img_folk4, icon_folkvillage)
mob_folk5 = monster("파란 왕도깨비", 12500, 135000, 86905, 95894, "아랫마을", img_folk5, icon_folkvillage)
mob_folk6 = monster("초록 왕도깨비", 12500, 135000, 95894, 86905, "아랫마을", img_folk6, icon_folkvillage)
mob_folk7 = monster("노란 왕도깨비", 14000, 160000, 90782, 100055, "아랫마을", img_folk7, icon_folkvillage)


mob_ereb1 = monster("티노", 5, 40, 10, 10, "에레브", img_ereb1, icon_ereb)
mob_ereb2 = monster("티브", 7, 40, 12, 12, "에레브", img_ereb2, icon_ereb)
mob_ereb3 = monster("티무", 7, 60, 13, 13, "에레브", img_ereb3, icon_ereb)
mob_ereb4 = monster("티루", 9, 60, 15, 15, "에레브", img_ereb4, icon_ereb)
mob_ereb5 = monster("티구르", 15, 100, 20, 20, "에레브", img_ereb5, icon_ereb)


mob_rien1 = monster("무루", 5, 40, 10, 10, "리엔", img_rien1, icon_rien)
mob_rien2 = monster("무루파", 7, 40, 12, 12, "리엔", img_rien2, icon_rien)
mob_rien3 = monster("무루피아", 7, 60, 13, 13, "리엔", img_rien3, icon_rien)
mob_rien4 = monster("무루무루", 9, 60, 15, 15, "리엔", img_rien4, icon_rien)
mob_rien5 = monster("무루쿤", 15, 100, 20, 20, "리엔", img_rien5, icon_rien)


mob_vic1 = monster("주황버섯", 5, 100, 10, 20, "헤네시스", img_vic1, icon_henesys)
mob_vic2 = monster("파란버섯", 6, 100, 10, 23, "헤네시스", img_vic2, icon_henesys)
mob_vic3 = monster("우는 파란버섯", 7, 105, 12, 23, "헤네시스", img_vic3, icon_henesys)
mob_vic4 = monster("초록버섯", 5, 120, 15, 25, "헤네시스", img_vic4, icon_henesys)
mob_vic5 = monster("뿔버섯", 15, 50, 20, 20, "헤네시스", img_vic5, icon_henesys)
mob_vic6 = monster("리본돼지", 5, 80, 10, 10, "리스항구", img_vic6, icon_victoria_island)
mob_vic7 = monster("파란 리본돼지", 6, 100, 15, 20, "리스항구", img_vic7, icon_victoria_island)
mob_vic8 = monster("이상한 돼지", 7, 100, 15, 20, "리스항구", img_vic8, icon_victoria_island)
mob_vic9 = monster("페어리", 10, 110, 20, 25, "엘리니아", img_vic9, icon_ellinia)
mob_vic10 = monster("로얄 페어리", 12, 120, 25, 25, "엘리니아", img_vic10, icon_ellinia)
mob_vic11 = monster("슬라임", 15, 130, 27, 32, "엘리니아", img_vic11, icon_ellinia)
mob_vic12 = monster("버블링", 15, 130, 32, 27, "엘리니아", img_vic12, icon_ellinia)
mob_vic13 = monster("이블아이", 20, 150, 35, 40, "엘리니아", img_vic13, icon_ellinia)
mob_vic14 = monster("커즈아이", 22, 160, 37, 44, "엘리니아", img_vic14, icon_ellinia)
mob_vic15 = monster("콜드아이", 24, 170, 39, 48, "엘리니아", img_vic15, icon_ellinia)
mob_vic16 = monster("서전아이", 30, 200, 41, 52, "엘리니아", img_vic16, icon_ellinia)
mob_vic17 = monster("스톤골렘", 35, 210, 47, 47, "헤네시스", img_vic17, icon_henesys)
mob_vic18 = monster("다크 스톤골렘", 37, 230, 50, 50, "헤네시스", img_vic18, icon_henesys)
mob_vic19 = monster("아이스 믹스골렘", 40, 250, 53, 53, "헤네시스", img_vic19, icon_henesys)
mob_vic20 = monster("파이어 믹스골렘", 42, 270, 56, 56, "헤네시스", img_vic20, icon_henesys)
mob_vic21 = monster("스텀프", 50, 330, 134, 82, "페리온", img_vic21, icon_perion)
mob_vic22 = monster("다크 스텀프", 55, 330, 146, 94, "페리온", img_vic22, icon_perion)
mob_vic23 = monster("엑스텀프", 53, 350, 153, 108, "페리온", img_vic23, icon_perion)
mob_vic24 = monster("다크 엑스텀프", 57, 350, 167, 120, "페리온", img_vic24, icon_perion)
mob_vic25 = monster("고스텀프", 60, 400, 184, 135, "페리온", img_vic25, icon_perion)
mob_vic26 = monster("히죽대는 고스텀프", 65, 400, 205, 146, "페리온", img_vic26, icon_perion)
mob_vic27 = monster("우드 마스크", 70, 450, 242, 160, "페리온", img_vic27, icon_perion)
mob_vic28 = monster("스톤 마스크", 70, 450, 205, 182, "페리온", img_vic28, icon_perion)
mob_vic29 = monster("달팽이", 1, 50, 10, 10, "리스 항구", img_vic29, icon_victoria_island)
mob_vic30 = monster("파란 달팽이", 5, 100, 20, 10, "리스 항구", img_vic30, icon_victoria_island)
mob_vic31 = monster("빨간 달팽이", 5, 100, 10, 20, "리스 항구", img_vic31, icon_victoria_island)
mob_vic32 = monster("스포아", 5, 150, 20, 20, "헤네시스", img_vic32, icon_henesys)
mob_vic33 = monster("스켈독", 90, 500, 305, 202, "페리온", img_vic33, icon_perion)
mob_vic34 = monster("스켈레톤 사병", 90, 540, 332, 226, "페리온", img_vic34, icon_perion)
mob_vic35 = monster("스켈레톤 장교", 95, 550, 344, 249, "페리온", img_vic35, icon_perion)
mob_vic36 = monster("스켈레톤 지휘관", 100, 600, 372, 358, "페리온", img_vic36, icon_perion)
mob_vic37 = monster("머쉬맘", 20, 1080, 500, 500, "헤네시스", img_vic37, icon_henesys) # 보스
mob_vic38 = monster("블루 머쉬맘", 25, 1250, 550, 550, "헤네시스", img_vic38, icon_henesys) # 보스
mob_vic39 = monster("스텀피", 30, 3000, 2050, 1850, "페리온", img_vic39, icon_perion) # 보스
mob_vic40 = monster("마노", 10, 1500, 600, 720, "헤네시스", img_vic40, icon_henesys) # 보스
mob_vic41 = monster("스켈레톤 총사령관", 60, 6000, 4025, 3350, "페리온", img_vic41, icon_perion) # 보스


mob_slp1 = monster("카파 드레이크", 125, 850, 422, 473, "슬리피우드", img_slp1, icon_sleepy_wood)
mob_slp2 = monster("드레이크", 130, 850, 455, 486, "슬리피우드", img_slp2, icon_sleepy_wood)
mob_slp3 = monster("레드 드레이크", 135, 850, 478, 500, "슬리피우드", img_slp3, icon_sleepy_wood)
mob_slp4 = monster("아이스 드레이크", 140, 850, 552, 435, "슬리피우드", img_slp4, icon_sleepy_wood)
mob_slp5 = monster("다크 드레이크", 150, 925, 536, 532, "슬리피우드", img_slp5, icon_sleepy_wood)
mob_slp6 = monster("와일드 카고", 75, 2000, 772, 804, "슬리피우드", img_slp6, icon_sleepy_wood)
mob_slp7 = monster("타우로마시스", 82, 2300, 864, 829, "슬리피우드", img_slp7, icon_sleepy_wood)
mob_slp8 = monster("타우로스피어", 197, 1040, 972, 1002, "슬리피우드", img_slp8, icon_sleepy_wood)
mob_slp9 = monster("좀비버섯", 100, 800, 404, 444, "슬리피우드", img_slp9, icon_sleepy_wood)
mob_slp10 = monster("주니어 발록", 95, 40850, 11890, 9005, "슬리피우드", img_slp10, icon_sleepy_wood) # 보스
mob_slp11 = monster("좀비 머쉬맘", 115, 22249, 7690, 6654, "슬리피우드", img_slp11, icon_sleepy_wood) # 보스


# name, damage, hp, meso, exp, world, img, icon
mob_riena1 = monster("암모나이트 화석", 125, 1150, 809, 908, "리에나 해협", img_riena1, icon_riena_strait)
mob_riena2 = monster("물고기 화석", 135, 1150, 829, 968, "리에나 해협", img_riena2, icon_riena_strait)
mob_riena3 = monster("찐득한 오염물", 150, 1300, 895, 1080, "리에나 해협", img_riena3, icon_riena_strait)
mob_riena4 = monster("찐득한 폐기물", 175, 1300, 937, 1175, "리에나 해협", img_riena4, icon_riena_strait)
mob_riena5 = monster("수상한 물개", 160, 1480, 999, 999, "리에나 해협", img_riena5, icon_riena_strait)
mob_riena6 = monster("수상한 바다표범", 188, 1480, 1095, 1085, "리에나 해협", img_riena6, icon_riena_strait)
mob_riena7 = monster("이동형 난로", 30, 8800, 1942, 2082, "리에나 해협", img_riena7, icon_riena_strait)
mob_riena8 = monster("이동형 쇄빙기", 750, 200, 1182, 1113, "리에나 해협", img_riena8, icon_riena_strait)


mob_elinel1 = monster("반딧불 슬라임", 40, 250, 53, 62, "요정 학원 엘리넬", img_elinel1, icon_fairy_academy_elinel)
mob_elinel2 = monster("페어리 슬라임", 42, 270, 56, 66, "요정 학원 엘리넬", img_elinel2, icon_fairy_academy_elinel)
mob_elinel3 = monster("미스틱 위습", 50, 330, 134, 105, "요정 학원 엘리넬", img_elinel3, icon_fairy_academy_elinel)
mob_elinel4 = monster("워터 엘리먼트", 55, 330, 146, 111, "요정 학원 엘리넬", img_elinel4, icon_fairy_academy_elinel)
mob_elinel5 = monster("트리 엘리먼트", 53, 350, 153, 136, "요정 학원 엘리넬", img_elinel5, icon_fairy_academy_elinel)
mob_elinel6 = monster("하급 마법책", 57, 350, 167, 143, "요정 학원 엘리넬", img_elinel6, icon_fairy_academy_elinel)
mob_elinel7 = monster("상급 마법책", 60, 400, 184, 155, "요정 학원 엘리넬", img_elinel7, icon_fairy_academy_elinel)
mob_elinel8 = monster("양파라고라", 65, 400, 205, 177, "요정 학원 엘리넬", img_elinel8, icon_fairy_academy_elinel)
mob_elinel9 = monster("순무라고라", 70, 450, 242, 185, "요정 학원 엘리넬", img_elinel9, icon_fairy_academy_elinel)
mob_elinel10 = monster("몰 킹", 100, 4000, 3000, 3000, "요정 학원 엘리넬", img_elinel10, icon_fairy_academy_elinel) # 보스


mob_goldbeach1 = monster("야자수 슬라임", 80, 500, 275, 555, "골드비치", img_goldbeach1, icon_gold_beach)
mob_goldbeach2 = monster("코코넛 슬라임", 65, 650, 302, 594, "골드비치", img_goldbeach2, icon_gold_beach)
mob_goldbeach3 = monster("초록조개 슬라임", 90, 720, 334, 612, "골드비치", img_goldbeach3, icon_gold_beach)
mob_goldbeach4 = monster("보라조개 슬라임", 90, 770, 334, 634, "골드비치", img_goldbeach4, icon_gold_beach)
mob_goldbeach5 = monster("갈매기 슬라임", 115, 690, 447, 484, "골드비치", img_goldbeach5, icon_gold_beach)
mob_goldbeach6 = monster("빨간 튜브 슬라임", 100, 835, 389, 706, "골드비치", img_goldbeach6, icon_gold_beach)
mob_goldbeach7 = monster("파란 튜브 슬라임", 100, 880, 414, 734, "골드비치", img_goldbeach7, icon_gold_beach)
mob_goldbeach8 = monster("새우 슬라임", 125, 1101, 497, 848, "골드비치", img_goldbeach8, icon_gold_beach)
mob_goldbeach9 = monster("날치 슬라임", 125, 1201, 534, 892, "골드비치", img_goldbeach9, icon_gold_beach)
mob_goldbeach10 = monster("불가사리 문어 슬라임", 140, 1450, 667, 1175, "골드비치", img_goldbeach10, icon_gold_beach)
mob_goldbeach11 = monster("소라문어 슬라임", 140, 1540, 1054, 784, "골드비치", img_goldbeach11, icon_gold_beach)
mob_goldbeach12 = monster("캡틴 블랙 슬라임", 185, 33780, 7582, 21154, "골드비치", img_goldbeach12, icon_gold_beach) # 보스


mob_elodin1 = monster("뾰족 가시나무", 10, 110, 25, 30, "비밀의 숲 엘로딘", img_elodin1, icon_secret_forest_elodin)
mob_elodin2 = monster("숲의 울음꾼", 11, 120, 27, 34, "비밀의 숲 엘로딘", img_elodin2, icon_secret_forest_elodin)
mob_elodin3 = monster("밤의 울음꾼", 12, 120, 27, 36, "비밀의 숲 엘로딘", img_elodin3, icon_secret_forest_elodin)
mob_elodin4 = monster("깊은 숲 위습", 20, 80, 34, 40, "비밀의 숲 엘로딘", img_elodin4, icon_secret_forest_elodin)
mob_elodin5 = monster("숲의 파수꾼", 13, 130, 31, 40, "비밀의 숲 엘로딘", img_elodin5, icon_secret_forest_elodin)
mob_elodin6 = monster("밤의 파수꾼", 15, 130, 33, 41, "비밀의 숲 엘로딘", img_elodin6, icon_secret_forest_elodin)
mob_elodin7 = monster("푸른 샘의 정령", 20, 165, 45, 36, "비밀의 숲 엘로딘", img_elodin7, icon_secret_forest_elodin)
mob_elodin8 = monster("깊은 샘의 정령", 21, 165, 37, 45, "비밀의 숲 엘로딘", img_elodin8, icon_secret_forest_elodin)
mob_elodin9 = monster("지푸라기 뭉치", 40, 115, 64, 46, "비밀의 숲 엘로딘", img_elodin9, icon_secret_forest_elodin)
mob_elodin10 = monster("먼지 뭉치", 5, 800, 239, 312, "비밀의 숲 엘로딘", img_elodin10, icon_secret_forest_elodin)


mob_mushroom1 = monster("버섯 샹들리에", 155, 1675, 1184, 1364, "버섯의 성", img_mushroom1, icon_mushroom_castle)
mob_mushroom2 = monster("버섯 철갑옷", 170, 1795, 1235, 1398, "버섯의 성", img_mushroom2, icon_mushroom_castle)
mob_mushroom3 = monster("노곤한 바이킹", 185, 2077, 1445, 1392, "버섯의 성", img_mushroom3, icon_mushroom_castle)
mob_mushroom4 = monster("피곤한 바이킹", 185, 2077, 1392, 1445, "버섯의 성", img_mushroom4, icon_mushroom_castle)
mob_mushroom5 = monster("푸근한 바이킹", 200, 2185, 1498, 1415, "버섯의 성", img_mushroom5, icon_mushroom_castle)
mob_mushroom6 = monster("넉넉한 바이킹", 200, 2185, 1415, 1498, "버섯의 성", img_mushroom6, icon_mushroom_castle)
mob_mushroom7 = monster("근엄한 바이킹", 229, 2440, 1672, 1527, "버섯의 성", img_mushroom7, icon_mushroom_castle)
mob_mushroom8 = monster("진지한 바이킹", 229, 2440, 1527, 1672, "버섯의 성", img_mushroom8, icon_mushroom_castle)
mob_mushroom9 = monster("오징어 노예간수", 50, 10184, 1884, 2124, "버섯의 성", img_mushroom9, icon_mushroom_castle)
mob_mushroom10 = monster("바이킹 군단", 2500, 301, 1508, 1444, "버섯의 성", img_mushroom10, icon_mushroom_castle)
mob_mushroom11 = monster("검은 바이킹", 165, 44875, 11889, 13987, "버섯의 성", img_mushroom11, icon_mushroom_castle) # 보스
mob_mushroom12 = monster("총리대신", 227, 50994, 14762, 17774, "버섯의 성", img_mushroom12, icon_mushroom_castle) # 보스


