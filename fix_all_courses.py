#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完全修复三个课程的题库点击问题
"""

import re

def fix_course_file(file_path):
    print(f"\n=== 修复文件: {file_path} ===")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 确保函数在全局作用域
    # 找到 DOMContentLoaded 的位置
    dom_start = content.find("document.addEventListener('DOMContentLoaded'")
    
    if dom_start == -1:
        print("⚠️ 未找到 DOMContentLoaded")
        return
    
    # 找到 DOMContentLoaded 回调的结束位置
    brace_count = 0
    dom_end = dom_start
    for i in range(dom_start, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                dom_end = i + 1
                break
    
    # 提取需要移到全局作用域的函数
    functions_to_move = [
        'showTab',
        'toggleChapter',
        'loadProgrammingProblem', 
        'loadChoiceQuestion',
        'runCode',
        'resetCode',
        'toggleFavorite',
        'toggleCodeEditor',
        'resetTimer',
        'updateTimer',
        'submitChoice',
        'selectChoice',
        'showChoiceAnalysis',
        'updateChoiceAnalysis',
        'initPyodide',
        'getKnowledgeSection',
        'getChapterName',
        'updateProblemItemStatus'
    ]
    
    # 在 DOMContentLoaded 回调内查找这些函数
    dom_content = content[dom_start:dom_end]
    moved_functions = []
    
    for func_name in functions_to_move:
        # 使用正则查找函数
        pattern = r"(function " + func_name + r"\([^)]*\)\s*\{[\s\S]*?\})"
        match = re.search(pattern, dom_content)
        if match:
            moved_functions.append(match.group(1))
            # 从 dom_content 中移除已找到的函数
            dom_content = dom_content[:match.start()] + dom_content[match.end():]
    
    # 如果找到了需要移动的函数
    if moved_functions:
        # 在 DOMContentLoaded 之前插入这些函数
        functions_str = '\n\n'.join(moved_functions) + '\n\n'
        content = content[:dom_start] + functions_str + content[dom_start:dom_start+len(content[dom_start:])-len(dom_content)] + dom_content
    
    # 确保 showTab 在 loadProgrammingProblem 中被调用
    if 'function loadProgrammingProblem' in content:
        func_start = content.find('function loadProgrammingProblem')
        check_pos = content.find('if (!problem) return;', func_start)
        if check_pos != -1 and 'showTab("question-bank")' not in content[func_start:func_start+500]:
            content = content[:check_pos+20] + '\n      showTab("question-bank");' + content[check_pos+20:]
            print("✓ 在 loadProgrammingProblem 中添加了 showTab 调用")
    
    # 确保 showTab 在 loadChoiceQuestion 中被调用
    if 'function loadChoiceQuestion' in content:
        func_start = content.find('function loadChoiceQuestion')
        check_pos = content.find('if (!currentChoiceQuestion)', func_start)
        if check_pos != -1 and 'showTab("question-bank")' not in content[func_start:func_start+500]:
            content = content[:check_pos] + 'showTab("question-bank");\n      ' + content[check_pos:]
            print("✓ 在 loadChoiceQuestion 中添加了 showTab 调用")
    
    # 写入修复后的文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ 文件修复完成")

# 修复所有三个课程文件
files = [
    '/workspace/courses/business-intelligence.html',
    '/workspace/courses/database-principles.html',
    '/workspace/courses/supply-chain-analysis.html'
]

for file in files:
    fix_course_file(file)

print("\n🎉 所有课程文件已修复完成！")
print("请刷新页面测试点击功能")