#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复供应链和商务智能考试文件中的JavaScript转义问题"""

def fix_escaping(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换错误的转义
    # 1. 模板字符串的反引号转义
    content = content.replace('\\`', '`')
    
    # 2. 模板字符串内部的变量转义
    content = content.replace('\\${', '${')
    content = content.replace('\\$', '$')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 已修复 {file_path}')

# 修复供应链考试文件
fix_escaping('/workspace/courses/supply-chain-analysis-exam.html')

# 修复商务智能考试文件
fix_escaping('/workspace/courses/business-intelligence-exam.html')

print('\n✅ 所有考试文件的JavaScript转义问题已修复！')
