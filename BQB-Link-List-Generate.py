import os
# localpath = 'G:\Code\Valine-Magic\BQB'
remotepath = 'https://bqb1.bili33.top/'
prefix= ''
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    base = './'
    linklist=[]
    num=1
    for i in findAllFile(base):
        linklist.append(prefix + str(num)+ ': \"' + remotepath + prefix+ '/' + i + '\"')
        num=num+1
    print(str(linklist).replace(',\', \'',', ').replace('\', \'',', '))
    # print(linklist)
if __name__ == '__main__':
    main()