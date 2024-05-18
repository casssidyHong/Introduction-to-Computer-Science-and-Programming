#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:33:21 2023

@author: candy

题目要求：
中国地图、世界地图（自己设定故事背景）

故事背景：
1. 中国地图 -> 各个省份录取清北人数
2. 挑选几个城市拉线至清北所在省份
3. 世界地图 -> 台湾人喜欢到哪里去读书
4. 找出前20个国家 标记数量

参考资料：
https://shirley.tw/2021y-study-abroad/
https://new.qq.com/rain/a/20210719A0EBFG00
"""

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()
china = Geo()

geo.add_coordinate_json(json_file='./data/world_country.json')
china.add_coordinate_json(json_file='./data/world_country.json')

#----中國地圖----
china.add_schema(maptype="china")
china.add("",
             [("西藏", 30), ("青海", 50), ("北京", 550), ("上海", 220),
              ("天津", 160), ("海南", 50), ("宁夏回族自治区", 70), ("吉林", 160),
              ("四川", 210), ("福建", 190), ("黑龙江", 160), ("內蒙古", 110),
              ("辽宁", 250), ("新疆", 140), ("甘肃", 130), ("浙江", 350),
              ("陕西", 240), ("山西", 210), ("云南", 100), ("江苏", 300),
              ("江西", 180), ("湖北", 310), ("贵州", 140), ("安徽", 230),
              ("广西", 160), ("山东", 300), ("湖南", 330), ("河北", 270),
              ("四川", 320), ("广东", 280), ("河南",400)
             ],
             type_=ChartType.EFFECT_SCATTER
)

china.add("学生来源",
          [("西藏", "北京"), ("青海", "北京"), ("北京", "北京"), ("上海", "北京"),
           ("天津", "北京"), ("海南", "北京"), ("宁夏回族自治区", "北京"), ("吉林", "北京"),
           ("四川", "北京"), ("福建", "北京"), ("黑龙江", "北京"), ("內蒙古", "北京"),
           ("辽宁", "北京")
          ],
          type_= GeoType.LINES,
          effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=3,color="black"),
          linestyle_opts=opts.LineStyleOpts(curve=0.2),
)

        
china.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
china.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=350),
                    title_opts=opts.TitleOpts(title="清北学生来源"))

china.render('./output/清华北大招生人数.html')
print('finish first one')

#----世界地圖----
src_filename = './data/台湾学生出国流向.csv'
src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()

del line_list[0]
word_list = []
cnt_list = []
wordfreq_list = []
word_shift = []

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))
    wordfreq_list.append((word_cnt[0],word_cnt[1]))
    #word_shift.append("Taiwan", word_cnt[0])

'''print(word_list)
print(cnt_list)
print(wordfreq_list)'''
print('-'*20)

#map_data = list(wordfreq_list.items()) 

c = (
    Geo() 
    .add_schema(maptype="world")
    .add("台湾学生出国留学（单位：位）", 
         #map_data,
         wordfreq_list,
         type_=ChartType.SCATTER,
         )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=12000, is_piecewise=True),
        title_opts=opts.TitleOpts(title="留学人数"),
    )
)

c.render("./output/台湾学生出国留学数据地图_geo.html")  
print('finish')

# 绘制流向
'''g = (
     Geo()
     .add("台灣學生出國流向",
         word_shift,
         type_= GeoType.LINES,
         effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                symbol_size=5,color="yellow"),
         linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
)
        
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100),
                    title_opts=opts.TitleOpts(title="學生流向"))

geo.render('./output/學生流向.html')'''
