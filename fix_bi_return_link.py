#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复商务智能考试文件的返回链接"""

with open('/workspace/courses/business-intelligence-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有返回链接
content = content.replace('supply-chain-analysis.html', 'business-intelligence.html')

with open('/workspace/courses/business-intelligence-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 商务智能考试文件的返回链接已修复！')
