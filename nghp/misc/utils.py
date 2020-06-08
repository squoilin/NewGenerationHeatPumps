# -*- coding: utf-8 -*-
"""
Useful functions for the Next Generation Heat Pump library

@author: Sylvain Quoilin
"""
import sys,os

class NoStdStreams(object):
    '''
    This class hides the std output of the executed function
    usage:
        with NoStdStreams()
            pass
    '''        
    def __init__(self,stdout = None, stderr = None):
        self.devnull = open(os.devnull,'w')
        self._stdout = stdout or self.devnull or sys.stdout
        self._stderr = stderr or self.devnull or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        self.devnull.close()

