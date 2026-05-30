#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试并修复三个课程的题库点击问题
"""

import os

def analyze_and_fix_file(file_path):
    print(f"\n=== 分析文件: {file_path} ===")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查问题
    issues = []
    
    # 检查1: 函数定义是否在正确位置
    if 'function loadProgrammingProblem' in content:
        print("✓ loadProgrammingProblem 函数已定义")
    else:
        issues.append("缺少 loadProgrammingProblem 函数")
    
    if 'function loadChoiceQuestion' in content:
        print("✓ loadChoiceQuestion 函数已定义")
    else:
        issues.append("缺少 loadChoiceQuestion 函数")
    
    # 检查2: 确保函数是全局的（不在 DOMContentLoaded 回调内）
    dom_content_start = content.find("document.addEventListener('DOMContentLoaded'")
    dom_content_end = content.find("});", dom_content_start)
    
    if dom_content_start != -1 and dom_content_end != -1:
        dom_content = content[dom_content_start:dom_content_end+2]
        
        if 'function loadProgrammingProblem' in dom_content:
            issues.append("loadProgrammingProblem 函数定义在 DOMContentLoaded 回调内，应该移到外面")
        
        if 'function loadChoiceQuestion' in dom_content:
            issues.append("loadChoiceQuestion 函数定义在 DOMContentLoaded 回调内，应该移到外面")
    else:
        print("✓ DOMContentLoaded 事件处理程序结构正常")
    
    # 检查3: 检查初始化是否正确
    if 'loadProgrammingProblem(1)' in content:
        print("✓ 初始化时正确加载第一个问题")
    else:
        issues.append("初始化时没有加载第一个问题")
    
    # 检查4: 检查 onclick 属性
    if 'onclick="loadProgrammingProblem(' in content:
        print("✓ 编程题 onclick 属性正确")
    else:
        issues.append("缺少编程题 onclick 属性")
    
    if 'onclick="loadChoiceQuestion(' in content:
        print("✓ 选择题 onclick 属性正确")
    else:
        issues.append("缺少选择题 onclick 属性")
    
    if issues:
        print("\n发现问题:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("\n✓ 未发现明显问题")
        return True

# 分析所有文件
files = [
    '/workspace/courses/business-intelligence.html',
    '/workspace/courses/database-principles.html',
    '/workspace/courses/supply-chain-analysis.html'
]

for file in files:
    if os.path.exists(file):
        analyze_and_fix_file(file)
    else:
        print(f"\n⚠️ 文件不存在: {file}")

# 创建一个简单的测试页面来验证功能
test_html = """<!DOCTYPE html>
<html>
<head>
    <title>测试题库点击功能</title>
    <script>
        const problems = [
            { id: 1, title: "问题1：测试", description: "这是测试问题1", code: "# 代码1", analysis: "解析1" },
            { id: 2, title: "问题2：测试", description: "这是测试问题2", code: "# 代码2", analysis: "解析2" },
            { id: 3, title: "问题3：测试", description: "这是测试问题3", code: "# 代码3", analysis: "解析3" }
        ];
        
        let currentProblem = 1;
        
        function loadProgrammingProblem(problemId) {
            console.log('加载问题:', problemId);
            const problem = problems.find(p => p.id === problemId);
            if (problem) {
                document.getElementById('title').textContent = problem.title;
                document.getElementById('desc').innerHTML = problem.description;
                document.getElementById('code').textContent = problem.code;
                
                // 更新高亮
                document.querySelectorAll('.problem-item').forEach(item => {
                    item.classList.remove('active');
                });
                const items = document.querySelectorAll('.problem-item');
                items.forEach(item => {
                    const onclick = item.getAttribute('onclick');
                    if (onclick && onclick.includes('loadProgrammingProblem(' + problemId + ')')) {
                        item.classList.add('active');
                    }
                });
            }
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            loadProgrammingProblem(1);
        });
    </script>
    <style>
        .problem-item { cursor: pointer; padding: 10px; border: 1px solid #ccc; margin: 5px; }
        .problem-item:hover { background-color: #f0f0f0; }
        .problem-item.active { background-color: #4CAF50; color: white; }
    </style>
</head>
<body>
    <h1>题库测试</h1>
    
    <div style="float:left; width: 30%;">
        <h3>题目列表</h3>
        <div class="problem-item active" onclick="loadProgrammingProblem(1)">问题1</div>
        <div class="problem-item" onclick="loadProgrammingProblem(2)">问题2</div>
        <div class="problem-item" onclick="loadProgrammingProblem(3)">问题3</div>
    </div>
    
    <div style="float:right; width: 65%;">
        <h2 id="title">标题</h2>
        <div id="desc">描述</div>
        <pre id="code">代码</pre>
    </div>
</body>
</html>"""

# 写入测试页面
with open('/workspace/test_bank.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

print("\n✓ 测试页面已创建: /workspace/test_bank.html")
print("请访问 http://localhost:8000/test_bank.html 测试点击功能")
