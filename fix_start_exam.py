#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复startExam函数"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 移除测试alert
old_button = '''          <button id="start-exam" onclick="alert('开始考试！'); startExam(); return false;" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

new_button = '''          <button id="start-exam" onclick="startExam(); return false;" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

content = content.replace(old_button, new_button)

# 在startExam函数开头添加调试
old_function = '''    function startExam() {
      const name = document.getElementById('student-name').value.trim();
      if (!name) {
        alert('请输入您的姓名');
        return;
      }

      studentName = name;
      document.getElementById('display-name').textContent = name;
      document.getElementById('result-name').textContent = name;

      // 初始化答案数组
      answers = new Array(examData.questions.length).fill('');

      // 显示考试页面
      document.getElementById('exam-start').classList.add('hidden');
      document.getElementById('exam-questions').classList.remove('hidden');'''

new_function = '''    function startExam() {
      alert('startExam函数开始执行！');
      const name = document.getElementById('student-name').value.trim();
      if (!name) {
        alert('请输入您的姓名');
        return;
      }

      studentName = name;
      alert('学生姓名: ' + studentName);
      
      document.getElementById('display-name').textContent = name;
      document.getElementById('result-name').textContent = name;

      // 初始化答案数组
      answers = new Array(examData.questions.length).fill('');

      // 显示考试页面
      document.getElementById('exam-start').classList.add('hidden');
      document.getElementById('exam-questions').classList.remove('hidden');
      alert('应该显示考试页面了！');'''

content = content.replace(old_function, new_function)

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已修复startExam函数，添加了调试alert')
print('现在会逐步显示函数执行情况')
