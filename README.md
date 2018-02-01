练习写一个定期删除服务器日志的Python小程序
# 程序说明
## 1.程序目的
该程序能够定时删除服务器日志文件。可控制的参数有：删除多少天的日志；从多少天前开始删除
## 2.程序实现
该程序用了比较轻的Python语言写的。Python开发环境为3.5。代码写好了之后，封装成.exe的文件放在windows系统的定时任务管理中<br/>
2.1 

    import datetime
    import time
    import os,os.path
    import shutil
    import configparser


    def removefile():
    
        # 获取配置文件
        config = configparser.ConfigParser()
        config.read(os.getcwd()+"\\config.init",encoding='UTF-8')
        URL = config.get("parameter","URL")
        try:
            delaytime = int(config.get("parameter","time"))
        except ValueError:
            print('Please input int time')
        # 获取配置文件信息
        days = int(config.get("parameter","days"))
        fileName = os.listdir(URL)
        for filenames in fileName:
            path = URL + filenames
            try:
                t = os.path.getctime(path)
            except FileNotFoundError:
                print('URl is not right')
            ctime = time.ctime(t)
            # 获取当前时间
            d1 = datetime.datetime.now()
            # 定义要删除的文件离当前距离的天数
            d3 = d1 + datetime.timedelta(days=-delaytime)
            d4 = d1 + datetime.timedelta(days=-(delaytime + days))
            if (time.strptime(ctime, '%a %b %d %H:%M:%S %Y') < d3.timetuple()) and (time.strptime(ctime, '%a %b %d %H:%M:%S %Y') > d4.timetuple()):
                # judging objects is tree or file
                if os.path.isdir(path):
                    shutil.rmtree(path)
                elif os.path.isfile(path):
                    os.remove(path)
                else:
                    print ("it's a special file (socket, FIFO, device file)")
                print(time.strftime("%Y-%m-%d %H:%M:%S")+'删除文件：'+ path)


    def main(h=10, m=33):
    '''h表示设定的小时，m为设定的分钟'''
    while True:
        # 判断是否达到设定时间，例如2:00
        while True:
            now = datetime.datetime.now()
            # 到达设定时间，结束内循环
            if now.hour==h and now.minute==m:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(20)
        # 做正事，一天做一次
        removefile()
    main()


## 3.实现验证
3.1 测试目录下创建测试日志文件<br/>
3.2 执行程序<br/>
3.3 文件删除<br/>
