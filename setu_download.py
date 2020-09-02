import os,shutil,time,datetime,requests

#API URL
setu_API_Url = "https://img.ijglb.com/api.php?action=mobile"
#setu下载数
setu_num = 100

'''
def mkdir(path):
    # 去除首位空格，并去除尾部 \ 符号
    path=(path.strip()).rstrip("\\")
  
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
  
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

#获取setu文件夹地址setu_path
setu_path = os.getcwd()
#获取现存涩图子文件夹 文件夹名yyyy-mm-dd 的时间
dir_list = os.listdir(setu_path)
exists_setu_dir_name = dir_list[0]
#现存涩图子文件夹完整路径setu_dir
#setu_dir = setu_path + "\\" + exists_setu_dir_name
#获取现存涩图子文件夹名转为时间，格式yyyy-mm-dd
exist_dir_date = time.strptime(exists_setu_dir_name, "%Y-%m-%d")
#获取系统日期sysdate格式yyyy-mm-dd
sysdate = time.localtime(time.time())
#获取时间差
d1 = datetime.datetime(exist_dir_date[0], exist_dir_date[1], exist_dir_date[2])
d2 = datetime.datetime(sysdate[0], sysdate[1], sysdate[2])
diff_days = (d2 - d1).days

#setu库一个月未更新则重新下载，否则不变
if diff_days > 30:
    #删除现存涩图子文件夹
    filepath = os.path.join(setu_path, exists_setu_dir_name)
    shutil.rmtree(filepath,True)
    #获取新涩图子文件夹地址
    new_setu_chil_dir = setu_path + "\\" + str('%04d' % sysdate[0]) + "-" + str('%02d' % sysdate[1]) + "-" + str('%02d' % sysdate[2])
    #print(new_setu_chil_dir)
    mkdir(new_setu_chil_dir)

    #调用GET
    r = requests.get(setu_API_Url)
    with open('picture.jpg', 'wb') as file:
        file.write(r.content)
    
else:
    pass
'''
#循环下载图片
for i in range(1,setu_num + 1):
    #调用GET
    r = requests.get(setu_API_Url)
    jpg_name = str('%03d' % i) + ".jpg"
    with open(jpg_name, 'wb') as file:
        file.write(r.content)
        print(jpg_name + "下载完毕！")