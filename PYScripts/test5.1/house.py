class House:
    def __init__(self, nName, nfloorNum):
        self.name = nName
        self.floorNum = nfloorNum

    def go_to_floor(self, new_floor):
        if (new_floor < self.floorNum) and (new_floor > 1):
            print(f"Вы на {new_floor}-м этаже")
        else:
            print("Этаж не найден")
