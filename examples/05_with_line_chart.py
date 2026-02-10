"""
条形图 + 折线图组合
=================
同时展示排名和趋势线
"""

import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'gdp_data.csv')

# 读取数据
df = pd.read_csv(data_path, index_col='Year')

# 选择主要国家
major_countries = ['美国', '中国', '日本', '德国', '英国', '法国', '印度']
df_major = df[major_countries]

fig, axes = plt.subplots(2, 1, figsize=(14, 10), 
                         gridspec_kw={'height_ratios': [2, 1]})

# 上方：条形竞赛图（这里使用静态展示某一年）
year = 2018
data_2018 = df_major.loc[year].sort_values(ascending=True)

ax1 = axes[0]
colors = plt.cm.Set3(np.linspace(0, 1, len(data_2018)))
bars = ax1.barh(data_2018.index, data_2018.values, color=colors, edgecolor='white', linewidth=1.5)
ax1.set_xlabel('GDP (亿美元)', fontsize=12)
ax1.set_title(f'{year}年 主要国家GDP排名', fontsize=16, fontweight='bold')
ax1.set_xlim(0, data_2018.max() * 1.1)

# 添加数值标签
for i, (country, value) in enumerate(data_2018.items()):
    ax1.text(value + data_2018.max() * 0.02, i, f'{value:,.0f}', 
             va='center', fontsize=10)

# 下方：趋势线图
ax2 = axes[1]
for country in major_countries:
    ax2.plot(df.index, df[country], marker='o', markersize=3, 
             label=country, linewidth=2, alpha=0.8)

ax2.set_xlabel('年份', fontsize=12)
ax2.set_ylabel('GDP (亿美元)', fontsize=12)
ax2.set_title('GDP变化趋势 (1973-2018)', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left', ncol=4, fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(df.index.min(), df.index.max())

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'output', '05_combined_chart.png'), dpi=200, bbox_inches='tight')
plt.close()

print("[OK] 组合图表已保存: output/05_combined_chart.png")
print("\n提示: 如需生成动态组合图表，建议分别生成条形图和折线图视频，")
print("     然后使用视频编辑软件进行合成。")
