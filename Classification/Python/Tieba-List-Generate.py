import os
import requests as r
# 百度贴吧表情包下载
BQBlist=[]
for i in range(34):
    if (i<10):
        bqbid='0'+str(i)
    else:
        bqbid=i
    BQBlist.append('i_f{}.png'.format(bqbid))
print(BQBlist)
url= "https://tb2.bdstatic.com/tb/editor/images/face/"
prefix='Tieba'
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