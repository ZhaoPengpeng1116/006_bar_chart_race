"""
自定义数值格式化
===============
展示不同的数值显示方式
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

# 示例1：以万亿美元为单位显示
df_trillion = df / 10000  # 转换为万亿美元

bcr.bar_chart_race(
    df=df_trillion,
    filename=os.path.join(base_dir, 'output', '06a_trillion_units.gif'),
    title='全球GDP排名（万亿美元）',
    cmap='dark12',
    period_length=1000,
    sort='desc',
    n_bars=10,
    figsize=(10, 6),
    dpi=150,
    bar_texttemplate='${x:.2f}T',  # 显示为 $X.XXT
    tick_template='{x:.1f}T',
)

print("[OK] 万亿美元版本已生成: output/06a_trillion_units.gif")

# 示例2：添加百分比变化
df_pct = df.pct_change().fillna(0) * 100  # 计算年度增长率

# 对于增长率，我们使用绝对值来排名（展示变化最大的）
df_pct_abs = df_pct.abs()

bcr.bar_chart_race(
    df=df_pct_abs,
    filename=os.path.join(base_dir, 'output', '06b_growth_rate.gif'),
    title='GDP增长率波动幅度排名（%）',
    cmap='coolwarm',
    period_length=1000,
    sort='desc',
    n_bars=10,
    figsize=(10, 6),
    dpi=150,
    bar_texttemplate='{x:.1f}%',
    tick_template='{x:.1f}%',
)

print("[OK] 增长率版本已生成: output/06b_growth_rate.gif")

# 示例3：排名变化（而非数值）
df_rank = df.rank(axis=1, ascending=False)

bcr.bar_chart_race(
    df=df_rank,
    filename=os.path.join(base_dir, 'output', '06c_rankings.gif'),
    title='GDP排名位次变化',
    cmap='tab20',
    period_length=1000,
    sort='asc',              # 升序（排名1在最上面）
    n_bars=15,
    figsize=(10, 8),
    dpi=150,
    bar_texttemplate='#{x:.0f}',
    tick_template='#{x:.0f}',
)

print("[OK] 排名变化版本已生成: output/06c_rankings.gif")
