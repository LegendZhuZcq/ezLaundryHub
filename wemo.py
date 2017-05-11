import datetime
import time
import ouimeaux
import urllib
import requests

from ouimeaux.environment import Environment

serverurl = "http://128.237.215.125:3000/api/add_schedule_anonymous?"

if __name__ == "__main__":
    print("")
    print("System Initiated, Looking for devices")
    print("---------------")
    env = Environment()
    machines = dict()
    try:
        env.start()
        env.discover(10)
        switches = env.list_switches() # creating dict for switches
        for switch in switches:
            machines[switch] = 0
        print "Found devices in the network",machines

        while True: #start detecting current power"
            env.wait(5)
            for key in machines:
                selectedMachine = env.get_switch(key)
                #mySwitch.toggle()
                machines[key] = selectedMachine.current_power
                # apiURL = "/add_schedule_anonymous?machine_id=%s&curr_power=%d" % (key,selectedMachine.current_power)
                # Test network connection : response = urllib.urlopen("https://www.google.com")
                PARAMS = {'machine_id': key, 'curr_power': selectedMachine.current_power}
                response = requests.post(serverurl, data=PARAMS)
                print response.json()

    except (KeyboardInterrupt, SystemExit):
        print("---------------")
        print("Goodbye!")
        print("---------------")
        # Turn off switch
        #env.get_switch(mySwitch).off()
