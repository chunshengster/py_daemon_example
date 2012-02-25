#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2012-2-23

@author: chunsheng
'''
import os
from time import sleep,asctime
from daemon.runner import *

class myDaemon:
    def __init__(self):
         
        self.name = 'myDaemon'
        self.working_directory = '/home/chunsheng/workspace/py_daemon_test/src/py_daemon/'
        self.stdin_path = os.devnull
        self.stdout_path = os.path.join('daemon.log')
        self.stderr_path = os.path.join('daemon.log')
        self.pidfile_path = '/var/run/myDaemon.pid'
        self.pidfile_timeout = 120
        
    def run(self):
        self.myEcho()
        
    def myEcho(self):
        '''
        any service or process as you want
        '''
        while True:
            with open('/tmp/myEcho.log','a') as f:
                try:
                    f.write(asctime())
                    f.flush()
                except Exception:
                    pass
                finally:
                    f.close()
            sleep(5)
    

if __name__ == '__main__':
    mydaemon = myDaemon()
    myRunner = DaemonRunner(mydaemon)
    myRunner.do_action()
        
    
    
    