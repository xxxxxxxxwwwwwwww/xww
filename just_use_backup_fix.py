#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最简单可靠的修复！就用原始备份，只修复转义问题
"""
import os
import shutil


def main():
    courses_dir = '/workspace/courses'
    
    print("开始最简单的修复！")
    
    # 1. 修复供应链分析
    backup_sc = os.path.join(courses_dir, 'supply-chain-analysis-backup.html')
    target_sc = os.path.join(courses_dir, 'supply-chain-analysis.html')
    
    print(f"\n修复供应链分析...")
    with open(backup_sc, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 只修复转义问题：将 \` 替换为 `
    content = content.replace(r'\`', '`')
    
    with open(target_sc, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  供应链分析修复完成！")
    
    # 2. 修复数据库原理
    backup_db = os.path.join(courses_dir, 'database-principles-backup.html')
    target_db = os.path.join(courses_dir, 'database-principles.html')
    
    print(f"\n修复数据库原理...")
    with open(backup_db, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(r'\`', '`')
    
    with open(target_db, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  数据库原理修复完成！")
    
    # 3. 修复商业智能
    target_bi = os.path.join(courses_dir, 'business-intelligence.html')
    
    print(f"\n修复商业智能...")
    with open(target_bi, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除重复的事件绑定代码
    # 找到重复的部分并删除
    import re
    content = re.sub(
        r'// === 绑定题目点击事件 ===.*?// === 题目点击事件绑定完成 ===',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 再移除 DOMContentLoaded 里多余的绑定代码
    content = re.sub(
        r'(document\.addEventListener\([\'"]DOMContentLoaded[\'"],\s*function\(\)\s*\{).*?(// 初始化代码编辑器)',
        lambda m: m.group(1) + '\n      ' + m.group(2),
        content,
        flags=re.DOTALL
    )
    
    with open(target_bi, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  商业智能修复完成！")
    
    print("\n✅ 最简单可靠的修复完成！")


if __name__ == '__main__':
    main()
