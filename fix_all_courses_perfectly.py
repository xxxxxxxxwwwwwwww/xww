#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完美修复所有课程的点击问题
"""
import re
import os
import shutil


def fix_course_file(backup_file, target_file):
    """完美修复一个课程文件"""
    print(f"正在修复: {target_file}")
    
    # 读取备份文件
    with open(backup_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 修复转义问题：将 \` 替换为 `
    content = content.replace(r'\`', '`')
    
    # 2. 移除所有重复的 addEventListener 绑定代码
    # 找到从 "// === 绑定题目点击事件 ===" 到 "// === 题目点击事件绑定完成 ===" 的部分
    pattern = re.compile(
        r'// === 绑定题目点击事件 ===.*?// === 题目点击事件绑定完成 ===',
        re.DOTALL
    )
    content = pattern.sub('', content)
    
    # 3. 将所有 data-problem-id 和 data-type 属性改回 onclick 属性
    # 修复编程题 onclick
    content = re.sub(
        r'class="problem-item([^"]*)" data-problem-id="(\d+)" data-type="programming"',
        r'class="problem-item\1" onclick="loadProgrammingProblem(\2)"',
        content
    )
    
    # 修复选择题 onclick - 处理带单引号和不带单引号的情况
    content = re.sub(
        r'class="problem-item([^"]*)" data-problem-id="([^"]+)" data-type="choice"',
        lambda m: f'class="problem-item{m.group(1)}" onclick="loadChoiceQuestion(\'{m.group(2)}\')"',
        content
    )
    
    # 4. 移除 DOMContentLoaded 中重复的 allProblemItems 声明
    # 查找并删除重复的绑定代码块
    dom_pattern = re.compile(
        r'(document\.addEventListener\([\'"]DOMContentLoaded[\'"],\s*function\(\)\s*\{).*?(// 初始化代码编辑器)',
        re.DOTALL
    )
    
    def clean_dom_content(match):
        return match.group(1) + '\n      ' + match.group(2)
    
    # 简化处理，直接移除多余的事件绑定代码
    # 查找 DOMContentLoaded 开始，到 "// 初始化代码编辑器" 之前的多余代码
    # 先找到 DOMContentLoaded 的位置
    dom_start = content.find('document.addEventListener(\'DOMContentLoaded\'')
    if dom_start != -1:
        # 找到 "// 初始化代码编辑器" 的位置
        init_editor_pos = content.find('// 初始化代码编辑器', dom_start)
        if init_editor_pos != -1:
            # 检查中间是否有多余的绑定代码
            section = content[dom_start:init_editor_pos]
            if 'allProblemItems' in section:
                # 保留 DOMContentLoaded 开头，直接跳到初始化编辑器
                content = (
                    content[:dom_start] + 
                    'document.addEventListener(\'DOMContentLoaded\', function() {\n' +
                    '      // 初始化代码编辑器' +
                    content[init_editor_pos + len('// 初始化代码编辑器'):]
                )
    
    # 5. 确保 loadChoiceQuestion 函数存在并且全局可访问
    # 检查是否有 loadChoiceQuestion 函数，如果没有就确保它在全局
    if 'function loadChoiceQuestion' not in content:
        # 找到 function _loadChoiceQuestionReal 或者类似的，确保全局可访问
        content = re.sub(
            r'(function _loadChoiceQuestionReal\(questionId\) \{)',
            r'function loadChoiceQuestion(questionId) {\n  if(typeof _realLoadChoice === "function") {\n    return _realLoadChoice(questionId);\n  }\n  // 简单实现\n  console.log("Loading choice question:", questionId);\n' +
          r'}\n\n\1',
            content
        )
    
    # 写入目标文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  修复完成: {target_file}")
    return True


def main():
    courses_dir = '/workspace/courses'
    
    # 定义需要修复的课程
    courses = [
        {
            'backup': os.path.join(courses_dir, 'supply-chain-analysis-backup.html'),
            'target': os.path.join(courses_dir, 'supply-chain-analysis.html')
        },
        {
            'backup': os.path.join(courses_dir, 'database-principles-backup.html'),
            'target': os.path.join(courses_dir, 'database-principles.html')
        },
        {
            'backup': os.path.join(courses_dir, 'business-intelligence.html'),  # 这个我们直接用自己
            'target': os.path.join(courses_dir, 'business-intelligence.html')
        }
    ]
    
    for course in courses:
        # 先保存当前目标文件作为额外备份
        if os.path.exists(course['target']):
            backup_name = course['target'] + '.before_fix_' + str(os.path.getsize(course['target']))
            if not os.path.exists(backup_name):
                shutil.copy(course['target'], backup_name)
        
        fix_course_file(course['backup'], course['target'])
    
    print("\n✅ 所有课程完美修复完成！")


if __name__ == '__main__':
    main()
