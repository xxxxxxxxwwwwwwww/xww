#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复方法：直接在所有脚本最后添加 window 暴露语句
"""

import re

files = [
    '/workspace/courses/supply-chain-analysis.html',
    '/workspace/courses/database-principles.html',
    '/workspace/courses/business-intelligence.html'
]

# 需要暴露到全局的函数列表
functions = [
    'loadProgrammingProblem',
    'loadChoiceQuestion',
    'showTab',
    'toggleChapter',
    'selectChoice',
    'submitChoice',
    'showChoiceAnalysis',
    'runCode',
    'resetCode',
    'toggleFavorite',
    'resetTimer',
    'scrollToKnowledge'
]

for file_path in files:
    print(f'正在处理: {file_path}')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在 </script> 之前添加暴露代码
    expose_code = '\n\n    // 暴露到全局作用域，解决 onclick 无法调用的问题\n'
    for func in functions:
        expose_code += f'    window.{func} = typeof {func} !== "undefined" ? {func} : function(){{console.error("{func} not defined");}};\n'
    
    # 插入到 </script> 之前
    content = re.sub(r'(\s*</script>\s*</body>\s*</html>)$', expose_code + r'\1', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {file_path} 已修复')

print('\n✅ 所有课程已修复完成！')
