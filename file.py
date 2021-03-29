# # 2.现有一个user.csv文件，内容如下：
# name,username,email
# 杨洋,yangy,yangy@sina.com
# 贾子豪,jiazh,jiazh@126.com
# 于飞,yuf,yuf@163.com
# 田宇辰,tianych,tianych@sina.com

import csv

lst = []
lst2=[]
with open('user.csv', mode='r', encoding='utf-8') as f:
    line = f.readline().strip()
    title = line.split(',')
    for line in f:
        dic = {}
        line = line.strip()
        data = line.split(',')
        lst2.append(data)
        for i in range(len(title)):
            dic[title[i]] = data[i]
        lst.append(dic)
print(lst)
# # 1)以字典格式读取csv文件并打印出每个人的名字和电子邮件地址
with open('usercopy.csv', mode='w+', encoding='gbk',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","username","email"])
    for r in lst:
        writer.writerow(r)
# 2)新建usercopy.csv文件，将user.csv文件的内容按照csv文件写入的方式写入进usercopy.csv中。