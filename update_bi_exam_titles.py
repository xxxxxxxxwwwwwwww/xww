#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新商务智能分析考试文件的标题"""

with open('/workspace/courses/business-intelligence-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有标题
content = content.replace('供应链数据分析考试', '商务智能分析考试')
content = content.replace('供应链数据分析', '商务智能分析')
content = content.replace('供应链分析题库', '商务智能分析题库')

# 写入文件
with open('/workspace/courses/business-intelligence-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 商务智能分析考试文件标题已全部更新！')
