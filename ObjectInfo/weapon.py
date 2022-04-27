class weapon:
    def __init__(self, name, number, meso, damage, critical_chance, critical_damage):
        self.name = name
        self.number = number
        self.meso = meso
        self.damage = damage
        self.c_chance = critical_chance
        self.c_damage = critical_damage


# 이름, 번호, 요구메소, 공격력, 치명타 확률, 치명타 데미지

w0 = weapon('낡은 글라디우스', 0, 0, 10, 0, 0.0)
w1 = weapon("검", 1, 2000, 15, 0, 0.0)
w2 = weapon("돼지치기 막대", 2, 3500, 40, 0, 0.0)
w3 = weapon("카알 대검", 3, 5000, 80, 0, 0.0)
w4 = weapon("초보 전사의 검", 4, 7499, 110, 15, 0.1)
w5 = weapon("사브르", 5, 10000, 170, 0, 0.0)
w6 = weapon("바이킹 소드", 6, 30000, 300, 10, 0.0)
w7 = weapon("쿠크리", 7, 95000, 500, 0, 0.0)
w8 = weapon("일룬", 8, 165000, 800, 20, 0.0)
w9 = weapon("글라디우스", 9, 475000, 1300, 15, 0.0)
w10 = weapon("커틀러스", 10, 1357000, 2200, 0, 0.5)

WL = [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10] # 무기들을 저장한 리스트 ( WL : WeaponList )