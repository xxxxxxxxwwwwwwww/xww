#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复选择题点击事件ID与数据ID不匹配的问题"""
import os

def main():
    target_file = '/workspace/courses/business-intelligence.html'
    
    print("修复选择题ID匹配问题...")
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换点击事件中的ID
    id_replacements = [
        ("loadChoiceQuestion('c1')", "loadChoiceQuestion('bi-cq1')"),
        ("loadChoiceQuestion('c2')", "loadChoiceQuestion('bi-cq2')"),
        ("loadChoiceQuestion('c3')", "loadChoiceQuestion('bi-cq3')"),
        ("loadChoiceQuestion('c4')", "loadChoiceQuestion('bi-cq4')"),
        ("loadChoiceQuestion('c5')", "loadChoiceQuestion('bi-cq5')"),
        ("loadChoiceQuestion('c6')", "loadChoiceQuestion('bi-cq6')"),
        ("loadChoiceQuestion('c7')", "loadChoiceQuestion('bi-cq7')"),
        ("loadChoiceQuestion('c8')", "loadChoiceQuestion('bi-cq8')"),
        ("loadChoiceQuestion('c9')", "loadChoiceQuestion('bi-cq9')"),
        ("loadChoiceQuestion('c10')", "loadChoiceQuestion('bi-cq10')"),
        ("loadChoiceQuestion('c11')", "loadChoiceQuestion('bi-cq11')"),
        ("loadChoiceQuestion('c12')", "loadChoiceQuestion('bi-cq12')"),
        ("loadChoiceQuestion('c13')", "loadChoiceQuestion('bi-cq13')"),
        ("loadChoiceQuestion('c14')", "loadChoiceQuestion('bi-cq14')"),
        ("loadChoiceQuestion('c15')", "loadChoiceQuestion('bi-cq15')"),
        ("loadChoiceQuestion('c16')", "loadChoiceQuestion('bi-cq16')"),
        ("loadChoiceQuestion('c17')", "loadChoiceQuestion('bi-cq17')"),
        ("loadChoiceQuestion('c18')", "loadChoiceQuestion('bi-cq18')"),
        ("loadChoiceQuestion('c19')", "loadChoiceQuestion('bi-cq19')"),
        ("loadChoiceQuestion('c20')", "loadChoiceQuestion('bi-cq20')"),
    ]
    
    for old, new in id_replacements:
        content = content.replace(old, new)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 已修复选择题点击事件ID匹配问题！")

if __name__ == '__main__':
    main()
