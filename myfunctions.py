def GetTime(format=None):
    import datetime, pytz
    if format == None: format = "%d.%m.%Y %H:%M:%S"
    fulltime = datetime.datetime.now(pytz.timezone('Europe/Istanbul'))
    fulltime = fulltime.strftime(format)
    return fulltime

def CalculateTime(Date1, Date2):
    format = "%d.%m.%Y %H:%M:%S"
    d1 = datetime.strptime(Date1, format)
    d2 = datetime.strptime(Date2, format)
    daysDiff = (d2-d1)
    return int(daysDiff.total_seconds())

def Choice(array:list):
    import random
    return str(random.choice(array))

def RandomNumber(args1:int,args2:int):
    import random
    randomnumber = random.randint(int(args1),int(args2))
    return randomnumber

def TurkishWord(word:str):
    from unicode_tr import unicode_tr
    return unicode_tr(u"{}".format(word))
