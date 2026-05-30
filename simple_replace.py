#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""直接复制供应链分析页面并替换为商务智能内容"""
import os

def main():
    source_file = '/workspace/courses/supply-chain-analysis.html'
    target_file = '/workspace/courses/business-intelligence.html'
    backup_file = '/workspace/courses/business-intelligence-simple-backup.html'
    
    print("开始修复 - 直接复制供应链分析模板并替换...")
    
    # 读取供应链分析文件
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份当前商务智能文件
    with open(backup_file, 'w', encoding='utf-8') as f:
        with open(target_file, 'r', encoding='utf-8') as f2:
            f.write(f2.read())
    
    print(f"✅ 已备份到: {backup_file}")
    
    # 替换标题和名称
    content = content.replace('供应链分析', '商务智能分析')
    content = content.replace('供应链', '商务智能')
    
    # 保存文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 已完成基础模板复制！现在需要更新练习题数据部分")
    
    # 现在我需要手动替换里面的题目数据
    # 读取刚才创建的有更新题目的内容来替换这个模板中的题目数据
    
if __name__ == '__main__':
    main()
