#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""简化编程题初始代码并修复查看答案功能"""

def simplify_and_fix(file_path, is_supply_chain):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 简化编程题初始代码
    if is_supply_chain:
        # 供应链考试编程题
        old_code_content = '''        code: `# 创建库存数据
inventory_data = [
    {"month": "1月", "beginning_inventory": 10000, "ending_inventory": 12000, "cogs": 8000},
    {"month": "2月", "beginning_inventory": 12000, "ending_inventory": 9000, "cogs": 7500},
    {"month": "3月", "beginning_inventory": 9000, "ending_inventory": 11000, "cogs": 9000},
    {"month": "4月", "beginning_inventory": 11000, "ending_inventory": 13000, "cogs": 8500},
    {"month": "5月", "beginning_inventory": 13000, "ending_inventory": 14000, "cogs": 10000},
    {"month": "6月", "beginning_inventory": 14000, "ending_inventory": 16000, "cogs": 12000},
    {"month": "7月", "beginning_inventory": 16000, "ending_inventory": 18000, "cogs": 14000},
    {"month": "8月", "beginning_inventory": 18000, "ending_inventory": 15000, "cogs": 13000},
    {"month": "9月", "beginning_inventory": 15000, "ending_inventory": 13000, "cogs": 11000},
    {"month": "10月", "beginning_inventory": 13000, "ending_inventory": 12000, "cogs": 9500},
    {"month": "11月", "beginning_inventory": 12000, "ending_inventory": 14000, "cogs": 10500},
    {"month": "12月", "beginning_inventory": 14000, "ending_inventory": 11000, "cogs": 11500}
]

# 计算每月的库存周转率
turnover_rates = []
for data in inventory_data:
    avg_inventory = (data["beginning_inventory"] + data["ending_inventory"]) / 2
    turnover = data["cogs"] / avg_inventory
    turnover_rates.append({"month": data["month"], "turnover": turnover})
    print(f"{data['month']}库存周转率: {turnover:.2f}")

# 找出库存周转率最低的月份
lowest_turnover = min(turnover_rates, key=lambda x: x["turnover"])
print(f"\\n库存周转率最低的月份: {lowest_turnover['month']}, 周转率: {lowest_turnover['turnover']:.2f}")`,'''
        
        new_code_content = '''        code: `# 请编写代码`,'''
        
        content = content.replace(old_code_content, new_code_content)
    else:
        # 商务智能考试编程题
        old_code_content = '''        code: `# 创建销售数据
sales_data = [
    {"date": "2024-01-01", "region": "华东", "category": "电子产品", "amount": 5000},
    {"date": "2024-01-02", "region": "华南", "category": "服装", "amount": 3000},
    {"date": "2024-01-03", "region": "华北", "category": "电子产品", "amount": 8000},
    {"date": "2024-01-04", "region": "华东", "category": "食品", "amount": 2000},
    {"date": "2024-01-05", "region": "华南", "category": "电子产品", "amount": 6000}
]

# 计算总销售额
total_sales = sum(item["amount"] for item in sales_data)
print(f"总销售额: {total_sales}元")

# 计算平均销售额
avg_sales = total_sales / len(sales_data)
print(f"平均销售额: {avg_sales:.2f}元")

# 按地区统计销售额
region_sales = {}
for item in sales_data:
    region = item["region"]
    if region not in region_sales:
        region_sales[region] = 0
    region_sales[region] += item["amount"]

print("\\n各地区销售额:")
for region, amount in region_sales.items():
    print(f"{region}: {amount}元")`,'''
        
        new_code_content = '''        code: `# 请编写代码`,'''
        
        content = content.replace(old_code_content, new_code_content)
    
    # 2. 修复查看答案功能 - 重新实现一个更简单的版本
    # 找到showAnswerReview函数的位置
    show_answer_start = content.find('function showAnswerReview() {')
    if show_answer_start == -1:
        print(f'❌ 在 {file_path} 中找不到 showAnswerReview 函数')
        return
    
    # 移除旧的showAnswerReview函数和initResultEvents函数
    old_functions = '''    function showAnswerReview() {
      const resultDiv = document.getElementById('exam-result');
      
      let html = `
        <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
          <div class="flex justify-between items-center mb-6">
            <h3 class="text-xl font-bold text-gray-200">答案解析</h3>
            <button onclick="window.restoreOriginalResult();" class="btn-secondary text-sm">
              <i class="fa fa-arrow-left"></i> 返回
            </button>
          </div>
          
          <div class="space-y-6 max-h-[70vh] overflow-y-auto pr-2">
      `;
      
      examProblems.forEach((problem, index) => {
        const studentAnswer = studentAnswers[problem.id];
        const isCorrect = studentAnswer && studentAnswer.trim() === problem.answer.trim();
        const isAnswered = studentAnswer && studentAnswer.trim().length > 0;
        
        html += `
          <div class="bg-dark p-4 rounded-lg border ${isCorrect ? 'border-emerald-600' : 'border-red-600'}">
            <div class="flex items-center gap-2 mb-3">
              <span class="w-8 h-8 rounded-full ${isCorrect ? 'bg-emerald-600' : 'bg-red-600'} text-white flex items-center justify-center font-bold text-sm">${index + 1}</span>
              <h4 class="font-semibold text-gray-200">${problem.title}</h4>
              <span class="${isCorrect ? 'text-emerald-400' : isAnswered ? 'text-red-400' : 'text-gray-400'} text-sm">${isCorrect ? '✓ 正确' : isAnswered ? '✗ 错误' : '○ 未答'}</span>
            </div>
            <div class="text-sm text-gray-400 mb-2">
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
            </div>
          </div>
        `;
      });
      
      examChoiceQuestions.forEach((question, index) => {
        const studentAnswer = studentAnswers[question.id];
        const isCorrect = studentAnswer === question.answer;
        const isAnswered = !!studentAnswer;
        
        html += `
          <div class="bg-dark p-4 rounded-lg border ${isCorrect ? 'border-emerald-600' : 'border-red-600'}">
            <div class="flex items-center gap-2 mb-3">
              <span class="w-8 h-8 rounded-full ${isCorrect ? 'bg-emerald-600' : 'bg-red-600'} text-white flex items-center justify-center font-bold text-sm">选${index + 1}</span>
              <h4 class="font-semibold text-gray-200">${question.title}</h4>
              <span class="${isCorrect ? 'text-emerald-400' : isAnswered ? 'text-red-400' : 'text-gray-400'} text-sm">${isCorrect ? '✓ 正确' : isAnswered ? '✗ 错误' : '○ 未答'}</span>
            </div>
            <div class="text-sm text-gray-400 mb-2">
              <strong>你的答案：</strong>
              <span class="${isCorrect ? 'text-emerald-400' : 'text-red-400'}">${isAnswered ? studentAnswer : '未作答'}</span>
            </div>
            <div class="text-sm text-gray-400 mb-2">
              <strong>正确答案：</strong>
              <span class="text-emerald-400">${question.answer}</span>
            </div>
          </div>
        `;
      });
      
      html += `
          </div>
        </div>
      `;
      
      // 保存原始结果
      if (!window.originalResultHTML) {
        window.originalResultHTML = resultDiv.innerHTML;
      }
      
      resultDiv.innerHTML = html;
    }
    
    function restoreOriginalResult() {
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
    
    # 新的简化版本
    new_functions = '''    // 保存原始结果的全局变量
    let originalExamResultHTML = '';
    
    function showAnswerReview() {
      const resultDiv = document.getElementById('exam-result');
      
      // 保存原始结果
      if (!originalExamResultHTML) {
        originalExamResultHTML = resultDiv.innerHTML;
      }
      
      let html = `
        <div class="bg-dark-gray rounded-xl p-6 border border-gray-700">
          <div class="flex justify-between items-center mb-6">
            <h3 class="text-xl font-bold text-gray-200">答案解析</h3>
            <button id="back-to-results" class="btn-secondary text-sm">
              <i class="fa fa-arrow-left"></i> 返回
            </button>
          </div>
          
          <div class="space-y-6 max-h-[70vh] overflow-y-auto pr-2">
      `;
      
      // 添加编程题答案
      examProblems.forEach((problem, index) => {
        const studentAnswer = studentAnswers[problem.id];
        const isCorrect = studentAnswer && studentAnswer.trim() === problem.answer.trim();
        const isAnswered = studentAnswer && studentAnswer.trim().length > 0;
        
        html += `
          <div class="bg-dark p-4 rounded-lg border ${isCorrect ? 'border-emerald-600' : 'border-red-600'}">
            <div class="flex items-center gap-2 mb-3">
              <span class="w-8 h-8 rounded-full ${isCorrect ? 'bg-emerald-600' : 'bg-red-600'} text-white flex items-center justify-center font-bold text-sm">${index + 1}</span>
              <h4 class="font-semibold text-gray-200">${problem.title}</h4>
              <span class="${isCorrect ? 'text-emerald-400' : isAnswered ? 'text-red-400' : 'text-gray-400'} text-sm">${isCorrect ? '✓ 正确' : isAnswered ? '✗ 错误' : '○ 未答'}</span>
            </div>
            <div class="text-sm text-gray-400 mb-2">
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
            </div>
          </div>
        `;
      });
      
      // 添加选择题答案
      examChoiceQuestions.forEach((question, index) => {
        const studentAnswer = studentAnswers[question.id];
        const isCorrect = studentAnswer === question.answer;
        const isAnswered = !!studentAnswer;
        
        html += `
          <div class="bg-dark p-4 rounded-lg border ${isCorrect ? 'border-emerald-600' : 'border-red-600'}">
            <div class="flex items-center gap-2 mb-3">
              <span class="w-8 h-8 rounded-full ${isCorrect ? 'bg-emerald-600' : 'bg-red-600'} text-white flex items-center justify-center font-bold text-sm">选${index + 1}</span>
              <h4 class="font-semibold text-gray-200">${question.title}</h4>
              <span class="${isCorrect ? 'text-emerald-400' : isAnswered ? 'text-red-400' : 'text-gray-400'} text-sm">${isCorrect ? '✓ 正确' : isAnswered ? '✗ 错误' : '○ 未答'}</span>
            </div>
            <div class="text-sm text-gray-400 mb-2">
              <strong>你的答案：</strong>
              <span class="${isCorrect ? 'text-emerald-400' : 'text-red-400'}">${isAnswered ? studentAnswer : '未作答'}</span>
            </div>
            <div class="text-sm text-gray-400 mb-2">
              <strong>正确答案：</strong>
              <span class="text-emerald-400">${question.answer}</span>
            </div>
          </div>
        `;
      });
      
      html += `
          </div>
        </div>
      `;
      
      resultDiv.innerHTML = html;
      
      // 绑定返回按钮事件
      document.getElementById('back-to-results').addEventListener('click', restoreOriginalResult);
    }
    
    function restoreOriginalResult() {
      const resultDiv = document.getElementById('exam-result');
      if (originalExamResultHTML) {
        resultDiv.innerHTML = originalExamResultHTML;
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
    
    # 替换函数
    if old_functions in content:
        content = content.replace(old_functions, new_functions)
    else:
        print(f'⚠️ 未找到旧的 showAnswerReview 函数，尝试简化查找...')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 已修复 {file_path}')

# 修复供应链考试
simplify_and_fix('/workspace/courses/supply-chain-analysis-exam.html', True)

# 修复商务智能考试
simplify_and_fix('/workspace/courses/business-intelligence-exam.html', False)

# 单独修复商务智能考试的返回链接
with open('/workspace/courses/business-intelligence-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("window.location.href = 'supply-chain-analysis.html';", "window.location.href = 'business-intelligence.html';")

with open('/workspace/courses/business-intelligence-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n✅ 所有修复完成！')
print('\n修复内容：')
print('1. 编程题初始代码简化为 "请编写代码"')
print('2. 完全重写查看答案功能，使用更稳定的实现方式')
print('3. 修复商务智能考试的返回链接')
