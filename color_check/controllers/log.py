from pathlib import Path
from datetime import datetime

def log(message):
	now = datetime.now()
	dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
	
	final_message = '{time} - {msg}'.format(time=dt_string, msg=message) 
	
	print(final_message)

	with open('log.txt', 'a+') as file:
		file.write(final_message + '\n')
