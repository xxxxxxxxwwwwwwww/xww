#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复思路：把所有需要的函数直接写在 problems 数组定义之前！
"""

import re

def fix_file(file_path, extra_vars):
    print(f'\n正在处理: {file_path}')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 找到 script 标签开始处
    script_start = content.find('<script>')
    if script_start == -1:
        print('错误：找不到 script 标签')
        return False
    
    # 在 <script> 之后，problems/choiceQuestions 定义之前，插入核心变量定义
    insert_pos = script_start + len('<script>')
    
    # 2. 先定义全局变量和函数框架
    pre_code = f"""\n
    // ============== 全局变量 ==============
    let editor = null;
    let pyodide = null;
    let currentProblem = 1;
    let timerInterval = null;
    let seconds = 0;
    let isCodeEditorCollapsed = false;
    {extra_vars}
    
    // ============== 核心全局函数（这里直接实现） ==============
    function showTab(tabId) {{
      if(!document.querySelectorAll) return;
      
      const tabs = document.querySelectorAll('.tab-content');
      if(tabs) {{
        tabs.forEach(tab => {{
          tab.classList.add('hidden');
        }});
      }}
      
      const target = document.getElementById(tabId);
      if(target) {{
        target.classList.remove('hidden');
      }}
      
      // 更新导航链接激活状态
      const navLinks = document.querySelectorAll('.nav-link');
      if(navLinks) {{
        navLinks.forEach(link => {{
          link.classList.remove('active');
          const onclickAttr = link.getAttribute('onclick');
          if(onclickAttr && onclickAttr.includes("'" + tabId + "'")) {{
            link.classList.add('active');
          }}
        }});
      }}
    }}
    
    function toggleChapter(chapterId) {{
      if(!document.getElementById) return;
      
      const content = document.getElementById(chapterId + '-content');
      const icon = document.getElementById(chapterId + '-icon');
      
      if(content && icon) {{
        if (content.classList.contains('collapsed')) {{
          content.classList.remove('collapsed');
          icon.classList.remove('fa-chevron-right');
          icon.classList.add('fa-chevron-down');
        }} else {{
          content.classList.add('collapsed');
          icon.classList.remove('fa-chevron-down');
          icon.classList.add('fa-chevron-right');
        }}
      }}
    }}
    
    function scrollToKnowledge(sectionId) {{
      if(!document.getElementById) return;
      const section = document.getElementById(sectionId);
      if (section) {{
        section.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}
    
    function resetTimer() {{
      if(timerInterval) clearInterval(timerInterval);
      seconds = 0;
      if(typeof updateTimer === "function") {{
        updateTimer();
      }}
      timerInterval = setInterval(() => {{
        seconds++;
        if(typeof updateTimer === "function") {{
          updateTimer();
        }}
      }}, 1000);
    }}
    
    // ============== 简单的加载问题函数（确保一定可用） ==============
    function loadProgrammingProblem(problemId) {{
      console.log('loadProgrammingProblem 被调用:', problemId);
      
      // 先确保激活题库标签页
      if(typeof showTab === "function") {{
        showTab('question-bank');
      }}
      
      if(typeof problems === "undefined" || !Array.isArray(problems)) {{
        console.error('problems 数组还没定义');
        return;
      }}
      
      const problem = problems.find(p => p.id === problemId);
      if (!problem) {{
        console.error('找不到问题:', problemId);
        return;
      }}
      
      currentProblem = problemId;
      
      // 更新问题标题
      const titleEl = document.getElementById('problem-title');
      if(titleEl) titleEl.textContent = problem.title;
      
      // 更新问题描述
      const descEl = document.getElementById('problem-description');
      if(descEl) descEl.innerHTML = problem.description;
      
      // 更新难度标签
      const diffTag = document.getElementById('difficulty-tag');
      if(diffTag) {{
        diffTag.className = 'difficulty-tag';
        diffTag.classList.add('difficulty-' + problem.difficulty);
        diffTag.textContent = problem.difficulty === 'easy' ? '简单' : problem.difficulty === 'medium' ? '中等' : '困难';
      }}
      
      // 更新代码编辑器
      if(editor && problem.code) {{
        editor.setValue(problem.code);
        editor.clearSelection();
      }}
      
      // 显示代码区域
      const codeContainer = document.getElementById('code-editor-container');
      if(codeContainer) codeContainer.style.display = 'block';
      const outputContainer = document.getElementById('code-output');
      if(outputContainer && outputContainer.parentElement && outputContainer.parentElement.parentElement) {{
        outputContainer.parentElement.parentElement.style.display = 'block';
      }}
      
      // 更新解析
      const analysisEl = document.getElementById('answer-analysis');
      if(analysisEl) analysisEl.innerHTML = problem.analysis;
      
      // 更新问题项高亮
      const allItems = document.querySelectorAll('.problem-item');
      if(allItems) {{
        allItems.forEach(item => {{
          item.classList.remove('active');
          const onclickAttr = item.getAttribute('onclick');
          if (onclickAttr && onclickAttr.includes('loadProgrammingProblem(' + problemId + ')')) {{
            item.classList.add('active');
          }}
        }});
      }}
      
      if(typeof resetTimer === "function") {{
        resetTimer();
      }}
    }}
    
    function loadChoiceQuestion(questionId) {{
      console.log('loadChoiceQuestion 被调用:', questionId);
      
      if(typeof showTab === "function") {{
        showTab('question-bank');
      }}
      
      if(typeof choiceQuestions === "undefined" || !Array.isArray(choiceQuestions)) {{
        console.error('choiceQuestions 数组还没定义');
        return;
      }}
      
      const question = choiceQuestions.find(q => q.id === questionId);
      if (!question) {{
        console.error('找不到选择题:', questionId);
        return;
      }}
      
      if(typeof _loadChoiceQuestionReal === "function") {{
        _loadChoiceQuestionReal(questionId); // 调用真实函数
      }} else {{
        console.log('真实函数还没加载，用简化版');
        // 简化版实现，确保至少能显示
        const titleEl = document.getElementById('problem-title');
        if(titleEl) titleEl.textContent = question.title;
      }}
    }}
    \n
    """
    
    # 3. 插入代码到 <script> 之后
    content = content[:insert_pos] + pre_code + content[insert_pos:]
    
    # 4. 找到后面真实的函数，重命名防止冲突（特别是 loadChoiceQuestion）
    content = re.sub(r'(function loadChoiceQuestion\()', r'function _loadChoiceQuestionReal(', content)
    
    # 5. 清理之前添加的 window.xxx 暴露代码，现在不需要了
    content = re.sub(r'\s*//\s*暴露到全局作用域.*?(?=\s*</script>)', '', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {file_path} 修复完成')
    return True

# 处理文件
fix_file('/workspace/courses/supply-chain-analysis.html', 
         "let currentChoiceQuestion = null;\n    let selectedAnswer = null;\n    let answeredQuestions = {};")

fix_file('/workspace/courses/database-principles.html', 
         "let currentChoiceQuestion = null;\n    let selectedAnswer = null;\n    let answeredQuestions = {};")

# 商业智能已经可以用了，不过也处理一下以防万一
fix_file('/workspace/courses/business-intelligence.html', 
         "let currentChoiceQuestion = null;\n    let selectedAnswer = null;\n    let answeredQuestions = {};")

print('\n✅ 所有文件修复完成！')
