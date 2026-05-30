#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完全修复查看答案功能"""

def fix_review_answers(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复1：showAnswerReview函数中的编程题判断逻辑
    old_review_logic = '''      examProblems.forEach((problem, index) => {
        const studentAnswer = studentAnswers[problem.id];
        const isCorrect = studentAnswer && studentAnswer.trim() === problem.answer.trim();
        const isAnswered = studentAnswer && studentAnswer.trim() !== problem.code.trim();'''
    
    new_review_logic = '''      examProblems.forEach((problem, index) => {
        const studentAnswer = studentAnswers[problem.id];
        const isCorrect = studentAnswer && studentAnswer.trim() === problem.answer.trim();
        const isAnswered = studentAnswer && studentAnswer.trim().length > 0;'''
    
    content = content.replace(old_review_logic, new_review_logic)
    
    # 修复2：修复答案显示中的"你的答案"部分，显示完整的代码
    old_answer_display = '''            <div class="text-sm text-gray-400 mb-2">
              <strong>你的答案：</strong>
              <span class="${isCorrect ? 'text-emerald-400' : 'text-red-400'}">${isAnswered ? (isCorrect ? '正确' : '错误') : '未作答'}</span>
            </div>
            <div class="bg-dark-gray p-3 rounded text-sm">
              <strong class="text-emerald-400">参考答案：</strong>
              <pre class="mt-2 text-gray-300 whitespace-pre-wrap">${problem.answer || '无'}</pre>
            </div>'''
    
    new_answer_display = '''            <div class="text-sm text-gray-400 mb-2">
              <strong>你的答案：</strong>
              <span class="${isCorrect ? 'text-emerald-400' : 'text-red-400'}">${isAnswered ? (isCorrect ? '正确' : '错误') : '未作答'}</span>
            </div>
            ${isAnswered ? `
            <div class="bg-dark-gray p-3 rounded text-sm mb-2">
              <strong class="text-cyan-400">你的代码：</strong>
              <pre class="mt-2 text-gray-300 whitespace-pre-wrap">${studentAnswer}</pre>
            </div>
            ` : ''}
            <div class="bg-dark-gray p-3 rounded text-sm">
              <strong class="text-emerald-400">参考答案：</strong>
              <pre class="mt-2 text-gray-300 whitespace-pre-wrap">${problem.answer || '无'}</pre>
            </div>'''
    
    content = content.replace(old_answer_display, new_answer_display)
    
    # 修复3：确保submitExam中正确保存original-result
    old_submit_code = '''      // 更新结果页面
      document.getElementById('result-name').textContent = `姓名：${studentName}`;
      document.getElementById('total-score').textContent = totalScore;
      document.getElementById('used-time').textContent = usedMinutes;
      document.getElementById('completion-rate').textContent = completionRate;
      document.getElementById('completed-count').textContent = completedCount;
      document.getElementById('correct-count').textContent = correctCount;
      document.getElementById('wrong-count').textContent = wrongCount > 0 ? wrongCount : 0;'''
    
    new_submit_code = '''      // 保存原始结果HTML
      const originalResultEl = document.getElementById('exam-result');
      const originalResultHtml = originalResultEl.innerHTML;
      
      // 更新结果页面
      document.getElementById('result-name').textContent = `姓名：${studentName}`;
      document.getElementById('total-score').textContent = totalScore;
      document.getElementById('used-time').textContent = usedMinutes;
      document.getElementById('completion-rate').textContent = completionRate;
      document.getElementById('completed-count').textContent = completedCount;
      document.getElementById('correct-count').textContent = correctCount;
      document.getElementById('wrong-count').textContent = wrongCount > 0 ? wrongCount : 0;
      
      // 保存更新后的原始结果
      const updatedOriginalHtml = originalResultEl.innerHTML;
      window.originalResultHTML = updatedOriginalHtml;'''
    
    content = content.replace(old_submit_code, new_submit_code)
    
    # 修复4：简化showAnswerReview的返回逻辑
    old_return_button = '''            <button onclick="document.getElementById('exam-result').innerHTML = document.getElementById('original-result').innerHTML; initResultEvents();" class="btn-secondary text-sm">
              <i class="fa fa-arrow-left"></i> 返回
            </button>'''
    
    new_return_button = '''            <button onclick="window.restoreOriginalResult();" class="btn-secondary text-sm">
              <i class="fa fa-arrow-left"></i> 返回
            </button>'''
    
    content = content.replace(old_return_button, new_return_button)
    
    # 修复5：修改showAnswerReview中保存original-result的方式
    old_original_save = '''      const originalResult = resultDiv.innerHTML;
      resultDiv.innerHTML = `
        <div id="original-result" class="hidden">${originalResult}</div>
        ${html}
      `;'''
    
    new_original_save = '''      // 保存原始结果
      if (!window.originalResultHTML) {
        window.originalResultHTML = resultDiv.innerHTML;
      }
      
      resultDiv.innerHTML = html;'''
    
    content = content.replace(old_original_save, new_original_save)
    
    # 修复6：添加restoreOriginalResult函数
    old_init_result_events = '''    function initResultEvents() {
      document.getElementById('back-to-course').addEventListener('click', function() {
        window.location.href = 'supply-chain-analysis.html';
      });
      document.getElementById('review-answers').addEventListener('click', function() {
        showAnswerReview();
      });
    }'''
    
    new_init_result_events = '''    function restoreOriginalResult() {
      const resultDiv = document.getElementById('exam-result');
      if (window.originalResultHTML) {
        resultDiv.innerHTML = window.originalResultHTML;
        initResultEvents();
      }
    }
    
    function initResultEvents() {
      document.getElementById('back-to-course').addEventListener('click', function() {
        window.location.href = 'supply-chain-analysis.html';
      });
      document.getElementById('review-answers').addEventListener('click', function() {
        showAnswerReview();
      });
    }'''
    
    content = content.replace(old_init_result_events, new_init_result_events)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 已修复 {file_path} 的查看答案功能')

# 修复供应链考试
fix_review_answers('/workspace/courses/supply-chain-analysis-exam.html')

# 修复商务智能考试
fix_review_answers('/workspace/courses/business-intelligence-exam.html')

print('\n✅ 查看答案功能已完全修复！')
print('\n修复内容：')
print('1. 修复编程题的判断逻辑：只要有答案就显示')
print('2. 答案页面显示学生的完整代码')
print('3. 修复从答案页面返回到结果页面的功能')
print('4. 优化了结果保存和恢复逻辑')
