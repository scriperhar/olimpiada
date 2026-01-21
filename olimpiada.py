import time

class Elevator:
    def __init__(self, floor, speed, name, doors_status, doors_open_time):
        self.floor = floor
        self.speed = speed
        self.name = name # A, B, C
        self.doors_status = doors_status # 0 - closed, 1 - opened
        self.doors_open_time = doors_open_time

status = ["  ", "][", "[]"]

def doors(lift):
    print(3 * "\n")
    lift.doors_status = 1
    current(lift.name)
    time.sleep(lift.doors_open_time)
    lift.doors_status = 0
    print(3 * "\n")
    current(lift.name)

def current(elevator_moved):
    print(f"{olimpiada1.name} {olimpiada2.name} {olimpiada3.name}")
    for floor in range(floors, 0, -1):
        # 1
        if elevator_moved == "A" and olimpiada1.doors_status == 1 and olimpiada1.floor == floor:
            ol1_status = 2
        elif olimpiada1.floor == floor:
            ol1_status = 1
        else:
            ol1_status = 0
        # 2
        if elevator_moved == "B" and olimpiada2.doors_status == 1 and olimpiada2.floor == floor:
            ol2_status = 2
        elif floor == olimpiada2.floor:
            ol2_status = 1
        else:
            ol2_status = 0
        # 3
        if elevator_moved == "C" and olimpiada3.doors_status == 1 and olimpiada3.floor == floor:
            ol3_status = 2
        elif floor == olimpiada3.floor:
            ol3_status = 1
        else:
            ol3_status = 0
        print(f"{status[ol1_status]}{status[ol2_status]}{status[ol3_status]} - {floor}")

def move(lift, call_floor):
    if call_floor > lift.floor:
        for i in range(lift.floor, call_floor):
            lift.floor += 1
            print(3 * "\n")
            current(lift.name)
            time.sleep(lift.speed)
    elif call_floor < lift.floor:
        for i in range(lift.floor, call_floor, -1):
            lift.floor -= 1
            print(3 * "\n")
            lift.doors = 1
            current(lift.name)
            time.sleep(lift.speed)

    doors(lift)

olimpiada1 = Elevator(1, 0.2, "A", 0, 1)
olimpiada2 = Elevator(25, 0.2, "B", 0, 1)
olimpiada3 = Elevator(12, 0.2, "C", 0, 1)
floors = 25

current(0)
while True:
    enter = input("Enter: ")
    while enter.count(" ") < 1:
        enter = input("Try again: ")
    enter = enter.split(" ")
    call = int(enter[1])

    if enter[0][0].lower() == "в":
        while call > floors or call < 1:
            enter = input("Try again: ")
            while enter.count(" ") < 1:
                enter = input("Try again: ")
            enter = enter.split(" ")
            call = int(enter[1])

        ol1_diff = abs(call - olimpiada1.floor)
        ol2_diff = abs(call - olimpiada2.floor)
        ol3_diff = abs(call - olimpiada3.floor)

        if call == olimpiada1.floor:
            doors(olimpiada1)

        elif call == olimpiada2.floor:
            doors(olimpiada2)

        elif call == olimpiada3.floor:
            doors(olimpiada3)

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
        while call > floors or call < 1 or int(enter[0][1]) > 3 or int(enter[0][1]) < 1:
            enter = input("Try again: ")
            while enter.count(" ") < 1:
                enter = input("Try again: ")
            enter = enter.split(" ")
            call = int(enter[1])

        if enter[0][1] == "1":
            move(olimpiada1, int(enter[1]))
        if enter[0][1] == "2":
            move(olimpiada2, int(enter[1]))
        if enter[0][1] == "3":
            move(olimpiada3, int(enter[1]))