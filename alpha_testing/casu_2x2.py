
from fabric.api import cd, run, settings, parallel

@parallel
def beearena_casu_003():
    with settings(host_string='casu-009', user='assisi'):
        with cd('deploy/beearena/casu-003'):
                run('export PYTHONPATH=/home/assisi/python:$PYTHONPATH; ./blink_and_send.py casu-003.rtc ')
                                  
@parallel
def beearena_casu_002():
    with settings(host_string='casu-009', user='assisi'):
        with cd('deploy/beearena/casu-002'):
                run('export PYTHONPATH=/home/assisi/python:$PYTHONPATH; ./blink_and_send.py casu-002.rtc ')
                                  
@parallel
def beearena_casu_001():
    with settings(host_string='casu-009', user='assisi'):
        with cd('deploy/beearena/casu-001'):
                run('export PYTHONPATH=/home/assisi/python:$PYTHONPATH; ./blink_and_send_seed.py casu-001.rtc ')
                                  
@parallel
def beearena_casu_004():
    with settings(host_string='casu-009', user='assisi'):
        with cd('deploy/beearena/casu-004'):
                run('export PYTHONPATH=/home/assisi/python:$PYTHONPATH; ./blink_and_send.py casu-004.rtc ')
                                  
def all():
    beearena_casu_003()
    beearena_casu_002()
    beearena_casu_001()
    beearena_casu_004()
