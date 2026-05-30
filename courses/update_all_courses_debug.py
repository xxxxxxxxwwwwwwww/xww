
import re

# 定义每个课程的配置
courses = {
    'database-principles.html': {
        'title': '数据库原理',
        'updated_file': 'database-principles-updated.html',
        'chapters': [
            {'name': '数据库基础概念', 'problems': [1], 'choices': ['c1', 'c2']},
            {'name': '关系数据库理论', 'problems': [], 'choices': ['c3', 'c4']},
            {'name': 'SQL语言', 'problems': [2], 'choices': ['c5', 'c6']},
            {'name': '数据库设计', 'problems': [], 'choices': ['c7']},
            {'name': '数据库管理', 'problems': [3, 4], 'choices': ['c8', 'c9']},
            {'name': '数据库应用开发', 'problems': [5], 'choices': ['c10']}
        ]
    },
    'business-intelligence.html': {
        'title': '商务智能',
        'updated_file': 'business-intelligence-updated.html',
        'chapters': [
            {'name': '商务智能基础', 'problems': [], 'choices': ['c1', 'c2']},
            {'name': '数据仓库设计', 'problems': [1, 2], 'choices': ['c3', 'c4', 'c5']},
            {'name': 'OLAP分析', 'problems': [3], 'choices': ['c6', 'c7']},
            {'name': '数据可视化', 'problems': [4], 'choices': ['c8']},
            {'name': '商业决策支持', 'problems': [5], 'choices': ['c9']},
            {'name': '综合项目实践', 'problems': [], 'choices': ['c10']}
        ]
    },
    'supply-chain-analysis.html': {
        'title': '供应链分析',
        'updated_file': 'supply-chain-updated.html',
        'chapters': [
            {'name': '供应链管理基础', 'problems': [], 'choices': ['c1', 'c2']},
            {'name': '需求预测分析', 'problems': [1], 'choices': ['c3', 'c4']},
            {'name': '库存优化', 'problems': [2], 'choices': ['c5', 'c6']},
            {'name': '供应商评估', 'problems': [3], 'choices': ['c7']},
            {'name': '物流优化', 'problems': [4], 'choices': ['c8', 'c9']},
            {'name': '综合案例分析', 'problems': [5], 'choices': ['c10']}
        ]
    }
}


def read_file(file_path):
    """读取文件内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(file_path, content):
    """写入文件内容"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_chapter_html(chapters, course_title):
    """生成章节导航HTML"""
    html_parts = []
    
    html_parts.append(f'            &lt;h2 class="section-title"&gt;{course_title}题库&lt;/h2&gt;\n\n            &lt;!-- 章节列表 --&gt;\n            &lt;div class="space-y-6"&gt;\n')
    
    for i, chapter in enumerate(chapters):
        chapter_num = i + 1
        is_active = i == 0
        
        html_parts.append(f'            &lt;!-- 章节{chapter_num}：{chapter["name"]} --&gt;\n')
        html_parts.append(f'            &lt;div class="chapter-item"&gt;\n')
        html_parts.append(f'                &lt;h3 class="topic-title" onclick="toggleChapter(\'chapter{chapter_num}\')"&gt;\n')
        html_parts.append(f'                    &lt;i class="fa fa-chevron-{"down" if is_active else "right"} text-gray-400 transition-transform duration-300" id="chapter{chapter_num}-icon"&gt;&lt;/i&gt;\n')
        html_parts.append(f'                    {chapter["name"]}\n')
        html_parts.append(f'                    &lt;span class="ml-auto text-xs text-gray-400"&gt;\n')
        total_items = len(chapter['problems']) + len(chapter['choices'])
        html_parts.append(f'                        &lt;span class="chapter-progress"&gt;0/{total_items}&lt;/span&gt;\n')
        html_parts.append(f'                        &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;\n')
        html_parts.append(f'                    &lt;/span&gt;\n')
        html_parts.append(f'                &lt;/h3&gt;\n')
        html_parts.append(f'                &lt;div class="chapter-content{" collapsed" if not is_active else ""}" id="chapter{chapter_num}-content"&gt;\n')
        
        # 添加编程题
        if chapter['problems']:
            html_parts.append(f'                    &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;\n')
            for problem_id in chapter['problems']:
                html_parts.append(f'                    &lt;div class="problem-item{" active" if problem_id == 1 else ""}" onclick="loadProgrammingProblem({problem_id})"&gt;\n')
                html_parts.append(f'                        &lt;div class="w-8 h-8 rounded-full bg-{"cyan-500 flex items-center justify-center text-gray-900" if problem_id == 1 else "gray-700 flex items-center justify-center"} font-bold"&gt;{problem_id}&lt;/div&gt;\n')
                html_parts.append(f'                        &lt;div class="flex-1"&gt;\n')
                html_parts.append(f'                            &lt;div class="font-medium"&gt;问题{problem_id}&lt;/div&gt;\n')
                html_parts.append(f'                            &lt;div class="flex items-center gap-2 mt-1"&gt;\n')
                html_parts.append(f'                                &lt;span class="difficulty-tag difficulty-{"medium" if problem_id in [3, 4] else "easy" if problem_id == 2 else "hard"}"&gt;{"中等" if problem_id in [3, 4] else "简单" if problem_id == 2 else "困难"}&lt;/span&gt;\n')
                html_parts.append(f'                                &lt;span class="text-xs text-gray-400"&gt;{"20" if problem_id == 4 else "25" if problem_id == 1 else "30"}分钟&lt;/span&gt;\n')
                html_parts.append(f'                            &lt;/div&gt;\n')
                html_parts.append(f'                        &lt;/div&gt;\n')
                html_parts.append(f'                    &lt;/div&gt;\n')
        
        # 添加选择题
        if chapter['choices']:
            html_parts.append(f'                    &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;\n')
            for j, choice_id in enumerate(chapter['choices']):
                letter = chr(ord('A') + j)
                html_parts.append(f'                    &lt;div class="problem-item" onclick="loadChoiceQuestion(\'{choice_id}\')"&gt;\n')
                html_parts.append(f'                        &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;{letter}&lt;/div&gt;\n')
                html_parts.append(f'                        &lt;div class="flex-1"&gt;\n')
                html_parts.append(f'                            &lt;div class="font-medium"&gt;选择题{j + 1}&lt;/div&gt;\n')
                html_parts.append(f'                            &lt;div class="flex items-center gap-2 mt-1"&gt;\n')
                html_parts.append(f'                                &lt;span class="difficulty-tag difficulty-{"medium" if choice_id in ["c2", "c4", "c5", "c7", "c9", "c10"] else "easy"}"&gt;{"中等" if choice_id in ["c2", "c4", "c5", "c7", "c9", "c10"] else "简单"}&lt;/span&gt;\n')
                html_parts.append(f'                                &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;\n')
                html_parts.append(f'                            &lt;/div&gt;\n')
                html_parts.append(f'                        &lt;/div&gt;\n')
                html_parts.append(f'                    &lt;/div&gt;\n')
        
        html_parts.append(f'                &lt;/div&gt;\n')
        html_parts.append(f'            &lt;/div&gt;\n\n')
    
    html_parts.append('            &lt;/div&gt;\n')
    
    return ''.join(html_parts)


def update_course(html_file, config):
    """更新单个课程文件"""
    print(f"\n正在更新课程: {config['title']}")
    
    # 读取原始HTML
    html_content = read_file(html_file)
    
    # 读取更新后的题目数据
    with open(config['updated_file'], 'r', encoding='utf-8') as f:
        new_data = f.read()
    
    # 提取新的problems和choiceQuestions
    problems_match = re.search(r'(    // 问题数据\n    const problems = \[.*?\];\n)', new_data, re.DOTALL)
    choices_match = re.search(r'(    // 选择题数据\n    const choiceQuestions = \[.*?\];\n)', new_data, re.DOTALL)
    
    if not problems_match or not choices_match:
        print(f"❌ 无法从 {config['updated_file']} 中提取数据")
        return False
    
    new_problems = problems_match.group(1)
    new_choices = choices_match.group(1)
    
    # 1. 更新problems数组
    problems_pattern = r'(    // 问题数据\n    )const problems = \[.*?\];\n'
    html_content = re.sub(problems_pattern, new_problems, html_content, flags=re.DOTALL)
    
    # 2. 更新choiceQuestions数组
    choices_pattern = r'(    // 选择题数据\n    )const choiceQuestions = \[.*?\];\n'
    html_content = re.sub(choices_pattern, new_choices, html_content, flags=re.DOTALL)
    
    # 3. 调试：查找关键注释
    print("查找关键注释：")
    print(f"第一个'左侧'注释位置：{html_content.find('左侧')}")
    print(f"第一个'错题'注释位置：{html_content.find('错题')}")
    print(f"第一个'章节列表'注释位置：{html_content.find('章节列表')}")
    
    # 先找到第222行左右的标题
    section_title = '            &lt;h2 class="section-title"&gt;数据分析技术题库&lt;/h2&gt;'
    section_title_start = html_content.find(section_title)
    
    if section_title_start == -1:
        print(f"❌ 无法找到原标题")
        return False
    
    # 查找右侧注释的位置
    right_comment = '          &lt;!-- 右侧：问题、代码编辑器、运行结果、答案解析 --&gt;'
    right_nav_start = html_content.find(right_comment, section_title_start)
    
    if right_nav_start == -1:
        print(f"❌ 无法找到右侧注释")
        return False
    
    print(f"✅ 找到原标题位置：{section_title_start}")
    print(f"✅ 找到右侧注释位置：{right_nav_start}")
    
    # 生成新的章节导航HTML
    new_chapter_html = generate_chapter_html(config['chapters'], config['title'])
    
    # 替换
    html_content = html_content[:section_title_start] + new_chapter_html + html_content[right_nav_start:]
    
    # 写入更新后的文件
    write_file(html_file, html_content)
    print(f"✅ 成功更新 {html_file}")
    
    return True


def main():
    """主函数"""
    print("=" * 60)
    print("课程题库更新工具 - 调试版")
    print("=" * 60)
    
    success_count = 0
    for html_file, config in courses.items():
        if update_course(html_file, config):
            success_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"更新完成！成功更新 {success_count}/{len(courses)} 个课程")
    print('=' * 60)


if __name__ == '__main__':
    main()
