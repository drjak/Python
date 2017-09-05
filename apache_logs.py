import collections
logfile = open("/var/log/nginx/access*", "r")
clean_log=[]

for line in logfile:
	try:
		clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
	except:
		pass

counter = collections.counter(clean_log)

for count in counter.most_common(50):
	print(str(count[1]) + "   " +str(count[0]))

logfile.close()