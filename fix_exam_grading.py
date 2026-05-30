#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复考试系统的答案保存和评分逻辑"""

def fix_exam_system(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复1：答案保存逻辑 - 移除错误的条件判断
    old_save_logic = '''      // 保存当前答案
      if (editor && currentQuestion <= 1) {
        studentAnswers[currentQuestion] = editor.getValue();
      }'''
    
    new_save_logic = '''      // 保存当前答案（如果当前是编程题）
      const currentQ = allExamQuestions.find(q => q.id === currentQuestion);
      if (editor && currentQ && currentQ.type !== 'choice') {
        studentAnswers[currentQuestion] = editor.getValue();
      }'''
    
    content = content.replace(old_save_logic, new_save_logic)
    
    # 修复2：编程题评分逻辑 - 修改判断条件
    old_programming_check = '''        } else {
          // 编程题评分
          if (studentAnswer && studentAnswer.trim() !== question.code.trim()) {
            completedCount++;
            if (studentAnswer.trim() === question.answer.trim()) {
              correctCount++;
              programmingCorrectCount++;
              totalScore += question.score;
            } else {
              totalScore += Math.floor(question.score * 0.5);
            }
          }
        }'''
    
    new_programming_check = '''        } else {
          // 编程题评分 - 只要写了代码就算作答
          if (studentAnswer && studentAnswer.trim().length > 0) {
            completedCount++;
            if (studentAnswer.trim() === question.answer.trim()) {
              correctCount++;
              programmingCorrectCount++;
              totalScore += question.score;
            } else {
              totalScore += Math.floor(question.score * 0.5);
            }
          }
        }'''
    
    content = content.replace(old_programming_check, new_programming_check)
    
    # 修复3：结果页面的编程题判断逻辑
    old_result_check = '''        const isAnswered = studentAnswer && studentAnswer.trim() !== problem.code.trim();
        const isCorrect = isAnswered && studentAnswer.trim() === problem.answer.trim();'''
    
    new_result_check = '''        const isAnswered = studentAnswer && studentAnswer.trim().length > 0;
        const isCorrect = isAnswered && studentAnswer.trim() === problem.answer.trim();'''
    
    content = content.replace(old_result_check, new_result_check)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 已修复 {file_path}')

# 修复供应链考试
fix_exam_system('/workspace/courses/supply-chain-analysis-exam.html')

# 修复商务智能考试
fix_exam_system('/workspace/courses/business-intelligence-exam.html')

print('\n✅ 考试系统的答案保存和评分逻辑已修复！')
print('\n修复内容：')
print('1. 答案保存：现在正确保存编程题的答案')
print('2. 编程题判断：只要写了代码就算作答，不要求与初始代码不同')
print('3. 结果显示：正确显示编程题的作答状态和正确性')
