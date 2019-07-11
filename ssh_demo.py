import sys
import os

port_number = 22
hostname = '148.79.163.153'
#password = 'linuxpassword123'
username = 'ujo48515'

data = {"username":"ujo48515",
		"hostname":"148.79.163.153",
		"command" : "/opt/ControlRoomApps/OnlineModel/script/run_2BA1 "+
		"002 1 3 0.25 0.25 71.5 5 21 -10 0.237 0.05 -0.05 337 T 3.012 "+
		"-4.719 -4.07 13.316 54.756 -46.099 55.974 20.743 -18.492 5.267 "+
		"-5.527 6.721 8.891 -3.8 9.9 -11.5 5.0 -3.5 -3.5 2.5 T"}

command = "ssh {username}@{hostname} {command}"
os.system(command.format(**data))