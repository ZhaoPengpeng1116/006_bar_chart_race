"""
横向与纵向对比
=============
展示不同方向的条形图
"""

import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'gdp_data.csv')

# 读取数据
df = pd.read_csv(data_path, index_col='Year')

# 只选取前5个国家进行对比
top5_countries = ['美国', '中国', '日本', '德国', '英国']
df_top5 = df[top5_countries]

print("横向条形图数据预览:")
print(df_top5.head())

# 横向条形图（默认）
bcr.bar_chart_race(
    df=df_top5,
    filename=os.path.join(base_dir, 'output', '04a_horizontal_bars.gif'),
    title='TOP5 国家GDP排名 - 横向条形图',
    orientation='h',         # 横向
    sort='desc',
    n_bars=5,
    period_length=800,
    figsize=(10, 6),
    dpi=150,
    cmap=['#1f77b4', '#d62728', '#ff7f0e', '#2ca02c', '#9467bd']
)

print("\n[OK] 横向条形图视频已生成: output/04a_horizontal_bars.gif")

# 纵向条形图
bcr.bar_chart_race(
    df=df_top5,
    filename=os.path.join(base_dir, 'output', '04b_vertical_bars.gif'),
    title='TOP5 国家GDP排名 - 纵向条形图',
    orientation='v',         # 纵向
    sort='desc',
    n_bars=5,
    period_length=800,
    figsize=(8, 8),
    dpi=150,
    cmap=['#1f77b4', '#d62728', '#ff7f0e', '#2ca02c', '#9467bd']
)

print("\n[OK] 纵向条形图视频已生成: output/04b_vertical_bars.gif")
