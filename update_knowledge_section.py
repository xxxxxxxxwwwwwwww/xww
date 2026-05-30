#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 business-intelligence.html 的知识点部分
"""

html_file = '/workspace/courses/business-intelligence.html'

# 新的知识点内容
new_knowledge_content = '''          <div class="space-y-8">
            <!-- 模块1：BI概述 -->
            <div id="module1-overview" class="knowledge-section">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-cubes"></i> 模块1：BI概述（8学时）
                </h3>
                
                <div class="grid md:grid-cols-2 gap-6">
                  <!-- BI基础概念 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o text-yellow-400"></i> 商业智能基础概念
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">商业智能（Business Intelligence，BI）是一套完整的解决方案，用于将企业中现有的数据转化为知识，帮助企业做出明智的业务经营决策。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 BI核心要素</h5>
                        <p class="text-gray-400 text-sm">数据整合、数据存储、数据分析、数据展示</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">🎯 BI应用价值</h5>
                        <p class="text-gray-400 text-sm">提高决策质量、优化业务流程、增强竞争优势、提升运营效率</p>
                      </div>
                    </div>
                    
                    <div class="bg-dark p-3 rounded font-mono text-sm">
                      <pre class="text-cyan-300">import pandas as pd
import numpy as np

# 简单的销售数据分析
sales_data = {
    'product': ['产品A', '产品B', '产品C'],
    'sales_q1': [1500, 2000, 1800],
    'sales_q2': [1800, 2200, 2100],
    'sales_q3': [1200, 1800, 2000]
}

df = pd.DataFrame(sales_data)
df['total_sales'] = df['sales_q1'] + df['sales_q2'] + df['sales_q3']
print("季度销售数据:")
print(df)
print("\n总销售额:", df['total_sales'].sum(), "元")</pre>
                    </div>
                  </div>

                  <!-- BI发展历程 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-sitemap text-emerald-400"></i> BI发展历程
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">BI从传统报表系统发展至今经历了多个阶段，从最初的简单报表，到数据仓库，再到现代的自助式BI和智能分析。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2 flex items-center gap-2">
                          <span>📋</span> 传统报表时代
                        </h5>
                        <p class="text-gray-400 text-sm mb-2">早期BI主要是制作和分发固定格式的报表，满足基本信息传递需求。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2 flex items-center gap-2">
                          <span>🛒</span> 数据仓库时代
                        </h5>
                        <p class="text-gray-400 text-sm mb-2">以数据仓库为核心，整合多源数据，提供历史数据分析。</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-2 flex items-center gap-2">
                          <span>🏭</span> 自助式BI时代
                        </h5>
                        <p class="text-gray-400 text-sm mb-2">业务用户可以自己进行数据分析，无需依赖IT部门。</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 模块2：数据仓库 -->
            <div id="module2-warehouse" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-database"></i> 模块2：数据仓库（8学时）
                </h3>
                
                <div class="grid md:grid-cols-2 gap-6">
                  <!-- 数据仓库基础 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o text-yellow-400"></i> 数据仓库基础
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">数据仓库是面向主题的、集成的、相对稳定的、反映历史变化的数据集合，用于支持管理决策。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 数据仓库特征</h5>
                        <p class="text-gray-400 text-sm">面向主题、集成、非易失、时变</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 ETL流程</h5>
                        <p class="text-gray-400 text-sm">Extract抽取、Transform转换、Load加载</p>
                      </div>
                    </div>
                    
                    <div class="bg-dark p-3 rounded font-mono text-sm">
                      <pre class="text-cyan-300">import pandas as pd

# 简单的ETL示例
# Extract（抽取）
raw_data = pd.DataFrame({
    'product': ['A', 'B', 'A', 'C'],
    'sales': [100, 200, 150, 300],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
})

# Transform（转换）
clean_data = raw_data.copy()
clean_data['date'] = pd.to_datetime(clean_data['date'])
clean_data['month'] = clean_data['date'].dt.month

# Load（加载）示例
print("清洗后的数据:")
print(clean_data)</pre>
                    </div>
                  </div>

                  <!-- 维度建模 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-calculator text-emerald-400"></i> 维度建模
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">维度建模是数据仓库设计的主要方法，包括星型模型、雪花模型等。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2">⭐ 星型模型</h5>
                        <p class="text-gray-400 text-sm">一个事实表围绕多个维度表</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2">❄️ 雪花模型</h5>
                        <p class="text-gray-400 text-sm">维度表进一步规范化</p>
                      </div>
                    </div>
                    
                    <div class="bg-dark p-3 rounded font-mono text-sm">
                      <pre class="text-cyan-300">-- 星型模型示例
-- 事实表
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    date_key INT,
    product_key INT,
    quantity INT,
    amount DECIMAL(10,2)
);

-- 维度表
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

            <!-- 模块3：OLAP分析 -->
            <div id="module3-olap" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-line-chart"></i> 模块3：OLAP分析（8学时）
                </h3>
                
                <div class="grid md:grid-cols-2 gap-6">
                  <!-- OLAP基础 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o text-yellow-400"></i> OLAP基础概念
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">联机分析处理（OLAP）是一种快速分析多维数据的技术，支持复杂的分析操作。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 OLAP vs OLTP</h5>
                        <p class="text-gray-400 text-sm">OLAP面向分析，OLTP面向事务</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 MOLAP vs ROLAP</h5>
                        <p class="text-gray-400 text-sm">多维OLAP使用多维数组，关系OLAP使用关系表</p>
                      </div>
                    </div>
                  </div>

                  <!-- OLAP操作 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-cubes text-emerald-400"></i> OLAP多维操作
                    </h4>
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2">⬇️ Drill-down（下钻）</h5>
                        <p class="text-gray-400 text-sm">从汇总数据查看详细数据</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2">⬆️ Roll-up（上卷）</h5>
                        <p class="text-gray-400 text-sm">从详细数据汇总</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-2">✂️ Slice（切片）</h5>
                        <p class="text-gray-400 text-sm">选择一个维度的特定值</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2">🔄 Pivot（旋转）</h5>
                        <p class="text-gray-400 text-sm">改变维度的排列</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 模块4：数据可视化 -->
            <div id="module4-visualization" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-bar-chart"></i> 模块4：数据可视化（8学时）
                </h3>
                
                <div class="grid md:grid-cols-2 gap-6">
                  <!-- 图表类型 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o text-yellow-400"></i> 常用图表类型
                    </h4>
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 折线图</h5>
                        <p class="text-gray-400 text-sm">显示趋势变化</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 柱状图</h5>
                        <p class="text-gray-400 text-sm">比较不同类别</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">🥧 饼图</h5>
                        <p class="text-gray-400 text-sm">显示各部分占比</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-blue-400 font-semibold mb-2">🗺️ 地图</h5>
                        <p class="text-gray-400 text-sm">地理数据可视化</p>
                      </div>
                    </div>
                    
                    <div class="bg-dark p-3 rounded font-mono text-sm">
                      <pre class="text-cyan-300">import matplotlib.pyplot as plt

# 数据可视化示例
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [1500, 2000, 1800, 2200, 2500, 2300]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linewidth=2, color='#06b6d4')
plt.title('月度销售趋势')
plt.xlabel('月份')
plt.ylabel('销售额(元)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()</pre>
                    </div>
                  </div>

                  <!-- 可视化原则 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-check-square-o text-emerald-400"></i> 可视化设计原则
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">好的数据可视化应该清晰、准确、有意义。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">🎯 目标明确</h5>
                        <p class="text-gray-400 text-sm">知道要展示什么信息</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">🎨 简洁清晰</h5>
                        <p class="text-gray-400 text-sm">避免过度装饰</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">🔢 选择合适图表</h5>
                        <p class="text-gray-400 text-sm">根据数据类型选择图表</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 模块5：BI工具 -->
            <div id="module5-tools" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-wrench"></i> 模块5：BI工具（8学时）
                </h3>
                
                <div class="grid md:grid-cols-2 gap-6">
                  <!-- 主流BI工具 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o text-yellow-400"></i> 主流BI工具介绍
                    </h4>
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">📊 Tableau</h5>
                        <p class="text-gray-400 text-sm">强大的可视化工具</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📈 Power BI</h5>
                        <p class="text-gray-400 text-sm">微软的BI工具</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">📉 FineReport</h5>
                        <p class="text-gray-400 text-sm">国产报表工具</p>
                      </div>
                    </div>
                  </div>

                  <!-- Python数据分析 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-code text-emerald-400"></i> Python数据分析
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">使用Python进行数据分析。</p>
                    
                    <div class="bg-dark p-3 rounded font-mono text-sm">
                      <pre class="text-cyan-300">import pandas as pd
import numpy as np

# 数据分析示例
data = pd.DataFrame({
    'product': ['A', 'B', 'A', 'B', 'C'],
    'sales': [100, 200, 150, 250, 300],
    'profit': [20, 40, 30, 50, 60]
})

print("基本统计:")
print(data.groupby('product').sum())</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 模块6：BI实战 -->
            <div id="module6-practice" class="knowledge-section hidden">
              <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                  <i class="fa fa-rocket"></i> 模块6：BI实战（8学时）
                </h3>
                
                <div class="grid md:grid-cols-2 gap-6">
                  <!-- KPI设计 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-tachometer text-yellow-400"></i> KPI设计
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">关键绩效指标（KPI）是衡量业务绩效的重要指标。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-2">📈 销售KPI</h5>
                        <p class="text-gray-400 text-sm">销售额、增长率、客户数</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-2">💹 财务KPI</h5>
                        <p class="text-gray-400 text-sm">利润率、ROI、成本</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-2">👥 客户KPI</h5>
                        <p class="text-gray-400 text-sm">客户满意度、留存率</p>
                      </div>
                    </div>
                  </div>

                  <!-- 仪表板设计 -->
                  <div class="bg-dark p-5 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                      <i class="fa fa-dashboard text-emerald-400"></i> 仪表板设计
                    </h4>
                    <p class="text-gray-300 mb-4 text-sm leading-relaxed">BI仪表板是数据展示的核心。</p>
                    
                    <div class="space-y-3 mb-4">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-emerald-400 font-semibold mb-1">🎯 明确目标用户</h5>
                        <p class="text-gray-400 text-sm">知道谁使用</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-yellow-400 font-semibold mb-1">📊 选择关键指标</h5>
                        <p class="text-gray-400 text-sm">只显示重要信息</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <h5 class="text-pink-400 font-semibold mb-1">🎨 合理布局</h5>
                        <p class="text-gray-400 text-sm">重要信息放显眼位置</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>'''

# 读取文件
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到需要替换的部分
start_marker = '          <div class="space-y-8">'
end_marker = '        </div>\n      </div>'

# 找到替换区域
start_idx = content.find(start_marker)
if start_idx == -1:
    print("找不到起始标记")
    exit(1)

# 找到结束标记，从 start_idx 之后开始找
end_idx = content.find(end_marker, start_idx + len(start_marker))
if end_idx == -1:
    print("找不到结束标记")
    exit(1)

# 加上结束标记的长度
end_idx += len(end_marker)

# 替换内容
new_content = content[:start_idx] + new_knowledge_content + content[end_idx:]

# 写回文件
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("成功更新知识点内容！")
