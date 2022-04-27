class armor:
    def __init__(self, name, number, meso, defense, critical_chance, critical_damage):
        self.name = name
        self.number = number
        self.meso = meso
        self.defense = defense
        self.c_chance = critical_chance
        self.c_damage = critical_damage

# 이름, 번호, 요구메소, 방어력, 치명타 확률, 치명타 데미지
a0 = armor('냄비 뚜껑', 0, 0, 5, 0, 0.0)
a1 = armor("안내의 포스실드", 1, 1000, 10, 0, 0.0)
a2 = armor("수호의 소울실드", 2, 2500, 50, 0, 0.0)
a3 = armor("강철 방패", 3, 4000, 70, 0, 0.0)
a4 = armor("미스릴 버클러", 4, 8000, 100, 0, 0.0)
a5 = armor("빨간 삼각 방패", 5, 36000, 150, 0, 0.0)
a6 = armor("긍지의 소울실드", 6, 50000, 300, 0, 0.1)
a7 = armor("레드 크로스 실드", 7, 118500, 350, 0, 0.0)
a8 = armor("의지의 포스실드", 8, 200200, 450, 10, 0.0)
a9 = armor("배틀 실드", 9, 507000, 870, 0, 0.5)
a10 = armor("미스릴 타워 실드", 10, 1587200, 1215, 20, 0.1)

AL = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10] # 아머들을 저장한 리스트 ( AL : ArmorList )