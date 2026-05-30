#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""根据知识点更新商务智能分析练习题库"""
import os

def main():
    input_file = '/workspace/courses/business-intelligence.html'
    backup_file = '/workspace/courses/business-intelligence-questions-backup.html'
    
    print("开始根据知识点更新练习题库...")
    
    # 备份当前文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已备份到: {backup_file}")
    
    # 新的选择题数据
    new_choice_questions = '''const choiceQuestions = [
      {
        id: 'bi-cq1',
        question: '商务智能（BI）的核心目标是什么？',
        options: [
          '收集海量数据',
          '将数据转化为知识，帮助做出明智的业务决策',
          '开发数据分析软件',
          '建立数据库系统'
        ],
        answer: 1,
        explanation: '商务智能的核心目标是将企业数据转化为知识，帮助企业做出明智的业务经营决策。'
      },
      {
        id: 'bi-cq2',
        question: '在数据→信息→知识→决策的价值链条中，哪个环节体现了从经验决策到科学决策的转变？',
        options: [
          '数据到信息',
          '信息到知识',
          '知识到决策',
          '数据到决策'
        ],
        answer: 2,
        explanation: '知识到决策的环节体现了从经验决策到科学决策的转变，因为决策是基于已发现的规律和模式。'
      },
      {
        id: 'bi-cq3',
        question: 'BI核心架构中，ETL代表什么？',
        options: [
          'Extract, Transform, Load',
          'Execute, Transfer, Log',
          'Extract, Transfer, Load',
          'Execute, Transform, Log'
        ],
        answer: 0,
        explanation: 'ETL代表Extract（抽取）、Transform（转换）、Load（加载），是数据仓库建设中的核心流程。'
      },
      {
        id: 'bi-cq4',
        question: '以下哪个不是描述性分析的特点？',
        options: [
          '回答发生了什么',
          '汇总历史数据',
          '预测未来趋势',
          '生成报表和图表'
        ],
        answer: 2,
        explanation: '预测未来趋势属于预测性分析的范畴，不是描述性分析的特点。'
      },
      {
        id: 'bi-cq5',
        question: '在维度拆解中，哪个维度用于分析不同地区的销售表现？',
        options: [
          '时间维度',
          '地区维度',
          '产品维度',
          '渠道维度'
        ],
        answer: 1,
        explanation: '地区维度用于分析不同地理区域的销售数据，如华东、华南、华北等。'
      },
      {
        id: 'bi-cq6',
        question: 'SQL中用于去重的关键字是？',
        options: [
          'UNIQUE',
          'DISTINCT',
          'GROUP BY',
          'WHERE'
        ],
        answer: 1,
        explanation: 'DISTINCT关键字用于去除查询结果中的重复记录。'
      },
      {
        id: 'bi-cq7',
        question: 'LEFT JOIN和INNER JOIN的主要区别是什么？',
        options: [
          'LEFT JOIN返回左表全部记录，INNER JOIN只返回匹配的记录',
          '性能不同',
          '语法不同',
          '没有区别'
        ],
        answer: 0,
        explanation: 'LEFT JOIN会返回左表的全部记录以及右表匹配的记录，而INNER JOIN只返回两表都匹配的记录。'
      },
      {
        id: 'bi-cq8',
        question: '窗口函数ROW_NUMBER()的作用是什么？',
        options: [
          '计算总和',
          '为每一行分配唯一的序号',
          '计算平均值',
          '分组统计'
        ],
        answer: 1,
        explanation: 'ROW_NUMBER()为查询结果的每一行分配一个唯一的序号，可用于排名、分页等场景。'
      },
      {
        id: 'bi-cq9',
        question: '在数据仓库维度建模中，星型模型的特点是？',
        options: [
          '只有一张表',
          '事实表在中心，连接多个维度表',
          '所有表都是维度表',
          '表之间没有关联'
        ],
        answer: 1,
        explanation: '星型模型由一个事实表和多个维度表组成，事实表在中心，维度表围绕在四周，形似星星。'
      },
      {
        id: 'bi-cq10',
        question: '数据仓库中的ODS层是指？',
        options: [
          '汇总数据层',
          '明细数据层',
          '操作数据层',
          '应用数据层'
        ],
        answer: 2,
        explanation: 'ODS（Operational Data Store）是操作数据层，存放原始数据，基本不做清洗转换。'
      },
      {
        id: 'bi-cq11',
        question: 'Excel中哪个函数用于多条件求和？',
        options: [
          'VLOOKUP',
          'SUMIF',
          'SUMIFS',
          'COUNT'
        ],
        answer: 2,
        explanation: 'SUMIFS函数用于根据多个条件对指定区域求和。'
      },
      {
        id: 'bi-cq12',
        question: 'RFM模型中，R代表什么？',
        options: [
          '消费金额',
          '消费频率',
          '最近一次消费时间',
          '客户等级'
        ],
        answer: 2,
        explanation: 'RFM模型中，R代表Recency（最近一次消费时间），用于衡量客户的活跃度。'
      },
      {
        id: 'bi-cq13',
        question: 'ABC分类法中，A类商品通常占销售额的比例是？',
        options: [
          '50%',
          '60%',
          '80%',
          '20%'
        ],
        answer: 2,
        explanation: 'ABC分类法中，A类商品通常占销售总额的80%，但数量只占20%，需要重点管理。'
      },
      {
        id: 'bi-cq14',
        question: 'Power BI中，DAX是指什么？',
        options: [
          '数据清洗语言',
          '数据分析表达式',
          '数据库查询语言',
          '数据可视化语言'
        ],
        answer: 1,
        explanation: 'DAX（Data Analysis Expressions）是Power BI中的数据分析表达式语言，用于创建计算列和度量值。'
      },
      {
        id: 'bi-cq15',
        question: 'Python中用于数据处理的核心库是？',
        options: [
          'NumPy',
          'Pandas',
          'Matplotlib',
          'Scikit-learn'
        ],
        answer: 1,
        explanation: 'Pandas是Python中用于数据处理和分析的核心库，提供了DataFrame数据结构。'
      },
      {
        id: 'bi-cq16',
        question: '同比增长率的计算公式是？',
        options: [
          '(本期值 - 上期值) / 上期值 × 100%',
          '(本期值 - 上期值) / 本期值 × 100%',
          '上期值 / 本期值 × 100%',
          '本期值 / 上期值 × 100%'
        ],
        answer: 0,
        explanation: '同比增长率 = (本期值 - 上期值) / 上期值 × 100%，反映与去年同期相比的增长情况。'
      },
      {
        id: 'bi-cq17',
        question: '在SQL聚合函数中，哪个函数用于计算平均值？',
        options: [
          'SUM',
          'COUNT',
          'AVG',
          'MAX'
        ],
        answer: 2,
        explanation: 'AVG函数用于计算指定字段的平均值。'
      },
      {
        id: 'bi-cq18',
        question: '数据可视化的首要原则是？',
        options: [
          '使用最复杂的图表',
          '使用多种颜色',
          '清晰准确地传达信息',
          '展示所有数据'
        ],
        answer: 2,
        explanation: '数据可视化的首要原则是清晰准确地传达信息，让观众快速理解数据背后的含义。'
      },
      {
        id: 'bi-cq19',
        question: '在窗口函数中，LAG函数的作用是？',
        options: [
          '获取前N行的值',
          '获取后N行的值',
          '计算排名',
          '计算聚合值'
        ],
        answer: 0,
        explanation: 'LAG函数用于获取当前行之前的第N行数据，常用于计算同比、环比等。'
      },
      {
        id: 'bi-cq20',
        question: '数据治理的主要目标是什么？',
        options: [
          '收集更多数据',
          '建立数据标准，确保数据质量和安全',
          '开发数据系统',
          '培训数据人才'
        ],
        answer: 1,
        explanation: '数据治理的主要目标是建立数据标准、规范数据管理流程，确保数据质量和安全。'
      }
    ]'''
    
    # 新的编程题数据（problems数组）
    new_problems = '''const problems = [
      {
        id: 1,
        title: "SQL查询：计算各地区销售额",
        description: `编写SQL查询语句，计算每个地区的总销售额和订单数量，按销售额降序排列。

<strong>题目背景：</strong>
分析不同地区的销售表现是商务智能分析的基础任务。

<strong>假设表结构：</strong>
- users(user_id, name, region)
- orders(order_id, user_id, amount, order_date)

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>关联users和orders表</li>
  <li>按地区分组统计</li>
  <li>输出地区、总销售额、总订单数</li>
  <li>按销售额降序排列</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `-- 请编写SQL查询
SELECT 
    -- 地区,
    -- 总销售额,
    -- 总订单数
FROM orders
-- 关联users表
-- 按地区分组
-- 按销售额降序排列
;`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用INNER JOIN或LEFT JOIN连接users和orders表</p>
<p>2. 使用GROUP BY按地区分组</p>
<p>3. 使用SUM()计算总销售额，COUNT()计算订单数量</p>
<p>4. 使用ORDER BY按销售额降序排列</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
SELECT 
    u.region AS 地区,
    SUM(o.amount) AS 总销售额,
    COUNT(o.order_id) AS 总订单数
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id
GROUP BY u.region
ORDER BY 总销售额 DESC;
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter3')">第3章：SQL基础语法</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2')">第2章：维度拆解</a></li>
</ul>`
      },
      {
        id: 2,
        title: "Python数据分析：计算同比增长率",
        description: `编写Python函数 calculate_growth_rate，计算同比增长率。

<strong>题目背景：</strong>
同比增长率是商务智能分析中的核心指标，用于衡量业务同比变化情况。

<strong>参数说明：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>current_period: 本期值（如本期销售额）</li>
  <li>previous_period: 上期值（如去年同期销售额）</li>
</ul>

<strong>返回值：</strong>
增长率百分比（保留2位小数）

<strong>示例：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>输入：(1100, 1000) → 输出：10.0</li>
  <li>输入：(900, 1000) → 输出：-10.0</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `def calculate_growth_rate(current_period, previous_period):
    """
    计算同比增长率
    
    Args:
        current_period: 本期值
        previous_period: 上期值
    
    Returns:
        增长率百分比（保留2位小数）
    """
    # 请编写代码
    pass`,
        analysis: `
<h4>解题思路</h4>
<p>1. 计算差值：本期值 - 上期值</p>
<p>2. 计算增长率：差值 / 上期值</p>
<p>3. 转换为百分比并保留2位小数</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
def calculate_growth_rate(current_period, previous_period):
    if previous_period == 0:
        return 0.0
    growth_rate = (current_period - previous_period) / previous_period * 100
    return round(growth_rate, 2)
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter7')">第7章：统计学基础</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter9')">第9章：Python数据分析</a></li>
</ul>`
      },
      {
        id: 3,
        title: "Python数据处理：RFM用户分层",
        description: `编写Python函数 rfm_classification，对用户进行RFM分层。

<strong>题目背景：</strong>
RFM模型是客户价值分析的重要工具，帮助企业识别不同价值的客户群体。

<strong>参数说明：</strong>
- users_data: 用户消费数据列表，每个元素是包含以下字段的字典：
  - user_id: 用户ID
  - recency: 最近一次消费距今天数（越小越好）
  - frequency: 消费频率（越大越好）
  - monetary: 消费金额（越大越好）

<strong>返回值：</strong>
字典，键为user_id，值为RFM等级：
- "高价值用户"：R、F、M三个指标都高于平均值
- "潜力用户"：R低但F、M低于平均值
- "流失风险"：R高且F、M低
- "一般用户"：其他情况

<strong>分层规则：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>每个指标：高于平均值记为"高"，低于平均值记为"低"</li>
  <li>高价值：高=高=高</li>
  <li>潜力：低=低=高</li>
  <li>流失风险：高=低=低</li>
  <li>一般用户：其他组合</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `def rfm_classification(users_data):
    """
    RFM用户分层
    
    Args:
        users_data: 用户消费数据列表
    
    Returns:
        字典，键为user_id，值为RFM等级
    """
    # 请编写代码
    # 1. 计算R、F、M的平均值
    # 2. 对每个用户判断R、F、M是高还是低
    # 3. 根据组合判断用户类型
    pass`,
        analysis: `
<h4>解题思路</h4>
<p>1. 计算R、F、M各自的平均值</p>
<p>2. 对每个用户：</p>
<p>   - 比较R、F、M与平均值的关系</p>
<p>   - 标记每个指标为"高"或"低"</p>
<p>3. 根据组合模式判断用户类型</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
def rfm_classification(users_data):
    if not users_data:
        return {}
    
    # 计算平均值
    avg_r = sum(u['recency'] for u in users_data) / len(users_data)
    avg_f = sum(u['frequency'] for u in users_data) / len(users_data)
    avg_m = sum(u['monetary'] for u in users_data) / len(users_data)
    
    result = {}
    for user in users_data:
        r_level = '高' if user['recency'] < avg_r else '低'
        f_level = '高' if user['frequency'] > avg_f else '低'
        m_level = '高' if user['monetary'] > avg_m else '低'
        
        if r_level == '高' and f_level == '高' and m_level == '高':
            result[user['user_id']] = '高价值用户'
        elif r_level == '低' and f_level == '低' and m_level == '高':
            result[user['user_id']] = '潜力用户'
        elif r_level == '高' and f_level == '低' and m_level == '低':
            result[user['user_id']] = '流失风险'
        else:
            result[user['user_id']] = '一般用户'
    
    return result
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter7')">第7章：RFM用户分层模型</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter9')">第9章：Python数据处理</a></li>
</ul>`
      },
      {
        id: 4,
        title: "SQL窗口函数：计算累计销售额",
        description: `编写SQL查询，使用窗口函数计算每日累计销售额。

<strong>题目背景：</strong>
累计销售额是销售分析中的重要指标，帮助了解销售增长趋势。

<strong>假设表结构：</strong>
- daily_sales(date, amount)

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>按日期升序排列</li>
  <li>计算每日累计销售额</li>
  <li>使用窗口函数实现</li>
</ul>

<strong>预期输出示例：</strong>
<table class="w-full text-sm mt-2">
  <tr><th>date</th><th>amount</th><th>cumulative</th></tr>
  <tr><td>2024-01-01</td><td>1000</td><td>1000</td></tr>
  <tr><td>2024-01-02</td><td>1500</td><td>2500</td></tr>
  <tr><td>2024-01-03</td><td>1200</td><td>3700</td></tr>
</table>`,
        difficulty: "easy",
        time: "10分钟",
        code: `-- 请编写SQL查询
SELECT 
    date,
    amount,
    -- 累计销售额（使用窗口函数）
FROM daily_sales
ORDER BY date ASC
;`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用窗口函数的SUM() OVER()语法</p>
<p>2. 使用ORDER BY指定排序方式</p>
<p>3. 默认框架（不指定ROWS）会包含当前行及之前所有行</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
SELECT 
    date,
    amount,
    SUM(amount) OVER(
        ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative
FROM daily_sales
ORDER BY date ASC;
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter3')">第3章：窗口函数</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2')">第2章：时间维度分析</a></li>
</ul>`
      },
      {
        id: 5,
        title: "ABC商品分类",
        description: `编写Python函数 abc_classification，对商品进行ABC分类。

<strong>题目背景：</strong>
ABC分类法是库存管理和商品分析的重要方法，基于帕累托原则（二八法则）。

<strong>分类规则：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>A类商品：销售额累计占比 0% - 80%（重点管理）</li>
  <li>B类商品：销售额累计占比 80% - 95%（常规管理）</li>
  <li>C类商品：销售额累计占比 95% - 100%（简化管理）</li>
</ul>

<strong>参数说明：</strong>
- products: 商品销售数据列表，每个元素是包含product_id、sales的字典

<strong>返回值：</strong>
字典，键为product_id，值为分类（"A"、"B"或"C"）

<strong>示例数据：</strong>
- P1: 销售额 50000
- P2: 销售额 25000
- P3: 销售额 15000
- P4: 销售额 10000
- 总销售额: 100000
- P1占比: 50%（累计50%）→ A类
- P2占比: 25%（累计75%）→ A类
- P3占比: 15%（累计90%）→ B类
- P4占比: 10%（累计100%）→ C类`,
        difficulty: "medium",
        time: "20分钟",
        code: `def abc_classification(products):
    """
    ABC商品分类
    
    Args:
        products: 商品销售数据列表
    
    Returns:
        字典，键为product_id，值为分类
    """
    # 请编写代码
    # 1. 按销售额降序排列
    # 2. 计算累计销售额和占比
    # 3. 根据占比阈值分类
    pass`,
        analysis: `
<h4>解题思路</h4>
<p>1. 按销售额降序排列商品</p>
<p>2. 计算总销售额</p>
<p>3. 计算每个商品的累计销售额和占比</p>
<p>4. 根据累计占比判断分类：</p>
<p>   - 累计占比 ≤ 80% → A类</p>
<p>   - 累计占比 ≤ 95% → B类</p>
<p>   - 其他 → C类</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
def abc_classification(products):
    # 按销售额降序排列
    sorted_products = sorted(products, key=lambda x: x['sales'], reverse=True)
    
    # 计算总销售额
    total_sales = sum(p['sales'] for p in products)
    
    result = {}
    cumulative = 0
    
    for product in sorted_products:
        cumulative += product['sales']
        cumulative_pct = cumulative / total_sales * 100
        
        if cumulative_pct <= 80:
            result[product['product_id']] = 'A'
        elif cumulative_pct <= 95:
            result[product['product_id']] = 'B'
        else:
            result[product['product_id']] = 'C'
    
    return result
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter7')">第7章：ABC分类、帕累托二八法则</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter9')">第9章：Python数据处理</a></li>
</ul>`
      },
      {
        id: 6,
        title: "Python数据聚合：多维度统计",
        description: `编写Python函数 multi_dimension_analysis，进行多维度销售分析。

<strong>题目背景：</strong>
多维度分析是商务智能分析的核心能力，帮助从不同角度理解业务。

<strong>参数说明：</strong>
- sales_data: 销售数据列表，每个元素包含：
  - region: 地区
  - product: 产品
  - channel: 渠道
  - amount: 销售额

<strong>返回值：</strong>
字典，按地区和产品维度聚合的总销售额
键格式：(region, product)
值：销售额总和

<strong>示例：</strong>
输入：
[
  {'region': '华东', 'product': '手机', 'channel': '线上', 'amount': 10000},
  {'region': '华东', 'product': '手机', 'channel': '线下', 'amount': 5000},
  {'region': '华北', 'product': '电脑', 'channel': '线上', 'amount': 15000}
]
输出：
{
  ('华东', '手机'): 15000,
  ('华北', '电脑'): 15000
}`,
        difficulty: "easy",
        time: "15分钟",
        code: `def multi_dimension_analysis(sales_data):
    """
    多维度销售分析
    
    Args:
        sales_data: 销售数据列表
    
    Returns:
        字典，按地区和产品聚合的销售额
    """
    # 请编写代码
    # 使用字典进行分组聚合
    pass`,
        analysis: `
<h4>解题思路</h4>
<p>1. 创建空字典存储结果</p>
<p>2. 遍历销售数据</p>
<p>3. 使用(region, product)元组作为键</p>
<p>4. 累加每个组合的销售额</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
def multi_dimension_analysis(sales_data):
    result = {}
    
    for sale in sales_data:
        key = (sale['region'], sale['product'])
        if key in result:
            result[key] += sale['amount']
        else:
            result[key] = sale['amount']
    
    return result
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2')">第2章：维度拆解</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter9')">第9章：Python数据处理</a></li>
</ul>`
      },
      {
        id: 7,
        title: "SQL子查询：找出高价值客户",
        description: `编写SQL查询，找出消费金额高于平均值的客户及其订单信息。

<strong>题目背景：</strong>
识别高价值客户是客户分析的基础，帮助企业制定针对性的营销策略。

<strong>假设表结构：</strong>
- customers(customer_id, name)
- orders(order_id, customer_id, amount)

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算每个客户的消费总额</li>
  <li>筛选消费总额高于平均值的客户</li>
  <li>输出：客户名称、消费总额、订单数量</li>
  <li>按消费总额降序排列</li>
</ul>`,
        difficulty: "medium",
        time: "15分钟",
        code: `-- 请编写SQL查询
SELECT 
    c.name,
    -- 消费总额,
    -- 订单数量
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
-- 分组统计
-- 筛选消费总额高于平均值
ORDER BY 消费总额 DESC
;`,
        analysis: `
<h4>解题思路</h4>
<p>1. 先计算所有客户的平均消费总额（子查询）</p>
<p>2. 关联customers和orders表</p>
<p>3. 按客户分组，计算消费总额和订单数量</p>
<p>4. 使用HAVING或WHERE筛选高于平均值的结果</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
SELECT 
    c.name,
    SUM(o.amount) AS total_amount,
    COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > (
    SELECT AVG(customer_avg)
    FROM (
        SELECT SUM(amount) AS customer_avg
        FROM orders
        GROUP BY customer_id
    ) t
)
ORDER BY total_amount DESC;
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter3')">第3章：子查询</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2')">第2章：客户分析思维</a></li>
</ul>`
      },
      {
        id: 8,
        title: "Python时间序列分析：移动平均",
        description: `编写Python函数 moving_average，计算移动平均值。

<strong>题目背景：</strong>
移动平均是时间序列分析中的基础方法，用于平滑数据波动，发现趋势。

<strong>参数说明：</strong>
- data: 数据列表（如每日销售额）
- window: 窗口大小

<strong>返回值：</strong>
列表，包含移动平均值（与输入数据等长）
- 前(window-1)个元素为None（无法计算完整的窗口）
- 之后的元素为窗口内的平均值

<strong>示例：</strong>
输入：[100, 120, 130, 140, 150], window=3
处理过程：
- 前2个：None（数据不足）
- 第3个：avg(100, 120, 130) = 116.67
- 第4个：avg(120, 130, 140) = 130.00
- 第5个：avg(130, 140, 150) = 140.00
输出：[None, None, 116.67, 130.0, 140.0]`,
        difficulty: "medium",
        time: "15分钟",
        code: `def moving_average(data, window):
    """
    计算移动平均值
    
    Args:
        data: 数据列表
        window: 窗口大小
    
    Returns:
        移动平均值列表
    """
    # 请编写代码
    pass`,
        analysis: `
<h4>解题思路</h4>
<p>1. 初始化结果列表</p>
<p>2. 遍历数据列表</p>
<p>3. 对于前(window-1)个元素，添加None</p>
<p>4. 对于其他元素，计算当前元素及前面(window-1)个元素的平均值</p>

<h4>参考解答</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
<pre class="text-cyan-300">
def moving_average(data, window):
    result = []
    
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            window_data = data[i-window+1:i+1]
            avg = sum(window_data) / window
            result.append(round(avg, 2))
    
    return result
</pre>
</div>

<h4>知识点关联</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter7')">第7章：时间序列分析</a></li>
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter9')">第9章：Python数据处理</a></li>
</ul>`
      }
    ]'''
    
    # 替换选择题数据
    old_choice_start = 'const choiceQuestions = ['
    old_choice_end = '];'
    choice_start_idx = content.find(old_choice_start)
    choice_end_idx = content.find(old_choice_end, choice_start_idx) + len('];')
    
    if choice_start_idx == -1:
        print("❌ 错误：未找到选择题数据")
        return
    
    content = content[:choice_start_idx] + new_choice_questions + content[choice_end_idx:]
    
    # 替换编程题数据（problems数组）
    old_problems_start = 'const problems = ['
    old_problems_end = '];'
    problems_start_idx = content.find(old_problems_start)
    problems_end_idx = content.find(old_problems_end, problems_start_idx) + len('];')
    
    if problems_start_idx == -1:
        print("❌ 错误：未找到编程题数据")
        return
    
    content = content[:problems_start_idx] + new_problems + content[problems_end_idx:]
    
    # 保存文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n" + "="*60)
    print("✅ 商务智能分析练习题库更新完成！")
    print("="*60)
    print(f"\n📝 已更新内容：")
    print("  • 选择题：20道（覆盖所有知识点）")
    print("  • 编程题：8道（SQL、Python、数据分析）")
    print("\n📚 题目覆盖范围：")
    print("  ✓ 第1章：BI基础概念、价值、架构")
    print("  ✓ 第2章：数据分析思维、维度拆解")
    print("  ✓ 第3章：SQL查询、JOIN、窗口函数")
    print("  ✓ 第4章：数据仓库、维度建模")
    print("  ✓ 第5章：Excel函数")
    print("  ✓ 第6章：BI工具、图表选型")
    print("  ✓ 第7章：RFM模型、ABC分类、时间序列")
    print("  ✓ 第8章：数据可视化原则")
    print("  ✓ 第9章：Python数据分析")
    print(f"\n📁 文件位置：{input_file}")
    print("💡 刷新浏览器即可查看更新后的题库")

if __name__ == '__main__':
    main()
