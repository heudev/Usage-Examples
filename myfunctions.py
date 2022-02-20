def GetTime(format=None):
    import datetime, pytz
    if format == None: format = "%d.%m.%Y %H:%M:%S"
    fulltime = datetime.datetime.now(pytz.timezone('Europe/Istanbul'))
    fulltime = fulltime.strftime(format)
    return fulltime

def CalculateTime(Date1, Date2):
    import datetime
    format = "%d.%m.%Y %H:%M:%S"
    d1 = datetime.datetime.strptime(Date1, format)
    d2 = datetime.datetime.strptime(Date2, format)
    daysDiff = (d2-d1)
    return int(daysDiff.total_seconds())

def find_between_two_dates(date1, date2):  # find_between_two_dates("20.02.2022", "27.04.2000")
    import datetime
    dt1 = datetime.datetime.strptime(date1, "%d.%m.%Y")
    dt2 = datetime.datetime.strptime(date2, "%d.%m.%Y")
    result = (dt1 - dt2).days
    return result

def Choice(array:list):
    import random
    return str(random.choice(array))

def RandomNumber(args1:int,args2:int):
    import random
    randomnumber = random.randint(int(args1), int(args2))
    return randomnumber

def TurkishWord(word:str):
    from unicode_tr import unicode_tr
    return unicode_tr(u"{}".format(word))

def speak(text):
    import gtts
    from playsound import playsound #("pip install playsound==1.2.2")
    import os
    tts = gtts.gTTS(text, lang="tr", slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
 
def python_installed_packages():
    import pkg_resources
    installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
    print(installed_packages)

def show_wifi_password():
    import subprocess
    data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
