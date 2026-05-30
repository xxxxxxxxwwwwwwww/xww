#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正确修复两个考试文件"""

# 1. 首先确保商务智能考试是正确的（已经从备份恢复）
# 2. 修改供应链考试文件，把内容改成供应链的

with open('/workspace/courses/business-intelligence-exam-page.html', 'r', encoding='utf-8') as f:
    bi_content = f.read()

# 复制一份作为供应链考试，然后修改
supply_content = bi_content.replace('商务智能分析', '供应链数据分析')
supply_content = supply_content.replace('business-intelligence.html', 'supply-chain-analysis.html')

# 替换供应链考试的编程题
old_bi_code = '''        code: `# 请编写代码`,
        answer: ``,'''
old_bi_desc = '''        description: `综合运用所学知识，完成一个完整的商务智能分析任务。

<strong>背景：</strong>
一家电商公司提供了销售数据，请对这份数据进行完整的商务智能分析。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>创建销售数据</li>
  <li>进行KPI分析</li>
  <li>输出分析结果</li>
</ul>`,'''
old_bi_title = '''        title: "编程题：商务智能分析",'''

new_supply_title = '''        title: "编程题：供应链库存分析",'''
new_supply_desc = '''        description: `综合运用所学知识，完成一个完整的供应链分析任务。

<strong>背景：</strong>
一家零售企业的供应链部门提供了过去12个月的库存数据，请编写代码分析库存周转率。

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>创建库存数据</li>
  <li>计算每月的库存周转率</li>
  <li>找出库存周转率最低的月份</li>
  <li>输出分析结果</li>
</ul>`,'''
new_supply_code = '''        code: `# 请编写代码`,
        answer: `# 创建库存数据
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

supply_content = supply_content.replace(old_bi_title, new_supply_title)
supply_content = supply_content.replace(old_bi_desc, new_supply_desc)
supply_content = supply_content.replace(old_bi_code, new_supply_code)

# 替换供应链考试的选择题
old_bi_choices = '''    // 考试选择题数据
    const examChoiceQuestions = [
      {
        id: 11,
        type: "choice",
        title: "选择题1：BI工具",
        question: "以下哪个是常用的BI可视化工具？",
        options: {
          A: "MySQL",
          B: "Tableau",
          C: "Git",
          D: "Docker"
        },
        answer: "B",
        score: 10
      },
      {
        id: 12,
        type: "choice",
        title: "选择题2：仪表板设计",
        question: "BI仪表板设计的黄金法则不包括以下哪项？",
        options: {
          A: "简洁清晰",
          B: "信息过载",
          C: "视觉层次分明",
          D: "交互式探索"
        },
        answer: "B",
        score: 10
      },
      {
        id: 13,
        type: "choice",
        title: "选择题3：多维分析",
        question: "在多维数据模型中，时间维度通常属于什么类型的维度？",
        options: {
          A: "缓慢变化维度",
          B: "快速变化维度",
          C: "固定维度",
          D: "退化维度"
        },
        answer: "A",
        score: 10
      },
      {
        id: 14,
        type: "choice",
        title: "选择题4：数据可视化原则",
        question: "当需要展示各部分占总体的比例关系时，最适合使用哪种图表？",
        options: {
          A: "条形图",
          B: "饼图",
          C: "雷达图",
          D: "热力图"
        },
        answer: "B",
        score: 10
      },
      {
        id: 15,
        type: "choice",
        title: "选择题5：BI架构",
        question: "BI系统架构中，哪个层负责数据的抽取、转换和加载？",
        options: {
          A: "数据源层",
          B: "ETL层",
          C: "数据仓库层",
          D: "分析展示层"
        },
        answer: "B",
        score: 10
      },
      {
        id: 16,
        type: "choice",
        title: "选择题6：OLAP多维立方体",
        question: "OLAP立方体的三个基本操作是？",
        options: {
          A: "创建、读取、更新",
          B: "切片、切块、旋转",
          C: "查询、过滤、排序",
          D: "插入、删除、修改"
        },
        answer: "B",
        score: 10
      },
      {
        id: 17,
        type: "choice",
        title: "选择题7：数据集市",
        question: "数据集市与数据仓库的主要区别是什么？",
        options: {
          A: "数据集市更大",
          B: "数据集市面向特定业务部门",
          C: "数据集市不包含历史数据",
          D: "数据集市不需要ETL"
        },
        answer: "B",
        score: 10
      },
      {
        id: 18,
        type: "choice",
        title: "选择题8：BI报表",
        question: "以下哪种报表适合用于高级管理人员快速了解业务概况？",
        options: {
          A: "明细报表",
          B: "汇总报表",
          C: "即席查询报表",
          D: "仪表盘"
        },
        answer: "D",
        score: 10
      },
      {
        id: 19,
        type: "choice",
        title: "选择题9：自助BI",
        question: "自助BI的核心优势是什么？",
        options: {
          A: "降低IT部门负担，让业务人员自主分析",
          B: "提高数据安全性",
          C: "减少数据存储量",
          D: "加快数据加载速度"
        },
        answer: "A",
        score: 10
      }
    ];'''

new_supply_choices = '''    // 考试选择题数据
    const examChoiceQuestions = [
      {
        id: 11,
        type: "choice",
        title: "选择题1：供应链管理目标",
        question: "供应链管理的核心目标是什么？",
        options: {
          A: "最大化利润",
          B: "以最低成本满足客户需求",
          C: "提高生产效率",
          D: "扩大市场份额"
        },
        answer: "B",
        score: 10
      },
      {
        id: 12,
        type: "choice",
        title: "选择题2：需求预测",
        question: "以下哪种预测方法适合新产品的需求预测？",
        options: {
          A: "时间序列分析法",
          B: "德尔菲法",
          C: "移动平均法",
          D: "指数平滑法"
        },
        answer: "B",
        score: 10
      },
      {
        id: 13,
        type: "choice",
        title: "选择题3：库存管理",
        question: "JIT（准时制生产）的核心思想是什么？",
        options: {
          A: "大量库存以应对需求波动",
          B: "消除浪费，只在需要时生产",
          C: "增加安全库存",
          D: "批量生产降低成本"
        },
        answer: "B",
        score: 10
      },
      {
        id: 14,
        type: "choice",
        title: "选择题4：供应商管理",
        question: "供应商评价的Kraljic矩阵主要考虑哪两个维度？",
        options: {
          A: "价格和质量",
          B: "供应风险和利润影响",
          C: "交货时间和服务",
          D: "距离和规模"
        },
        answer: "B",
        score: 10
      },
      {
        id: 15,
        type: "choice",
        title: "选择题5：物流配送",
        question: "以下哪种运输方式最适合长距离、大批量货物运输？",
        options: {
          A: "公路运输",
          B: "铁路运输",
          C: "航空运输",
          D: "水路运输"
        },
        answer: "D",
        score: 10
      },
      {
        id: 16,
        type: "choice",
        title: "选择题6：供应链协调",
        question: "牛鞭效应主要是由什么原因引起的？",
        options: {
          A: "需求信息在供应链中被逐级放大",
          B: "供应商产能不足",
          C: "物流成本过高",
          D: "产品质量问题"
        },
        answer: "A",
        score: 10
      },
      {
        id: 17,
        type: "choice",
        title: "选择题7：采购策略",
        question: "以下哪种采购策略适合标准化、大批量的物资？",
        options: {
          A: "单一来源采购",
          B: "多供应商采购",
          C: "集中采购",
          D: "分散采购"
        },
        answer: "C",
        score: 10
      },
      {
        id: 18,
        type: "choice",
        title: "选择题8：供应链绩效",
        question: "库存周转率的计算公式是？",
        options: {
          A: "销售成本 / 平均库存",
          B: "销售收入 / 平均库存",
          C: "平均库存 / 销售成本",
          D: "平均库存 / 销售收入"
        },
        answer: "A",
        score: 10
      },
      {
        id: 19,
        type: "choice",
        title: "选择题9：供应链风险",
        question: "以下哪项不属于供应链外部风险？",
        options: {
          A: "自然灾害",
          B: "政治风险",
          C: "供应商违约",
          D: "市场需求波动"
        },
        answer: "C",
        score: 10
      }
    ];'''

supply_content = supply_content.replace(old_bi_choices, new_supply_choices)

# 给商务智能考试添加完整的参考答案
new_bi_answer = '''        answer: `# 创建销售数据
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

bi_content = bi_content.replace('        answer: ``,', new_bi_answer)

# 保存文件
with open('/workspace/courses/business-intelligence-exam.html', 'w', encoding='utf-8') as f:
    f.write(bi_content)

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(supply_content)

print('✅ 商务智能考试文件已更新，包含完整的参考答案')
print('✅ 供应链考试文件已创建，包含供应链相关内容')
print('\n🎉 所有考试文件已正确修复！')
