from time import gmtime, strftime
from datetime import datetime, timedelta
from json2html import *

def MakeTwoDigits(something):
	if something < 10:
		ans = "0" + str(something)
	else:
		ans = str(something)
	return ans



if __name__ == "__main__":


	# strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	end = gmtime()
	end = strftime("%m/%d/%Y", end)
	end = datetime.strptime(end, "%m/%d/%Y") #string to date
	start = end - timedelta(days=10) # date - days

	# print(start, end)
	# end = strftime("%Y%m%dT00:00:00Z", end)
	# # dd
	# if end.month < 10:
	# 	yr = "0"+str(end.month)
	# else:
	# 	yr = str(end.month)

	yr = MakeTwoDigits(end.year)
	mo = MakeTwoDigits(end.month)
	dy = MakeTwoDigits(end.day)

	# print(f"{end.month}/{end.day}/{end.year}")
	# print(f"{end.year}{end.month}{end.day}")
	# print(start.month)

	input = {
        "name": "json2html",
        "description": "Converts JSON to HTML tabular representation"
	}
	new_input = json2html.convert(json = input)
	print(new_input)

