import time
import msvcrt

finish=30
f1=10
f2=20
count=0
 
print "Press enter to start!"
raw_input()
s_time=time.time()

while 1:
	key=msvcrt.getch()
	if key=='d':
		count+=1
		print "--> ",
		if count==f1:
			print "Turn down."
			break
	else:
		print "Wrong key!"
		break
if count==f1:
	while 1:
   		key1=msvcrt.getch()
		if key1=='s':
			count+=1
			print "						 "
			print "						|"
			print "						v"
			if count==f2:
				print "						Turn right.",
				break
		else:
			print "Wrong key!"
			break
if count==f2:	
	while 1:
   		key2=msvcrt.getch()
		if key2=='d':
			count+=1
			print "--> ",
			if count==finish:
				break
		else:
			print "Wrong key!"
			break

time_elapsed=time.time()-s_time
print "Game over"
if count==finish:
	print "Time taken: " + str(time_elapsed)
