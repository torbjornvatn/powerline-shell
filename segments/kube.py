from subprocess import Popen, PIPE
from shlex import split

def add_kube_segment(powerline):
    try:
        cmd = "kubectl config view -o=jsonpath={.current-context} | sed -e 's/gke_uc-prox-//g;s/_europe-west1-b_/-/g' | tr -d '\n'"
        output = Popen("%s " % cmd, stdout=PIPE, shell=True).communicate()[0]

    except OSError:
        return
    powerline.append(output, Color.HOSTNAME_FG, Color.HOSTNAME_BG)
