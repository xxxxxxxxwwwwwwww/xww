import re

# 读取文件
with open('data-analysis-exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在 loadChoiceQuestion 函数中添加调试日志
debug_code = '''    function loadChoiceQuestion(problem) {
      console.log('加载选择题:', problem);
      // 隐藏代码编辑器区域
      document.getElementById('exam-code-editor').parentElement.parentElement.style.display = 'none';
      document.getElementById('exam-code-output').parentElement.parentElement.style.display = 'none';
      
      const selectedAnswer = choiceAnswers[problem.id] || null;
      
      let optionsHtml = problem.options.map(opt => {
        let optionClass = 'choice-option';
        if (selectedAnswer === opt.label) {
          optionClass += ' selected';
        }
        return `
          <div class="${optionClass}" onclick="selectExamChoice('${problem.id}', '${opt.label}')" data-label="${opt.label}">
            <div class="choice-label">${opt.label}</div>
            <div class="flex-1 text-gray-200">${opt.text}</div>
          </div>
        `;
      }).join('');

      console.log('选项HTML:', optionsHtml);

      document.getElementById('exam-problem-description').innerHTML = `
        <div class="mb-6">
          <p class="text-lg text-gray-200">${problem.question}</p>
        </div>
        <div class="space-y-3" id="choice-options">
          ${optionsHtml}
        </div>
      `;
    }'''

# 替换原来的 loadChoiceQuestion 函数
content = re.sub(
    r'    function loadChoiceQuestion\(problem\) \{.*?\}',
    debug_code,
    content,
    flags=re.DOTALL
)

# 在 loadExamQuestion 函数中添加调试
content = re.sub(
    r'    function loadExamQuestion\(index\) \{',
    '''    function loadExamQuestion(index) {
      console.log('加载题目索引:', index);
      console.log('当前所有题目:', allExamQuestions);''',
    content
)

# 写入更新后的文件
with open('data-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("调试代码已添加")
