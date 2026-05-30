#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完全重新创建两个考试文件，确保功能正常"""

def recreate_exam(source_file, target_file, title, return_page, programming_title, programming_desc, programming_answer):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换标题
    content = content.replace('数据分析技术考试', title)
    content = content.replace('数据分析技术', title.replace('考试', ''))
    content = content.replace('data-analysis-tech.html', return_page)
    
    # 替换编程题部分
    old_prog_title = '''title: "编程题：数据清洗",'''
    new_prog_title = f'''title: "{programming_title}",'''
    content = content.replace(old_prog_title, new_prog_title)
    
    # 简化初始代码
    old_code_part = '''code: `# 数据清洗示例
import pandas as pd

# 创建数据
data = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', None, '赵六', '钱七'],
    '年龄': [25, None, 30, 28, 35, 32],
    '城市': ['北京', '上海', None, '广州', '深圳', '上海'],
    '销售额': [1000, 2000, 1500, None, 3000, 2500]
})

print("原始数据：")
print(data)
print("\\n缺失值统计：")
print(data.isnull().sum())

# 处理缺失值
data_clean = data.copy()
data_clean['姓名'] = data_clean['姓名'].fillna('未知')
data_clean['年龄'] = data_clean['年龄'].fillna(data_clean['年龄'].mean())
data_clean['城市'] = data_clean['城市'].fillna('其他')
data_clean['销售额'] = data_clean['销售额'].fillna(data_clean['销售额'].median())

print("\\n清洗后的数据：")
print(data_clean)`,'''
    
    new_code_part = '''code: `# 请编写代码`,'''
    
    content = content.replace(old_code_part, new_code_part)
    
    # 替换参考答案
    old_answer_start = '''answer: `# 数据清洗示例'''
    old_answer_end = '''score: 10'''
    # 找到位置并替换
    if old_answer_start in content:
        answer_start = content.find(old_answer_start)
        answer_end = content.find(old_answer_end, answer_start) + len(old_answer_end)
        old_answer_section = content[answer_start:answer_end]
        
        new_answer_section = f'''answer: {programming_answer},
        score: 10'''
        
        content = content.replace(old_answer_section, new_answer_section)
    
    # 替换题目描述
    old_desc_part = '''description: `<strong>背景：</strong>
某电商平台收集了一些销售数据，但数据存在缺失值。请编写代码完成数据清洗任务。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>识别并统计数据中的缺失值</li>
  <li>使用合适的方法填充缺失值</li>
  <li>输出清洗后的完整数据</li>
</ul>`,'''
    
    new_desc_part = f'''description: {programming_desc},'''
    
    content = content.replace(old_desc_part, new_desc_part)
    
    # 保存文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 已创建 {target_file}')

# 供应链考试数据
supply_title = "供应链数据分析考试"
supply_return = "supply-chain-analysis.html"
supply_prog_title = "编程题：供应链库存分析"
supply_prog_desc = '''`<strong>背景：</strong>
一家零售企业的供应链部门提供了过去12个月的库存数据。请编写代码分析库存周转率。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>创建库存数据</li>
  <li>计算每月的库存周转率</li>
  <li>找出库存周转率最低的月份</li>
  <li>输出分析结果</li>
</ul>`'''
supply_prog_answer = '''`# 创建库存数据
inventory_data = [
    {"month": "1月", "beginning_inventory": 10000, "ending_inventory": 12000, "cogs": 8000},
    {"month": "2月", "beginning_inventory": 12000, "ending_inventory": 9000, "cogs": 7500},
    {"month": "3月", "beginning_inventory": 9000, "ending_inventory": 11000, "cogs": 9000},
    {"month": "4月", "beginning_inventory": 11000, "ending_inventory": 13000, "cogs": 8500},
    {"month": "5月", "beginning_inventory": 13000, "ending_inventory": 14000, "cogs": 10000},
    {"month": "6月", "beginning_inventory": 14000, "ending_inventory": 16000, "cogs": 12000},
    {"month": "7月", "beginning_inventory": 16000, "ending_inventory": 18000, "cogs": 14000},
    {"month": "8月", "beginning_inventory": 18000, "ending_inventory": 15000, "cogs": 13000},
    {"month": "9月", "beginning_inventory": 15000, "ending_inventory": 13000, "cogs": 11000},
    {"month": "10月", "beginning_inventory": 13000, "ending_inventory": 12000, "cogs": 9500},
    {"month": "11月", "beginning_inventory": 12000, "ending_inventory": 14000, "cogs": 10500},
    {"month": "12月", "beginning_inventory": 14000, "ending_inventory": 11000, "cogs": 11500}
]

# 计算每月的库存周转率
turnover_rates = []
for data in inventory_data:
    avg_inventory = (data["beginning_inventory"] + data["ending_inventory"]) / 2
    turnover = data["cogs"] / avg_inventory
    turnover_rates.append({"month": data["month"], "turnover": turnover})
    print(f"{data['month']}库存周转率: {turnover:.2f}")

# 找出库存周转率最低的月份
lowest_turnover = min(turnover_rates, key=lambda x: x["turnover"])
print(f"\\n库存周转率最低的月份: {lowest_turnover['month']}, 周转率: {lowest_turnover['turnover']:.2f}")`'''

recreate_exam(
    '/workspace/courses/data-analysis-exam.html',
    '/workspace/courses/supply-chain-analysis-exam.html',
    supply_title,
    supply_return,
    supply_prog_title,
    supply_prog_desc,
    supply_prog_answer
)

# 商务智能考试数据
bi_title = "商务智能分析考试"
bi_return = "business-intelligence.html"
bi_prog_title = "编程题：销售数据分析"
bi_prog_desc = '''`<strong>背景：</strong>
一家企业的销售部门提供了销售数据，请编写代码分析销售情况。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>创建销售数据</li>
  <li>计算总销售额</li>
  <li>计算平均销售额</li>
  <li>按地区统计销售额</li>
</ul>`'''
bi_prog_answer = '''`# 创建销售数据
sales_data = [
    {"date": "2024-01-01", "region": "华东", "category": "电子产品", "amount": 5000},
    {"date": "2024-01-02", "region": "华南", "category": "服装", "amount": 3000},
    {"date": "2024-01-03", "region": "华北", "category": "电子产品", "amount": 8000},
    {"date": "2024-01-04", "region": "华东", "category": "食品", "amount": 2000},
    {"date": "2024-01-05", "region": "华南", "category": "电子产品", "amount": 6000}
]

# 计算总销售额
total_sales = sum(item["amount"] for item in sales_data)
print(f"总销售额: {total_sales}元")

# 计算平均销售额
avg_sales = total_sales / len(sales_data)
print(f"平均销售额: {avg_sales:.2f}元")

# 按地区统计销售额
region_sales = {}
for item in sales_data:
    region = item["region"]
    if region not in region_sales:
        region_sales[region] = 0
    region_sales[region] += item["amount"]

print("\\n各地区销售额:")
for region, amount in region_sales.items():
    print(f"{region}: {amount}元")`'''

recreate_exam(
    '/workspace/courses/data-analysis-exam.html',
    '/workspace/courses/business-intelligence-exam.html',
    bi_title,
    bi_return,
    bi_prog_title,
    bi_prog_desc,
    bi_prog_answer
)

print('\n✅ 所有考试文件已重新创建完成！')
