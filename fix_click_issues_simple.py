#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单可靠的修复脚本 - 从备份恢复并修复点击问题
"""
import re
import os


def fix_course_file(backup_file, target_file):
    """修复课程文件"""
    print(f"正在修复 {target_file}...")
    
    # 读取备份文件
    with open(backup_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 替换 onclick 属性为 data 属性
    # 替换 loadProgrammingProblem 的 onclick
    def replace_programming_onclick(match):
        problem_id = match.group(1)
        return f'data-problem-id="{problem_id}" data-type="programming"'
    
    def replace_choice_onclick(match):
        problem_id = match.group(1)
        return f'data-problem-id="{problem_id}" data-type="choice"'
    
    # 先处理编程题
    content = re.sub(
        r'onclick="loadProgrammingProblem\((\d+)\)"',
        replace_programming_onclick,
        content
    )
    
    # 再处理选择题
    content = re.sub(
        r'onclick="loadChoiceQuestion\(([^\)]+)\)"',
        replace_choice_onclick,
        content
    )
    
    # 2. 找到 DOMContentLoaded 事件并添加事件绑定代码
    dom_content_loaded_pattern = r'(document\.addEventListener\([\'"]DOMContentLoaded[\'"],\s*function\(\)\s*\{)'
    
    # 要插入的事件绑定代码
    event_binding_code = '''
      // === 绑定题目点击事件 ===
      console.log('开始绑定题目项...');
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
      console.log('所有题目项绑定完成！');
      // === 题目点击事件绑定完成 ===
'''
    
    # 检查是否已经有事件绑定代码，避免重复
    if '// === 绑定题目点击事件 ===' in content:
        print("  检测到已存在事件绑定代码，跳过添加")
    else:
        # 在 DOMContentLoaded 函数内部的开始位置插入
        def insert_after_dom_ready(match):
            return match.group(1) + event_binding_code
        
        content = re.sub(
            dom_content_loaded_pattern,
            insert_after_dom_ready,
            content
        )
    
    # 3. 修复 loadProgrammingProblem 和 loadChoiceQuestion 函数中的 active 类切换逻辑
    # 它们之前是用 onclick 查找，现在我们用 data 属性查找
    
    def fix_load_programming(match):
        old_code = match.group(0)
        # 替换旧的 active 类切换代码
        new_code = old_code.replace(
            '''// 更新问题项状态
      document.querySelectorAll('.problem-item').forEach(item => {
        item.classList.remove('active');
      });
      // 给当前点击的问题项添加 active 类
      const allProblemItems = document.querySelectorAll('.problem-item');
      allProblemItems.forEach(item => {
        const onclickAttr = item.getAttribute('onclick');
        if (onclickAttr && onclickAttr.includes('loadProgrammingProblem(' + problemId + ')')) {
          item.classList.add('active');
        }
      });''',
            '''// 更新问题项状态
      const allProblemItems = document.querySelectorAll('.problem-item');
      allProblemItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('data-problem-id') == problemId && item.getAttribute('data-type') === 'programming') {
          item.classList.add('active');
        }
      });'''
        )
        return new_code
    
    # 修复 loadProgrammingProblem
    content = re.sub(
        r'(// 更新问题项状态[\s\S]*?item\.classList\.add\(\'active\'\);[\s\S]*?\n    })',
        fix_load_programming,
        content
    )
    
    def fix_load_choice(match):
        old_code = match.group(0)
        new_code = old_code.replace(
            '''// 更新问题项状态
      document.querySelectorAll('.problem-item').forEach(item => {
        item.classList.remove('active');
      });
      // 给当前点击的问题项添加 active 类
      const allProblemItems = document.querySelectorAll('.problem-item');
      allProblemItems.forEach(item => {
        const onclickAttr = item.getAttribute('onclick');
        if (onclickAttr && onclickAttr.includes('loadChoiceQuestion(\\'' + questionId + '\\')')) {
          item.classList.add('active');
        }
      });''',
            '''// 更新问题项状态
      const allProblemItems = document.querySelectorAll('.problem-item');
      allProblemItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('data-problem-id') === questionId && item.getAttribute('data-type') === 'choice') {
          item.classList.add('active');
        }
      });'''
        )
        return new_code
    
    # 修复 loadChoiceQuestion
    content = re.sub(
        r'(// 更新问题项状态[\s\S]*?item\.classList\.add\(\'active\'\);[\s\S]*?\n    })',
        fix_load_choice,
        content
    )
    
    # 写入目标文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  修复完成: {target_file}")
    return True


def main():
    courses_dir = '/workspace/courses'
    
    # 修复供应链分析
    fix_course_file(
        os.path.join(courses_dir, 'supply-chain-analysis-backup.html'),
        os.path.join(courses_dir, 'supply-chain-analysis.html')
    )
    
    # 修复数据库原理
    fix_course_file(
        os.path.join(courses_dir, 'database-principles-backup.html'),
        os.path.join(courses_dir, 'database-principles.html')
    )
    
    # 修复商业智能 - 用现有的文件作为基础
    fix_course_file(
        os.path.join(courses_dir, 'business-intelligence.html'),
        os.path.join(courses_dir, 'business-intelligence.html')
    )
    
    print("\n所有课程修复完成！")


if __name__ == '__main__':
    main()
