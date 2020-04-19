import json as js
import os
path = 'D:\OneDrive - 87ouo,Inc\Github\Picture-repo-v1\img\BQB'
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    base = './'
    linklist=[]
    num=1
    for i in findAllFile(base):
        linklist.append('custom{}: "https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@master/img/BQB/{}",'.format(num,i))
        num=num+1
    print(str(linklist).replace(',\', \'',', '))
    # print(linklist)
if __name__ == '__main__':
    main()