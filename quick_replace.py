#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正确地替换商务智能课程的所有内容"""
import os

def main():
    source_file = '/workspace/courses/supply-chain-analysis.html'
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("开始修复商务智能课程...")
    
    # 第一步：复制源文件内容
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换页面标题
    content = content.replace('供应链分析', '商务智能分析')
    
    # 替换章节标题
    replacements = [
        ('供应链概述', 'BI基础与SQL'],
        ('需求预测', '数据分析思维'],
        ('库存管理', 'SQL高级应用'],
        ('供应商管理', '商务分析模型'],
        ('供应链数据分析', '综合应用与工具'],
        ('供应链风险与优化', '综合应用'],
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    # 替换编程题标题
    programming_replacements = [
        ('供应链数据预处理', 'SQL查询：各地区销售额'),
        ('供应商绩效评估', 'Python：计算同比增长率'),
        ('移动平均预测', 'Python：多维度统计'),
        ('指数平滑预测', 'SQL窗口函数：累计销售额'),
        ('EOQ经济订货量', 'SQL子查询：高价值客户'),
        ('安全库存计算', 'Python：RFM用户分层'),
        ('供应商选择', 'Python：ABC商品分类'),
        ('供应商评估', 'Python：时间序列移动平均'),
        ('供应链数据分析', '数据分析实战'),
        ('供应链可视化', '数据可视化'),
    ]
    
    for old, new in programming_replacements:
        content = content.replace(old, new)
    
    # 替换选择题标题
    choice_replacements = [
        ('供应链基本概念', 'BI概念与价值'],
        ('供应链核心流程', '数据价值链条'],
        ('供应链管理目标', 'BI架构与ETL'],
        ('预测方法比较', '四种分析层次'],
        ('预测误差分析', '维度拆解'],
        ('库存成本分析', 'SQL查询基础'],
        ('库存ABC分类', 'JOIN查询'],
        ('供应商KPI', '窗口函数'],
        ('供应商关系管理', '数据仓库与维度建模'],
        ('供应链风险管理', '数据分层'],
        ('供应链优化策略', 'Excel高级函数'],
    ]
    
    for old, new in choice_replacements:
        content = content.replace(old, new)
    
    # 保存
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("基础替换完成！现在需要更新具体内容...")

if __name__ == '__main__':
    main()
