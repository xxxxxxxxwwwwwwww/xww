#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为商业智能课程的知识点部分添加详细内容
"""

with open('/workspace/courses/business-intelligence.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义要替换的内容
new_module2 = '''
            <div id="module2-warehouse" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-database"></i> 模块2：数据仓库（8学时）
                </h3>
                <div class="grid md:grid-cols-2 gap-6">
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o text-yellow-400"></i> 数据仓库基础概念
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">数据仓库是面向主题的、集成的、相对稳定的、反映历史变化的数据集合，用于支持管理决策。与传统数据库不同，数据仓库专门用于分析和决策支持。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 数据仓库特征</h5>
                        <p class="text-gray-400 text-sm">面向主题（Subject-Oriented）、集成（Integrated）、非易失（Non-Volatile）、时变（Time-Variant）</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">🛠️ 数据仓库架构</h5>
                        <p class="text-gray-400 text-sm">源数据层、数据集成层、数据存储层、数据访问层</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300"># ETL示例
import pandas as pd

# Extract - 抽取数据
raw_data = pd.read_csv('sales.csv')

# Transform - 数据转换
cleaned = raw_data.dropna()
cleaned['date'] = pd.to_datetime(cleaned['date'])
cleaned['year'] = cleaned['date'].dt.year

# Load - 加载到数据仓库
# warehouse.append(cleaned)</pre>
                    </div>
                  </div>
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-calculator text-emerald-400"></i> 维度建模
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">维度建模是数据仓库设计的主要方法，包括星型模型和雪花模型。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2">⭐ 星型模型</h5>
                        <p class="text-gray-400 text-sm mb-2">一个中心事实表 surrounded by 多个维度表，查询简单，性能好。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2">❄️ 雪花模型</h5>
                        <p class="text-gray-400 text-sm mb-2">维度表进一步规范化，节省空间，但查询更复杂。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-2">📋 事实表与维度表</h5>
                        <p class="text-gray-400 text-sm">事实表存储业务度量，维度表描述业务维度</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300">-- 星型模型示例
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    date_key INT,        -- 维度表外键
    product_key INT,     -- 维度表外键
    customer_key INT,    -- 维度表外键
    quantity INT,
    amount DECIMAL(10,2)
);

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    year INT,
    quarter INT,
    month INT
);</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

new_module3 = '''
            <div id="module3-olap" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-line-chart"></i> 模块3：OLAP分析（8学时）
                </h3>
                <div class="grid md:grid-cols-2 gap-6">
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-cube text-yellow-400"></i> OLAP基础概念
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">联机分析处理（OLAP）是一种快速分析多维数据的技术，使分析人员能够从多个角度对数据进行快速、一致地交互访问。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 OLAP vs OLTP</h5>
                        <p class="text-gray-400 text-sm">OLAP面向分析，OLTP面向事务处理。OLAP注重查询性能，OLTP注重数据更新。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 MOLAP vs ROLAP</h5>
                        <p class="text-gray-400 text-sm">MOLAP使用多维数组存储，性能快但占用空间大。ROLAP使用关系表，节省空间但查询较慢。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">💾 数据立方体</h5>
                        <p class="text-gray-400 text-sm">多维数据组织方式，支持快速切片和切块操作</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300">import pandas as pd

# 创建数据透视表
data = {
    'product': ['A', 'B', 'A', 'B'],
    'region': ['华东', '华东', '华南', '华南'],
    'sales': [100, 80, 90, 70]
}
df = pd.DataFrame(data)

# OLAP透视表操作
pivot = df.pivot_table(
    values='sales',
    index='product',
    columns='region',
    aggfunc='sum'
)
print(pivot)</pre>
                    </div>
                  </div>
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-random text-emerald-400"></i> OLAP多维操作
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">OLAP提供了丰富的多维分析操作，支持用户从不同角度观察数据。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2 flex items-center gap-2"><span>⬇️</span> Drill-down（下钻）</h5>
                        <p class="text-gray-400 text-sm mb-2">从汇总数据查看详细数据。例如：从年→季度→月→日</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2 flex items-center gap-2"><span>⬆️</span> Roll-up（上卷）</h5>
                        <p class="text-gray-400 text-sm mb-2">从详细数据汇总。例如：从日→月→季度→年</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-2 flex items-center gap-2"><span>✂️</span> Slice（切片）</h5>
                        <p class="text-gray-400 text-sm mb-2">选择一个维度的特定值。例如：只看2024年的数据</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2 flex items-center gap-2"><span>🔄</span> Dice（切块）</h5>
                        <p class="text-gray-400 text-sm mb-2">选择多个维度的值域。例如：2024年1-6月的华东地区数据</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-purple-400 font-semibold mb-2 flex items-center gap-2"><span>🔃</span> Pivot（旋转）</h5>
                        <p class="text-gray-400 text-sm">改变维度的排列位置，查看不同视角的数据</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

new_module4 = '''
            <div id="module4-visualization" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-bar-chart"></i> 模块4：数据可视化（8学时）
                </h3>
                <div class="grid md:grid-cols-2 gap-6">
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-picture-o text-yellow-400"></i> 常用图表类型
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">不同的数据类型和分析目的需要选择不同的图表类型。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 折线图</h5>
                        <p class="text-gray-400 text-sm">显示数据随时间变化的趋势，适合时间序列数据。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 柱状图</h5>
                        <p class="text-gray-400 text-sm">比较不同类别之间的数值大小。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">🥧 饼图</h5>
                        <p class="text-gray-400 text-sm">显示各部分占总体的比例关系。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2">🗺️ 地图</h5>
                        <p class="text-gray-400 text-sm">地理数据的可视化展示。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-purple-400 font-semibold mb-2">📉 散点图</h5>
                        <p class="text-gray-400 text-sm">展示两个变量之间的相关性。</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300">import matplotlib.pyplot as plt

# 各种图表示例
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 折线图
axes[0, 0].plot([1, 2, 3], [10, 20, 15])
axes[0, 0].set_title('折线图')

# 柱状图
axes[0, 1].bar(['A', 'B', 'C'], [30, 50, 40])
axes[0, 1].set_title('柱状图')

# 饼图
axes[1, 0].pie([30, 50, 20], labels=['A', 'B', 'C'])
axes[1, 0].set_title('饼图')

# 散点图
axes[1, 1].scatter([1, 2, 3], [10, 20, 15])
axes[1, 1].set_title('散点图')

plt.tight_layout()
plt.show()</pre>
                    </div>
                  </div>
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-paint-brush text-emerald-400"></i> 可视化设计原则
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">好的数据可视化应该清晰、准确、美观、易于理解。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">🎯 目标明确</h5>
                        <p class="text-gray-400 text-sm">明确可视化要传达的信息，选择最合适的图表类型。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">🎨 简洁清晰</h5>
                        <p class="text-gray-400 text-sm">避免过度装饰，保持图表简洁明了，去除不必要的元素。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">🔢 选择合适图表</h5>
                        <p class="text-gray-400 text-sm">根据数据类型和分析目的选择图表：比较用柱状图，趋势用折线图，比例用饼图。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-1">🎨 合理配色</h5>
                        <p class="text-gray-400 text-sm">使用对比度高的颜色，避免使用过于花哨的颜色组合。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-purple-400 font-semibold mb-1">📏 恰当标注</h5>
                        <p class="text-gray-400 text-sm">添加清晰的标题、坐标轴标签和图例。</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300"># 良好的可视化设计
plt.figure(figsize=(10, 6))

# 清晰的标题
plt.title('月度销售趋势', fontsize=16, fontweight='bold')

# 坐标轴标签
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额（万元）', fontsize=12)

# 合理的数据点标记
plt.plot(months, sales, marker='o', linewidth=2)

# 添加网格线
plt.grid(True, alpha=0.3, linestyle='--')

# 图例
plt.legend(['实际销售', '预测'], loc='best')

plt.tight_layout()
plt.show()</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

new_module5 = '''
            <div id="module5-tools" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-wrench"></i> 模块5：BI工具（8学时）
                </h3>
                <div class="grid md:grid-cols-2 gap-6">
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-th-large text-yellow-400"></i> 主流BI工具介绍
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">市场上有很多成熟的BI工具，各有特点。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 Tableau</h5>
                        <p class="text-gray-400 text-sm mb-2">全球最受欢迎的数据可视化工具，拖拽式操作，易于使用。</p>
                        <p class="text-gray-500 text-xs">优点：可视化能力强，社区活跃</p>
                        <p class="text-gray-500 text-xs">缺点：价格较高</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 Power BI</h5>
                        <p class="text-gray-400 text-sm mb-2">微软的BI工具，与Office 365无缝集成。</p>
                        <p class="text-gray-500 text-xs">优点：免费版功能强大，与Excel集成好</p>
                        <p class="text-gray-500 text-xs">缺点：处理大数据量时性能一般</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">📉 FineReport</h5>
                        <p class="text-gray-400 text-sm mb-2">帆软出品，国产BI工具，企业级应用。</p>
                        <p class="text-gray-500 text-xs">优点：报表功能强大，本地化服务好</p>
                        <p class="text-gray-500 text-xs">缺点：可视化灵活度一般</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2">🛠️ 其他工具</h5>
                        <p class="text-gray-400 text-sm">QuickBI（阿里云）、永洪BI、FineBI等</p>
                      </div>
                    </div>
                  </div>
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-code text-emerald-400"></i> Python数据分析工具
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">Python拥有丰富的数据分析和可视化库，是数据科学家的首选工具。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">🐼 Pandas</h5>
                        <p class="text-gray-400 text-sm">强大的数据处理和分析库，支持数据清洗、转换、聚合等操作。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📊 Matplotlib</h5>
                        <p class="text-gray-400 text-sm">最基础的Python可视化库，可以创建各种静态图表。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">📈 Seaborn</h5>
                        <p class="text-gray-400 text-sm">基于Matplotlib的高级可视化库，美观的默认样式。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2">🔄 Plotly</h5>
                        <p class="text-gray-400 text-sm">交互式可视化库，支持Web图表。</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300">import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 使用Pandas分析数据
df = pd.read_csv('sales_data.csv')

# 数据统计
print(df.describe())

# 使用Seaborn可视化
sns.barplot(data=df, x='product', y='sales')
plt.title('产品销售对比')
plt.show()</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

new_module6 = '''
            <div id="module6-practice" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-rocket"></i> 模块6：BI实战（8学时）
                </h3>
                <div class="grid md:grid-cols-2 gap-6">
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-tachometer text-yellow-400"></i> KPI设计
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">KPI（关键绩效指标）是衡量业务目标达成程度的重要工具。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2">📈 销售KPI</h5>
                        <p class="text-gray-400 text-sm">销售额、销售增长率、市场占有率、客户数、客单价</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2">💹 财务KPI</h5>
                        <p class="text-gray-400 text-sm">利润率、ROI（投资回报率）、成本费用率、资产周转率</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-2">👥 客户KPI</h5>
                        <p class="text-gray-400 text-sm">客户满意度、客户留存率、客户生命周期价值（CLV）</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2">🏭 运营KPI</h5>
                        <p class="text-gray-400 text-sm">库存周转率、订单完成率、准时交货率</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300"># KPI计算示例
import pandas as pd

df = pd.read_csv('sales_data.csv')

# 计算销售KPI
kpis = {
    '总销售额': df['amount'].sum(),
    '平均客单价': df['amount'].mean(),
    '订单数': len(df),
    '销售增长率': (df['amount'].iloc[-1] - df['amount'].iloc[0]) / df['amount'].iloc[0] * 100
}

for kpi_name, kpi_value in kpis.items():
    print(f"{kpi_name}: {kpi_value:.2f}")</pre>
                    </div>
                  </div>
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-dashboard text-emerald-400"></i> 仪表板设计
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">BI仪表板是数据展示的核心，需要精心设计以提供最佳用户体验。</p>
                    <div class="space-y-3">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">🎯 明确目标用户</h5>
                        <p class="text-gray-400 text-sm">了解谁使用仪表板，不同用户关注不同指标。高管关注宏观数据，运营人员关注详细数据。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📊 选择关键指标</h5>
                        <p class="text-gray-400 text-sm">只显示最重要的指标，避免信息过载。建议每个仪表板不超过10个核心指标。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">🎨 合理布局</h5>
                        <p class="text-gray-400 text-sm">重要信息放在显眼位置（如左上角），使用大小、颜色区分重要性。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-1">🔄 交互设计</h5>
                        <p class="text-gray-400 text-sm">支持筛选、下钻等交互操作，让用户能够深入探索数据。</p>
                      </div>
                    </div>
                    <div class="bg-dark p-3 rounded font-mono text-sm mt-4">
                      <pre class="text-cyan-300"># 仪表板布局示例
fig = plt.figure(figsize=(15, 10))

# KPI卡片区域
ax1 = fig.add_subplot(2, 3, 1)
ax1.text(0.5, 0.5, f'¥{total_sales}万', 
         ha='center', va='center', fontsize=24, fontweight='bold')
ax1.set_title('总销售额')

# 图表区域
ax2 = fig.add_subplot(2, 3, (2, 3))
ax2.plot(dates, sales)
ax2.set_title('销售趋势')

ax3 = fig.add_subplot(2, 3, 4)
ax3.bar(products, sales)
ax3.set_title('产品销售')

ax4 = fig.add_subplot(2, 3, 5)
ax4.pie(regions, labels=regions, autopct='%1.1f%%')
ax4.set_title('区域分布')

ax5 = fig.add_subplot(2, 3, 6)
ax5.axis('off')

plt.tight_layout()
plt.show()</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

# 替换各个模块
content = content.replace(
    '<div id="module2-warehouse" class="knowledge-section hidden">',
    new_module2
)

content = content.replace(
    '<div id="module3-olap" class="knowledge-section hidden">',
    new_module3
)

content = content.replace(
    '<div id="module4-visualization" class="knowledge-section hidden">',
    new_module4
)

content = content.replace(
    '<div id="module5-tools" class="knowledge-section hidden">',
    new_module5
)

content = content.replace(
    '<div id="module6-practice" class="knowledge-section hidden">',
    new_module6
)

with open('/workspace/courses/business-intelligence.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 知识点模块内容已详细补充！")