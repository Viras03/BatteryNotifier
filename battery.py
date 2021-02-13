import psutil 
from plyer import notification 
import time  

N = 15

while(True):
    battery = psutil.sensors_battery() 
    percent = battery.percent
    plugged_in = battery.power_plugged #check whether charger is plugged in or not 
    if( percent <= N and not plugged_in):    
        notification.notify( 
            title = "Warning. Battery low", 
            message = str(percent) + "% Battery remaining.\nConnect the charger.", 
            timeout = 10 # notification will appear for 10 seconds
        )  
    time.sleep(30) #code will check after every 30 seconds 
