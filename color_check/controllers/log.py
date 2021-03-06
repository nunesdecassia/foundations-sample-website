from pathlib import Path
from datetime import datetime

Path("tmp/").mkdir(parents=True, exist_ok=True)

def log(message):
	now = datetime.now()
	dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
	
	final_message = f'{dt_string} - {message}' 
	
	print(final_message)

	with open('tmp/log.txt', 'a+') as file:
		file.write(final_message + '\n')
