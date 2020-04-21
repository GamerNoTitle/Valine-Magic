import requests as r
import os
BQBlist=[]
url= ""
series_name= ''
def imgdl(url, BQBlist):
    for i in range(len(BQBlist)):
        image = r.get(url+BQBlist[i]).content
        try:
            with open('BQB/{}/'.format(series_name) + BQBlist[i], 'wb') as f:
                f.write(image)
        except FileNotFoundError:
            os.makedirs('BQB/'+series_name)
            with open('BQB/{}/'.format(series_name) + BQBlist[i], 'wb') as f:
                f.write(image)
imgdl(url, BQBlist)