#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新考试选择题内容"""

def update_choice_questions(file_path, questions):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到选择题数据部分并替换
    old_start = '''// 考试选择题数据
    const examChoiceQuestions = ['''
    old_end = '''    ];
    
    // 全局变量'''
    
    if old_start in content and old_end in content:
        start_idx = content.find(old_start) + len(old_start)
        end_idx = content.find(old_end, start_idx)
        
        old_questions = content[start_idx:end_idx]
        new_questions = questions
        
        content = content.replace(old_start + old_questions + old_end, 
                                old_start + new_questions + old_end)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ 已更新 {file_path} 的选择题')

# 供应链选择题
supply_choices = '''
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
'''

update_choice_questions('/workspace/courses/supply-chain-analysis-exam.html', supply_choices)

# 商务智能选择题
bi_choices = '''
      {
        id: 11,
        type: "choice",
        title: "选择题1：商务智能概念",
        question: "商务智能（BI）的核心目标是什么？",
        options: {
          A: "收集海量数据",
          B: "将数据转化为知识，帮助做出明智的业务决策",
          C: "开发数据分析软件",
          D: "建立数据库系统"
        },
        answer: "B",
        score: 10
      },
      {
        id: 12,
        type: "choice",
        title: "选择题2：数据仓库",
        question: "数据仓库的主要特点是？",
        options: {
          A: "面向事务、实时更新",
          B: "面向主题、集成、相对稳定、反映历史变化",
          C: "只存储结构化数据",
          D: "主要用于在线交易处理"
        },
        answer: "B",
        score: 10
      },
      {
        id: 13,
        type: "choice",
        title: "选择题3：数据分析",
        question: "以下哪种分析方法用于预测未来趋势？",
        options: {
          A: "描述性分析",
          B: "诊断性分析",
          C: "预测性分析",
          D: "规范性分析"
        },
        answer: "C",
        score: 10
      },
      {
        id: 14,
        type: "choice",
        title: "选择题4：数据可视化",
        question: "以下哪种图表最适合展示数据随时间的变化趋势？",
        options: {
          A: "饼图",
          B: "柱状图",
          C: "折线图",
          D: "散点图"
        },
        answer: "C",
        score: 10
      },
      {
        id: 15,
        type: "choice",
        title: "选择题5：ETL过程",
        question: "ETL过程中的T代表什么？",
        options: {
          A: "传输（Transfer）",
          B: "转换（Transform）",
          C: "测试（Test）",
          D: "时间（Time）"
        },
        answer: "B",
        score: 10
      },
      {
        id: 16,
        type: "choice",
        title: "选择题6：OLAP",
        question: "OLAP（联机分析处理）的主要特点是？",
        options: {
          A: "快速的事务处理",
          B: "复杂的分析查询，支持多维度分析",
          C: "实时数据更新",
          D: "主要用于数据录入"
        },
        answer: "B",
        score: 10
      },
      {
        id: 17,
        type: "choice",
        title: "选择题7：数据挖掘",
        question: "数据挖掘中的聚类分析属于什么类型？",
        options: {
          A: "监督学习",
          B: "无监督学习",
          C: "强化学习",
          D: "深度学习"
        },
        answer: "B",
        score: 10
      },
      {
        id: 18,
        type: "choice",
        title: "选择题8：关键指标",
        question: "KPI代表什么？",
        options: {
          A: "关键绩效指标（Key Performance Indicator）",
          B: "关键流程指标（Key Process Indicator）",
          C: "关键产品指标（Key Product Indicator）",
          D: "关键项目指标（Key Project Indicator）"
        },
        answer: "A",
        score: 10
      },
      {
        id: 19,
        type: "choice",
        title: "选择题9：数据质量",
        question: "以下哪项不属于数据质量的基本要求？",
        options: {
          A: "准确性",
          B: "完整性",
          C: "美观性",
          D: "一致性"
        },
        answer: "C",
        score: 10
      }
'''

update_choice_questions('/workspace/courses/business-intelligence-exam.html', bi_choices)

print('\n✅ 所有选择题已更新完成！')
