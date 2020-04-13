import time
 
# 获得当前时间时间戳
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

import datetime
 
# 获得当前时间
nowt = datetime.datetime.now()
# 转换为指定的格式
otherStyleTimeT = nowt.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTimeT)