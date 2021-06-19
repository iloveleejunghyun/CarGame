# -*- encoding=utf8 -*-
__author__ = "Administrator"

auto_setup(__file__)
import airtest
from airtest.core.settings import Settings as ST
from util import *
import sys
#只能在未连接模拟器时使用
# dev = connect_device("Android:///")
ST.LOG_FILE = "log.txt"
ST.CVSTRATEGY = ['tpl']
ST.THRESHOLD = 0.9


def check_start():
    if not exists(Template(r"tpl1623061463746.png", record_pos=(-0.438, -0.807), resolution=(900, 1600))):
        while True:
            
            stop_app("com.kairogame.android.Paddock2")
            sleep(5)
            start_app("com.kairogame.android.Paddock2")
            sleep(5)
            if wait_click(Template(r"tpl1623062470610.png", record_pos=(-0.161, 0.086), resolution=(900, 1600)),1, False):
                keyevent("KEYCODE_HOME")
                continue
            if not wait_click(Template(r"tpl1623061904200.png", record_pos=(0.243, 0.313), resolution=(900, 1600)), 10):
                continue

            sleep(20)

            if not wait_click(Template(r"tpl1623062004226.png", record_pos=(-0.002, 0.176), resolution=(900, 1600)), 10):
                continue

            break
    return True
       

def click_dialog():

    wait_click([Template(r"tpl1623756901348.png", record_pos=(0.003, 0.134), resolution=(900, 1600)),Template(r"tpl1623368752644.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"yes.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"tpl1623020125057.png", record_pos=(-0.009, 0.079), resolution=(900, 1600)),Template(r"tpl1623019985426.png", record_pos=(0.0, -0.06), resolution=(900, 1600)),Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)), Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)),Template(r"tpl1623368961771.png", record_pos=(0.372, 0.157), resolution=(900, 1600)),Template(r"tpl1623754255589.png", record_pos=(0.281, -0.371), resolution=(900, 1600))], 3)




def getBonus():
    click_dialog()
    wait_click(Template(r"tpl1622984917583.png", record_pos=(0.371, 0.618), resolution=(900, 1600)), 3)
    
    if exists(Template(r"tpl1623147781059.png", record_pos=(0.291, 0.178), resolution=(900, 1600))):

        wait_click(Template(r"tpl1623147781059.png", record_pos=(0.291, 0.178), resolution=(900, 1600)), 3, False)
        count = 0

        while not exists(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))) and count < 12: 
#             keyevent("KEYCODE_BACK")
            count += 1
            sleep(10)

            
        if not wait_click([Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))], 3):
            sys.stderr.write("can't find close advertisement")
            touch((71,62))
            print(f"touch (71,62)")
        wait_click([Template(r"tpl1623229848480.png", record_pos=(0.267, 0.811), resolution=(900, 1600)),Template(r"exit2.png", resolution=(900, 1600))], 3)
        sleep(5)
        wait_click(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600)), 1)
        click_dialog()
        for i in range(11):
            sleep(60)
            print(f"waited for {i+1} minutes")
        return True
    else:
        return False
        
def swipe_to_collect():
    for  _ in range(4):
        swipe((100,900),(900,100))
    sleep(1)
    for  _ in range(2):
        swipe((900,250),(250,900))
    sleep(1)
    swipe((900,900),(500,500))
    sleep(1)
    
def collect_assets():
    click_dialog()
    click_dialog()
    swipe_to_collect()
    wait_click(Template(r"tpl1623066268636.png", record_pos=(-0.059, -0.658), resolution=(900, 1600)), 1, False)
    wait_click(Template(r"tpl1623066281804.png", record_pos=(0.07, -0.593), resolution=(900, 1600)), 1, False)
    wait_click(Template(r"tpl1623066294618.png", record_pos=(0.194, -0.532), resolution=(900, 1600)), 1, False)
    wait_click(Template(r"tpl1623066308919.png", record_pos=(0.32, -0.468), resolution=(900, 1600)), 1, False)

def game():
    click_dialog()
    if not wait_click(Template(r"tpl1623754023851.png", record_pos=(-0.339, 0.486), resolution=(900, 1600)),3):
        return False
#     wait_click(Template(r"tpl1623754046432.png", record_pos=(-0.237, -0.073), resolution=(900, 1600)),3)
    wait_click(Template(r"tpl1623929291043.png", record_pos=(-0.258, 0.002), resolution=(900, 1600)),3)

    wait_click(Template(r"tpl1623754065964.png", record_pos=(-0.008, 0.206), resolution=(900, 1600)),3)
    wait_click(Template(r"tpl1623754090535.png", record_pos=(0.039, 0.206), resolution=(900, 1600)),3)
    wait_click(Template(r"tpl1623758819964.png", record_pos=(-0.154, -0.054), resolution=(900, 1600)),1)

    wait_click(Template(r"tpl1623754138933.png", record_pos=(0.086, -0.542), resolution=(900, 1600)),20)
    wait_click(Template(r"tpl1623754161078.png", record_pos=(0.119, -0.373), resolution=(900, 1600)),3)
    wait_click(Template(r"tpl1623754184288.png", record_pos=(-0.121, 0.532), resolution=(900, 1600)),30)

    wait_click(Template(r"tpl1623756736831.png", record_pos=(-0.171, 0.418), resolution=(900, 1600)), 3)

    click_dialog()
    sleep(5)
    click_dialog()
    sleep(5)
    click_dialog()
    sleep(5)
    click_dialog()

# wait_click(Template(r"tpl1623756901348.png", record_pos=(0.003, 0.134), resolution=(900, 1600)))
# click_dialog()
# sleep(5)

dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")
for i in range(1000):
    try:
        check_start()
        sleep(5)
        collect_assets()
        game()
        while not getBonus():
            sleep(10)
    except Exception as e:
        print("error", str(e))
        if type(e) is airtest.core.error.AdbShellError:
            sys.stderr.write("需要重启模拟器")
            break
        pass
    

