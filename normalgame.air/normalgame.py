# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


sleep(1)
def wait_click(temp_list):
    if type(temp_list) is not list:
        temp_list = [temp_list]
    while True:
        sleep(2)
        find = False
        for temp in temp_list:
            if exists(temp):
                try:
                    touch(temp)
                    find = True
                except:
                    pass
        if find == False:
            return

        
def click_dialog():
    wait_click(Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))
#     wait_click([
#         Template(r"tpl1622891848339.png", record_pos=(0.003, -0.289), resolution=(900, 1600)),
#         Template(r"tpl1622892205536.png", record_pos=(0.003, -0.377), resolution=(900, 1600)),
#         Template(r"tpl1622892615154.png", record_pos=(0.001, -0.471), resolution=(900, 1600)),
#         Template(r"tpl1622895168465.png", record_pos=(0.007, -0.472), resolution=(900, 1600)),
#         Template(r"tpl1622895310850.png", record_pos=(0.001, -0.473), resolution=(900, 1600))])
    wait_click(Template(r"tpl1622895401210.png", record_pos=(-0.322, 0.137), resolution=(900, 1600)))

click_dialog()

touch(Template(r"tpl1622889807636.png", record_pos=(-0.364, 0.629), resolution=(900, 1600)))
touch(Template(r"tpl1622901079070.png", record_pos=(-0.236, -0.257), resolution=(900, 1600)))


touch(Template(r"tpl1622889815641.png", record_pos=(0.01, 0.267), resolution=(900, 1600)))
if not exists(Template(r"tpl1622889819146.png", record_pos=(0.01, 0.127), resolution=(900, 1600))):
    click_dialog()

touch(Template(r"tpl1622889819146.png", record_pos=(0.01, 0.127), resolution=(900, 1600)))
touch(Template(r"tpl1622889825567.png", record_pos=(-0.077, 0.259), resolution=(900, 1600)))
sleep(10)

wait_click(Template(r"tpl1622889851911.png", record_pos=(0.082, -0.447), resolution=(900, 1600)))
# while exists(Template(r"tpl1622889851911.png", record_pos=(0.082, -0.447), resolution=(900, 1600))):
#     touch(Template(r"tpl1622889851911.png", record_pos=(0.082, -0.447), resolution=(900, 1600)))
#     except:
#         pass
    
wait_click(Template(r"tpl1622889864952.png", record_pos=(-0.204, 0.192), resolution=(900, 1600)))
# while exists(Template(r"tpl1622889864952.png", record_pos=(-0.204, 0.192), resolution=(900, 1600))):
#     touch(Template(r"tpl1622889864952.png", record_pos=(-0.204, 0.192), resolution=(900, 1600)))
#     except:
#         pass


sleep(10)

while exists(Template(r"tpl1622890543725.png", record_pos=(-0.359, 0.692), resolution=(900, 1600))):
    if exists(Template(r"tpl1622894075842.png", record_pos=(0.354, 0.634), resolution=(900, 1600))):
        try:
            touch(Template(r"tpl1622894075842.png", record_pos=(0.354, 0.634), resolution=(900, 1600)))
        except:
            pass

    sleep(5)

wait_click(Template(r"tpl1622889964581.png", record_pos=(0.114, -0.304), resolution=(900, 1600)))
# while exists(Template(r"tpl1622889964581.png", record_pos=(0.114, -0.304), resolution=(900, 1600))):
#     touch(Template(r"tpl1622889964581.png", record_pos=(0.114, -0.304), resolution=(900, 1600)))
#     except:
#         pass

click_dialog()
wait_click(Template(r"tpl1622889968685.png", record_pos=(0.043, -0.304), resolution=(900, 1600)))
# while exists(Template(r"tpl1622889968685.png", record_pos=(0.043, -0.304), resolution=(900, 1600))):
#     touch(Template(r"tpl1622889968685.png", record_pos=(0.043, -0.304), resolution=(900, 1600)))
#     except:
#         pass
wait_click(Template(r"tpl1622889972569.png", record_pos=(0.042, -0.302), resolution=(900, 1600)))
# while exists(Template(r"tpl1622889972569.png", record_pos=(0.042, -0.302), resolution=(900, 1600))):
#     try:
#         touch(Template(r"tpl1622889972569.png", record_pos=(0.042, -0.302), resolution=(900, 1600)))
#     except:
#         pass



click_dialog()
sleep(5)
wait_click(Template(r"tpl1622889994155.png", record_pos=(-0.12, 0.464), resolution=(900, 1600)))
# while exists(Template(r"tpl1622889994155.png", record_pos=(-0.12, 0.464), resolution=(900, 1600))):
#     try:
#         touch(Template(r"tpl1622889994155.png", record_pos=(-0.12, 0.464), resolution=(900, 1600)))
#     except:
#         pass
# click_dialog()
    
