#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接修复函数位置问题
"""

def fix_file(file_path):
    print(f"\n=== 修复文件: {file_path} ===")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 找到 script 标签开始位置和 DOMContentLoaded 开始位置
    script_start = -1
    dom_start_line = -1
    dom_end_line = -1
    brace_count = 0
    
    for i, line in enumerate(lines):
        if '<script>' in line and script_start == -1:
            script_start = i
        if "document.addEventListener('DOMContentLoaded'" in line:
            dom_start_line = i
            # 找到回调的开始大括号
            for j in range(i, len(lines)):
                if '{' in lines[j]:
                    brace_count += 1
                    # 找到第一个 { 后开始计数
                    if brace_count == 1:
                        first_brace_line = j
                        # 继续找匹配的 }
                        for k in range(j+1, len(lines)):
                            brace_count += lines[k].count('{')
                            brace_count -= lines[k].count('}')
                            if brace_count == 0:
                                dom_end_line = k
                                break
                        break
            break
    
    if dom_start_line == -1 or dom_end_line == -1:
        print("⚠️ 未找到DOMContentLoaded")
        return
    
    print(f"DOMContentLoaded 行: {dom_start_line+1} - {dom_end_line+1}")
    
    # 提取所有在DOMContentLoaded内部的函数
    functions_to_move = []
    func_start = -1
    func_brace_count = 0
    
    for i in range(dom_start_line, dom_end_line+1):
        line = lines[i]
        # 检测函数开始
        if 'function ' in line and '(' in line and ')' in line:
            func_start = i
            func_brace_count = line.count('{') - line.count('}')
            if func_brace_count == 0:
                # 单行函数
                functions_to_move.append((i, i))
                func_start = -1
        elif func_start != -1:
            func_brace_count += line.count('{')
            func_brace_count -= line.count('}')
            if func_brace_count == 0:
                functions_to_move.append((func_start, i))
                func_start = -1
    
    print(f"找到 {len(functions_to_move)} 个需要移动的函数")
    
    if not functions_to_move:
        print("⚠️ 未找到需要移动的函数")
        return
    
    # 提取函数内容
    func_content = []
    for start, end in functions_to_move:
        func_content.append(''.join(lines[start:end+1]))
    
    # 创建新文件内容
    # 1. 保留 script 标签后到 DOMContentLoaded 前的内容
    # 2. 添加移出来的函数
    # 3. 保留 DOMContentLoaded 回调（移除内部函数）
    
    # 移除内部函数的行
    lines_to_keep = []
    removed_ranges = set()
    for start, end in functions_to_move:
        for i in range(start, end+1):
            removed_ranges.add(i)
    
    new_lines = []
    for i, line in enumerate(lines):
        if i in removed_ranges:
            continue
        new_lines.append(line)
    
    # 在 DOMContentLoaded 前插入函数
    # 找到新位置的 DOMContentLoaded
    dom_insert_pos = -1
    for i, line in enumerate(new_lines):
        if "document.addEventListener('DOMContentLoaded'" in line:
            dom_insert_pos = i
            break
    
    if dom_insert_pos != -1:
        # 在 DOMContentLoaded 前插入函数
        new_lines.insert(dom_insert_pos, '\n\n' + ''.join(func_content))
    
    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("✓ 已修复函数位置")

# 修复所有文件
files = [
    '/workspace/courses/business-intelligence.html',
    '/workspace/courses/database-principles.html',
    '/workspace/courses/supply-chain-analysis.html'
]

for file in files:
    fix_file(file)

print("\n🎉 修复完成！")