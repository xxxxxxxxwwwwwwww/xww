#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""添加最简单的测试"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在startExam函数的最开始添加alert
old_start = '''    function startExam() {
      alert('startExam函数开始执行！');
      const name = document.getElementById('student-name').value.trim();'''

new_start = '''    function startExam() {
      alert('🎉 startExam函数被调用了！请截图告诉我！');
      const name = document.getElementById('student-name').value.trim();'''

content = content.replace(old_start, new_start)

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已添加最明显的测试alert')
