#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""精确替换选择题内容"""
import os

def main():
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("精确替换选择题内容...")
    
    # 读取当前文件
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到选择题数据的开始和结束位置
    start_marker = '    // 选择题数据\n    const choiceQuestions = ['
    end_marker = '    // 问题数据\n    const problems = ['
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print("❌ 找不到选择题数据位置")
        return
    
    print(f"找到选择题位置：{start_idx} - {end_idx}")
    
    # 新的选择题数据
    new_choice_data = '''    // 选择题数据
    const choiceQuestions = [
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
        analysis: "商务智能的核心目标是将企业数据转化为知识，帮助企业做出明智的业务经营决策。",
        difficulty: "easy"
      },
      {
        id: 'c2',
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
        id: 'c3',
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
        id: 'c4',
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
        id: 'c5',
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
        id: 'c6',
        chapter: 3,
        title: "选择题6：SQL查询基础",
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
        id: 'c7',
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
        id: 'c8',
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
        id: 'c9',
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
        id: 'c10',
        chapter: 5,
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
        id: 'c11',
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
      }
    ];

    '''
    
    # 替换选择题部分
    content = content[:start_idx] + new_choice_data + content[end_idx:]
    
    # 保存文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 选择题内容精确替换完成！")

if __name__ == '__main__':
    main()
