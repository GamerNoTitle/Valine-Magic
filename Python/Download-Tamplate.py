import requests as r
import os
BQBlist=[]
url= ""
prefix=''
def imgdl(url, BQBlist):
    for i in range(len(BQBlist)):
        image = r.get(url+BQBlist[i]).content
        try:
            with open('{}/'.format(prefix) + BQBlist[i], 'wb') as f:
                f.write(image)
        except FileNotFoundError:
            os.makedirs(prefix)
            with open('{}/'.format(prefix) + BQBlist[i], 'wb') as f:
                f.write(image)
imgdl(url, BQBlist)