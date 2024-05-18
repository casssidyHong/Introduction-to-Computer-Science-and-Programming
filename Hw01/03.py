#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 02:54:09 2023

@author: candy

题目要求：组合图表（自己设定故事背景）
故事背景：
1. 比较去年每个月的花销 (NTD)
2. 分为饮食、交通、总和
"""

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Page, Pie, Timeline
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

food = [4120, 4631, 6172, 5529, 5448, 4764, 6653, 5239, 7640, 7154, 9729, 9767]
transport = [415, 416, 610, 1383, 1896, 949, 1628, 5736, 3369, 889, 2883, 1545]
total = [6490, 10615, 10252, 8658, 10113, 16083, 11638, 15331, 13306, 15218, 19068, 13554]
title = ['伙食费', '交通费']

#line.overlap(bar) 疊加
#line.render()

#--------------------------------------------------------------

x = Faker.choose()
tl = Timeline()
bar = Timeline()
last = Timeline()


## 每次循環生成一張圖
## Practice
for i in range(1, 14):
    
    if(i<13):
        bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
        .add_xaxis(title)
        .add_yaxis("伙食费", [food[i-1], 0], itemstyle_opts=opts.ItemStyleOpts(color="#9ACD32", opacity=1))
        .add_yaxis("交通费", [0, transport[i-1]], itemstyle_opts=opts.ItemStyleOpts(color="#228B22", opacity=1))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} NTD", color="003300")),
                title_opts=opts.TitleOpts(title="{}月花销".format(i),
                subtitle="2022")
            )
        )
        tl.add(bar, "{}月".format(i))
    
    if(i==13):
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
            .add_xaxis(Faker.months)
            .add_yaxis("伙食费", food, itemstyle_opts=opts.ItemStyleOpts(color="#9ACD32", opacity=0.8))
            .add_yaxis("交通费", transport, itemstyle_opts=opts.ItemStyleOpts(color="#228B22", opacity=0.8))
            .extend_axis(
                yaxis=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(formatter="{value} NTD", color="CC3300"),
                    interval=3000
                )
            )
            #.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                #yaxis_opts = opts.AxisOpts(is_show = False),
                title_opts=opts.TitleOpts(title="2022全年花销"),
            )
        )
        line = (
                Line()
                .add_xaxis(Faker.months)
                .add_yaxis("total", total, yaxis_index=1,
                           linestyle_opts=opts.LineStyleOpts(color="#ff7f0e", width=3),
                           itemstyle_opts=opts.ItemStyleOpts(color="#CC3300"))
                #使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用
                .set_series_opts(
                    markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(y=total)]),
                    itemstyle_opts=opts.ItemStyleOpts(opacity=1)
                )
        )
        
        bar.overlap(line)
        tl.add(bar, "综观2022每月花销")


tl.render("./output/2022年每月花销.html")
print("finish")

"""tl_practice.render('./output/2022年每月花銷_tl.html')"""
