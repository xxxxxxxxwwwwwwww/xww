#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""继续替换剩余的标题"""
import os

def main():
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("继续替换剩余的题目标题...")
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更多的替换
    more_replacements = [
        ('移动平均预测', 'Python：时间序列移动平均'),
        ('指数平滑预测', 'Python：多维度统计'),
        ('预测方法比较', '四种分析层次'),
        ('预测误差分析', '维度拆解'),
        ('SQL窗口函数：累计销售额', 'SQL窗口函数：累计销售额'),
        ('Python：RFM用户分层', 'Python：RFM用户分层'),
        ('Python：ABC商品分类', 'Python：ABC商品分类'),
        ('库存成本分析', '数据仓库与维度建模'),
        ('库存ABC分类', 'RFM模型'),
        ('供应商选择', 'SQL窗口函数：累计销售额'),
        ('供应商评估', 'Python：时间序列移动平均'),
        ('供应商KPI', 'Python：多维度统计'),
        ('供应商关系管理', 'SQL子查询：高价值客户'),
        ('供应链可视化', '图表选型与应用'),
        ('供应链风险管理', 'Excel与BI工具'),
        ('供应链优化策略', '数据治理与职业拓展')
    ]
    
    for old, new in more_replacements:
        content = content.replace(old, new)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 已完成所有题目标题的替换！")

if __name__ == '__main__':
    main()
