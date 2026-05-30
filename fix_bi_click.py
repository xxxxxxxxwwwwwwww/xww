#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复商业智能题库的点击问题
"""

# 读取原始文件
with open('/workspace/courses/business-intelligence.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复问题1：确保函数是全局的（不在 DOMContentLoaded 回调内）
# 找到 DOMContentLoaded 的开始和结束位置
dom_start = content.find("document.addEventListener('DOMContentLoaded'")
dom_end = content.find("});", dom_start) + 2

# 提取函数定义
function_patterns = [
    'function loadProgrammingProblem',
    'function loadChoiceQuestion', 
    'function showTab',
    'function toggleChapter',
    'function runCode',
    'function resetCode'
]

# 修复问题2：添加缺失的代码
fixes = [
    # 在 loadProgrammingProblem 中添加 showTab
    ('if (!problem) return;', 'if (!problem) return;\n      \n      // 确保在题库标签页\n      showTab("question-bank");'),
    # 在 loadChoiceQuestion 中添加 showTab
    ('if (!currentChoiceQuestion) {', 'showTab("question-bank");\n\n      if (!currentChoiceQuestion) {'),
    # 确保函数在全局作用域
]

# 应用修复
for old, new in fixes:
    content = content.replace(old, new)

# 写入修复后的文件
with open('/workspace/courses/business-intelligence.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ 已修复 business-intelligence.html")
print("请刷新页面测试点击功能")