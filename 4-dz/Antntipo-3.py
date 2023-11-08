class ExpDescriptor:
    def __init__(self):
        self.exp = 100

    def __get__(self, instance, owner):
        return self.exp

    def __set__(self, instance, value):
        if value >= 10000:
            self.exp = 10000
        else:
            self.exp = value


class Warrior:
    experience = ExpDescriptor()
    ranks = {0: "Pushover", 10: "Novice", 20: "Fighter", 30: "Warrior", 40: "Veteran", 50: "Sage",
             60: "Elite", 70: "Conqueror", 80: "Champion", 90: "Master", 100: "Greatest"}

    def __init__(self):
        self.experience = 100
        self.achievements = []

    @staticmethod
    def rank_calculate(level):
        rank_key = (level // 10) * 10
        return Warrior.ranks[rank_key]
    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.rank_calculate(self.level)

    def training(self, training_conditions: list):
        description = training_conditions[0]
        exp = training_conditions[1]
        requirement_level = training_conditions[2]
        if self.level >= requirement_level:
            self.achievements.append(description)
            self.experience += exp
            return description
        return "Not strong enough"

    def battle(self, enemy_level):
        diff = self.level - enemy_level
        if not 0 < enemy_level < 101:
            return "Invalid level"
        elif diff >= 2:
            return "Easy fight"
        elif diff >= 0:
            self.experience += 10 if diff == 0 else 5
            return "A good fight"
        elif diff >= -4 or self.rank == Warrior.rank_calculate(enemy_level):
            self.experience += 20 * diff * diff
            return "An intense fight"
        return "You've been defeated"


bruce = Warrior()
bruce.training(["12345", 4201, 1])
print(bruce.achievements, bruce.rank, bruce.level, bruce.experience)
print(bruce.battle(49))
print(bruce.achievements, bruce.rank, bruce.level, bruce.experience)
print(bruce.battle(30))
print(bruce.battle(48))
print(bruce.battle(47))
print(bruce.achievements, bruce.rank, bruce.level, bruce.experience)
