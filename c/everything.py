#coding:utf-8
import os,time,datetime

start_time=time.time()
print("-------------Start---------------")
sou_num='0' #1开启一直写入文件测试，0关闭
#搜索文件路径
# file_path1=r"C:\Users\grep-yq"
file_path1=r"I:\学习-linux\2018linux新增\4-14-GitLab与Jenkins结合构建持续集成-CI环境"
#搜索文件名
sou_name=r'jenkins.repo'
now_path=os.getcwd()
w_filename=os.path.join(now_path,'every.txt')
print(w_filename)
print ('=' * 50)
Flist=[]
def Filelist(file_path,filelist=[],err_dir=[]):
    if os.path.isfile(file_path) :
        filelist.append(file_path)
    elif os.path.isdir(file_path) :
        for dir1 in os.listdir(file_path):
            new_path = os.path.join(file_path,dir1)
            try:
                Filelist(new_path,filelist)
            except Exception as err:
                err_dir.append(new_path)
                continue
    return filelist,err_dir

def w_file(file_name,content1):
    with open(file_name,'a') as wf:
        for i in content1:
            wf.write(i+'\n')

def r_file(file_name):
    with open(file_name,'r+') as rf:
        Flist=[]
        for i in rf:
            Flist.append(i)
    return Flist

def sou_isexist(Flist,file_name):
    content1 = []
    for i in Flist:
        if file_name in i:
            content1.append(i)
    return content1


if  os.path.exists(w_filename):
    if sou_num == '1' or start_time - os.path.getatime(w_filename) > 3600 or start_time - os.path.getctime(w_filename) > 3600:
        print("----更新文件----")
        print("getatime:",start_time - os.path.getatime(w_filename) )
        os.remove(w_filename)
        TT = Filelist(file_path1)
        Flist = TT[0]
        Dlist = TT[1]
        Flist.insert(0,"搜索目录 : " + file_path1)
        w_file(w_filename,Flist)
        existfile=sou_isexist(Flist,sou_name)
        print(existfile)
    else:
        print("getatime:",start_time - os.path.getatime(w_filename) )
        print("----直接读取存储文件----")
        Flist=r_file(w_filename)
        existfile=sou_isexist(Flist,sou_name)
        print(existfile)
else:
    TT = Filelist(file_path1)
    Flist = TT[0]
    Dlist = TT[1]
    Flist.insert(0, "搜索目录 : " + file_path1)
    w_file(w_filename, Flist)
    existfile = sou_isexist(Flist, sou_name)
    print(existfile)



print("-------------END---------------")
end_time=time.time()
running_time=end_time-start_time
print("running:",running_time)

