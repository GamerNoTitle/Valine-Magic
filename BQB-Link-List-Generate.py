import os
remotepath = 'https://valinecdn.bili33.top/'
prefix= ''
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main():
    base = './'
    linklist=[]
    num=1
    print('```json')
    print('{')
    for i in findAllFile(base):
        print('\"{}{}\": \"{}/{}\",'.format(prefix,num,prefix,i))
        num=num+1
    print('}')
    print('```')
    num=1
    for i in findAllFile(base):
        print('![{}{}]({}{}/{})'.format(prefix,num,remotepath,prefix,i))
        num=num+1
if __name__ == '__main__':
    main()