#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""精确替换选择题内容 - 改进版"""
import os

def main():
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("精确替换选择题内容...")
    
    # 读取当前文件
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 查找选择题数据的开始和结束
    start_line = -1
    end_line = -1
    
    for i, line in enumerate(lines):
        if '// 选择题数据' in line:
            start_line = i
        elif start_line != -1 and '// 问题数据' in line:
            end_line = i
            break
    
    if start_line == -1 or end_line == -1:
        print("❌ 找不到选择题数据位置")
        return
    
    print(f"找到选择题位置：第{start_line}行 - 第{end_line}行")
    
    # 新的选择题数据
    new_choice_lines = [
        '    // 选择题数据\n',
        '    const choiceQuestions = [\n',
        '      {\n',
        '        id: \'c1\',\n',
        '        chapter: 1,\n',
        '        title: "选择题1：BI概念与价值",\n',
        '        question: "商务智能（BI）的核心目标是什么？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'收集海量数据\' },\n',
        '          { label: \'B\', text: \'将数据转化为知识，帮助做出明智的业务决策\' },\n',
        '          { label: \'C\', text: \'开发数据分析软件\' },\n',
        '          { label: \'D\', text: \'建立数据库系统\' }\n',
        '        ],\n',
        '        answer: \'B\',\n',
        '        analysis: "商务智能的核心目标是将企业数据转化为知识，帮助企业做出明智的业务经营决策。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c2\',\n',
        '        chapter: 1,\n',
        '        title: "选择题2：数据价值链条",\n',
        '        question: "在数据→信息→知识→决策的价值链条中，哪个环节体现了从经验决策到科学决策的转变？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'数据到信息\' },\n',
        '          { label: \'B\', text: \'信息到知识\' },\n',
        '          { label: \'C\', text: \'知识到决策\' },\n',
        '          { label: \'D\', text: \'数据到决策\' }\n',
        '        ],\n',
        '        answer: \'C\',\n',
        '        analysis: "知识到决策的环节体现了从经验决策到科学决策的转变，因为决策是基于已发现的规律和模式。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c3\',\n',
        '        chapter: 1,\n',
        '        title: "选择题3：BI架构与ETL",\n',
        '        question: "BI核心架构中，ETL代表什么？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'Extract, Transform, Load\' },\n',
        '          { label: \'B\', text: \'Execute, Transfer, Log\' },\n',
        '          { label: \'C\', text: \'Extract, Transfer, Load\' },\n',
        '          { label: \'D\', text: \'Execute, Transform, Log\' }\n',
        '        ],\n',
        '        answer: \'A\',\n',
        '        analysis: "ETL代表Extract（抽取）、Transform（转换）、Load（加载），是数据仓库建设中的核心流程。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c4\',\n',
        '        chapter: 2,\n',
        '        title: "选择题4：四种分析层次",\n',
        '        question: "以下哪个不是描述性分析的特点？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'回答发生了什么\' },\n',
        '          { label: \'B\', text: \'汇总历史数据\' },\n',
        '          { label: \'C\', text: \'预测未来趋势\' },\n',
        '          { label: \'D\', text: \'生成报表和图表\' }\n',
        '        ],\n',
        '        answer: \'C\',\n',
        '        analysis: "预测未来趋势属于预测性分析的范畴，不是描述性分析的特点。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c5\',\n',
        '        chapter: 2,\n',
        '        title: "选择题5：维度拆解",\n',
        '        question: "在维度拆解中，哪个维度用于分析不同地区的销售表现？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'时间维度\' },\n',
        '          { label: \'B\', text: \'地区维度\' },\n',
        '          { label: \'C\', text: \'产品维度\' },\n',
        '          { label: \'D\', text: \'渠道维度\' }\n',
        '        ],\n',
        '        answer: \'B\',\n',
        '        analysis: "地区维度用于分析不同地理区域的销售数据，如华东、华南、华北等。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c6\',\n',
        '        chapter: 3,\n',
        '        title: "选择题6：SQL查询基础",\n',
        '        question: "SQL中用于去重的关键字是？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'UNIQUE\' },\n',
        '          { label: \'B\', text: \'DISTINCT\' },\n',
        '          { label: \'C\', text: \'GROUP BY\' },\n',
        '          { label: \'D\', text: \'WHERE\' }\n',
        '        ],\n',
        '        answer: \'B\',\n',
        '        analysis: "DISTINCT关键字用于去除查询结果中的重复记录。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c7\',\n',
        '        chapter: 3,\n',
        '        title: "选择题7：JOIN查询",\n',
        '        question: "LEFT JOIN和INNER JOIN的主要区别是什么？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'LEFT JOIN返回左表全部记录，INNER JOIN只返回匹配的记录\' },\n',
        '          { label: \'B\', text: \'性能不同\' },\n',
        '          { label: \'C\', text: \'语法不同\' },\n',
        '          { label: \'D\', text: \'没有区别\' }\n',
        '        ],\n',
        '        answer: \'A\',\n',
        '        analysis: "LEFT JOIN会返回左表的全部记录以及右表匹配的记录，而INNER JOIN只返回两表都匹配的记录。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c8\',\n',
        '        chapter: 3,\n',
        '        title: "选择题8：窗口函数",\n',
        '        question: "窗口函数ROW_NUMBER()的作用是什么？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'计算总和\' },\n',
        '          { label: \'B\', text: \'为每一行分配唯一的序号\' },\n',
        '          { label: \'C\', text: \'计算平均值\' },\n',
        '          { label: \'D\', text: \'分组统计\' }\n',
        '        ],\n',
        '        answer: \'B\',\n',
        '        analysis: "ROW_NUMBER()为查询结果的每一行分配一个唯一的序号，可用于排名、分页等场景。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c9\',\n',
        '        chapter: 4,\n',
        '        title: "选择题9：数据仓库与维度建模",\n',
        '        question: "在数据仓库维度建模中，星型模型的特点是？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'只有一张表\' },\n',
        '          { label: \'B\', text: \'事实表在中心，连接多个维度表\' },\n',
        '          { label: \'C\', text: \'所有表都是维度表\' },\n',
        '          { label: \'D\', text: \'表之间没有关联\' }\n',
        '        ],\n',
        '        answer: \'B\',\n',
        '        analysis: "星型模型由一个事实表和多个维度表组成，事实表在中心，维度表围绕在四周，形似星星。",\n',
        '        difficulty: "medium"\n',
        '      },\n',
        '      {\n',
        '        id: \'c10\',\n',
        '        chapter: 5,\n',
        '        title: "选择题10：数据分层",\n',
        '        question: "数据仓库中的ODS层是指？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'汇总数据层\' },\n',
        '          { label: \'B\', text: \'明细数据层\' },\n',
        '          { label: \'C\', text: \'操作数据层\' },\n',
        '          { label: \'D\', text: \'应用数据层\' }\n',
        '        ],\n',
        '        answer: \'C\',\n',
        '        analysis: "ODS（Operational Data Store）是操作数据层，存放原始数据，基本不做清洗转换。",\n',
        '        difficulty: "easy"\n',
        '      },\n',
        '      {\n',
        '        id: \'c11\',\n',
        '        chapter: 5,\n',
        '        title: "选择题11：Excel高级函数",\n',
        '        question: "Excel中哪个函数用于多条件求和？",\n',
        '        options: [\n',
        '          { label: \'A\', text: \'VLOOKUP\' },\n',
        '          { label: \'B\', text: \'SUMIF\' },\n',
        '          { label: \'C\', text: \'SUMIFS\' },\n',
        '          { label: \'D\', text: \'COUNT\' }\n',
        '        ],\n',
        '        answer: \'C\',\n',
        '        analysis: "SUMIFS函数用于根据多个条件对指定区域求和。",\n',
        '        difficulty: "easy"\n',
        '      }\n',
        '    ];\n',
        '\n',
    ]
    
    # 替换选择题部分
    new_lines = lines[:start_line] + new_choice_lines + lines[end_line:]
    
    # 保存文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("✅ 选择题内容精确替换完成！")

if __name__ == '__main__':
    main()
