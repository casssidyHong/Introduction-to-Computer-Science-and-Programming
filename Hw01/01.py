#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:39:15 2023

@author: cassidy

题目要求：
词频统计图  选择自己熟悉领域的某一长篇文本进行某一类词的词频分析（也可选科研著作）
将结果可视化，可使用柱状图或词云，也可用课上未讲到的其他图表形式

故事背景：
1. 统计毛语录中不同人名出现的次数 
2. 生成柱状图 
3. 生成词云
"""

import jieba
import jieba.posseg as pseg
               
# 输入文件
txt_file_name = './data/毛语录.txt'
# 输出文件
node_file_name = './output/毛语录-人物词频.csv'

ignore_list = ['乌云','明智','许可', '任凭', '莫斯科', '封锁', '老虎', 
               '黎巴嫩', '阿拉伯', '盼灏', '西风', '英勇', '陆军', '宣言', 
               '友谊', '巴掌', '智慧', '祝词', '明白', '纪律性', '北山愚', 
               '满天飞', '小学生', '须知', '周密', '光荣', '党纲', '归公',
               '鲁莽', '修正', '关怀', '明朗', '菲薄', '德育', '道德',
               '高潮', '井大', '齐备', '道德', '寿辰', '左翼', '孙子',
               '望一望', '红旗',]
               
##--- 准备工作
# 加载用户自定义字典，其中包含人名和词性，确保统计不会遗漏
# 可以先不加载字典，检查识别效果
#jieba.load_userdict('./data/userdict.txt')

# 打开文件，读入文字
txt_file = open(txt_file_name, 'r', encoding='utf-8')
line_list = txt_file.readlines() # 返回列表，每一行（段落）是列表的一个元素
txt_file.close()

##--- 第1步：生成基础数据（一个列表，一个字典）
line_name_list = []  # 每个段落出现的人物列表
name_cnt_dict = {}  # 统计人物出现次数

for line in line_list: # 逐个段落循环处理
    word_gen = pseg.cut(line) # peseg.cut返回分词结果，“生成器”类型
    line_name_list.append([])
    
    for one in word_gen:
        word = one.word
        flag = one.flag
        key = 0
        
        if len(word) <= 1:
            continue
        if len(word) >= 4:
            continue
        for w in word:
            if w == '兵':
                key = 1
        if key == 1:
            continue
        if word in ignore_list:
            continue
        if flag == 'nr': 
            line_name_list[-1].append(word)
            if word in name_cnt_dict.keys():
                name_cnt_dict[word] = name_cnt_dict[word] + 1
            else:
                name_cnt_dict[word] = 1

#print(name_cnt_dict)


node_file = open(node_file_name, 'w') 
# 节点文件，格式：Name,Weight -> 人名,出现次数
node_file.write('Name,Weight\n')
for name,cnt in name_cnt_dict.items(): 
    node_file.write(name + ',' + str(cnt) + '\n')
node_file.close()


import matplotlib
import matplotlib.pyplot as plt
import os
if os.name == "nt": # Windows系统
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
else: # MacOS系统
    plt.rcParams["font.family"] = 'Arial Unicode MS'  
plt.rcParams['axes.unicode_minus'] = False  # 支持负号的正常显示

from pyecharts.charts import WordCloud


src_filename = './output/毛语录-人物词频.csv'

src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()

word_list = []
cnt_list = []

#print(line_list)
del line_list[0] #删除csv文件中的标题行
wordfreq_list = []

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))
    wordfreq_list.append((word_cnt[0],word_cnt[1]))

del wordfreq_list[0]

print('finishing saving names')
print('-'*30)

n = len(cnt_list)
plt.figure(figsize=(30,5))

ax = plt.subplot(111)
plt.title('人物词频统计', fontsize=20) # 图表标题
ax.set_xlabel('人物', fontsize=15)
ax.set_ylabel('出现次数', fontsize=15)
#plt.xticks(fontsize=7)
#為什麼加上第125行改變柱狀圖寬度之後標題跟xylabel就會消失

plt.bar(range(n), cnt_list[0:n])
plt.xticks(range(n), word_list[0:n])
plt.yticks(range(0,max(cnt_list)+100,100))

plt.savefig("./output/毛语录-人物词频.png")
plt.show()

print('finish saving bar chart')
print('-'*30)

cloud = WordCloud()
# 向词云中添加内容，第一个参数可以设为空，第二个参数为元组列表（词和词频）
cloud.add('', wordfreq_list)

# render会生成HTML文件。默认是当前目录render.html，也可以指定文件名参数
out_filename = './output/毛语录-人物词云.html'
cloud.render(out_filename)

print('finish saving name cloud')
print('-'*30)
    
