# Pokemon 타입별 설정
# 노말 = 바위 0.5 고스트 0
# 불꽃 = 불꽃 물 바위 드래곤 0.5 풀 얼음 벌레 2
# 물 = 물 풀 드래곤 0.5 불꽃 땅 바위 2
# 전기 = 물 비행 2 드래곤 전기 풀 0.5 땅 0
# 풀 = 불꽃 풀 독 비행 벌레 드래곤 0.5 물 땅 바위 2
# 얼음 = 불꽃 물 얼음 0.5 풀 땅 비행 드래곤 2
# 격투 = 노말 얼음 바위 2 독 비행 에스퍼 벌레 0.5 고스트 0
# 독 = 풀 2 독 땅 바위 고스트 0.5
# 땅 = 불꽃 전기 독 바위 2 풀 벌레 0.5 비행 0
# 비행 = 풀 격투 벌레 2 전기 바위 0.5
# 에스퍼 = 격투 독 2 에스퍼 0.5
# 벌레 = 불꽃 격투 독 비행 고스트 0.5 풀 에스퍼 2
# 바위 = 불꽃 얼음 비행 벌레 2 격투 땅 0.5
# 고스트 = 노말 0 에스퍼 고스트 2
# 드래곤 = 드래곤 2

class Normal(Pokemon):
    ptype = "노말"

    def body_attack(self):
        damage = 40
        aim = 100
        if random.choice(range(100)) in range(aim)
            if "바위" in enemy.ptype:
                enemy.hp -= damage * 0.5 + self.level * 0.3
            else:
                enemy.hp -= damage + self.level * 0.3
        else:
            print(f"")
            