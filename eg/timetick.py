import time
print('按下回车开始计时，按下 Ctrl + C 停止计时。')

while True:
  input("")
  starttime = time.time()
  print("开始")
  try:
    while True:
      print('当前时间：', round(time.time() - starttime, 2), '秒', end="\r")
  except KeyboardInterrupt:
    print('结束')
    endtime = time.time()
    print('总共的时间为：', round(endtime - starttime, 2), '秒' )