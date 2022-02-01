class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()

# # 드랍쉽
# dropship = FlyableUnit() # "Unit 생성자" 라고만 뜸  # flyableunit(unit,flyable)순서라서

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit() # Flyable 생성자 # flyableunit(flyable,unit) 순서라서


