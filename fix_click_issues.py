#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复三个课程的题目点击加载功能
"""
import re

files_to_fix = [
    '/workspace/courses/supply-chain-analysis.html',
    '/workspace/courses/database-principles.html',
    '/workspace/courses/business-intelligence.html'
]

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复 loadProgrammingProblem 函数：添加 active 类给被点击的题目，并且确保在 question-bank 标签页
    pattern1 = r'(// 加载编程题\s+function loadProgrammingProblem\(problemId\) \{[\s\S]*?// 更新问题项状态\s+document\.querySelectorAll\(\'\.problem-item\'\)\.forEach\(item => \{[\s\S]*?item\.classList\.remove\(\'active\'\);[\s\S]*?\}\);[\s\S]*?\})'
    
    replacement1 = '''// 加载编程题
    function loadProgrammingProblem(problemId) {
      currentProblem = problemId;
      const problem = problems.find(p => p.id === problemId);
      
      if (!problem) return;
      
      // 确保在题库标签页
      showTab('question-bank');
      
      // 更新问题信息
      document.getElementById('problem-title').textContent = problem.title;
      document.getElementById('problem-description').innerHTML = problem.description;
      
      // 更新难度标签
      const difficultyTag = document.getElementById('difficulty-tag');
      difficultyTag.className = 'difficulty-tag';
      difficultyTag.classList.add('difficulty-' + problem.difficulty);
      difficultyTag.textContent = problem.difficulty === 'easy' ? '简单' : problem.difficulty === 'medium' ? '中等' : '困难';
      
      // 显示代码编辑器和运行结果区域
      const codeContainer = document.getElementById('code-editor-container');
      codeContainer.style.display = 'block';
      if (isCodeEditorCollapsed) {
        isCodeEditorCollapsed = false;
        document.getElementById('toggle-code-icon').classList.remove('fa-chevron-down');
        document.getElementById('toggle-code-icon').classList.add('fa-chevron-up');
      }
      document.getElementById('code-output').parentElement.parentElement.style.display = 'block';
      
      // 更新代码编辑器
      editor.setValue(problem.code);
      editor.clearSelection();
      
      // 更新答案解析
      document.getElementById('answer-analysis').innerHTML = problem.analysis;
      
      // 重置计时器
      resetTimer();
      
      // 更新问题项状态
      document.querySelectorAll('.problem-item').forEach(item => {
        item.classList.remove('active');
      });
      // 给当前点击的问题项添加 active 类
      const allProblemItems = document.querySelectorAll('.problem-item');
      allProblemItems.forEach(item => {
        const onclick = item.getAttribute('onclick');
        if (onclick && onclick.includes(`loadProgrammingProblem(${problemId})`)) {
          item.classList.add('active');
        }
      });
    }'''
    
    # 修复 loadChoiceQuestion 函数：添加 active 类给被点击的题目
    pattern2 = r'(// 更新问题项状态\s+document\.querySelectorAll\(\'\.problem-item\'\)\.forEach\(item => \{[\s\S]*?item\.classList\.remove\(\'active\'\);[\s\S]*?\}\);[\s\S]*?\})'
    
    # 首先替换 loadProgrammingProblem 函数
    # 使用一个更安全的方法，先找到该函数的结束位置
    # 让我们分别处理每个文件的替换
    new_content = content
    
    # 修复 loadProgrammingProblem
    # 找到函数开始的位置
    load_prog_start = new_content.find('// 加载编程题')
    if load_prog_start != -1:
        # 找到函数结束的位置
        brace_count = 0
        func_start = new_content.find('{', load_prog_start)
        func_end = func_start
        for i in range(func_start, len(new_content)):
            if new_content[i] == '{':
                brace_count += 1
            elif new_content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    func_end = i
                    break
        
        if func_end > func_start:
            old_func = new_content[load_prog_start:func_end+1]
            new_content = new_content[:load_prog_start] + replacement1 + new_content[func_end+1:]
    
    # 现在修复 loadChoiceQuestion 函数，确保它也更新 active 类
    # 找到 loadChoiceQuestion 函数
    load_choice_start = new_content.find('// 加载选择题')
    if load_choice_start != -1:
        # 找到更新问题项状态的部分
        update_status_start = new_content.find('// 更新问题项状态', load_choice_start)
        if update_status_start != -1:
            # 找到该部分的结束位置
            update_status_end = new_content.find('}', update_status_start) + 1
            
            # 替换这部分
            old_update_status = new_content[update_status_start:update_status_end]
            new_update_status = '''      // 更新问题项状态
      document.querySelectorAll('.problem-item').forEach(item => {
        item.classList.remove('active');
      });
      // 给当前点击的问题项添加 active 类
      const allProblemItems = document.querySelectorAll('.problem-item');
      allProblemItems.forEach(item => {
        const onclick = item.getAttribute('onclick');
        if (onclick && onclick.includes(`loadChoiceQuestion('${questionId}')`)) {
          item.classList.add('active');
        }
      });
    }'''
            
            new_content = new_content[:update_status_start] + new_update_status + new_content[update_status_end:]
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ 已修复 {file_path}")
    else:
        print(f"- {file_path} 无需修复或已修复")

# 修复所有文件
for file_path in files_to_fix:
    try:
        fix_file(file_path)
    except Exception as e:
        print(f"✗ 修复 {file_path} 时出错: {e}")
