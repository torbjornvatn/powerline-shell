import re
import subprocess
import os
from emoji import emojize

#Unicode: U+1F433 (U+D83D U+DC33), UTF-8: F0 9F 90 B3
def get_docker_machine_status(powerline):
    anchor = emojize(" :spouting_whale:  ") 
    dm_status = subprocess.Popen(['docker-machine', 'status', 'default'],
            stdout=subprocess.PIPE).communicate()[0] 
    if dm_status.strip() == 'Running':
        powerline.append(anchor, Color.PATH_FG, Color.HOME_BG)


def add_docker_machine_segment(powerline):
    try:
        get_docker_machine_status(powerline)
    except:
        print ("Unexpected error:", sys.exc_info()[0])
        pass
