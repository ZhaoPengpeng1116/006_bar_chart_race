# 🎬 Bar Chart Race 项目

一个使用 Python 的 `bar_chart_race` 库创建动态条形竞赛图的项目。

## 📁 项目结构

```
.
├── data/                   # 数据文件
│   └── gdp_data.csv       # 示例GDP数据（1973-2018）
├── examples/              # 示例代码
│   ├── 01_basic_bar_chart_race.py      # 基础示例
│   ├── 02_advanced_customization.py    # 高级自定义
│   ├── 03_chinese_support.py           # 中文支持
│   ├── 04_horizontal_vs_vertical.py    # 横向纵向对比
│   ├── 05_with_line_chart.py           # 组合图表
│   ├── 06_custom_formatter.py          # 自定义格式化
│   └── 07_create_your_own.py           # 自定义模板
├── output/                # 输出视频文件（运行后生成）
├── requirements.txt       # 依赖包
└── README.md             # 项目说明
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行示例

```bash
# 基础示例
cd examples
python 01_basic_bar_chart_race.py

# 高级自定义
python 02_advanced_customization.py

# 中文支持
python 03_chinese_support.py
```

## 📊 数据格式

数据需要是 CSV 格式，格式如下：

```csv
Year,美国,中国,日本,德国,英国
1973,14286,1386,4312,2633,1898
1974,15428,1442,4731,2874,2095
...
```

- 第一列是**时间索引**（如年份）
- 其他列是**类别**（如国家）
- 数值会用于排序和显示

## 🎨 主要功能

| 示例 | 功能描述 |
|------|----------|
| `01_basic_bar_chart_race.py` | 最简单的入门示例 |
| `02_advanced_customization.py` | 配色、标签、动画速度等高级设置 |
| `03_chinese_support.py` | 中文字体支持配置 |
| `04_horizontal_vs_vertical.py` | 横向/纵向条形图对比 |
| `05_with_line_chart.py` | 条形图+折线图组合 |
| `06_custom_formatter.py` | 数值格式化（万亿美元、百分比等）|
| `07_create_your_own.py` | 自定义数据模板 |

## ⚙️ 核心参数说明

```python
bcr.bar_chart_race(
    df=df,                      # DataFrame数据
    filename='output.mp4',      # 输出文件名
    title='标题',               # 图表标题
    n_bars=10,                  # 显示条形数量
    period_length=1000,         # 每帧时长（毫秒）
    steps_per_period=20,        # 过渡步数（平滑度）
    sort='desc',                # 排序方式：desc/asc
    orientation='h',            # 方向：h横向/v纵向
    bar_color='dark12',         # 配色方案
    figsize=(10, 6),            # 图像尺寸
    dpi=150,                    # 分辨率
)
```

## 🎨 配色方案

内置配色方案：
- `'dark12'` - 深色12色
- `'dark24'` - 深色24色
- `'tab10'` - Tableau 10色
- `'tab20'` - Tableau 20色
- `'Set1'`, `'Set2'`, `'Set3'` - Set配色
- `'Pastel1'`, `'Pastel2'` - 柔和色
- `'coolwarm'` - 冷暖渐变

也可以使用自定义颜色字典：
```python
colors = {'美国': '#1f77b4', '中国': '#d62728', ...}
```

## 📝 使用自己的数据

1. 准备CSV文件，确保格式正确
2. 参考 `07_create_your_own.py` 创建脚本
3. 运行脚本生成视频

```python
import bar_chart_race as bcr
import pandas as pd

# 读取你的数据
df = pd.read_csv('your_data.csv', index_col='Year')

# 生成视频
bcr.bar_chart_race(
    df=df,
    filename='output.mp4',
    title='我的标题',
    n_bars=8,
    period_length=1000
)
```

## 🔧 常见问题

### 1. 视频生成失败

确保已安装 ffmpeg：
```bash
# Windows (使用 chocolatey)
choco install ffmpeg

# Mac
brew install ffmpeg

# Ubuntu
sudo apt-get install ffmpeg
```

### 3. 动画不够平滑

增加 `steps_per_period` 参数：
```python
bcr.bar_chart_race(..., steps_per_period=40)
```

## 📚 参考资料

- [bar_chart_race 官方文档](https://www.dexplo.org/bar_chart_race/)
- [Matplotlib 文档](https://matplotlib.org/)
- [Pandas 文档](https://pandas.pydata.org/)

## 📄 License

Copyright (c) 2024 ZhaoPengpeng1116

本项目采用 [MIT License](LICENSE) 开源许可证。

详见 [LICENSE](LICENSE) 文件了解更多信息。
