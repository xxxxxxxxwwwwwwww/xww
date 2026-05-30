#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查并修复供应链考试文件"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 检查是否有初始化代码
if 'document.addEventListener' not in content:
    print('❌ 初始化代码缺失！')
else:
    print('✅ 初始化代码存在')

# 检查按钮绑定
if "addEventListener('click', startExam)" not in content:
    print('❌ 开始考试按钮事件未绑定！')
else:
    print('✅ 开始考试按钮事件已绑定')

# 检查startExam函数
if 'function startExam()' not in content:
    print('❌ startExam函数缺失！')
else:
    print('✅ startExam函数存在')

print('\n供应链考试文件检查完成！')
print('问题可能在于JavaScript代码中的转义字符。')
