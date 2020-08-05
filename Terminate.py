#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python
# File name: python terminator
# Description: some process termination
 
import psutil
import os
import signal

# In[2]:

print("----------------------------- show all processes info --------------------------------")
# show processes info
pids = psutil.pids()
#for pid in pids:
#   p = psutil.Process(pid)
##    # get process name according to pid
#   process_name = p.name()
    
#   print("Process name is: %s, pid is: %s" %(process_name, pid))


# In[3]:


print("----------------------------- kill specific process --------------------------------")
# pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    # get process name according to pid
    process_name = p.name()
    # kill process "sleep_test1"
    if 'Battle.net' == process_name:
        print("kill specific process: name(%s)-pid(%s)" %(process_name, pid))
        os.kill(pid, signal.SIGKILL)
    elif 'UUBooster' == process_name:
        print("kill specific process: name(%s)-pid(%s)" %(process_name, pid))
        os.kill(pid, signal.SIGKILL)
    elif 'World of Warcraft' == process_name:
        print("kill specific process: name(%s)-pid(%s)" %(process_name, pid))
        os.kill(pid, signal.SIGKILL)
        
exit(0)

