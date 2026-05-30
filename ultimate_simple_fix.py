#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最最简单的修复 - 只用 onclick，不要折腾了
"""
import os
import shutil


def just_use_backup(backup_file, target_file):
    """直接使用备份文件，保持原样！！！"""
    print(f"恢复备份文件 {backup_file} -> {target_file}")
    shutil.copy(backup_file, target_file)
    print("  备份已恢复 - 现在 onclick 应该正常工作！")


def main():
    courses_dir = '/workspace/courses'
    
    # 恢复供应链分析
    just_use_backup(
        os.path.join(courses_dir, 'supply-chain-analysis-backup.html'),
        os.path.join(courses_dir, 'supply-chain-analysis.html')
    )
    
    # 恢复数据库原理
    just_use_backup(
        os.path.join(courses_dir, 'database-principles-backup.html'),
        os.path.join(courses_dir, 'database-principles.html')
    )
    
    print("\n✅ 已恢复原始备份 - 原始的 onclick 应该可以正常工作了！")


if __name__ == '__main__':
    main()
