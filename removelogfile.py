import datetime
import time
import os,os.path
import shutil
import configparser


def removefile():

    config = configparser.ConfigParser()
    config.read(os.getcwd()+"\\config.init",encoding='UTF-8')
    URL = config.get("parameter","URL")
    try:
        delaytime = int(config.get("parameter","time"))
    except ValueError:
        print('Please input int time')
    days = int(config.get("parameter","days"))
    fileName = os.listdir(URL)
    for filenames in fileName:
        path = URL + filenames
        try:
            t = os.path.getctime(path)
        except FileNotFoundError:
            print('URl is not right')
        ctime = time.ctime(t)
        d1 = datetime.datetime.now()
        d3 = d1 + datetime.timedelta(days=-delaytime)
        d4 = d1 + datetime.timedelta(days=-(delaytime + days))
        if (time.strptime(ctime, '%a %b %d %H:%M:%S %Y') < d3.timetuple()) and (time.strptime(ctime, '%a %b %d %H:%M:%S %Y') > d4.timetuple()):
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
            else:
                print ("it's a special file (socket, FIFO, device file)")
            print(time.strftime("%Y-%m-%d %H:%M:%S")+'删除文件：'+ path)



def main(h=15, m=25):
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour==h and now.minute==m:
                break
            time.sleep(20)
        removefile()


main()

