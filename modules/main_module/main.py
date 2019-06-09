import sys
import os
from sub_module1.sub1 import sub_fun1
import sub_module2.sub2

'''
!not os.path, but sys.path which is for python search path
sys.path shall include main project folder/directory via below
export PYTHONPATH=/home/cf/project/dashboard/dashboard/modules/
'''

if __name__ == '__main__':
    sub_fun1()
    sub_module2.sub2.sub_fun2()
    print ('finished')
    print ('sys.path:', sys.path)
    print ('os.path:', os.path)
