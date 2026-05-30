#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""直接替换所有供应链相关的文本"""
import os

def main():
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("开始逐个替换所有供应链相关文本...")
    
    # 读取文件
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 基础替换
    replacements = [
        ('供应链数据预处理', 'SQL查询：各地区销售额'),
        ('供应商绩效评估', 'Python：计算同比增长率'),
        ('供应链基本概念', 'BI概念与价值'),
        ('供应链核心流程', '数据价值链条'),
        ('供应链管理目标', 'BI架构与ETL'),
        ('供应链概述', 'BI基础与SQL'),
        ('需求预测', '数据分析思维'),
        ('库存管理', 'SQL高级应用'),
        ('供应商管理', '商务分析模型'),
        ('供应链数据分析', '综合应用与工具'),
        ('供应链风险与优化', '综合应用'),
        ('EOQ经济订货量', 'Python：RFM用户分层'),
        ('安全库存计算', 'Python：ABC商品分类'),
        ('库存成本分析', '数据仓库与维度建模'),
        ('库存ABC分类', 'RFM模型'),
        ('供应商选择', 'SQL窗口函数：累计销售额'),
        ('供应商评估', 'Python：时间序列移动平均'),
        ('供应商KPI', 'Python：多维度统计'),
        ('供应商关系管理', 'SQL子查询：高价值客户'),
        ('供应链可视化', '图表选型与应用'),
        ('问题1：供应链数据预处理', 'SQL查询：各地区销售额'),
        ('包含缺失值和异常值的供应链数据', '分析不同地区的销售表现')
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    # 保存
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 已替换所有题目标题！")

if __name__ == '__main__':
    main()
