#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查并修复三个课程的点击问题
问题分析：函数定义在DOMContentLoaded回调内部，导致onclick无法访问
"""

def analyze_and_fix_file(file_path):
    print(f"\n=== 分析文件: {file_path} ===")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查函数位置
    dom_start = content.find("document.addEventListener('DOMContentLoaded'")
    load_func_pos = content.find("function loadProgrammingProblem")
    
    if dom_start != -1 and load_func_pos != -1:
        if load_func_pos > dom_start:
            print("❌ 问题：loadProgrammingProblem 函数在 DOMContentLoaded 回调内部")
            
            # 需要找到回调结束位置并把函数移出来
            # 找到DOMContentLoaded回调的结束
            brace_count = 1
            dom_end = dom_start
            for i in range(dom_start + len("document.addEventListener('DOMContentLoaded', function() {"), len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        dom_end = i + 2  # 包含最后的 });
                        break
            
            # 提取所有函数定义
            import re
            # 匹配函数定义
            func_pattern = r"(function \w+\([^)]*\)\s*\{[\s\S]*?\})"
            matches = list(re.finditer(func_pattern, content))
            
            # 找出在DOMContentLoaded内部的函数
            functions_inside_dom = []
            for match in matches:
                if match.start() > dom_start and match.end() < dom_end:
                    functions_inside_dom.append(match)
            
            print(f"⚠️ 发现 {len(functions_inside_dom)} 个函数在DOMContentLoaded内部")
            
            # 创建修复后的内容
            # 1. 保留DOMContentLoaded之前的内容
            # 2. 插入被移出来的函数
            # 3. 保留DOMContentLoaded回调（移除内部函数）
            
            # 提取函数内容
            moved_funcs = []
            new_dom_content = content[dom_start:dom_end]
            
            for match in functions_inside_dom:
                moved_funcs.append(content[match.start():match.end()])
                # 从DOMContentLoaded中移除
                new_dom_content = new_dom_content.replace(content[match.start()-dom_start:match.end()-dom_start], '')
            
            # 重新组合内容
            if moved_funcs:
                new_content = content[:dom_start] + '\n\n'.join(moved_funcs) + '\n\n' + new_dom_content + content[dom_end:]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✓ 已将函数移到全局作用域")
                return True
        else:
            print("✓ loadProgrammingProblem 函数在全局作用域")
    else:
        print("⚠️ 未找到函数或DOMContentLoaded")
    
    return False

# 修复所有文件
files = [
    '/workspace/courses/business-intelligence.html',
    '/workspace/courses/database-principles.html',
    '/workspace/courses/supply-chain-analysis.html'
]

for file in files:
    analyze_and_fix_file(file)

print("\n🎉 分析和修复完成！")