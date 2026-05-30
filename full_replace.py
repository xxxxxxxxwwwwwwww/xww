#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完整替换商务智能课程的内容"""
import re

def main():
    # 读取原始文件
    with open('/workspace/courses/supply-chain-analysis.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 修改页面标题
    html_content = html_content.replace('<title>供应链分析题库</title>', '<title>商务智能分析题库</title>')
    
    # 修改顶部标题
    html_content = html_content.replace('供应链分析', '商务智能分析')
    
    # 替换左侧章节标题
    html_content = html_content.replace('供应链概述', 'BI基础与SQL')
    html_content = html_content.replace('需求预测', '数据分析思维')
    html_content = html_content.replace('库存管理', 'SQL高级应用')
    html_content = html_content.replace('物流优化', '商务分析模型')
    html_content = html_content.replace('供应商管理', '综合应用与工具')
    html_content = html_content.replace('供应链风险与优化', '综合应用')
    
    # 删除章节6的HTML内容
    # 先找到章节5和章节6的部分
    chapter5_start = html_content.find('<!-- 章节5：综合应用与工具 -->')
    chapter6_start = html_content.find('<!-- 章节6：综合应用 -->', chapter5_start) if chapter5_start != -1 else -1
    
    if chapter5_start != -1 and chapter6_start != -1:
        # 找到章节6结束位置
        chapter6_end = html_content.find('</div>', chapter6_start)
        # 向后查找，找到章节结束的位置
        count = 0
        pos = chapter6_end
        while count < 3 and pos != -1:
            pos = html_content.find('</div>', pos + 6)
            if pos != -1:
                count += 1
        if pos != -1:
            # 删除章节6
            html_content = html_content[:chapter6_start] + html_content[pos:]
    
    # 替换JavaScript中的问题数据
    # 首先找到problems数组开始
    problems_start = html_content.find('const problems = [')
    if problems_start == -1:
        print("Error: problems array not found")
        return
    
    # 找到problems数组结束
    bracket_count = 1
    pos = problems_start + len('const problems = [')
    while bracket_count > 0 and pos < len(html_content):
        if html_content[pos] == '[':
            bracket_count += 1
        elif html_content[pos] == ']':
            bracket_count -= 1
        pos += 1
    problems_end = pos
    
    # 替换problems数组
    new_problems = '''const problems = [
      {
        id: 1,
        title: "问题1：SQL查询：各地区销售额",
        description: `编写SQL查询，统计各地区的总销售额。
<strong>输入：</strong>
sales表：包含region, amount, date字段
<strong>输出：</strong>
各地区的销售总额，按销售额降序排列
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>使用GROUP BY按地区分组</li>
  <li>计算每个地区的总销售额</li>
  <li>使用ORDER BY按销售额降序排序</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `-- 请编写SQL代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用GROUP BY按region分组</p>
<p>2. 使用SUM函数计算总销售额</p>
<p>3. 使用ORDER BY按销售额降序排列</p>
<h4>SQL示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('sql-basics')">SQL基础</a></li>
  <li>GROUP BY分组</li>
  <li>聚合函数SUM</li>
</ul>`
      },
      {
        id: 2,
        title: "问题2：Python：计算同比增长率",
        description: `编写Python程序，计算月度销售额的同比增长率。
<strong>输入：</strong>
月度销售数据（包含年份、月份、销售额）
<strong>输出：</strong>
每个月的同比增长率
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算去年同期数据</li>
  <li>计算同比增长率 = (本期-同期)/同期</li>
  <li>处理同比增长为负数的情况</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 将数据按年份分组</p>
<p>2. 匹配去年同期的数据</p>
<p>3. 计算同比增长率</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

# 示例数据
data = {
    'year': [2022, 2022, 2023, 2023],
    'month': [1, 2, 1, 2],
    'sales': [100, 110, 120, 132]
}
df = pd.DataFrame(data)

# 按月份和年份排序
df = df.sort_values(['month', 'year'])

# 计算同比增长
df['last_year_sales'] = df.groupby('month')['sales'].shift(1)
df['growth_rate'] = (df['sales'] - df['last_year_sales']) / df['last_year_sales']
df['growth_rate_percent'] = df['growth_rate'] * 100

print("销售数据及同比增长:")
print(df)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('pandas-basics')">Pandas基础</a></li>
  <li>分组和移位操作</li>
  <li>增长率计算</li>
</ul>`
      },
      {
        id: 3,
        title: "问题3：Python：多维度统计",
        description: `编写Python程序，从多个维度（地区、产品、时间）统计销售数据。
<strong>输入：</strong>
销售数据（包含地区、产品、月份、销售额）
<strong>输出：</strong>
多维度统计报表
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>按地区统计</li>
  <li>按产品统计</li>
  <li>按地区×产品交叉统计</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用groupby进行单维度分组</p>
<p>2. 使用pivot_table或crosstab做交叉表</p>
<p>3. 格式化输出结果</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

# 示例数据
data = {
    'region': ['华北', '华北', '华东', '华东', '华南', '华南'],
    'product': ['产品A', '产品B', '产品A', '产品B', '产品A', '产品B'],
    'sales': [100, 150, 120, 180, 90, 130]
}
df = pd.DataFrame(data)

# 单维度统计
print("按地区统计:")
region_stats = df.groupby('region')['sales'].sum()
print(region_stats)
print()

print("按产品统计:")
product_stats = df.groupby('product')['sales'].sum()
print(product_stats)
print()

# 交叉表
print("地区×产品交叉表:")
pivot = df.pivot_table(index='region', columns='product', values='sales', aggfunc='sum', fill_value=0)
print(pivot)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>多维度分析</li>
  <li>PivotTable透视表</li>
  <li>交叉分析</li>
</ul>`
      },
      {
        id: 4,
        title: "问题4：SQL窗口函数：累计销售额",
        description: `使用SQL窗口函数计算累计销售额。
<strong>输入：</strong>
包含日期、销售额的销售表
<strong>输出：</strong>
每日的累计销售额
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>使用窗口函数SUM() OVER()</li>
  <li>按日期排序计算累计值</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `-- 请编写SQL代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用窗口函数定义按日期排序的窗口</p>
<p>2. 在窗口上累加销售额</p>
<h4>SQL示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
SELECT 
  date,
  amount,
  SUM(amount) OVER (ORDER BY date) AS cumulative_amount
FROM sales
ORDER BY date;
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('sql-window')">窗口函数</a></li>
  <li>SUM() OVER()</li>
  <li>累计计算</li>
</ul>`
      },
      {
        id: 5,
        title: "问题5：SQL子查询：高价值客户",
        description: `找出购买金额超过平均水平的高价值客户。
<strong>输入：</strong>
订单表order（customer_id, amount）
<strong>输出：</strong>
平均购买金额高于总体平均的客户
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>使用子查询计算总体平均值</li>
  <li>找出超过平均值的客户</li>
</ul>`,
        difficulty: "medium",
        time: "15分钟",
        code: `-- 请编写SQL代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 先计算总体平均购买金额</p>
<p>2. 再找出高于这个平均值的客户</p>
<h4>SQL示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
WITH customer_avg AS (
  SELECT customer_id, AVG(amount) AS avg_amount
  FROM orders
  GROUP BY customer_id
),
overall_avg AS (
  SELECT AVG(avg_amount) AS avg_value
  FROM customer_avg
)
SELECT ca.*
FROM customer_avg ca, overall_avg oa
WHERE ca.avg_amount > oa.avg_value
ORDER BY ca.avg_amount DESC;
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>CTE公用表表达式</li>
  <li>子查询</li>
  <li>复杂条件筛选</li>
</ul>`
      },
      {
        id: 6,
        title: "问题6：Python：RFM用户分层",
        description: `使用RFM模型对用户进行分层（Recency, Frequency, Monetary）。
<strong>输入：</strong>
用户消费记录（user_id, purchase_date, amount）
<strong>输出：</strong>
每个用户的RFM分数和分层
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算最近一次消费（R）</li>
  <li>计算消费频率（F）</li>
  <li>计算消费金额（M）</li>
  <li>进行分层打分</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 计算每个用户的R、F、M三个指标</p>
<p>2. 对每个指标进行分段打分（如1-5分）</p>
<p>3. 综合得分进行用户分层</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
from datetime import datetime

# 示例数据
data = {
    'user_id': [1,1,2,2,2,3],
    'purchase_date': ['2023-12-01','2023-12-15','2023-11-20','2023-12-05','2023-12-10','2023-10-01'],
    'amount': [100, 150, 80, 90, 110, 200]
}
df = pd.DataFrame(data)
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# 当前日期
current_date = datetime(2023,12,20)

# 计算RFM
rfm = df.groupby('user_id').agg({
    'purchase_date': lambda x: (current_date - x.max()).days,
    'user_id': 'count',
    'amount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# 打分 (1-5分)
rfm['R_score'] = pd.qcut(rfm['Recency'], q=5, labels=[1,2,3,4,5], duplicates='drop')
rfm['F_score'] = pd.qcut(rfm['Frequency'], q=5, labels=[5,4,3,2,1], duplicates='drop')
rfm['M_score'] = pd.qcut(rfm['Monetary'], q=5, labels=[5,4,3,2,1], duplicates='drop')

print("RFM分析结果:")
print(rfm)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('rfm-model')">RFM模型</a></li>
  <li>用户分层</li>
  <li>分位数切割</li>
</ul>`
      },
      {
        id: 7,
        title: "问题7：Python：ABC商品分类",
        description: `对商品进行ABC分类（帕累托法则）。
<strong>输入：</strong>
商品销售数据（product_id, sales_amount）
<strong>输出：</strong>
每个商品的ABC分类
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>按销售额降序排序</li>
  <li>计算累计占比</li>
  <li>A类：80%, B类：15%, C类：5%</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 按销售额降序排序</p>
<p>2. 计算累计销售额和累计占比</p>
<p>3. 根据累计占比划分ABC类别</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

# 示例数据
data = {
    'product_id': ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'],
    'sales': [1000, 800, 500, 300, 200, 100, 50, 30, 15, 5]
}
df = pd.DataFrame(data)

# 按销售额降序排序
df = df.sort_values('sales', ascending=False).reset_index(drop=True)

# 计算累计销售和占比
df['cumulative'] = df['sales'].cumsum()
df['percentage'] = df['cumulative'] / df['sales'].sum() * 100

# ABC分类
def abc_category(pct):
    if pct <= 80:
        return 'A'
    elif pct <= 95:
        return 'B'
    else:
        return 'C'

df['category'] = df['percentage'].apply(abc_category)

print("ABC分类结果:")
print(df)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>ABC分析</li>
  <li>帕累托法则</li>
  <li>累计占比</li>
</ul>`
      },
      {
        id: 8,
        title: "问题8：Python：时间序列移动平均",
        description: `使用移动平均法对时间序列进行平滑和预测。
<strong>输入：</strong>
月度销售数据
<strong>输出：</strong>
移动平均值和预测结果
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算简单移动平均</li>
  <li>计算加权移动平均</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用pandas的rolling窗口计算移动平均</p>
<p>2. 加权移动平均需要自定义权重</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
import numpy as np

# 示例数据
sales = [100, 110, 105, 120, 115, 130, 125, 140, 135, 150]
dates = pd.date_range('2023-01-01', periods=10, freq='MS')
df = pd.DataFrame({'sales': sales}, index=dates)

# 3个月简单移动平均
df['SMA_3'] = df['sales'].rolling(3).mean()

# 3个月加权移动平均 (权重: 0.5, 0.3, 0.2)
weights = np.array([0.5, 0.3, 0.2])
df['WMA_3'] = df['sales'].rolling(3).apply(lambda x: (x * weights).sum(), raw=True)

print("移动平均结果:")
print(df)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('time-series')">时间序列</a></li>
  <li>移动平均</li>
  <li>rolling窗口</li>
</ul>`
      },
      {
        id: 9,
        title: "问题9：数据分析实战",
        description: `综合运用所学知识，完成一次完整的数据分析任务。
<strong>输入：</strong>
一份包含销售、用户、产品信息的数据集
<strong>输出：</strong>
完整的数据分析报告
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>数据清洗和预处理</li>
  <li>多维度分析</li>
  <li>关键指标计算</li>
</ul>`,
        difficulty: "hard",
        time: "30分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 理解数据，制定分析目标</p>
<p>2. 逐步进行数据清洗、探索、分析</p>
<p>3. 得出可执行的业务结论</p>
<h4>代码框架</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
import matplotlib.pyplot as plt

# 1. 数据读取和初步探索
df = pd.read_csv('sales_data.csv')
print(df.head())
print(df.describe())

# 2. 数据清洗
df = df.dropna()
df = df[df['amount'] > 0]

# 3. 关键指标计算
total_sales = df['amount'].sum()
avg_order = df['amount'].mean()
customer_count = df['user_id'].nunique()

# 4. 多维度分析
monthly_sales = df.resample('M', on='date')['amount'].sum()
product_sales = df.groupby('product')['amount'].sum()

print(f"总销售额: {total_sales}")
print(f"平均客单价: {avg_order:.2f}")
print(f"客户数: {customer_count}")
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>完整数据分析流程</li>
  <li>业务洞察</li>
  <li>综合应用</li>
</ul>`
      },
      {
        id: 10,
        title: "问题10：数据可视化",
        description: `使用Python库（如matplotlib、seaborn）进行数据可视化。
<strong>输入：</strong>
销售数据
<strong>输出：</strong>
美观的图表
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>绘制折线图（趋势）</li>
  <li>绘制柱状图（对比）</li>
  <li>图表标注清晰</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写Python代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 选择合适的图表类型</p>
<p>2. 设置合适的标题、标签、图例</p>
<p>3. 美化图表样式</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据
months = ['1月','2月','3月','4月','5月','6月']
sales = [100, 120, 110, 130, 140, 150]

# 折线图
plt.figure(figsize=(10,6))
plt.plot(months, sales, marker='o', linewidth=2, color='#3498db')
plt.title('月度销售趋势', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 柱状图
plt.figure(figsize=(10,6))
plt.bar(months, sales, color='#2ecc71', alpha=0.8)
plt.title('各月销售额对比', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额', fontsize=12)
plt.tight_layout()
plt.show()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('visualization')">数据可视化</a></li>
  <li>matplotlib</li>
  <li>图表美化</li>
</ul>`
      }
    ];'''
    html_content = html_content[:problems_start] + new_problems + html_content[problems_end:]
    
    # 现在替换选择题数据
    choices_start = html_content.find('const choiceQuestions = [')
    if choices_start == -1:
        print("Error: choiceQuestions array not found")
        return
    
    bracket_count = 1
    pos = choices_start + len('const choiceQuestions = [')
    while bracket_count > 0 and pos < len(html_content):
        if html_content[pos] == '[':
            bracket_count += 1
        elif html_content[pos] == ']':
            bracket_count -= 1
        pos += 1
    choices_end = pos
    
    new_choices = '''const choiceQuestions = [
      {
        id: 'c1',
        chapter: 1,
        title: "选择题1：BI概念与价值",
        question: "商务智能（BI）的核心目标是什么？",
        options: [
          { label: 'A', text: '收集海量数据' },
          { label: 'B', text: '将数据转化为知识，帮助做出明智的业务决策' },
          { label: 'C', text: '开发数据分析软件' },
          { label: 'D', text: '建立数据库系统' }
        ],
        answer: 'B',
        analysis: "商务智能的核心目标是将企业数据转化为知识，帮助做出明智的业务决策。数据收集、软件开发、数据库都是BI的手段而非目标。",
        difficulty: "easy"
      },
      {
        id: 'c2',
        chapter: 1,
        title: "选择题2：数据价值链条",
        question: "数据价值的递进链条是？",
        options: [
          { label: 'A', text: '数据 → 知识 → 信息 → 智慧' },
          { label: 'B', text: '数据 → 信息 → 知识 → 智慧' },
          { label: 'C', text: '信息 → 数据 → 知识 → 智慧' },
          { label: 'D', text: '数据 → 知识 → 智慧 → 信息' }
        ],
        answer: 'B',
        analysis: "数据→信息→知识→智慧：数据是原始事实，信息是处理后有意义的数据，知识是理解的模式，智慧是运用知识做决策。",
        difficulty: "easy"
      },
      {
        id: 'c3',
        chapter: 1,
        title: "选择题3：BI架构与ETL",
        question: "ETL过程中的E、T、L分别代表什么？",
        options: [
          { label: 'A', text: 'Extract, Transform, Load' },
          { label: 'B', text: 'Export, Transform, Load' },
          { label: 'C', text: 'Extract, Transfer, Load' },
          { label: 'D', text: 'Extract, Transform, Leave' }
        ],
        answer: 'A',
        analysis: "ETL是Extract（抽取）、Transform（转换）、Load（加载）的缩写，是数据仓库的核心过程。",
        difficulty: "easy"
      },
      {
        id: 'c4',
        chapter: 2,
        title: "选择题4：四种分析层次",
        question: "以下哪项不是BI分析的四个层次之一？",
        options: [
          { label: 'A', text: '描述性分析' },
          { label: 'B', text: '诊断性分析' },
          { label: 'C', text: '回顾性分析' },
          { label: 'D', text: '规范性分析' }
        ],
        answer: 'C',
        analysis: "BI分析四个层次是：描述性（发生了什么）、诊断性（为什么发生）、预测性（会发生什么）、规范性（应该怎么做）。",
        difficulty: "easy"
      },
      {
        id: 'c5',
        chapter: 2,
        title: "选择题5：维度拆解",
        question: "以下哪种方法属于维度拆解？",
        options: [
          { label: 'A', text: '把总销售额按地区、产品、渠道拆分' },
          { label: 'B', text: '计算总销售额' },
          { label: 'C', text: '预测下个月的销售额' },
          { label: 'D', text: '制作一个漂亮的图表' }
        ],
        answer: 'A',
        analysis: "维度拆解就是从不同维度（如地区、产品）对总体指标进行拆分分析，以发现问题所在。",
        difficulty: "easy"
      },
      {
        id: 'c6',
        chapter: 3,
        title: "选择题6：SQL查询基础",
        question: "SQL中用于分组的关键字是？",
        options: [
          { label: 'A', text: 'ORDER BY' },
          { label: 'B', text: 'GROUP BY' },
          { label: 'C', text: 'WHERE' },
          { label: 'D', text: 'JOIN' }
        ],
        answer: 'B',
        analysis: "GROUP BY用于按一个或多个列对结果集进行分组，通常配合聚合函数（SUM, AVG等）使用。",
        difficulty: "easy"
      },
      {
        id: 'c7',
        chapter: 3,
        title: "选择题7：JOIN查询",
        question: "要同时获取两张表的数据且只保留匹配的记录，应该使用？",
        options: [
          { label: 'A', text: 'LEFT JOIN' },
          { label: 'B', text: 'RIGHT JOIN' },
          { label: 'C', text: 'INNER JOIN' },
          { label: 'D', text: 'FULL JOIN' }
        ],
        answer: 'C',
        analysis: "INNER JOIN只保留两张表中匹配的记录。",
        difficulty: "easy"
      },
      {
        id: 'c8',
        chapter: 3,
        title: "选择题8：窗口函数",
        question: "窗口函数与普通聚合函数的区别是？",
        options: [
          { label: 'A', text: '窗口函数更快' },
          { label: 'B', text: '窗口函数保留原始行，不改变行数' },
          { label: 'C', text: '窗口函数只能用在MySQL中' },
          { label: 'D', text: '窗口函数不支持排序' }
        ],
        answer: 'B',
        analysis: "窗口函数不会像GROUP BY那样合并行，而是在保留原始行的基础上计算聚合结果。",
        difficulty: "easy"
      },
      {
        id: 'c9',
        chapter: 4,
        title: "选择题9：数据仓库与维度建模",
        question: "维度建模中，描述事实的上下文（如时间、地点）的表称为？",
        options: [
          { label: 'A', text: '事实表' },
          { label: 'B', text: '维度表' },
          { label: 'C', text: '汇总表' },
          { label: 'D', text: '临时表' }
        ],
        answer: 'B',
        analysis: "维度建模中，维度表存放描述性信息（如时间、地点、产品），事实表存放可度量的数值。",
        difficulty: "medium"
      },
      {
        id: 'c10',
        chapter: 4,
        title: "选择题10：数据分层",
        question: "典型的数据仓库分层架构顺序是？",
        options: [
          { label: 'A', text: 'ODS → DWD → DWS → ADS' },
          { label: 'B', text: 'ADS → DWS → DWD → ODS' },
          { label: 'C', text: 'DWD → ODS → DWS → ADS' },
          { label: 'D', text: 'ODS → ADS → DWD → DWS' }
        ],
        answer: 'A',
        analysis: "ODS（原始数据层）→ DWD（明细数据层）→ DWS（汇总数据层）→ ADS（应用数据层）。",
        difficulty: "easy"
      },
      {
        id: 'c11',
        chapter: 5,
        title: "选择题11：Excel高级函数",
        question: "在Excel中，根据条件查找匹配值的函数是？",
        options: [
          { label: 'A', text: 'SUM' },
          { label: 'B', text: 'VLOOKUP/XLOOKUP' },
          { label: 'C', text: 'AVERAGE' },
          { label: 'D', text: 'COUNT' }
        ],
        answer: 'B',
        analysis: "VLOOKUP或XLOOKUP用于在表格中查找匹配值。",
        difficulty: "easy"
      }
    ];'''
    
    html_content = html_content[:choices_start] + new_choices + html_content[choices_end:]
    
    # 替换知识点部分
    knowledge_start = html_content.find('<!-- 知识点模块 -->')
    if knowledge_start == -1:
        knowledge_start = html_content.find('<div class="tab-content" id="knowledge">')
    
    if knowledge_start != -1:
        # 找到知识点模块结束位置
        # 这里直接找下一个tab-content的位置或者后面的script标签
        # 简化处理，我们创建一个新的知识点模块
        knowledge_end = html_content.find('</div>', knowledge_start)
        # 多找几个结束标签
        count = 0
        pos = knowledge_end
        while count < 10 and pos != -1:
            pos = html_content.find('</div>', pos + 6)
            if pos != -1:
                count += 1
        if count == 10 and pos != -1:
            new_knowledge = '''<!-- 知识点模块 -->
            <div class="tab-content" id="knowledge">
              <div class="space-y-8">
                <!-- 模块1：BI基础与SQL -->
                <div id="module1-bi" class="knowledge-section">
                  <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                    <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                      <i class="fa fa-book"></i> 模块1：BI基础与SQL（8学时）
                    </h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-lightbulb-o text-yellow-400"></i> 什么是商务智能？
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">商务智能（BI）是将企业数据转化为知识，帮助做出明智业务决策的过程。核心是数据→信息→知识→智慧的转化。</p>
                        <div class="space-y-2">
                          <div class="flex items-start gap-2">
                            <span class="text-cyan-400 text-lg">📊</span>
                            <div>
                              <strong class="text-gray-200">描述性分析</strong>
                              <p class="text-gray-400 text-xs">发生了什么？</p>
                            </div>
                          </div>
                          <div class="flex items-start gap-2">
                            <span class="text-yellow-400 text-lg">🔍</span>
                            <div>
                              <strong class="text-gray-200">诊断性分析</strong>
                              <p class="text-gray-400 text-xs">为什么发生？</p>
                            </div>
                          </div>
                          <div class="flex items-start gap-2">
                            <span class="text-pink-400 text-lg">📈</span>
                            <div>
                              <strong class="text-gray-200">预测性分析</strong>
                              <p class="text-gray-400 text-xs">会发生什么？</p>
                            </div>
                          </div>
                          <div class="flex items-start gap-2">
                            <span class="text-blue-400 text-lg">🎯</span>
                            <div>
                              <strong class="text-gray-200">规范性分析</strong>
                              <p class="text-gray-400 text-xs">应该怎么做？</p>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-database text-emerald-400"></i> SQL基础
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">SQL是数据分析的核心工具，用于查询和处理关系型数据库中的数据。</p>
                        <div class="bg-dark-gray p-3 rounded font-mono text-sm">
                          <pre class="text-cyan-300">
-- 简单查询
SELECT * FROM sales;

-- 分组统计
SELECT region, SUM(amount) 
FROM sales 
GROUP BY region;

-- 排序
SELECT * FROM sales 
ORDER BY amount DESC;
                          </pre>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 模块2：数据分析思维 -->
                <div id="module2-thinking" class="knowledge-section hidden">
                  <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                    <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                      <i class="fa fa-brain"></i> 模块2：数据分析思维（6学时）
                    </h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-sitemap text-yellow-400"></i> 维度拆解
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">当发现问题时，从多个维度对指标进行拆分，找到问题的根源。</p>
                        <div class="bg-dark-gray p-3 rounded-lg">
                          <h5 class="text-emerald-400 font-semibold mb-2">例：销售额下降，从哪些维度看？</h5>
                          <ul class="text-gray-400 text-sm space-y-1">
                            <li>• 按地区：哪个地区下降最多？</li>
                            <li>• 按产品：哪类产品卖得不好？</li>
                            <li>• 按渠道：线上还是线下？</li>
                            <li>• 按时间：哪周开始下降？</li>
                          </ul>
                        </div>
                      </div>
                      
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-balance-scale text-emerald-400"></i> 对比思维
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">孤立的数据没有意义，只有通过对比才能产生洞察。</p>
                        <div class="space-y-2">
                          <div class="bg-dark-gray p-2 rounded text-sm">
                            <span class="text-cyan-400">同比：</span>
                            <span class="text-gray-400">与去年同期比较</span>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-sm">
                            <span class="text-yellow-400">环比：</span>
                            <span class="text-gray-400">与上个月/周比较</span>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-sm">
                            <span class="text-pink-400">目标完成率：</span>
                            <span class="text-gray-400">实际/目标</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 模块3：SQL高级应用 -->
                <div id="module3-sql" class="knowledge-section hidden">
                  <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                    <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                      <i class="fa fa-terminal"></i> 模块3：SQL高级应用（8学时）
                    </h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-sort-amount-desc text-yellow-400"></i> 窗口函数
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">窗口函数允许在不合并行的情况下计算聚合值，非常适合排序、累计、排名等场景。</p>
                        <div class="bg-dark-gray p-3 rounded font-mono text-sm">
                          <pre class="text-cyan-300">
-- 累计求和
SELECT date, amount,
  SUM(amount) OVER (ORDER BY date) 
  AS cumulative
FROM sales;

-- 排序排名
SELECT user_id, amount,
  RANK() OVER (ORDER BY amount DESC) 
  AS rank
FROM sales;
                          </pre>
                        </div>
                      </div>
                      
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-code-fork text-emerald-400"></i> CTE与子查询
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">使用CTE（Common Table Expression）可以让复杂查询更清晰可读。</p>
                        <div class="bg-dark-gray p-3 rounded font-mono text-sm">
                          <pre class="text-cyan-300">
WITH daily_sales AS (
  SELECT date, SUM(amount) AS total
  FROM sales
  GROUP BY date
)
SELECT * FROM daily_sales
WHERE total > 10000;
                          </pre>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 模块4：商务分析模型 -->
                <div id="module4-models" class="knowledge-section hidden">
                  <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                    <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                      <i class="fa fa-cubes"></i> 模块4：商务分析模型（8学时）
                    </h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-users text-yellow-400"></i> RFM用户分层
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">RFM是经典的用户价值分层模型，通过三个维度衡量用户价值：</p>
                        <div class="space-y-2">
                          <div class="flex justify-between bg-dark-gray p-2 rounded">
                            <span class="text-cyan-400 font-semibold">R (Recency)</span>
                            <span class="text-gray-400 text-sm">最近一次消费</span>
                          </div>
                          <div class="flex justify-between bg-dark-gray p-2 rounded">
                            <span class="text-yellow-400 font-semibold">F (Frequency)</span>
                            <span class="text-gray-400 text-sm">消费频率</span>
                          </div>
                          <div class="flex justify-between bg-dark-gray p-2 rounded">
                            <span class="text-pink-400 font-semibold">M (Monetary)</span>
                            <span class="text-gray-400 text-sm">消费金额</span>
                          </div>
                        </div>
                      </div>
                      
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-shopping-cart text-emerald-400"></i> ABC商品分类
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">ABC分类基于帕累托法则（80/20法则），将商品分为三类：</p>
                        <div class="space-y-2">
                          <div class="bg-dark-gray p-2 rounded">
                            <span class="text-cyan-400 font-semibold">A类</span>
                            <span class="text-gray-400 text-sm">20%商品贡献80%销售额</span>
                          </div>
                          <div class="bg-dark-gray p-2 rounded">
                            <span class="text-yellow-400 font-semibold">B类</span>
                            <span class="text-gray-400 text-sm">30%商品贡献15%销售额</span>
                          </div>
                          <div class="bg-dark-gray p-2 rounded">
                            <span class="text-gray-400 font-semibold">C类</span>
                            <span class="text-gray-400 text-sm">50%商品贡献5%销售额</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 模块5：综合应用 -->
                <div id="module5-practice" class="knowledge-section hidden">
                  <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
                    <h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2">
                      <i class="fa fa-rocket"></i> 模块5：综合应用（8学时）
                    </h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-line-chart text-yellow-400"></i> 数据可视化
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">好的可视化能让数据讲故事，让洞察更清晰。选择合适的图表类型很重要。</p>
                        <div class="grid grid-cols-2 gap-2">
                          <div class="bg-dark-gray p-2 rounded text-center text-xs">
                            <div class="text-cyan-400 mb-1">📈 折线图</div>
                            <div class="text-gray-400">看趋势</div>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-center text-xs">
                            <div class="text-yellow-400 mb-1">📊 柱状图</div>
                            <div class="text-gray-400">做对比</div>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-center text-xs">
                            <div class="text-pink-400 mb-1">🥧 饼图</div>
                            <div class="text-gray-400">看占比</div>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-center text-xs">
                            <div class="text-blue-400 mb-1">🔘 散点图</div>
                            <div class="text-gray-400">看关系</div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="bg-dark p-5 rounded-lg border border-gray-700">
                        <h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2">
                          <i class="fa fa-file-excel-o text-emerald-400"></i> Excel实用技巧
                        </h4>
                        <p class="text-gray-300 mb-4 text-sm leading-relaxed">Excel仍然是数据分析中最常用的工具之一。</p>
                        <div class="space-y-1">
                          <div class="bg-dark-gray p-2 rounded text-sm">
                            <span class="text-cyan-400">VLOOKUP/XLOOKUP</span>
                            <span class="text-gray-400">查找匹配</span>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-sm">
                            <span class="text-yellow-400">数据透视表</span>
                            <span class="text-gray-400">快速交叉分析</span>
                          </div>
                          <div class="bg-dark-gray p-2 rounded text-sm">
                            <span class="text-pink-400">条件格式</span>
                            <span class="text-gray-400">数据高亮</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>'''
            
            html_content = html_content[:knowledge_start] + new_knowledge + html_content[pos:]
    
    # 写入新文件
    with open('/workspace/courses/business-intelligence.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("商务智能课程内容已完整替换！")
    print("请预览验证功能是否正常")

if __name__ == '__main__':
    main()
