"""
高级自定义条形竞赛图
=================
展示更多自定义选项：配色、标签、注释等
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
output_path = os.path.join(base_dir, 'output', '02_global_gdp_rank_advanced.gif')

# 读取数据
df = pd.read_csv(data_path, index_col='Year')

# 生成高级自定义视频
bcr.bar_chart_race(
    df=df,
    filename=output_path,
    
    # 标题设置
    title='🌍 1973-2018 全球GDP排名变化（亿美元）',
    title_size=18,
    
    # 配色 - 使用内置配色方案
    cmap='dark12',
    
    # 布局
    n_bars=12,               # 显示前12名
    figsize=(12, 7),         # 图像大小
    dpi=200,                 # 分辨率
    
    # 动画参数
    period_length=1000,      # 每年动画时长（毫秒）
    steps_per_period=30,     # 过渡步数（更平滑）
    
    # 排序
    sort='desc',             # 降序排列
    
    # 标签设置
    bar_label_size=12,
    tick_label_size=11,
    
    # 边距
    bar_kwargs={'alpha': 0.9, 'ec': 'white', 'lw': 1.5},
)

print(f"\n[OK] 视频已生成: {output_path}")
