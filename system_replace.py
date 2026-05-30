#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""系统替换供应链内容为商务智能内容"""
import os

def main():
    source_file = '/workspace/courses/supply-chain-analysis.html'
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("系统替换供应链内容为商务智能内容...")
    
    # 读取源文件
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 基本标题替换
    content = content.replace('供应链分析', '商务智能分析')
    
    # 左侧章节标题
    content = content.replace('供应链概述', 'BI基础与SQL')
    content = content.replace('需求预测', '数据分析思维')
    content = content.replace('库存管理', 'SQL高级应用')
    content = content.replace('供应商管理', '商务分析模型')
    content = content.replace('供应链数据分析', '综合应用与工具')
    content = content.replace('供应链风险与优化', '综合应用')
    
    # 左侧题目
    content = content.replace('供应链数据预处理', 'SQL查询：各地区销售额')
    content = content.replace('供应商绩效评估', 'Python：计算同比增长率')
    content = content.replace('供应链基本概念', 'BI概念与价值')
    content = content.replace('供应链核心流程', '数据价值链条')
    content = content.replace('供应链管理目标', 'BI架构与ETL')
    content = content.replace('移动平均预测', 'Python：时间序列移动平均')
    content = content.replace('指数平滑预测', 'Python：多维度统计')
    content = content.replace('预测方法比较', '四种分析层次')
    content = content.replace('预测误差分析', '维度拆解')
    content = content.replace('EOQ经济订货量', 'SQL窗口函数：累计销售额')
    content = content.replace('安全库存计算', 'SQL子查询：高价值客户')
    content = content.replace('库存成本分析', '数据仓库与维度建模')
    content = content.replace('库存ABC分类', 'RFM模型')
    content = content.replace('供应商选择', 'Python：RFM用户分层')
    content = content.replace('供应商评估', 'Python：ABC商品分类')
    content = content.replace('供应商KPI', 'Excel与BI工具')
    content = content.replace('供应商关系管理', '数据治理与职业发展')
    content = content.replace('供应链数据分析', '数据分析实战')
    content = content.replace('供应链可视化', '数据可视化')
    content = content.replace('供应链风险管理', 'Power BI与DAX')
    content = content.replace('供应链优化策略', 'Python数据分析库')
    
    # 保存文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 基础内容替换完成！")

if __name__ == '__main__':
    main()
