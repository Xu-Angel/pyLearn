import datetime
def getYesterday():
  today = datetime.date.today()
  oneday = datetime.timedelta(days=1)
  yesterday = today - oneday
  return yesterday
print(getYesterday())

def _getYesterday():
  yesterday = datetime.date.today() + datetime.timedelta(-1)
  return yesterday
print(_getYesterday())