import time
s = input("Sec: ") #input veld sec
s = int(s)
m = input("Min:") #input veld min
m = int(m)
h = input("Hour:")#input veld uur
h = int(h) 

while (s < 60): # als seconden kleiner is dan 60 runt hij de print en doet er elke keer 1 bij en de seconden timer wordt gereset
    print ("H:"+str(h) +" "+ "Min:"+ str(m)+" "+ "Sec:" + str(s)) 
    time.sleep(1)
    s=s+1
    if (s == 60): #als s gelijk is aan 60 komt er +1 bij bij de minuut
        m=m+1
        s = 0

    elif(m == 60): #als de minuut gelijk is aan 60 dan komt er +1 uur bij
        h=h+1
        m = 0
        s = 0
    
    elif(h == 24): #als h gelijk is aan 24 reset uren en begint hij helemaal opnieuw
        h = 0