from datetime import time,datetime,timedelta

stations = {
    'pp1': {
        'up': {'start': time(5, 30, 0), 'end': time(22, 56, 0)},
        'down': {'start': time(6, 32, 0), 'end': time(23, 8, 0)}
    },
    'pp2': {
        'up': {'start': time(5, 32, 0), 'end': time(22, 58, 0)},
        'down': {'start': time(6, 30, 0), 'end': time(0, 6, 0)}
    },
    'pp3': {
        'up': {'start': time(5, 35, 0), 'end': time(23, 1, 0)},
        'down': {'start': time(6, 28, 0), 'end': time(0, 3, 0)}
    },
    'pp4': {
        'up': {'start': time(5, 37, 0), 'end': time(23, 3, 0)},
        'down': {'start': time(6, 25, 0), 'end': time(0, 1, 0)}
    },
    'pp5': {
        'up': {'start': time(5, 39, 0), 'end': time(23, 5, 0)},
        'down': {'start': time(6, 23, 0), 'end': time(23, 59, 0)}
    },
    'pp6': {
        'up': {'start': time(5, 42, 0), 'end': time(23, 7, 0)},
        'down': {'start': time(6, 21, 0), 'end': time(23, 57, 0)}
    },
    'pp7': {
        'up': {'start': time(5, 44, 0), 'end': time(23, 9, 0)},
        'down': {'start': time(6, 20, 0), 'end': time(23, 55, 0)}
    },
    'pp8': {
        'up': {'start': time(5, 46, 0), 'end': time(23, 12, 0)},
        'down': {'start': time(6, 17, 0), 'end': time(23, 52, 0)}
    },
    'pp9': {
        'up': {'start': time(5, 49, 0), 'end': time(23, 14, 0)},
        'down': {'start': time(6, 15, 0), 'end': time(23, 50, 0)}
    },
    'pp10': {
        'up': {'start': time(5, 51, 0), 'end': time(23, 16, 0)},
        'down': {'start': time(6, 13, 0), 'end': time(23, 48, 0)}
    },
    'pp11': {
        'up': {'start': time(5, 53, 0), 'end': time(23, 18, 0)},
        'down': {'start': time(6, 11, 0), 'end': time(23, 46, 0)}
    },
    'pp12': {
        'up': {'start': time(5, 57, 0), 'end': time(23, 21, 0)},
        'down': {'start': time(6, 8, 0), 'end': time(23, 43, 0)}
    },
    'pp13': {
        'up': {'start': time(5, 59, 0), 'end': time(23, 24, 0)},
        'down': {'start': time(6, 6, 0), 'end': time(23, 40, 0)}
    },
    'pp14': {
        'up': {'start': time(6, 2, 0), 'end': time(23, 26, 0)},
        'down': {'start': time(6, 4, 0), 'end': time(23, 38, 0)}
    },
    'pp15': {
        'up': {'start': time(6, 5, 0), 'end': time(23, 29, 0)},
        'down': {'start': time(6, 2, 0), 'end': time(23, 35, 0)}
    },
    'pp16': {
        'up': {'start': time(6, 7, 0), 'end': time(23, 31, 0)},
        'down': {'start': time(6, 0, 0), 'end': time(23, 33, 0)}
    }
}
# แสดงเวลาปัจจุบัน
real_time_now = datetime.now()
today = datetime.now().date()  # เอาวันปัจจุบันมาใช้ใน combine()
def weekends_time(station,direction):
     
    ### คำนวณเวลาในช่วงที่รถผ่าน
    if direction =="up":
        new_time_start = datetime.combine(today,stations[f"pp{station}"]['up']['start']) 
        new_time_end = datetime.combine(today,stations[f"pp{station}"]['up']['end'])
        time_calculate = new_time_start + timedelta(minutes=30)
    elif direction =="down":
        new_time_start = datetime.combine(today,stations[f"pp{station}"]['down']['start']) 
        new_time_end = datetime.combine(today,stations[f"pp{station}"]['down']['end'])
        time_calculate = new_time_start + timedelta(minutes=18)
    next_train = []
    print(f"ตารางเวลาของสถานี:pp{station}")
    while time_calculate < new_time_end:
        print(time_calculate.strftime(('%H:%M:%S')))
        time_calculate += timedelta(minutes=9,seconds=30)

        if real_time_now < time_calculate:
            next_train.append(time_calculate.strftime(('%H:%M:%S')))
        
    print(f"ขบวนสุดท้ายออกเวลา: {time_calculate.strftime(('%H:%M:%S'))}")
    print(f"ขบวนถัดไปมา{next_train[0]}")

def station_ask(station,direction):
    #Check station
    if station == "16" and direction =='up':
        print("This is terminal station")
    elif station == "1" and direction =='down':
        print("This is terminal station")
    else:
        return(weekends_time(station,direction))

station_ask(input("where are you now??"),input("which directions?"))