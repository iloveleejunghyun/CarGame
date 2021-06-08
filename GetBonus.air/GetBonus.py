# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


#只能在未连接模拟器时使用
# dev = connect_device("Android:///")


def check_start():
    dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")
    if not exists(Template(r"tpl1623061463746.png", record_pos=(-0.438, -0.807), resolution=(900, 1600))):
        while True:
            
            stop_app("com.kairogame.android.Paddock2")
            sleep(5)
            start_app("com.kairogame.android.Paddock2")
            sleep(5)
            if wait_click(Template(r"tpl1623062470610.png", record_pos=(-0.161, 0.086), resolution=(900, 1600)),False):
                keyevent("KEYCODE_HOME")
                continue
            count = 0
            while True:
                pos = exists(Template(r"tpl1623061904200.png", record_pos=(0.243, 0.313), resolution=(900, 1600)))
                if pos:
                    touch(pos)
                    break
                count += 1
                if count >= 20:
                    break
                sleep(1)
            if count >= 20:
                continue
                
            sleep(20)
            count = 0
            while True:
                pos = exists(Template(r"tpl1623062004226.png", record_pos=(-0.002, 0.176), resolution=(900, 1600)))
                if pos:
                    touch(pos)
                    break
                
                count += 1
                if count >= 20:
                    break
                sleep(1)
            if count >= 20:
                continue

            break
    return True
       

def wait_click(temp_list, disapear=True):
    if type(temp_list) is not list:
        temp_list = [temp_list]
    for i in range(15):
        find = False
        for temp in temp_list:
            pos =  exists(temp)
            if pos:
                try:
                    touch(pos)
                    find = True
                    sleep(2)
                    if disapear == False:
                        return True
                except:
                    pass
        if find == False:
            return False

        
def click_dialog():
    wait_click(Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))
    wait_click(Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))
    wait_click(Template(r"tpl1623019985426.png", record_pos=(0.0, -0.06), resolution=(900, 1600)))
    wait_click(Template(r"tpl1623020125057.png", record_pos=(-0.009, 0.079), resolution=(900, 1600)))


    wait_click(Template(r"tpl1622895401210.png", record_pos=(-0.322, 0.137), resolution=(900, 1600)))
    


def getBonus():
    click_dialog()
    wait_click(Template(r"tpl1622984917583.png", record_pos=(0.371, 0.618), resolution=(900, 1600)))
    
    if not exists(Template(r"tpl1623063985838.png", record_pos=(0.278, 0.18), resolution=(900, 1600))) and not exists(Template(r"tpl1623064016297.png", record_pos=(0.351, 0.183), resolution=(900, 1600))):
        wait_click(Template(r"tpl1622981912990.png", record_pos=(0.356, 0.154), resolution=(900, 1600)))
        count = 0

        while not exists(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))) and count < 12:
            sleep(10)
            keyevent("KEYCODE_BACK")
            count += 1
        wait_click(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600)))
        for i in range(14):
            sleep(60)
            print(f"waited for {i+1} minutes")
        
def collect_assets():
    click_dialog()
    wait_click(Template(r"tpl1623066268636.png", record_pos=(-0.059, -0.658), resolution=(900, 1600)), False)
    wait_click(Template(r"tpl1623066281804.png", record_pos=(0.07, -0.593), resolution=(900, 1600)), False)
    wait_click(Template(r"tpl1623066294618.png", record_pos=(0.194, -0.532), resolution=(900, 1600)), False)
    wait_click(Template(r"tpl1623066308919.png", record_pos=(0.32, -0.468), resolution=(900, 1600)), False)

# print(wait_click(Template(r"tpl1623062470610.png", record_pos=(-0.161, 0.086), resolution=(900, 1600)),False))
for i in range(1000):
    check_start()
    sleep(5)
    collect_assets()
    getBonus()
    

