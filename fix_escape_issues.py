#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
先修复备份文件的转义问题
"""
import re
import os


def fix_file(file_path):
    """修复文件中的转义问题"""
    print(f"修复文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复转义的反引号
    # 将 \` 替换为 `
    content = content.replace(r'\`', '`')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  转义字符已修复！")


def main():
    courses_dir = '/workspace/courses'
    fix_file(os.path.join(courses_dir, 'supply-chain-analysis-backup.html'))
    fix_file(os.path.join(courses_dir, 'database-principles-backup.html'))
    
    # 然后复制到目标文件
    import shutil
    shutil.copy(
        os.path.join(courses_dir, 'supply-chain-analysis-backup.html'),
        os.path.join(courses_dir, 'supply-chain-analysis.html')
    )
    shutil.copy(
        os.path.join(courses_dir, 'database-principles-backup.html'),
        os.path.join(courses_dir, 'database-principles.html')
    )
    
    print("\n✅ 已修复并恢复原始文件 - 现在 onclick 应该可以正常工作了！")


if __name__ == '__main__':
    main()
