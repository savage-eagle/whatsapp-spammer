from time import strftime

def printValues(value, showConsole=True, prefix = ""):
	name_file = 'logs/logs_'

	if prefix != "":
		name_file += prefix + "_"

	end_file = name_file + strftime("%d-%m-%Y") + '.log'
	printValue = "[" + strftime("%d-%m-%Y %H:%M:%S") + "] - " + str(value)
	
	output_file = name_file + strftime("%d-%m-%Y")
	end_file = output_file + ".log"

	if (showConsole):
		print(printValue, flush=True)
	
	with open(end_file, "a", encoding="utf-8") as f:
		f.write(printValue + "\n")
	
	f.close()
	return end_file