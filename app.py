import requests
import datetime
import json
from plyer import notification
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import time

#Utility functions
def jsonToDict(json_file):
    with open(json_file) as jsonData:
        data = json.load(jsonData)
    return data

def notifyMe(title, text):
    sound="./public/sound.mp3"
    notification.notify(title=title, 
                        message=text,
                        app_name="Cowin notifier",
                        app_icon="public/icon.ico",
                        timeout=10,
                        toast=True)
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()

#parsing json
data=jsonToDict("searchData.json")
tmpData=jsonToDict("public/data.json")

district_id=None
for i in tmpData:
    if i["state_name"].lower()==data["state"].lower() and i["district name"].lower()==data["district"].lower():
        district_id=i["district id"]
        break
        del tmpData

#getting path of desktop for making the centers availability file
try:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
except:
    desktop="./"



#checking for invalid input
if district_id==None:
    notifyMe("No center found!!!", "Please check the entered details.")
    time.sleep(10)
else:
    # print(district_id)
    # welcome to infinite loop
    while(True):
        now=str(datetime.datetime.now().strftime("%d/%m/%Y"))
        msg18=""
        msgSpec=""

        # getting data from cowin and using it
        results=requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={now}",
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        centers=results.json()["centers"]
        for i in centers:
            for k in i["sessions"]:
                if  k["available_capacity"]>0 and data["specificLocality"].lower() in i["address"].lower():
                    if (data["18plus"]=="yes" or data["18plus"]=="true") and k["min_age_limit"]==18:
                        
                        msg18+=f"{i['name']}, Available-{k['available_capacity']}\n"
                            
                    elif k["min_age_limit"]==45:
                        msgSpec+=f"{i['name']}, Available-{k['available_capacity']}\n"
                     

        # notifications  
        if (data["18plus"]=="yes" or data["18plus"]=="true"):
            if len(msg18)>10:
                notifyMe(f'Vaccination slots are available in {data["specificLocality"]} {data["district"]} for 18 +', f"Visit Cowin website. Avaliability at {msg18[:150]}" )
                print("-"*50)
                print(f"AVAILABILITY AT \n"+msg18)
                with open(desktop+"/18plus_slots.txt", "w") as centerFile:
                    centerFile.write(msg18)
                



        elif len(msgSpec)>10:
            notifyMe(f'Vaccination slots are available in {data["specificLocality"]} {data["district"]} for 45 +', f"Visit Cowin website. Avaliability at {msgSpec[:150]}")
            print("-"*50)
            print(f"AVAILABILITY AT \n"+msgSpec)
            with open(desktop+"/45plus_slots.txt", "w") as centerFile:
                    centerFile.write(msgSpec)

        # making the loop sleep for sometime
        time.sleep(int(data["checksInEveryGivenSeconds"]) if len(data["checksInEveryGivenSeconds"])>0 else 600)