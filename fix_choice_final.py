#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""直接读取和替换选择题数据"""
import os

def main():
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("修复选择题数据格式...")
    
    # 读取整个文件
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 找到选择题数据的开始和结束位置
    start_line = -1
    end_line = -1
    for i, line in enumerate(lines):
        if '// 选择题数据' in line and 'const choiceQuestions = [' in lines[i+1]:
            start_line = i + 1
        elif start_line != -1 and 'const' in line and i > start_line + 10:
            # 找到下一个const声明
            if 'problems' in line:
                end_line = i
                break
    
    if start_line == -1 or end_line == -1:
        print("❌ 找不到位置！")
        return
    
    print(f"找到选择题数据：第{start_line}行 - 第{end_line}行")
    
    # 新的选择题数据
    new_choice_data = '''    // 选择题数据
    const choiceQuestions = [
      {
        id: 'bi-cq1',
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
        analysis: "商务智能的核心目标是将企业数据转化为知识，帮助企业做出明智的业务经营决策。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq2',
        chapter: 1,
        title: "选择题2：数据价值链条",
        question: "在数据→信息→知识→决策的价值链条中，哪个环节体现了从经验决策到科学决策的转变？",
        options: [
          { label: 'A', text: '数据到信息' },
          { label: 'B', text: '信息到知识' },
          { label: 'C', text: '知识到决策' },
          { label: 'D', text: '数据到决策' }
        ],
        answer: 'C',
        analysis: "知识到决策的环节体现了从经验决策到科学决策的转变，因为决策是基于已发现的规律和模式。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq3',
        chapter: 1,
        title: "选择题3：BI架构与ETL",
        question: "BI核心架构中，ETL代表什么？",
        options: [
          { label: 'A', text: 'Extract, Transform, Load' },
          { label: 'B', text: 'Execute, Transfer, Log' },
          { label: 'C', text: 'Extract, Transfer, Load' },
          { label: 'D', text: 'Execute, Transform, Log' }
        ],
        answer: 'A',
        analysis: "ETL代表Extract（抽取）、Transform（转换）、Load（加载），是数据仓库建设中的核心流程。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq4',
        chapter: 2,
        title: "选择题4：四种分析层次",
        question: "以下哪个不是描述性分析的特点？",
        options: [
          { label: 'A', text: '回答发生了什么' },
          { label: 'B', text: '汇总历史数据' },
          { label: 'C', text: '预测未来趋势' },
          { label: 'D', text: '生成报表和图表' }
        ],
        answer: 'C',
        analysis: "预测未来趋势属于预测性分析的范畴，不是描述性分析的特点。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq5',
        chapter: 2,
        title: "选择题5：维度拆解",
        question: "在维度拆解中，哪个维度用于分析不同地区的销售表现？",
        options: [
          { label: 'A', text: '时间维度' },
          { label: 'B', text: '地区维度' },
          { label: 'C', text: '产品维度' },
          { label: 'D', text: '渠道维度' }
        ],
        answer: 'B',
        analysis: "地区维度用于分析不同地理区域的销售数据，如华东、华南、华北等。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq6',
        chapter: 3,
        title: "选择题6：SQL基础",
        question: "SQL中用于去重的关键字是？",
        options: [
          { label: 'A', text: 'UNIQUE' },
          { label: 'B', text: 'DISTINCT' },
          { label: 'C', text: 'GROUP BY' },
          { label: 'D', text: 'WHERE' }
        ],
        answer: 'B',
        analysis: "DISTINCT关键字用于去除查询结果中的重复记录。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq7',
        chapter: 3,
        title: "选择题7：JOIN查询",
        question: "LEFT JOIN和INNER JOIN的主要区别是什么？",
        options: [
          { label: 'A', text: 'LEFT JOIN返回左表全部记录，INNER JOIN只返回匹配的记录' },
          { label: 'B', text: '性能不同' },
          { label: 'C', text: '语法不同' },
          { label: 'D', text: '没有区别' }
        ],
        answer: 'A',
        analysis: "LEFT JOIN会返回左表的全部记录以及右表匹配的记录，而INNER JOIN只返回两表都匹配的记录。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq8',
        chapter: 3,
        title: "选择题8：窗口函数",
        question: "窗口函数ROW_NUMBER()的作用是什么？",
        options: [
          { label: 'A', text: '计算总和' },
          { label: 'B', text: '为每一行分配唯一的序号' },
          { label: 'C', text: '计算平均值' },
          { label: 'D', text: '分组统计' }
        ],
        answer: 'B',
        analysis: "ROW_NUMBER()为查询结果的每一行分配一个唯一的序号，可用于排名、分页等场景。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq9',
        chapter: 4,
        title: "选择题9：数据仓库与维度建模",
        question: "在数据仓库维度建模中，星型模型的特点是？",
        options: [
          { label: 'A', text: '只有一张表' },
          { label: 'B', text: '事实表在中心，连接多个维度表' },
          { label: 'C', text: '所有表都是维度表' },
          { label: 'D', text: '表之间没有关联' }
        ],
        answer: 'B',
        analysis: "星型模型由一个事实表和多个维度表组成，事实表在中心，维度表围绕在四周，形似星星。",
        difficulty: "medium"
      },
      {
        id: 'bi-cq10',
        chapter: 4,
        title: "选择题10：数据分层",
        question: "数据仓库中的ODS层是指？",
        options: [
          { label: 'A', text: '汇总数据层' },
          { label: 'B', text: '明细数据层' },
          { label: 'C', text: '操作数据层' },
          { label: 'D', text: '应用数据层' }
        ],
        answer: 'C',
        analysis: "ODS（Operational Data Store）是操作数据层，存放原始数据，基本不做清洗转换。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq11',
        chapter: 5,
        title: "选择题11：Excel高级函数",
        question: "Excel中哪个函数用于多条件求和？",
        options: [
          { label: 'A', text: 'VLOOKUP' },
          { label: 'B', text: 'SUMIF' },
          { label: 'C', text: 'SUMIFS' },
          { label: 'D', text: 'COUNT' }
        ],
        answer: 'C',
        analysis: "SUMIFS函数用于根据多个条件对指定区域求和。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq12',
        chapter: 4,
        title: "选择题12：RFM模型",
        question: "RFM模型中，R代表什么？",
        options: [
          { label: 'A', text: '消费金额' },
          { label: 'B', text: '消费频率' },
          { label: 'C', text: '最近一次消费时间' },
          { label: 'D', text: '客户等级' }
        ],
        answer: 'C',
        analysis: "RFM模型中，R代表Recency（最近一次消费时间），用于衡量客户的活跃度。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq13',
        chapter: 4,
        title: "选择题13：ABC分类法",
        question: "ABC分类法中，A类商品通常占销售额的比例是？",
        options: [
          { label: 'A', text: '50%' },
          { label: 'B', text: '60%' },
          { label: 'C', text: '80%' },
          { label: 'D', text: '20%' }
        ],
        answer: 'C',
        analysis: "ABC分类法中，A类商品通常占销售总额的80%，但数量只占20%，需要重点管理。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq14',
        chapter: 5,
        title: "选择题14：Power BI与DAX",
        question: "Power BI中，DAX是指什么？",
        options: [
          { label: 'A', text: '数据清洗语言' },
          { label: 'B', text: '数据分析表达式' },
          { label: 'C', text: '数据库查询语言' },
          { label: 'D', text: '数据可视化语言' }
        ],
        answer: 'B',
        analysis: "DAX（Data Analysis Expressions）是Power BI中的数据分析表达式语言，用于创建计算列和度量值。",
        difficulty: "medium"
      },
      {
        id: 'bi-cq15',
        chapter: 5,
        title: "选择题15：Python数据分析库",
        question: "Python中用于数据处理的核心库是？",
        options: [
          { label: 'A', text: 'NumPy' },
          { label: 'B', text: 'Pandas' },
          { label: 'C', text: 'Matplotlib' },
          { label: 'D', text: 'Scikit-learn' }
        ],
        answer: 'B',
        analysis: "Pandas是Python中用于数据处理和分析的核心库，提供了DataFrame数据结构。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq16',
        chapter: 3,
        title: "选择题16：同比环比计算",
        question: "同比增长率的计算公式是？",
        options: [
          { label: 'A', text: '(本期值 - 上期值) / 上期值 × 100%' },
          { label: 'B', text: '(本期值 - 上期值) / 本期值 × 100%' },
          { label: 'C', text: '上期值 / 本期值 × 100%' },
          { label: 'D', text: '本期值 / 上期值 × 100%' }
        ],
        answer: 'A',
        analysis: "同比增长率 = (本期值 - 上期值) / 上期值 × 100%，反映与去年同期相比的增长情况。",
        difficulty: "medium"
      },
      {
        id: 'bi-cq17',
        chapter: 3,
        title: "选择题17：SQL聚合函数",
        question: "在SQL聚合函数中，哪个函数用于计算平均值？",
        options: [
          { label: 'A', text: 'SUM' },
          { label: 'B', text: 'COUNT' },
          { label: 'C', text: 'AVG' },
          { label: 'D', text: 'MAX' }
        ],
        answer: 'C',
        analysis: "AVG函数用于计算指定字段的平均值。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq18',
        chapter: 5,
        title: "选择题18：数据可视化原则",
        question: "数据可视化的首要原则是？",
        options: [
          { label: 'A', text: '使用最复杂的图表' },
          { label: 'B', text: '使用多种颜色' },
          { label: 'C', text: '清晰准确地传达信息' },
          { label: 'D', text: '展示所有数据' }
        ],
        answer: 'C',
        analysis: "数据可视化的首要原则是清晰准确地传达信息，让观众快速理解数据背后的含义。",
        difficulty: "easy"
      },
      {
        id: 'bi-cq19',
        chapter: 3,
        title: "选择题19：窗口函数应用",
        question: "在窗口函数中，LAG函数的作用是？",
        options: [
          { label: 'A', text: '获取前N行的值' },
          { label: 'B', text: '获取后N行的值' },
          { label: 'C', text: '计算排名' },
          { label: 'D', text: '计算聚合值' }
        ],
        answer: 'A',
        analysis: "LAG函数用于获取当前行之前的第N行数据，常用于计算同比、环比等。",
        difficulty: "medium"
      },
      {
        id: 'bi-cq20',
        chapter: 5,
        title: "选择题20：数据治理",
        question: "数据治理的主要目标是什么？",
        options: [
          { label: 'A', text: '收集更多数据' },
          { label: 'B', text: '建立数据标准，确保数据质量和安全' },
          { label: 'C', text: '开发数据系统' },
          { label: 'D', text: '培训数据人才' }
        ],
        answer: 'B',
        analysis: "数据治理的主要目标是建立数据标准、规范数据管理流程，确保数据质量和安全。",
        difficulty: "easy"
      }
    ]
    '''
    
    # 替换内容
    new_lines = new_choice_data.splitlines(keepends=True)
    
    # 替换
    lines = lines[:start_line] + new_lines + lines[end_line:]
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("✅ 已修复选择题数据格式！")

if __name__ == '__main__':
    main()
