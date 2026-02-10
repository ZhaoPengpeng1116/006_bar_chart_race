"""
创建你自己的条形竞赛图
=====================
这是一个模板，帮助你使用自己的数据创建视频
"""

import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

def create_bar_chart_race(
    data_path,
    output_path,
    title='Bar Chart Race',
    index_col=0,
    n_bars=10,
    period_length=1000,
    dpi=150
):
    """
    创建条形竞赛图的通用函数
    
    参数:
    ------
    data_path : str
        CSV数据文件路径
        格式要求：第一列为时间索引，其他列为类别
    output_path : str
        输出视频文件路径
    title : str
        视频标题
    index_col : str or int
        作为索引的列名或列号
    n_bars : int
        显示的条形数量
    period_length : int
        每帧持续时间（毫秒）
    dpi : int
        图像分辨率
    """
    
    # 读取数据
    df = pd.read_csv(data_path, index_col=index_col)
    
    print(f"数据加载成功！")
    print(f"数据形状: {df.shape}")
    print(f"时间范围: {df.index.min()} - {df.index.max()}")
    print(f"类别数量: {len(df.columns)}")
    
    # 创建视频
    bcr.bar_chart_race(
        df=df,
        filename=output_path,
        title=title,
        cmap='dark12',
        period_length=period_length,
        sort='desc',
        n_bars=n_bars,
        steps_per_period=25,
        figsize=(12, 7),
        dpi=dpi,
        title_size=18,
        bar_label_size=12,
        tick_label_size=11,
        bar_kwargs={'alpha': 0.9, 'ec': 'white', 'lw': 1}
    )
    
    print(f"\n[OK] 视频已生成: {output_path}")


# 使用示例
if __name__ == "__main__":
    
    # 获取项目根目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 示例1：使用项目自带的GDP数据
    create_bar_chart_race(
        data_path=os.path.join(base_dir, 'data', 'gdp_data.csv'),
        output_path=os.path.join(base_dir, 'output', '07_custom_output.gif'),
        title='我的GDP排名视频',
        n_bars=12,
        period_length=800
    )
    
    # 示例2：如果你有其他数据，取消下面的注释并修改路径
    # create_bar_chart_race(
    #     data_path='your_data.csv',      # 替换为你的数据文件
    #     output_path=os.path.join(base_dir, 'output', 'my_video.gif'),
     #     title='我的自定义条形竞赛图',
    #     index_col='Year',                # 根据你的数据修改
    #     n_bars=8,
    #     period_length=1200
    # )
