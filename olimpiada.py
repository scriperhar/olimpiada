import time

class Elevator:
    def __init__(self, floor, speed, name):
        self.floor = floor
        self.speed = speed
        self.name = name

def current():
    print(olimpiada1.name, olimpiada2.name, olimpiada3.name)
    for floor in range(floors,0, -1):
        if floor == olimpiada1.floor:
            ol1_current = "X"
        else:
            ol1_current = "."
        if floor == olimpiada2.floor:
            ol2_current = "X"
        else:
            ol2_current = "."
        if floor == olimpiada3.floor:
            ol3_current = "X"
        else:
            ol3_current = "."
        print(ol1_current, ol2_current, ol3_current, floor)

def move(lift, call_floor):
    if call_floor > lift.floor:
        for i in range(lift.floor, call_floor):
            lift.floor += 1
            print(3 * "\n")
            current()
            time.sleep(lift.speed)
    elif call_floor < lift.floor:
        for i in range(lift.floor, call_floor, -1):
            lift.floor -= 1
            print(3 * "\n")
            current()
            time.sleep(lift.speed)

olimpiada1 = Elevator(1, 0.2, "A")
olimpiada2 = Elevator(25, 0.2, "B")
olimpiada3 = Elevator(12, 0.2, "C")
floors = 25

current()
while True:
    enter = input("Ввод: ")
    enter = enter.split(" ")
    call = int(enter[1])
    while call > floors or call < 1:
        enter = input("ебанат пиши нормально")
        enter = enter.split(" ")
        call = int(enter[1])

    if enter[0].lower() == "в":
        while call > floors or call < 1:
            call = int(input("ебанат пиши нормально"))
        ol1_diff = abs(call - olimpiada1.floor)
        ol2_diff = abs(call - olimpiada2.floor)
        ol3_diff = abs(call - olimpiada3.floor)

        if call == olimpiada1.floor or call == olimpiada2.floor or call == olimpiada3.floor:
            print("on the floor")

        elif ol1_diff < ol2_diff and ol1_diff < ol3_diff:
            move(olimpiada1, call)

        elif ol2_diff < ol1_diff and ol2_diff < ol3_diff:
            move(olimpiada2, call)

        elif ol3_diff < ol1_diff and ol3_diff < ol2_diff:
            move(olimpiada3, call)

        elif ol1_diff == ol2_diff or ol1_diff == ol3_diff:
            move(olimpiada1, call)

        elif ol2_diff == ol3_diff:
            move(olimpiada2, call)

    if enter[0][0].lower() == "п":
        if enter[0][1] == "1":
            move(olimpiada1, int(enter[1]))
        if enter[0][1] == "2":
            move(olimpiada2, int(enter[1]))
        if enter[0][1] == "3":
            move(olimpiada3, int(enter[1]))