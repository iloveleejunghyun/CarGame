# -*- encoding=utf8 -*-
__author__ = "Administrator"


from airtest.core.api import *
from airtest.core.api import *
from airtest.aircv import *
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.settings import Settings as ST
import logging
logger=logging.getLogger("airtest")


def match_in_predict_area(template,screen=None,rect=None):
    if screen is None:
        screen=G.DEVICE.snapshots()
    if rect is None:
        return template.match_in(screen)
    if not isinstance(rect,(list,tuple)):
        raise Exception("crop a image,rect should be a list")
    else:
        predict_screen=aircv.crop_image(screen,rect)
        focus_pos=template.match_in(predict_screen)
        if not focus_pos:
            return False
        else:
            return focus_pos[0]+rect[0],focus_pos[1]+rect[1]

import time
def mutiple_exists(targets,area=None,threshold=0.80,rgb=False,inti=5):
    if (G.DEVICE.display_info['orientation']%2):
        height=G.DEVICE.display_info['height']
        width=G.DEVICE.display_info['width']
    else:
        height = G.DEVICE.display_info['height']
        width = G.DEVICE.display_info['width']
    
    for i in range(inti):
        fullScreen=G.DEVICE.snapshot()
        for target in targets:
            if target:
                focus_pos=match_in_predict_area(target, fullScreen,area)
#                 print(time.time())
                if focus_pos:
                    ref=targets.index(target)
                    return ref,focus_pos
        sleep(0.2)
    return -1,None

def wait_click(name,temp_list, search_times=1, disapear=True):
    
    if type(temp_list) is not list:
        temp_list = [temp_list]
    res = False
    cur_times = 0
    ref = -1
    while cur_times < search_times:
        cur_times += 1
        ref, pos = mutiple_exists(temp_list)
        
        if ref > -1:
            
            touch(pos)
            logger.info(f"touch {pos}, index = {ref}")
            res = True
            sleep(2)
            if disapear == False:
                return res
        else:
            if res == True: #如果之前找到了就返回。没有找到过就继续找. 这里无法处理多图重复出现之间时间间隔过大的情况
                break
        sleep(1)
    if res:
        logger.info(f"Found {name}")
    else:
        logger.info(f"Didn't find {name}")
    return res