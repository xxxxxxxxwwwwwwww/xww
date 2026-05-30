#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复供应链分析课程的点击问题
"""

with open('/workspace/courses/supply-chain-analysis.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 DOMContentLoaded 的位置
dom_start = content.find("document.addEventListener('DOMContentLoaded'")
if dom_start == -1:
    print("未找到 DOMContentLoaded")
    exit(1)

# 找到 DOMContentLoaded 回调的结束位置
brace_count = 1
dom_end = dom_start
for i in range(dom_start + len("document.addEventListener('DOMContentLoaded', function() {"), len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            dom_end = i + 1
            break

print(f"DOMContentLoaded 范围: {dom_start} - {dom_end}")

# 提取所有在 DOMContentLoaded 内部的函数
functions_to_move = [
    'loadProgrammingProblem',
    'loadChoiceQuestion',
    'selectChoice',
    'submitChoice',
    'showChoiceAnalysis',
    'updateChoiceAnalysis',
    'resetTimer',
    'updateTimer'
]

import re

moved_functions = []
dom_content = content[dom_start:dom_end]

for func_name in functions_to_move:
    # 匹配函数定义
    pattern = r"(// [^\n]+\n    function " + func_name + r"\([\s\S]*?\n    \})"
    match = re.search(pattern, dom_content)
    if match:
        moved_functions.append((func_name, match.group(0)))
        print(f"找到函数: {func_name}")
        dom_content = dom_content[:match.start()] + dom_content[match.end():]

# 构建新内容
if moved_functions:
    # 把函数移到 DOMContentLoaded 之前
    functions_str = '\n\n'.join([f[1] for f in moved_functions]) + '\n\n'
    new_content = content[:dom_start] + functions_str + content[dom_start:]
    
    with open('/workspace/courses/supply-chain-analysis.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ 已移动 {len(moved_functions)} 个函数到全局作用域")
else:
    print("⚠️ 未找到需要移动的函数")
