from datetime import datetime, timedelta

station_start_from_1_to_16 = {
"pp1" :datetime(2025,10,20,5,30,0),
"pp2" :datetime(2025,10,20,5,32,0),
"pp3" :datetime(2025,10,20,5,35,0),
"pp4" :datetime(2025,10,20,5,37,0),
"pp5" :datetime(2025,10,20,5,39,0),
"pp6" :datetime(2025,10,20,5,42,0),
"pp7" :datetime(2025,10,20,5,44,0),
"pp8" :datetime(2025,10,20,5,46,0),
"pp9" :datetime(2025,10,20,5,49,0),
"pp10":datetime(2025,10,20,5,51,0),
"pp11":datetime(2025,10,20,5,53,0),
"pp12":datetime(2025,10,20,5,57,0),
"pp13":datetime(2025,10,20,5,59,0),
"pp14":datetime(2025,10,20,6,2,0),
"pp15":datetime(2025,10,20,6,5,0),
"pp16":datetime(2025,10,20,6,7,0),
}
station_from_16_to_1 = {
"pp16":datetime(2025,10,20,6,0,0),
"pp15":datetime(2025,10,20,6,2,0),
"pp14":datetime(2025,10,20,6,4,0),
"pp13":datetime(2025,10,20,6,6,0),
"pp12":datetime(2025,10,20,6,8,0),
"pp11":datetime(2025,10,20,6,11,0),
"pp10":datetime(2025,10,20,6,13,0),
"pp9" :datetime(2025,10,20,6,15,0),
"pp8" :datetime(2025,10,20,6,17,0),
"pp7" :datetime(2025,10,20,6,20,0),
"pp6" :datetime(2025,10,20,6,21,0),
"pp5" :datetime(2025,10,20,6,23,0),
"pp4" :datetime(2025,10,20,6,25,0),
"pp3" :datetime(2025,10,20,6,28,0),
"pp2" :datetime(2025,10,20,6,30,0),
"pp1" :datetime(2025,10,20,6,32,0),
}
station_end_from_1_to_16 = {
"pp1" :datetime(2025,10,20,22,56,0),
"pp2" :datetime(2025,10,20,22,58,0),
"pp3" :datetime(2025,10,20,23,1,0),
"pp4" :datetime(2025,10,20,23,3,0),
"pp5" :datetime(2025,10,20,23,5,0),
"pp6" :datetime(2025,10,20,23,7,0),
"pp7" :datetime(2025,10,20,23,9,0),
"pp8" :datetime(2025,10,20,23,12,0),
"pp9" :datetime(2025,10,20,23,14,0),
"pp10":datetime(2025,10,20,23,16,0),
"pp11":datetime(2025,10,20,23,18,0),
"pp12":datetime(2025,10,20,23,21,0),
"pp13":datetime(2025,10,20,23,24,0),
"pp14":datetime(2025,10,20,23,26,0),
"pp15":datetime(2025,10,20,23,29,0),
"pp16":datetime(2025,10,20,23,31,0),
}

station_end_from_16_to_1 = {
"pp16" :datetime(2025,10,20,23,33,0),
"pp15" :datetime(2025,10,20,23,35,0),
"pp14" :datetime(2025,10,20,23,38,0),
"pp13" :datetime(2025,10,20,23,40,0),
"pp12" :datetime(2025,10,20,23,43,0),
"pp11" :datetime(2025,10,20,23,46,0),
"pp10" :datetime(2025,10,20,23,48,0),
"pp9" :datetime(2025,10,20,23,50,0),
"pp8" :datetime(2025,10,20,23,52,0),
"pp7":datetime(2025,10,20,23,55,0),
"pp6":datetime(2025,10,20,23,57,0),
"pp5":datetime(2025,10,20,23,59,0),
"pp4":datetime(2025,10,21,0,1,0),
"pp3":datetime(2025,10,21,0,3,0),
"pp2":datetime(2025,10,21,0,6,0),
"pp1":datetime(2025,10,21,23,8,0),
}

def weekends_time(station):
    ### คำนวณเวลาในช่วงที่รถผ่าน
    new_time_start_from1_to_16 = station_start_from_1_to_16[f"pp{station}"] 
    new_time_end_from1_to_16 = station_end_from_1_to_16[f"pp{station}"]
    time_calculate_from_1_to_16 = new_time_start_from1_to_16 + timedelta(minutes=30)
    print(f"ตารางเวลาของสถานี:pp{station}")
    while time_calculate_from_1_to_16 < new_time_end_from1_to_16:
        print(time_calculate_from_1_to_16.strftime(('%H:%M:%S')))
        time_calculate_from_1_to_16 += timedelta(minutes=9,seconds=30)

    print(f"ขบวนสุดท้ายออกเวลา: {time_calculate_from_1_to_16.strftime(('%H:%M:%S'))}")
        
        
weekends_time(input("where do you want to go?"))