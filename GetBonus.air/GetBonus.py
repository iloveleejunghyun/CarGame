# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

# keyevent("KEYCODE_BACK")
# sleep(10)
def wait_click(temp_list):
    if type(temp_list) is not list:
        temp_list = [temp_list]
    while True:
        find = False
        for temp in temp_list:
            pos =  exists(temp)
            if pos:
                try:
                    touch(pos)
                    find = True
                    sleep(2)
                except:
                    pass
        if find == False:
            return

        
def click_dialog():
    wait_click(Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))
    wait_click(Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))

    wait_click(Template(r"tpl1622895401210.png", record_pos=(-0.322, 0.137), resolution=(900, 1600)))

click_dialog()
wait_click(Template(r"tpl1622984917583.png", record_pos=(0.371, 0.618), resolution=(900, 1600)))
wait_click(Template(r"tpl1622981912990.png", record_pos=(0.356, 0.154), resolution=(900, 1600)))
sleep(5)
keyevent("KEYCODE_BACK")
sleep(5)
keyevent("KEYCODE_BACK")
count = 0
while not exists(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))) and count < 12:
    sleep(10)
    count += 1
wait_click(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600)))
sleep(60*15)


