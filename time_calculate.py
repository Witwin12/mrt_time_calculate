from datetime import time,datetime,timedelta

from datetime import time, timedelta

stations = {
    'pp1': {
        'up': {'start': time(5, 30, 0), 'end': time(22, 56, 0)},
        'down': {'start': timedelta(minutes=32), 'end': time(0, 8, 0)}
    },
    'pp2': {
        'up': {'start': timedelta(minutes=2), 'end': time(22, 58, 0)},
        'down': {'start': timedelta(minutes=30), 'end': time(0, 6, 0)}
    },
    'pp3': {
        'up': {'start': timedelta(minutes=5), 'end': time(23, 1, 0)},
        'down': {'start': timedelta(minutes=28), 'end': time(0, 3, 0)}
    },
    'pp4': {
        'up': {'start': timedelta(minutes=7), 'end': time(23, 3, 0)},
        'down': {'start': timedelta(minutes=25), 'end': time(0, 1, 0)}
    },
    'pp5': {
        'up': {'start': timedelta(minutes=9), 'end': time(23, 5, 0)},
        'down': {'start': timedelta(minutes=23), 'end': time(23, 59, 0)}
    },
    'pp6': {
        'up': {'start': timedelta(minutes=12), 'end': time(23, 7, 0)},
        'down': {'start': timedelta(minutes=21), 'end': time(23, 57, 0)}
    },
    'pp7': {
        'up': {'start': timedelta(minutes=14), 'end': time(23, 9, 0)},
        'down': {'start': timedelta(minutes=20), 'end': time(23, 55, 0)}
    },
    'pp8': {
        'up': {'start': timedelta(minutes=16), 'end': time(23, 12, 0)},
        'down': {'start': timedelta(minutes=17), 'end': time(23, 52, 0)}
    },
    'pp9': {
        'up': {'start': timedelta(minutes=19), 'end': time(23, 14, 0)},
        'down': {'start': timedelta(minutes=15), 'end': time(23, 50, 0)}
    },
    'pp10': {
        'up': {'start': timedelta(minutes=21), 'end': time(23, 16, 0)},
        'down': {'start': timedelta(minutes=13), 'end': time(23, 48, 0)}
    },
    'pp11': {
        'up': {'start': timedelta(minutes=23), 'end': time(23, 18, 0)},
        'down': {'start': timedelta(minutes=11), 'end': time(23, 46, 0)}
    },
    'pp12': {
        'up': {'start': timedelta(minutes=27), 'end': time(23, 21, 0)},
        'down': {'start': timedelta(minutes=8), 'end': time(23, 43, 0)}
    },
    'pp13': {
        'up': {'start': timedelta(minutes=29), 'end': time(23, 24, 0)},
        'down': {'start': timedelta(minutes=6), 'end': time(23, 40, 0)}
    },
    'pp14': {
        'up': {'start': timedelta(minutes=32), 'end': time(23, 26, 0)},
        'down': {'start': timedelta(minutes=4), 'end': time(23, 38, 0)}
    },
    'pp15': {
        'up': {'start': timedelta(minutes=35), 'end': time(23, 29, 0)},
        'down': {'start': timedelta(minutes=2), 'end': time(23, 35, 0)}
    },
    'pp16': {
        'up': {'start': timedelta(minutes=37), 'end': time(23, 31, 0)},
        'down': {'start': time(6, 0, 0), 'end': time(23, 33, 0)}
    }
}

# แสดงเวลาปัจจุบัน
real_time_now = datetime.now()
today = datetime.now().date()  # เอาวันปัจจุบันมาใช้ใน combine()
next_train = []
time_first_station = []
def weekends_time(station,direction):
     
    ### คำนวณเวลาสำหรับวันหยุด เสา-อาทิตย์
    if direction =="up":
        time_start = (stations[f"pp{station}"]['up']['start'])

    elif direction =="down":
        time_start = (stations[f"pp{station}"]['down']['start'])

    print(f"ตารางเวลาของสถานี:pp{station}")
    for t in time_first_station:
        t_time = datetime.strptime(t, "%H:%M:%S").time()
        t_datetime = datetime.combine(today, t_time)
        # แล้วบวกกับ new_time_start (ต้องเป็น timedelta)
        new_time = t_datetime + time_start  
        print(new_time.strftime(('%H:%M:%S')))
        check_status_train(new_time)
    print(f"ขบวนสุดท้ายออกเวลา: {new_time.strftime(('%H:%M:%S'))}")
    if next_train == []:
        print("ไม่มีขบวนถัดไป")
    else:
        print(f"ขบวนถัดไปมา{next_train[0]}")

def weekdays_time(station,direction):
    #คำนวณเวลาสำหรับวันทำงาน จันทร์ - ศุกร์
    if direction =="up":
        new_time_start = (stations[f"pp{station}"]['up']['start']) 
    elif direction =="down":
        new_time_start = (stations[f"pp{station}"]['down']['start']) 

    print(f"ตารางเวลาของสถานี:pp{station}")
    for t in time_first_station:
        t_time = datetime.strptime(t, "%H:%M:%S").time()
        t_datetime = datetime.combine(today, t_time)
        # แล้วบวกกับ new_time_start (ต้องเป็น timedelta)
        new_time = t_datetime + new_time_start  
        print(new_time.strftime(('%H:%M:%S')))

        check_status_train(new_time)
    print(f"ขบวนสุดท้ายออกเวลา: {new_time.strftime(('%H:%M:%S'))}")
    if next_train == []:
        print("ไม่มีขบวนถัดไป")
    else:
        print(f"ขบวนถัดไปมา{next_train[0]}")

def check_status_train(time_calculate):
    # check next train alive
    if real_time_now < time_calculate:
        next_train.append(time_calculate.strftime(('%H:%M:%S')))

def station_ask():
    #Check station
    station = input("Where are you live now?")
    direction = input("Which directions you want to go?")
    if (station == "16" and direction =='up') or (station == "1" and direction =='down'):
        print("This is terminal station")
                # คืนค่า list จากฟังก์ชันเวลา (วันธรรมดาหรือวันหยุด)
    elif (station == "16" and direction =='down') or (station == "1" and direction =='up'):
            # คืนค่า list จากฟังก์ชันเวลา (วันธรรมดาหรือวันหยุด)
        if real_time_now.weekday() < 5:
            return first_station_weekdays_time(direction),print(time_first_station)
        else:
            return first_station_weekend_time(direction), print(time_first_station)
    elif real_time_now.weekday() < 5:
        return(first_station_weekdays_time(direction),weekdays_time(station,direction))
    else:
        return(first_station_weekend_time(direction),weekends_time(station,direction))
    
    
def first_station_weekend_time(direction):
    ### คำนวณเวลาสำหรับสถานีแรกวันหยุด เสา-อาทิตย์
    if direction =="up":
        new_time_start = datetime.combine(today,stations["pp1"]['up']['start']) 
        new_time_end = datetime.combine(today,stations["pp1"]['up']['end'])
        time_calculate = new_time_start + timedelta(minutes=30)
    elif direction =="down":
        new_time_start = datetime.combine(today,stations["pp16"]['down']['start']) 
        new_time_end = datetime.combine(today,stations["pp16"]['down']['end'])
        time_calculate = new_time_start + timedelta(minutes=18)

    while time_calculate < new_time_end:
        time_first_station.append(time_calculate.strftime(('%H:%M:%S')))
        time_calculate += timedelta(minutes=9,seconds=30)
    time_first_station.append(time_calculate.strftime(('%H:%M:%S')))

def first_station_weekdays_time(direction):
    #คำนวณเวลาสำหรับวันทำงาน จันทร์ - ศุกร์
    time_in_5am_to_6am = time(6,30,0)
    time_in_6am_to_8am = (time(8,30,0))
    time_in_8am_to_9am = (time(6,30,0))
    time_in_9am_to_5pm = (time(17,0,0))
    time_in_5pm_to_8pm = (time(20,0,0))
    time_in_8pm_to_9pm = (time(21,0,0))
    time_in_9pm_to_0am = (time(23,59,59))
    if direction =="up":
        new_time_start = datetime.combine(today,stations["pp1"]['up']['start']) 
        new_time_end = datetime.combine(today,stations["pp1"]['up']['end'])
    elif direction =="down":
        new_time_start = datetime.combine(today,stations["pp16"]['down']['start']) 
        new_time_end = datetime.combine(today,stations["pp16"]['down']['end'])

    time_first_station.append(new_time_start.strftime(('%H:%M:%S')))#add first time
    while new_time_start < new_time_end:
        if  new_time_start.time() < time_in_5am_to_6am:
            new_time_start += timedelta(minutes=7,seconds=12)
        elif new_time_start.time() < time_in_6am_to_8am:
            new_time_start += timedelta(minutes=4,seconds=50)
        elif new_time_start.time() < time_in_8am_to_9am:
            new_time_start += timedelta(minutes=6, seconds=25)
        elif  new_time_start.time() < time_in_9am_to_5pm:
            new_time_start += timedelta(minutes=8,seconds=30)
        elif  new_time_start.time() <  time_in_5pm_to_8pm:
            new_time_start += timedelta(minutes=4,seconds=50)
        elif new_time_start.time() < time_in_8pm_to_9pm:
            new_time_start += timedelta(minutes=6, seconds=25)
        elif new_time_start.time() < time_in_9pm_to_0am:
            new_time_start += timedelta(minutes=9, seconds=30)
        time_first_station.append(new_time_start.strftime(('%H:%M:%S')))

       
station_ask()


