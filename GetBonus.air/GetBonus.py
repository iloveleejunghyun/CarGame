# -*- encoding=utf8 -*-
__author__ = "Administrator"

auto_setup(__file__)
import airtest
from airtest.core.settings import Settings as ST
from util import *
import sys
import os
import logging
logger1=logging.getLogger("airtest")
logger1.setLevel(logging.INFO)
ST.LOG_FILE = "log.txt"
ST.CVSTRATEGY = ['tpl']
ST.THRESHOLD = 0.9
# print(" ", __name__)
# logger=logging.getLogger("airtest")
# def initLog(level=logging.DEBUG,filename="pocoLog.txt"):
#     '''初始化日志配置
#     @param level:设置的日志级别。默认：DEBUG
#     @param filename: 日志文件名。默认：当前目录下的pocoLog.txt，也可为绝对路径名
#     '''
#     logger = logging.getLogger(__name__.split('.')[0])    #日志名为当前包路径project.util.common的
#     logger.setLevel(level)
#     if logger.handlers:
#         for handler in logger.handlers:
#             logger.removeHandler(handler)
#     streamHandler = logging.StreamHandler(sys.stderr) #输出到控制台
#     fileHandler=logging.FileHandler(filename=filename,mode='w',encoding='utf-8',delay=False)
#     LOG_FORMAT1='[%(asctime)s] [%(levelname)s] <%(name)s> (%(lineno)d) %(message)s'  
#     LOG_FORMAT2='[%(asctime)s] [%(levelname)s] <%(name)s> <%(pathname)s]> (%(lineno)d) %(message)s'
#     formatter1 = logging.Formatter(
#         fmt=LOG_FORMAT1,
#         datefmt='%Y-%m-%d  %H:%M:%S'
#     )
#     formatter2 = logging.Formatter(
#         fmt=LOG_FORMAT2,
#         datefmt='%Y-%m-%d  %H:%M:%S'
#     )    
#     streamHandler.setFormatter(formatter1)
#     fileHandler.setFormatter(formatter2)
#     logger.addHandler(streamHandler)
#     logger.addHandler(fileHandler)
#     #logger.debug('这里是测试用，initlog的logger的debug日志') 
# def setPocoLog(name):
#     '''设置poco日志配置'''
#     pocoLogDIR= os.path.join(ST.PROJECT_ROOT, 'logDir') #poco日志目录
#     pocoLogFile=os.path.join(pocoLogDIR,'pocoLog.txt')  #poco日志文件名
#     initLog(level=logging.INFO,filename=pocoLogFile)    #poco日志初始化
#     print(name)
#     logger=logging.getLogger(name)
#     return logger
# logger = setPocoLog(__name__) #日志方法调用

def check_start():

    if not exists(Template(r"tpl1623061463746.png", record_pos=(-0.438, -0.807), resolution=(900, 1600))) and not exists(Template(r"tpl1624884387459.png", record_pos=(-0.442, -0.809), resolution=(900, 1600))):
        while True:
            
            stop_app("com.kairogame.android.Paddock2")
            sleep(5)
            start_app("com.kairogame.android.Paddock2")
            sleep(5)
            if wait_click("重新打开应用",Template(r"tpl1623062470610.png", record_pos=(-0.161, 0.086), resolution=(900, 1600)),1, False):
                keyevent("KEYCODE_HOME")
                continue
            wait_click("公告",Template(r"tpl1624622804412.png", record_pos=(0.013, -0.604), resolution=(900, 1600)),5)

            if not wait_click("登陆",Template(r"tpl1623061904200.png", record_pos=(0.243, 0.313), resolution=(900, 1600)), 5):
                continue

            sleep(20)

            if not wait_click("点击开始",Template(r"tpl1623062004226.png", record_pos=(-0.002, 0.176), resolution=(900, 1600)), 10):
                continue

            break
    return True

def click_dialog():

    wait_click("返回",[Template(r"tpl1624801775279.png", record_pos=(0.074, -0.559), resolution=(900, 1600)),Template(r"tpl1623756901348.png", record_pos=(0.003, 0.134), resolution=(900, 1600)),Template(r"tpl1624465507828.png", record_pos=(0.297, -0.183), resolution=(900, 1600)),Template(r"yes.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"tpl1623020125057.png", record_pos=(-0.009, 0.079), resolution=(900, 1600)),Template(r"tpl1623019985426.png", record_pos=(0.0, -0.06), resolution=(900, 1600)),Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)), Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)),Template(r"tpl1623368961771.png", record_pos=(0.372, 0.157), resolution=(900, 1600)),Template(r"tpl1623368752644.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"back1.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"tpl1625319122618.png", record_pos=(0.371, 0.483), resolution=(900, 1600))], 3)





def getBonus():
    click_dialog()
    wait_click("菜单",Template(r"tpl1622984917583.png", record_pos=(0.371, 0.618), resolution=(900, 1600)), 3)
    
    if exists(Template(r"tpl1623147781059.png", record_pos=(0.291, 0.178), resolution=(900, 1600))):

        wait_click("免费广告",Template(r"tpl1623147781059.png", record_pos=(0.291, 0.178), resolution=(900, 1600)), 3, False)
        count = 0

        while not exists(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))) and count < 12: 
#             keyevent("KEYCODE_BACK")
            count += 1
            sleep(10)

            
        if not wait_click("广告退出",[Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))], 3):
            logger.info("can't find close advertisement")
            touch((71,62))
            logger.info(f"touch (71,62)")
        wait_click("安装退出",[Template(r"tpl1623229848480.png", record_pos=(0.267, 0.811), resolution=(900, 1600)),Template(r"exit2.png", resolution=(900, 1600))], 3)
        sleep(5)
        wait_click("广告退出",Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600)), 1)
        click_dialog()
        for i in range(0):
            sleep(60)
            logger.info(f"waited for {i+1} minutes")
        return True
    else:
        return False
        
def swipe_to_collect():
    for  _ in range(6):
        swipe((100,900),(900,100))
        sleep(1)
    for  _ in range(2):
        swipe((900,250),(250,900))
        sleep(1)
    swipe((900,900),(250,450))
    sleep(1)
    
def collect_assets():
    click_dialog()
    click_dialog()
    swipe_to_collect()
    wait_click("氮氧",Template(r"tpl1623066268636.png", record_pos=(-0.059, -0.658), resolution=(900, 1600)), 1, False)
    wait_click("钱",Template(r"tpl1623066281804.png", record_pos=(0.07, -0.593), resolution=(900, 1600)), 1, False)
    wait_click("油",Template(r"tpl1623066294618.png", record_pos=(0.194, -0.532), resolution=(900, 1600)), 1, False)
    wait_click("研究点",Template(r"tpl1623066308919.png", record_pos=(0.32, -0.468), resolution=(900, 1600)), 1, False)

def game():
    click_dialog()
    if not wait_click("比赛",Template(r"tpl1623754023851.png", record_pos=(-0.339, 0.486), resolution=(900, 1600)),3):
        return False
    if wait_click("主任",Template(r"tpl1624804733428.png", record_pos=(-0.287, -0.313), resolution=(900, 1600)), 1):
        wait_click("一决高下",Template(r"tpl1624804788104.png", record_pos=(-0.004, -0.176), resolution=(900, 1600)), 1)

    wait_click("北极站",Template(r"tpl1624801296945.png", record_pos=(-0.281, -0.076), resolution=(900, 1600)),3)



    wait_click("参加",Template(r"tpl1623754065964.png", record_pos=(-0.008, 0.206), resolution=(900, 1600)),3)

    wait_click("出发",Template(r"tpl1623754090535.png", record_pos=(0.039, 0.206), resolution=(900, 1600)),3)

    
    if not wait_click("官方预选赛",Template(r"tpl1623754161078.png", record_pos=(0.119, -0.373), resolution=(900, 1600)),10):
        logger.info("没有燃料了，可能")
        wait_click("返回",Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)), 5)
        return

    wait_click("行驶中",Template(r"tpl1623754138933.png", record_pos=(0.086, -0.542), resolution=(900, 1600)),20)
    wait_click("官方预选赛",Template(r"tpl1623754161078.png", record_pos=(0.119, -0.373), resolution=(900, 1600)),3)
    wait_click("公里小时",Template(r"tpl1623756736831.png", record_pos=(-0.171, 0.418), resolution=(900, 1600)), 30)
    wait_click("刹车",Template(r"tpl1623754184288.png", record_pos=(-0.121, 0.532), resolution=(900, 1600)),3)

    

    click_dialog()
    sleep(5)
    click_dialog()
    sleep(5)
    click_dialog()
    sleep(5)
    click_dialog()

def train():
    click_dialog()
    logger.info("移动到训练营")
    swipe_to_collect()
    logger.info("查找训练营")
    if wait_click("训练中",Template(r"tpl1624280293894.png", record_pos=(-0.292, -0.312), resolution=(900, 1600)),2):
        logger.info("正在训练中1")
        click_dialog()
        return
    if not wait_click("空闲训练营",Template(r"tpl1624279237729.png", record_pos=(-0.237, -0.376), resolution=(900, 1600)),2):
        logger.info("没有找到空闲训练营，可能在升级中")
        return
    if wait_click("训练中2",Template(r"tpl1624279887092.png", record_pos=(0.352, -0.158), resolution=(900, 1600)),2):
        logger.info("正在训练中2")
        return


    logger.info("查找教育机械师按钮")
    wait_click("教育机械师",Template(r"tpl1624279261927.png", record_pos=(-0.002, 0.127), resolution=(900, 1600)),1)
    logger.info("滑动bar")
    try:
        swipe(Template(r"tpl1624769917261.png", record_pos=(0.439, -0.279), resolution=(900, 1600)), vector=[-0.0009, 0.1831],duration=1)
    except Exception as e:
        logger.error(e)
        pass

    logger.info("点击训练对象")
#     wait_click("克拉克",[Template(r"tpl1624980904312.png", record_pos=(-0.073, -0.082), resolution=(900, 1600)),Template(r"tpl1624980929855.png", record_pos=(-0.073, -0.077), resolution=(900, 1600))],3)
    wait_click("宋传伟",[Template(r"tpl1625320015868.png", record_pos=(-0.151, -0.154), resolution=(900, 1600)),Template(r"tpl1625320024597.png", record_pos=(-0.152, -0.152), resolution=(900, 1600))],3)




    logger.info("点击开始")
    wait_click("开始",Template(r"tpl1624279688744.png", record_pos=(-0.001, 0.191), resolution=(900, 1600)),3)
    pass

def start_extra():
    import time
    localtime = time.localtime(time.time())

    if not (localtime.tm_hour >= 21):
        logger.info("Can't trade before 21:00")
        return
    import os
    if not os.path.exists("trade.log"):
        logger.info("create trade.log")
        with open("trade.log", 'w'):
            pass
    # 格式化成2016-03-20 11:45:39形式
    date =  time.strftime("%Y-%m-%d", time.localtime()) + '\n'
    with open("trade.log", 'r') as f:
        lines = f.readlines()
        logger.info(lines)
        if len(lines) != 0:
            line = lines[-1]
            
            logger.info(date + ","+line)
            if date == line:
                logger.info("Have traded today")
                return
    logger.info("Start to trade today")
    res = os.system('D: && cd D:\Tiger_Trade\Tiger_Trade2.air && D:\AirtestIDE\AirtestIDE runner D:\Tiger_Trade\Tiger_Trade2.air  --log D:\Tiger_Trade\log')
    logger.info(res)
    with open("trade.log", 'a') as f:
        f.write(date)
    logger.info("Finish trade")
    return
# swipe_to_collect()
# sleep(20)


# sleep(10)
# while True:
#     train()
# dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")
# click_dialog()
# sleep(20)
# start_extra()



while True:
    try:
        dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")
        break
    except Exception as e:
        logger.info(e)
        logger.info("Try to connect the device after 10s")
        sleep(10)
for i in range(1000):
    try:
        start_extra()
        sleep(5)
        check_start()
        sleep(5)
        collect_assets()
        click_dialog()
        train()
        click_dialog()
        game()
#         click_dialog()
#         game()
        for i in range(45):
            if getBonus():
                break
            sleep(10)
    except Exception as e:
        logger.error("error", str(e))
        logger.error("需要重启模拟器")
        os.system("shutdown -r -t 120")
        if type(e) is airtest.core.error.AdbShellError:
            
            pass
        pass
    

