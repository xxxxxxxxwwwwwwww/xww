#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
彻底修复嵌套模板字符串问题 - 将嵌套模板改为字符串拼接
"""
import os


def fix_nested_template(file_path):
    """修复文件中的嵌套模板字符串问题"""
    print(f"修复文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到问题行并替换
    # 原来的问题行（第2420行）:
    old_line = '            <p class="text-gray-300">您的答案：${selectedAnswer ? \\`<span class="${isCorrect ? \'text-emerald-400\' : \'text-red-400\'} font-bold">${selectedAnswer}</span>\\` : \'<span class="text-gray-500">未作答</span>\'}</p>'
    
    # 改为不使用嵌套模板字符串的版本
    new_line = '''            <p class="text-gray-300">您的答案：<span class="''' + '''${isCorrect ? 'text-emerald-400' : 'text-red-400'} font-bold">${selectedAnswer}</span>''' + '''</p>'''
    
    # 但是这样不对，因为我们需要条件判断
    # 更好的方法是使用字符串拼接
    
    # 正确的修复：使用字符串拼接代替嵌套模板
    fixed_line = '''            <p class="text-gray-300">您的答案：''' + '''${selectedAnswer ? ('<span class=' + '"' + '''${isCorrect ? 'text-emerald-400' : 'text-red-400'}''' + '"' + ''' font-bold>' + selectedAnswer + '</span>') : '<span class="text-gray-500">未作答</span>'}''' + '''</p>'''
    
    # 替换
    content = content.replace(old_line, fixed_line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  修复完成！")


def fix_all_nested_templates(file_path):
    """修复所有嵌套模板字符串问题"""
    print(f"修复文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式找到所有嵌套的模板字符串
    # 模式：在模板字符串中找到 `...` 这种形式
    # 需要把 ${xxx ? `...` : `...`} 改成 ${xxx ? '...' : '...'}
    
    import re
    
    # 修复嵌套模板字符串
    # 模式: ${xxx ? `内容` : `内容`}
    # 改为: ${xxx ? '内容' : '内容'}
    def fix_match(match):
        # 获取匹配的内容
        full_match = match.group(0)
        # 将反引号改为单引号
        fixed = full_match.replace('`', "'")
        return fixed
    
    # 找到所有嵌套模板的模式
    content = re.sub(
        r'\$\{[^}]*?`[^`]*`[^}]*?`[^`]*`[^}]*\}',
        fix_match,
        content
    )
    
    # 还要修复只有一个反引号的情况
    content = re.sub(
        r'\$\{[^}]*?`[^`]*`[^}]*\}',
        fix_match,
        content
    )
    
    # 修复单个反引号
    content = content.replace(r'\`', "'")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  修复完成！")


def main():
    courses_dir = '/workspace/courses'
    
    fix_all_nested_templates(os.path.join(courses_dir, 'supply-chain-analysis.html'))
    fix_all_nested_templates(os.path.join(courses_dir, 'database-principles.html'))
    fix_all_nested_templates(os.path.join(courses_dir, 'business-intelligence.html'))
    
    print("\n✅ 嵌套模板字符串问题修复完成！")


if __name__ == '__main__':
    main()
