import time
sec = input("Sec: ")  # input veld sec
sec = int(sec)
mi = input("Min:")  # input veld min
mi = int(mi)
hour = input("Hour:")  # input veld uur
hour = int(hour)


def timer(h, m, s):
    sstr = str(s)
    mstr = str(m)
    hstr = str(h)

    if h < 10:
        hstr = "0" + hstr
        mstr = str(m)
    if m < 10:
        mstr = "0" + mstr
        sstr = str(s)
    if s < 10:
        sstr = "0" + sstr
    tstr = hstr + ":" + mstr + ":" + sstr
    print(tstr)
    return


while(True):
    for h in range(hour, 24):
        hour = 0
        for m in range(mi, 60):
            mi = 0
            for s in range(sec, 60):
                sec = 0
                time.sleep(0.001)
                timer(h, m, s)
