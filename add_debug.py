#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在供应链考试文件中添加调试代码"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在DOMContentLoaded中添加一个alert来测试
old_init = '''    // 初始化函数
    document.addEventListener('DOMContentLoaded', function() {
      // 绑定开始考试按钮事件
      document.getElementById('start-exam').addEventListener('click', startExam);'''

new_init = '''    // 初始化函数
    document.addEventListener('DOMContentLoaded', function() {
      alert('供应链考试页面加载成功！');
      // 绑定开始考试按钮事件
      const startBtn = document.getElementById('start-exam');
      if (startBtn) {
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

print('✅ 已在供应链考试文件中添加调试代码')
print('现在打开页面时会弹出提示，确认是否加载成功')
