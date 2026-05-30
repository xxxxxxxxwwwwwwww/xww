#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接修复第2420行的嵌套模板字符串问题
"""
import os


def fix_2420_line(file_path):
    """修复第2420行的问题"""
    print(f"修复文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 第2420行（索引是2419）
    if len(lines) > 2419:
        # 原来的问题行
        old_line = lines[2419]
        
        # 修复嵌套的反引号 - 将内部的反引号转义
        # 找到 `<span class="\${isCorrect ? 'text-emerald-400' : 'text-red-400'} font-bold">\${selectedAnswer}</span>`
        # 替换为转义的版本
        new_line = old_line.replace(
            '`<span class="\${isCorrect ? \'text-emerald-400\' : \'text-red-400\'} font-bold">\${selectedAnswer}</span>`',
            '\\`<span class="\${isCorrect ? \'text-emerald-400\' : \'text-red-400\'} font-bold">\${selectedAnswer}</span>\\`'
        )
        
        lines[2419] = new_line
        print("  修复了第2420行的嵌套模板字符串")
    else:
        print("  文件行数不足")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("  修复完成！")


def main():
    courses_dir = '/workspace/courses'
    
    # 修复备份文件
    fix_2420_line(os.path.join(courses_dir, 'supply-chain-analysis-backup.html'))
    fix_2420_line(os.path.join(courses_dir, 'database-principles-backup.html'))
    
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
    
    print("\n✅ 修复完成！")


if __name__ == '__main__':
    main()
