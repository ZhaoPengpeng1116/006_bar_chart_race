"""
中文支持版本
===========
解决中文显示问题，使用支持中文的字体
"""

import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'gdp_data.csv')
output_path = os.path.join(base_dir, 'output', '03_global_gdp_rank_chinese.gif')

# 读取数据
df = pd.read_csv(data_path, index_col='Year')

# 生成中文版本的条形竞赛图
bcr.bar_chart_race(
    df=df,
    filename=output_path,
    title='1973-2018 全球GDP排名变化（单位：亿美元）',
    cmap='dark12',
    period_length=1000,
    sort='desc',
    n_bars=10,
    figsize=(12, 7),
    dpi=200,
    title_size=20,
    bar_label_size=12,
    tick_label_size=12,
    steps_per_period=25,
    bar_kwargs={'alpha': 0.9, 'ec': 'white', 'lw': 1},
    period_fmt='{x:.0f}年',  # 年份格式
)

print(f"\n[OK] 视频已生成: {output_path}")
