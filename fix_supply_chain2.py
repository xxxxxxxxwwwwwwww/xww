#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复供应链分析课程的点击问题
"""

with open('/workspace/courses/supply-chain-analysis.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到 DOMContentLoaded 的行号
dom_start_line = -1
for i, line in enumerate(lines):
    if "document.addEventListener('DOMContentLoaded'" in line:
        dom_start_line = i
        break

if dom_start_line == -1:
    print("未找到 DOMContentLoaded")
    exit(1)

print(f"DOMContentLoaded 在第 {dom_start_line + 1} 行")

# 找到需要移动的函数的起始位置（loadProgrammingProblem 之前）
func_start_line = -1
for i in range(dom_start_line, min(dom_start_line + 200, len(lines))):
    if "// 加载编程题" in lines[i]:
        func_start_line = i - 1  # 包括前面的空行
        break

if func_start_line == -1:
    print("未找到函数起始位置")
    exit(1)

print(f"函数起始位置在第 {func_start_line + 1} 行")

# 找到所有函数的结束位置
# 需要找到 DOMContentLoaded 之前的所有函数
# 搜索到 DOMContentLoaded 之前的所有 function 声明
func_end_line = dom_start_line

# 向前搜索找到最后一个函数结束的位置
brace_count = 0
for i in range(dom_start_line - 1, max(dom_start_line - 200, 0), -1):
    line = lines[i]
    brace_count += line.count('}')
    brace_count -= line.count('{')
    if brace_count == 0 and ('function' in line or '//' in line):
        # 找到了一个代码块的开始
        func_end_line = i
        break

print(f"函数结束位置在第 {func_end_line + 1} 行")

# 提取所有需要移动的函数行
func_lines = lines[func_end_line:func_start_line + 1]
print(f"需要移动 {len(func_lines)} 行")

# 构建新文件内容
# 1. 保留 DOMContentLoaded 之前的内容（不包括函数）
# 2. 插入被移动的函数
# 3. 保留 DOMContentLoaded 及之后的内容（不包括原来的函数）

new_lines = []
new_lines.extend(lines[:func_end_line])
new_lines.append('\n')
new_lines.extend(func_lines)
new_lines.append('\n')
new_lines.extend(lines[func_start_line + 1:])

with open('/workspace/courses/supply-chain-analysis.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"✓ 已移动 {len(func_lines)} 行到 DOMContentLoaded 之前")
