#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复嵌套模板字符串的问题
"""
import re
import os


def fix_template_strings(file_path):
    """修复文件中的嵌套模板字符串问题"""
    print(f"修复文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 问题: 在模板字符串中又使用了反引号
    # 需要将内部的反引号转义
    
    # 修复 updateChoiceAnalysis 函数中的嵌套模板字符串
    # 找到问题区域
    start_marker = '// 更新选择题解析内容'
    end_marker = '// 提交选择题答案'
    
    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker, start_pos)
    
    if start_pos != -1 and end_pos != -1:
        # 获取这个函数的内容
        section = content[start_pos:end_pos]
        
        # 找到所有模板字符串中的反引号
        # 将嵌套的反引号替换为转义的反引号
        # 模式: 在模板字符串中找到 `<span class="...` 这种模式
        fixed_section = re.sub(
            r'(contentHtml = `[^`]*?)(`)([^`]*?`)',
            lambda m: m.group(1) + r'\`' + m.group(3),
            section
        )
        
        # 再次处理可能还有的嵌套
        fixed_section = re.sub(
            r'(contentHtml = `[^`]*?)(`)([^`]*?`)',
            lambda m: m.group(1) + r'\`' + m.group(3),
            fixed_section
        )
        
        # 替换回去
        content = content[:start_pos] + fixed_section + content[end_pos:]
        
        print("  修复了嵌套模板字符串问题")
    else:
        print("  未找到需要修复的区域")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  修复完成！")


def main():
    courses_dir = '/workspace/courses'
    
    fix_template_strings(os.path.join(courses_dir, 'supply-chain-analysis-backup.html'))
    fix_template_strings(os.path.join(courses_dir, 'database-principles-backup.html'))
    
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
    
    print("\n✅ 模板字符串问题修复完成！")


if __name__ == '__main__':
    main()
