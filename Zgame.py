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
while 1:
   	key2=msvcrt.getch()
	if key2=='d':
		count+=1
		print "--> ",
		if count==finish:
			break

time_elapsed=time.time()-s_time
print "Game over"
print "Time taken: " + str(time_elapsed)
