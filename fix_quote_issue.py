#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复选择题 problem-id 多余单引号问题
"""
import re
import os


def fix_quotes_in_file(file_path):
    """修复文件中的引号问题"""
    print(f"正在修复 {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复 data-problem-id="'c1'" 这种问题，改为 data-problem-id="c1"
    content = re.sub(
        r'data-problem-id="\'([^\']+)\'"',
        r'data-problem-id="\1"',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  修复完成")


def main():
    courses_dir = '/workspace/courses'
    fix_quotes_in_file(os.path.join(courses_dir, 'supply-chain-analysis.html'))
    fix_quotes_in_file(os.path.join(courses_dir, 'database-principles.html'))
    fix_quotes_in_file(os.path.join(courses_dir, 'business-intelligence.html'))
    
    print("\n所有引号问题修复完成！")


if __name__ == '__main__':
    main()
