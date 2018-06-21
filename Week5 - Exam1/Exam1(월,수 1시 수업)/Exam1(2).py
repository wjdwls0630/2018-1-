def convert_to_second(hour, minute, second) :
    result=3600*hour+60*minute+second
    return result

import time
a=time.ctime()
print(a)
hour=int(a[11:13])
minute=int(a[14:16])
second=int(a[17:19])

print(convert_to_second(hour,minute,second))
