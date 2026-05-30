#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""直接修复编程题初始代码"""

def fix_code(file_path, old_code_part, new_code_part):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换代码
    if old_code_part in content:
        content = content.replace(old_code_part, new_code_part)
        print(f'✅ 已替换 {file_path} 中的代码')
    else:
        print(f'⚠️ 未找到代码，尝试寻找部分匹配...')
        # 尝试寻找部分匹配
        if 'inventory_data = [' in content:
            print('  → 找到库存数据代码，进行替换')
            # 找到code部分的范围
            code_start = content.find('code: `# 创建库存数据')
            if code_start != -1:
                code_end = content.find('answer: `', code_start)
                if code_end != -1:
                    old_code = content[code_start:code_end]
                    content = content.replace(old_code, 'code: `# 请编写代码`,\n        ')
                    print(f'  → 已成功替换为简化代码')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 供应链考试 - 替换库存数据代码
supply_old = '''code: `# 创建库存数据
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

supply_new = '''code: `# 请编写代码`,'''

fix_code('/workspace/courses/supply-chain-analysis-exam.html', supply_old, supply_new)

# 商务智能考试 - 替换销售数据代码
bi_old = '''code: `# 创建销售数据
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
    print(f"{region}: {amount}元")`,'''

bi_new = '''code: `# 请编写代码`,'''

fix_code('/workspace/courses/business-intelligence-exam.html', bi_old, bi_new)

print('\n✅ 所有编程题初始代码已简化！')
