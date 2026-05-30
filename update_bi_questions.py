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
    
    # 新的编程题数据
    new_coding_questions = '''const codingQuestions = [
      {
        id: 'bi-code1',
        title: 'SQL查询：计算各地区销售额',
        description: '编写SQL查询语句，计算每个地区的总销售额和订单数量，按销售额降序排列。\n\n假设有三个表：\n- users(user_id, name, region)\n- orders(order_id, user_id, amount, order_date)\n\n请输出地区、总销售额、总订单数。',
        starterCode: `-- 请编写SQL查询
SELECT 
    -- 地区,
    -- 总销售额,
    -- 总订单数
FROM orders
-- 关联users表
-- 按地区分组
-- 按销售额降序排列
;`,
        testCases: [
          {
            input: [[
              {'user_id': 1, 'name': '张三', 'region': '华东'},
              {'user_id': 2, 'name': '李四', 'region': '华北'},
              {'user_id': 3, 'name': '王五', 'region': '华东'}
            ], [
              {'order_id': 101, 'user_id': 1, 'amount': 1000, 'order_date': '2024-01-01'},
              {'order_id': 102, 'user_id': 2, 'amount': 2000, 'order_date': '2024-01-02'},
              {'order_id': 103, 'user_id': 3, 'amount': 1500, 'order_date': '2024-01-03'},
              {'order_id': 104, 'user_id': 1, 'amount': 800, 'order_date': '2024-01-04'}
            ]],
            expected: [
              {'region': '华东', 'total_amount': 2300, 'order_count': 2},
              {'region': '华北', 'total_amount': 2000, 'order_count': 1}
            ]
          }
        ]
      },
      {
        id: 'bi-code2',
        title: 'Python数据分析：计算同比增长率',
        description: '编写Python函数 calculate_growth_rate，计算同比增长率。\n\n参数：\n- current_period: 本期值\n- previous_period: 上期值（去年同期）\n\n返回值：增长率百分比（保留2位小数）',
        starterCode: `def calculate_growth_rate(current_period, previous_period):
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
        testCases: [
          {'input': [1100, 1000], 'expected': 10.0},
          {'input': [900, 1000], 'expected': -10.0},
          {'input': [1250, 1000], 'expected': 25.0}
        ]
      },
      {
        id: 'bi-code3',
        title: 'Python数据处理：RFM用户分层',
        description: '编写Python函数 rfm_classification，对用户进行RFM分层。\n\n参数：\n- users_data: 用户消费数据列表，每个元素是包含user_id、recency、frequency、monetary的字典\n\n返回值：\n- 字典，键为user_id，值为RFM等级（如"高价值"、"潜力用户"等）',
        starterCode: `def rfm_classification(users_data):
    """
    RFM用户分层
    
    Args:
        users_data: 用户消费数据列表
    
    Returns:
        字典，键为user_id，值为RFM等级
    """
    # 请编写代码
    # 根据R、F、M三个指标打分
    # 综合评分进行分层
    pass`,
        testCases: [
          {
            'input': [
              {'user_id': 1, 'recency': 10, 'frequency': 50, 'monetary': 10000},
              {'user_id': 2, 'recency': 100, 'frequency': 5, 'monetary': 500}
            ],
            'expected': {'1': '高价值', '2': '流失风险'}
          }
        ]
      },
      {
        id: 'bi-code4',
        title: 'SQL窗口函数：计算累计销售额',
        description: '编写SQL查询，使用窗口函数计算每日累计销售额。\n\n假设表结构：\n- daily_sales(date, amount)\n\n按日期升序，计算累计销售额。',
        starterCode: `-- 请编写SQL查询
SELECT 
    date,
    amount,
    -- 累计销售额（使用窗口函数）
FROM daily_sales
ORDER BY date ASC
;`,
        testCases: [
          {
            'input': [[
              {'date': '2024-01-01', 'amount': 1000},
              {'date': '2024-01-02', 'amount': 1500},
              {'date': '2024-01-03', 'amount': 1200}
            ]],
            'expected': [
              {'date': '2024-01-01', 'amount': 1000, 'cumulative': 1000},
              {'date': '2024-01-02', 'amount': 1500, 'cumulative': 2500},
              {'date': '2024-01-03', 'amount': 1200, 'cumulative': 3700}
            ]
          }
        ]
      },
      {
        id: 'bi-code5',
        title: 'ABC商品分类',
        description: '编写Python函数 abc_classification，对商品进行ABC分类。\n\n规则：\n- A类：销售额累计占比0-80%的商品\n- B类：销售额累计占比80%-95%的商品\n- C类：销售额累计占比95%-100%的商品\n\n参数：\n- products: 商品销售数据列表，每个元素是包含product_id、sales的字典\n\n返回值：\n- 字典，键为product_id，值为分类（"A"、"B"或"C"）',
        starterCode: `def abc_classification(products):
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
        testCases: [
          {
            'input': [
              {'product_id': 'P1', 'sales': 50000},
              {'product_id': 'P2', 'sales': 25000},
              {'product_id': 'P3', 'sales': 15000},
              {'product_id': 'P4', 'sales': 10000}
            ],
            'expected': {'P1': 'A', 'P2': 'A', 'P3': 'B', 'P4': 'C'}
          }
        ]
      },
      {
        id: 'bi-code6',
        title: 'Python数据聚合：多维度统计',
        description: '编写Python函数 multi_dimension_analysis，进行多维度销售分析。\n\n参数：\n- sales_data: 销售数据列表，每个元素包含region、product、channel、amount\n\n返回值：\n- 字典，按地区和产品维度聚合的总销售额',
        starterCode: `def multi_dimension_analysis(sales_data):
    """
    多维度销售分析
    
    Args:
        sales_data: 销售数据列表
    
    Returns:
        字典，按地区和产品聚合的销售额
    """
    # 请编写代码
    # 使用字典或pandas进行分组聚合
    pass`,
        testCases: [
          {
            'input': [
              {'region': '华东', 'product': '手机', 'channel': '线上', 'amount': 10000},
              {'region': '华东', 'product': '手机', 'channel': '线下', 'amount': 5000},
              {'region': '华北', 'product': '电脑', 'channel': '线上', 'amount': 15000}
            ],
            'expected': {
              ('华东', '手机'): 15000,
              ('华北', '电脑'): 15000
            }
          }
        ]
      },
      {
        id: 'bi-code7',
        title: 'SQL子查询：找出高价值客户',
        description: '编写SQL查询，找出消费金额高于平均值的客户及其订单信息。\n\n表结构：\n- customers(customer_id, name)\n- orders(order_id, customer_id, amount)\n\n输出：客户名称、消费总额（高于平均值）、订单数量',
        starterCode: `-- 请编写SQL查询
SELECT 
    c.name,
    -- 消费总额,
    -- 订单数量
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
-- 筛选消费总额高于平均值
ORDER BY 消费总额 DESC
;`,
        testCases: [
          {
            'input': [[
              {'customer_id': 1, 'name': '张三'},
              {'customer_id': 2, 'name': '李四'},
              {'customer_id': 3, 'name': '王五'}
            ], [
              {'order_id': 101, 'customer_id': 1, 'amount': 1000},
              {'order_id': 102, 'customer_id': 2, 'amount': 500},
              {'order_id': 103, 'customer_id': 3, 'amount': 800},
              {'order_id': 104, 'customer_id': 1, 'amount': 700}
            ]],
            'expected': [
              {'name': '张三', 'total_amount': 1700, 'order_count': 2}
            ]
          }
        ]
      },
      {
        id: 'bi-code8',
        title: 'Python时间序列分析：移动平均',
        description: '编写Python函数 moving_average，计算移动平均值。\n\n参数：\n- data: 数据列表（如每日销售额）\n- window: 窗口大小\n\n返回值：\n- 列表，包含移动平均值（与输入数据等长）',
        starterCode: `def moving_average(data, window):
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
        testCases: [
          {
            'input': [[100, 120, 130, 140, 150], 3],
            'expected': [None, None, 116.67, 130.0, 140.0]
          }
        ]
      }
    ]'''
    
    # 替换选择题数据
    old_choice_start = 'const choiceQuestions = ['
    old_choice_end = ']'
    choice_start_idx = content.find(old_choice_start)
    choice_end_idx = content.find(old_choice_end, choice_start_idx) + len(']')
    
    if choice_start_idx == -1:
        print("❌ 错误：未找到选择题数据")
        return
    
    content = content[:choice_start_idx] + new_choice_questions + content[choice_end_idx:]
    
    # 替换编程题数据
    old_code_start = 'const codingQuestions = ['
    old_code_end = ']'
    code_start_idx = content.find(old_code_start)
    code_end_idx = content.find(old_code_end, code_start_idx) + len(']')
    
    if code_start_idx == -1:
        print("❌ 错误：未找到编程题数据")
        return
    
    content = content[:code_start_idx] + new_coding_questions + content[code_end_idx:]
    
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
    print("  ✓ 第7章：RFM模型、ABC分类")
    print("  ✓ 第8章：数据可视化原则")
    print("  ✓ 第9章：Python数据分析")
    print(f"\n📁 文件位置：{input_file}")
    print("💡 刷新浏览器即可查看更新后的题库")

if __name__ == '__main__':
    main()
