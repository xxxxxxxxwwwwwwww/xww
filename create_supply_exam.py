#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""基于python-exam.html重新创建供应链考试"""

with open('/workspace/courses/python-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修改标题和导航
content = content.replace('Python考试', '供应链数据分析考试')
content = content.replace('python-basics.html', 'supply-chain-analysis.html')

# 修改HTML中的标题
content = content.replace('<h2 class="text-2xl font-bold text-gray-200 mb-6">Python考试</h2>',
                         '<h2 class="text-2xl font-bold text-gray-200 mb-6">供应链数据分析考试</h2>')

# 修改编程题
old_prog_title = '''title: "编程题：字符串处理",'''
new_prog_title = '''title: "编程题：供应链库存分析",'''
content = content.replace(old_prog_title, new_prog_title)

old_desc = '''description: `请编写一个Python函数，实现字符串的去重和排序功能。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>接收一个字符串参数</li>
  <li>去除字符串中的重复字符</li>
  <li>按字母顺序排列剩余字符</li>
  <li>返回处理后的字符串</li>
</ul>`,'''
new_desc = '''description: `一家零售企业的供应链部门提供了过去12个月的库存数据。请编写代码分析库存周转率。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>创建库存数据</li>
  <li>计算每月的库存周转率</li>
  <li>找出库存周转率最低的月份</li>
  <li>输出分析结果</li>
</ul>`,'''
content = content.replace(old_desc, new_desc)

# 简化初始代码
old_code = '''code: `# 请在这里编写代码
def process_string(s):
    # 实现字符串去重和排序
    pass

# 测试
result = process_string("bcaabac")
print(result)  # 应该输出: abc`,'''
new_code = '''code: `# 请编写代码`,'''
content = content.replace(old_code, new_code)

# 修改参考答案
old_answer = '''answer: `# 请在这里编写代码
def process_string(s):
    # 实现字符串去重和排序
    # 去重：使用set
    unique_chars = set(s)
    # 排序：转换为列表并排序
    sorted_chars = sorted(unique_chars)
    # 拼接成字符串
    return ''.join(sorted_chars)

# 测试
result = process_string("bcaabac")
print(result)  # 应该输出: abc`,'''
new_answer = '''answer: `# 创建库存数据
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
print(f"\\n库存周转率最低的月份: {lowest_turnover['month']}, 周转率: {lowest_turnover['turnover']:.2f}")`,'''
content = content.replace(old_answer, new_answer)

# 修改选择题（这里简单修改前几道）
old_choices = [
    ('选择题1：变量命名', '以下哪个是正确的Python变量命名？', 'A: 以数字开头', 'B: 包含字母、数字和下划线'),
    ('选择题2：数据类型', 'Python中列表和元组的主要区别是？', 'A: 列表可修改，元组不可修改', 'B: 列表不可修改，元组可修改'),
]

new_choices = [
    ('选择题1：供应链管理目标', '供应链管理的核心目标是什么？', 'A: 最大化利润', 'B: 以最低成本满足客户需求'),
    ('选择题2：需求预测', '以下哪种预测方法适合新产品的需求预测？', 'A: 时间序列分析法', 'B: 德尔菲法'),
]

for i, (old_title, old_q, old_a, old_b) in enumerate(old_choices):
    new_title, new_q, new_a, new_b = new_choices[i]
    content = content.replace(f'title: "{old_title}",\n        question: "{old_q}",', f'title: "{new_title}",\n        question: "{new_q}",')
    content = content.replace(f'A: "{old_a}",\n          B: "{old_b}",', f'A: "{new_a}",\n          B: "{new_b}",')

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 供应链考试文件已基于python-exam.html重新创建')
