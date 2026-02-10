"""
基础条形竞赛图示例
===============
最简单的使用方式，生成全球GDP排名的动态条形图视频
"""

import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']  # 优先使用微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 获取项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'gdp_data.csv')
output_path = os.path.join(base_dir, 'output', '01_global_gdp_rank_basic.gif')

# 读取数据
# 数据格式：年份为索引，国家为列，GDP为值
df = pd.read_csv(data_path, index_col='Year')

print("数据预览:")
print(df.head())
print(f"\n数据形状: {df.shape}")
print(f"年份范围: {df.index.min()} - {df.index.max()}")

# 生成动态条形图视频（使用 GIF 格式，不需要 ffmpeg）
bcr.bar_chart_race(
    df=df,
    filename=output_path,
    title='1973-2018 全球GDP排名（亿美元）',
    cmap='dark12',           # 配色方案
    period_length=800,       # 每年动画时长（毫秒）
    sort='desc',             # 降序排列
    n_bars=10,               # 显示前10名
    steps_per_period=20,     # 每帧的过渡步数
    figsize=(10, 6),         # 图像大小
    dpi=144,                 # 分辨率
    title_size=16,           # 标题字体大小
    bar_label_size=11,       # 条形标签字体大小
    tick_label_size=11,      # 刻度标签字体大小
    bar_kwargs={'alpha': 0.9, 'ec': 'white', 'lw': 1}
)

print(f"\n[OK] 视频已生成: {output_path}")
