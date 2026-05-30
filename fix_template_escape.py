#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复模板字符串转义问题 - 将 \${ 替换回 ${
"""
import os

def fix_file(file_path):
    print(f"修复文件: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 将 \${ 替换回 ${
    content = content.replace(r'\${', '${')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  修复完成！")

def main():
    courses_dir = '/workspace/courses'
    
    # 修复所有三个课程
    fix_file(os.path.join(courses_dir, 'supply-chain-analysis.html'))
    fix_file(os.path.join(courses_dir, 'database-principles.html'))
    fix_file(os.path.join(courses_dir, 'business-intelligence.html'))
    
    print("\n✅ 所有课程修复完成！")

if __name__ == '__main__':
    main()
