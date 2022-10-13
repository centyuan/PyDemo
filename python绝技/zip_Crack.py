import zipfile
import optparse
from threading import Thread


def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print('+Password='+password+'\n')

    except Exception as e:
        #extractall抛出了一个口令错误异常 忽略继续执行下一个
        pass

def main():
    ##usage 定义的是使用方法，%prog 表示脚本本身，version定义的是脚本名字和版本号
    parser = optparse.OptionParser("usage%prog"+"-f <zipfile> -d <dictionary>")
    #dest 将该用户输入的参数保存到变量zname中，可以通过options.user方式来获取该值
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dictionary file ')
    #options，它是一个对象（optpars.Values），保存有命令行参数值。只要知道命令行参数名，如 zname，就可以访问其对应的值： options.zname
    #args:返回一个位置参数的列表
    options,args = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile,password))
        t.start()
if __name__ == '__main__':
    main()
