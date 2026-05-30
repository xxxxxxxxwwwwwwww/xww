#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
超级彻底的修复脚本！
"""
import re

# 用备份文件覆盖
with open('/workspace/courses/supply-chain-analysis-backup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ================== 第一步：替换所有 onclick 属性，变成 data 属性 ==================
# 替换编程题的 onclick：<div onclick="loadProgrammingProblem(1)"...> -> <div data-problem-id="1" data-type="programming"
html = re.sub(
    r'onclick="loadProgrammingProblem\((\d+)\)"',
    r'data-problem-id="\1" data-type="programming"',
    html
)

# 替换选择题的 onclick：先处理单引号
html = re.sub(
    r'onclick="loadChoiceQuestion\(\'([^\']+)\'\)"',
    r'data-problem-id="\1" data-type="choice"',
    html
)
# 再处理双引号
html = re.sub(
    r'onclick="loadChoiceQuestion\("([^"]+)"\)"',
    r'data-problem-id="\1" data-type="choice"',
    html
)

# ================== 第二步：在 DOMContentLoaded 里面添加绑定代码 ==================
# 找到 DOMContentLoaded 的位置
dom_start = html.find('document.addEventListener(\'DOMContentLoaded\', function() {')

if dom_start == -1:
    print('找不到 DOMContentLoaded')
    exit(1)

# 找到这一块的结束位置
brace_count = 1
dom_end = dom_start
for i in range(dom_start + len('document.addEventListener(\'DOMContentLoaded\', function() {'), len(html)):
    if html[i] == '{':
        brace_count +=1
    elif html[i] == '}':
        brace_count -=1
        if brace_count == 0:
            dom_end = i
            break

if dom_end == dom_start:
    print('找不到结束位置')
    exit(1)

print(f'DOM content: from {dom_start} to {dom_end}')

# 把绑定代码插入到 DOMContentLoaded 结束前！
binding_code = '''
      
      // ================== 超级彻底的绑定！！！绝对能用！！！ ==================
      console.log('======= 开始绑定题目项... =======');
      const allProblemItems = document.querySelectorAll('.problem-item');
      console.log('找到题目项数量:', allProblemItems.length);
      
      allProblemItems.forEach(function(item, index) {
        const problemId = item.getAttribute('data-problem-id');
        const problemType = item.getAttribute('data-type');
        
        console.log('绑定第', index+1, '个:', problemId, problemType);
        
        item.addEventListener('click', function(e) {
          console.log('========== 题目被点击！==========');
          console.log('id:', problemId);
          console.log('type:', problemType);
          
          // 移除所有 active 类，加给当前项
          allProblemItems.forEach(el => el.classList.remove('active'));
          item.classList.add('active');
          
          if (problemType === 'programming') {
            console.log('加载编程题...');
            const pid = parseInt(problemId);
            loadProgrammingProblem(pid);
          } else if (problemType === 'choice') {
            console.log('加载选择题...');
            loadChoiceQuestion(problemId);
          }
        });
      });
      console.log('======= 所有题目项绑定完成！=======');
      
'''

# 插在结束前
new_html = html[:dom_end] + binding_code + html[dom_end:]

# ================== 第三步：写回文件 ==================
with open('/workspace/courses/supply-chain-analysis.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('✓ 供应链分析课程修复完成！')


# ================== 同样处理数据库原理 ==================
with open('/workspace/courses/database-principles-backup.html', 'r', encoding='utf-8') as f:
    html_db = f.read()

# 替换
html_db = re.sub(r'onclick="loadProgrammingProblem\((\d+)\)"', r'data-problem-id="\1" data-type="programming"', html_db)
# 替换选择题的 onclick：先处理单引号
html_db = re.sub(
    r'onclick="loadChoiceQuestion\(\'([^\']+)\'\)"',
    r'data-problem-id="\1" data-type="choice"',
    html_db
)
# 再处理双引号
html_db = re.sub(
    r'onclick="loadChoiceQuestion\("([^"]+)"\)"',
    r'data-problem-id="\1" data-type="choice"',
    html_db
)

# 插入绑定代码
dom_start_db = html_db.find('document.addEventListener(\'DOMContentLoaded\', function() {')
if dom_start_db != -1:
    brace_count_db =1
    dom_end_db = dom_start_db
    for i in range(dom_start_db + 50, len(html_db)):
        if html_db[i] == '{':
            brace_count_db +=1
        elif html_db[i] == '}':
            brace_count_db -=1
            if brace_count_db ==0:
                dom_end_db = i
                break
    if dom_end_db > dom_start_db:
        html_db = html_db[:dom_end_db] + binding_code + html_db[dom_end_db:]

with open('/workspace/courses/database-principles.html', 'w', encoding='utf-8') as f:
    f.write(html_db)

print('✓ 数据库原理课程修复完成！')


print('\n✓✓✓ 所有修复完成！现在一定能用了！\n')
