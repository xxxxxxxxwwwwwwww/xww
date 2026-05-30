#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在供应链考试中添加调试alert"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在开始考试按钮的div之前添加一个测试按钮
old_button = '''          <button id="start-exam" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

new_button = '''          <button id="test-button" onclick="alert('测试按钮点击成功！')" class="btn-secondary mx-auto mb-4">
            <i class="fa fa-check"></i> 测试按钮
          </button>
          
          <button id="start-exam" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

content = content.replace(old_button, new_button)

# 在DOMContentLoaded中添加alert
old_init = '''    document.addEventListener('DOMContentLoaded', function() {
      initEditor();
      initPyodide();

      // 开始考试按钮
      document.getElementById('start-exam').addEventListener('click', startExam);'''

new_init = '''    document.addEventListener('DOMContentLoaded', function() {
      alert('页面加载成功！');
      initEditor();
      initPyodide();

      // 开始考试按钮
      const startBtn = document.getElementById('start-exam');
      if (startBtn) {
        alert('找到开始考试按钮！');
        startBtn.addEventListener('click', function() {
          alert('开始考试按钮被点击！');
          startExam();
        });
      } else {
        alert('错误：找不到开始考试按钮！');
      }'''

content = content.replace(old_init, new_init)

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已在供应链考试中添加测试按钮和调试alert')
print('现在请打开页面，会弹出提示确认：')
print('1. 页面加载成功')
print('2. 找到开始考试按钮')
print('3. 点击开始考试按钮时会弹出提示')
