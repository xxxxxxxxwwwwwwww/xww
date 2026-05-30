#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""创建最简单的测试版本"""

with open('/workspace/courses/supply-chain-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 最简单的方法：直接在onclick中调用
old_button = '''          <button id="start-exam" onclick="startExam()" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

new_button = '''          <button id="start-exam" onclick="alert('开始考试！'); startExam(); return false;" class="btn-primary mx-auto">
            <i class="fa fa-play"></i> 开始考试
          </button>'''

content = content.replace(old_button, new_button)

# 同时确保studentName变量已定义
if 'let studentName' not in content and 'var studentName' not in content:
    content = content.replace('// 全局变量', '// 全局变量\n    let studentName = "";')

with open('/workspace/courses/supply-chain-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已创建测试版本')
print('点击按钮时会先弹出alert确认是否响应')
