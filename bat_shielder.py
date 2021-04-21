#!/usr/bin/python
# python script showing battery details 
import subprocess
import notify2
import psutil 
from playsound import playsound

# function returning time in hh:mm:ss 
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return "%d:%02d:%02d" % (hours, minutes, seconds) 

class bat_warn():
    def __init__(self):
        self.warn = False
        # returns a tuple
        self.battery = psutil.sensors_battery() 
    
    def sound_play(self):
        playsound('/usr/lib/slack/resources/flitterbug.mp3')
    
    def prcnt_get(self):
        return self.battery.percent

    def plugged_get(self):
        return self.battery.power_plugged

    def note_show(self, val):
        notify2.init("Battery Warning")
        n = notify2.Notification("Battery has reached {}%, disconnect charger!".format(val), icon="")
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(5000)
        n.show()


inst = bat_warn()

if inst.prcnt_get()>= 80 and \
    inst.plugged_get() == True and \
    inst.warn == False:
    inst.sound_play()
    inst.note_show(80)
    inst.warn = True
else:
    if inst.plugged_get() == True: 
        inst.warn = False

    print("percentage: {:.2f}% plugged: {}".format(inst.prcnt_get(),inst.plugged_get()))
