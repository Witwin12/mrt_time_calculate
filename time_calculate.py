from datetime import datetime, timedelta ,time

station_start_from_1_to_16 = {
"pp1" :time(5,30,0),
"pp2" :time(5,32,0),
"pp3" :time(5,35,0),
"pp4" :time(5,37,0),
"pp5" :time(5,39,0),
"pp6" :time(5,42,0),
"pp7" :time(5,44,0),
"pp8" :time(5,46,0),
"pp9" :time(5,49,0),
"pp10":time(5,51,0),
"pp11":time(5,53,0),
"pp12":time(5,57,0),
"pp13":time(5,59,0),
"pp14":time(6,2,0),
"pp15":time(6,5,0),
"pp16":time(6,7,0),
}
station_from_16_to_1 = {
"pp16":time(6,0,0),
"pp15":time(6,2,0),
"pp14":time(6,4,0),
"pp13":time(6,6,0),
"pp12":time(6,8,0),
"pp11":time(6,11,0),
"pp10":time(6,13,0),
"pp9" :time(6,15,0),
"pp8" :time(6,17,0),
"pp7" :time(6,20,0),
"pp6" :time(6,21,0),
"pp5" :time(6,23,0),
"pp4" :time(6,25,0),
"pp3" :time(6,28,0),
"pp2" :time(6,30,0),
"pp1" :time(6,32,0),
}
station_end_from_1_to_16 = {
"pp1" :time(22,56,0),
"pp2" :time(22,58,0),
"pp3" :time(23,1,0),
"pp4" :time(23,3,0),
"pp5" :time(23,5,0),
"pp6" :time(23,7,0),
"pp7" :time(23,9,0),
"pp8" :time(23,12,0),
"pp9" :time(23,14,0),
"pp10":time(23,16,0),
"pp11":time(23,18,0),
"pp12":time(23,21,0),
"pp13":time(23,24,0),
"pp14":time(23,26,0),
"pp15":time(23,29,0),
"pp16":time(23,31,0),
}

station_end_from_16_to_1 = {
"pp16" :time(23,33,0),
"pp15" :time(23,35,0),
"pp14" :time(23,38,0),
"pp13" :time(23,40,0),
"pp12" :time(23,43,0),
"pp11" :time(23,46,0),
"pp10" :time(23,48,0),
"pp9" :time(23,50,0),
"pp8" :time(23,52,0),
"pp7":time(23,55,0),
"pp6":time(23,57,0),
"pp5":time(23,59,0),
"pp4":time(0,1,0),
"pp3":time(0,3,0),
"pp2":time(0,6,0),
"pp1":time(23,8,0),
}
# แสดงเวลาปัจจุบัน
real_time_now = datetime.now()
today = datetime.now().date()  # เอาวันปัจจุบันมาใช้ใน combine()
def weekends_time(station):
    ### คำนวณเวลาในช่วงที่รถผ่าน
    new_time_start_from1_to_16 = datetime.combine(today,station_start_from_1_to_16[f"pp{station}"]) 
    new_time_end_from1_to_16 = datetime.combine(today,station_end_from_1_to_16[f"pp{station}"])
    time_calculate_from_1_to_16 = new_time_start_from1_to_16 + timedelta(minutes=30)
    next_train = []
    print(f"ตารางเวลาของสถานี:pp{station}")
    while time_calculate_from_1_to_16 < new_time_end_from1_to_16:
        print(time_calculate_from_1_to_16.strftime(('%H:%M:%S')))
        time_calculate_from_1_to_16 += timedelta(minutes=9,seconds=30)

        if real_time_now < time_calculate_from_1_to_16:
            next_train.append(time_calculate_from_1_to_16.strftime(('%H:%M:%S')))
        
    print(f"ขบวนสุดท้ายออกเวลา: {time_calculate_from_1_to_16.strftime(('%H:%M:%S'))}")
    print(f"ขบวนถัดไปมา{next_train[0]}")
        
weekends_time(input("where do you want to go?"))