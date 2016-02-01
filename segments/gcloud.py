from subprocess import Popen, PIPE
from shlex import split

def add_gcloud_segment(powerline):
    try:
        cmd = "gcloud config list| grep project | tr '=' ' ' | tr -s ' ' ' ' | cut -d' ' -f2 | cut -d'-' -f3 | tr -d '\n'"
        output = Popen('%s' % cmd, stdout=PIPE, shell=True).communicate()[0]

    except OSError:
        return
    powerline.append(output, Color.JOBS_FG, Color.JOBS_BG)
