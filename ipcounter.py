#### Requirements ####
# apt-get install python3
####
### Usage ####
# python3 filename pathtoaccesslog limit
####
# Writtern by Reny Ouseph
# Writtern on 16-07-2018
####

import os
import sys
import collections
import requests
import json


arguments = sys.argv

COUNTER = collections.Counter()
EXCLUDES = ('127.0.0.1','::1')

#### Find the IP location #########
def getgeolocation(IP):
    ACCESS_KEY = '6d60636037944d6c20d5795228f46579'
    reply = requests.get('http://api.ipstack.com/{}?access_key={}'.format(IP,ACCESS_KEY))
    cc = reply.json()
    location = cc['country_code']
    return location
####


if len(arguments) == 3:
    logfile = arguments[1]
    limit = int(arguments[2])
    if os.path.exists(logfile):
        with open(logfile) as fh:
            for logline in fh:
                ip = logline.split()[0]
                if ip not in EXCLUDES:
                    COUNTER.update((ip,))
		

        for ip,count in COUNTER.most_common(limit):
            print('{:15}[{}] : {}'.format(ip,getgeolocation(ip),count))
		
    else:
        print()
        print('File {} does not exists'.format(logfile))
        print()


else:
    print()
    print('Usage ipcounter.py  /path/to/access_log  limit')
    print()
