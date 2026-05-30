#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复供应链考试按钮，使用onclick而不是addEventListener"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 方法1：直接在按钮上使用onclick属性
old_button = '''          <button id="test-button" onclick="alert('测试按钮点击成功！')" class="btn-secondary mx-auto mb-4">
            <i class="fa fa-check"></i> 测试按钮
          </button>
          
          <button id="start-exam" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

new_button = '''          <button id="start-exam" onclick="startExam()" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

content = content.replace(old_button, new_button)

# 方法2：在DOMContentLoaded中使用onclick
old_init = '''    document.addEventListener('DOMContentLoaded', function() {
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

new_init = '''    document.addEventListener('DOMContentLoaded', function() {
      initEditor();
      initPyodide();
    }'''

content = content.replace(old_init, new_init)

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已修复供应链考试按钮，使用onclick属性')
print('现在点击"开始考试"按钮应该能正常工作')
