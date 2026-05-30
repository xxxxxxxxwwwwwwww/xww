
def update_navigation(target_file, course_name, chapters_html):
    """更新目标文件的左侧章节导航"""
    
    # 读取目标文件
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找章节导航部分
    # 找到题库标签页后的标题
    question_bank_pos = content.find('题库标签页')
    title_start = content.find('&lt;h2 class="section-title"&gt;', question_bank_pos)
    right_comment_start = content.find('          &lt;!-- 右侧：问题、代码编辑器、运行结果、答案解析 --&gt;', title_start)
    
    # 替换章节导航部分
    content = content[:title_start] + chapters_html + content[right_comment_start:]
    
    # 写入更新后的文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"成功更新 {target_file} 的章节导航！")

# 数据库原理课程的章节导航HTML
db_chapters = '''            &lt;h2 class="section-title"&gt;数据库原理题库&lt;/h2&gt;

            &lt;!-- 章节列表 --&gt;
            &lt;div class="space-y-6"&gt;
              &lt;!-- 章节1：数据库基础概念 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter1')"&gt;
                  &lt;i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"&gt;&lt;/i&gt;
                  数据库基础概念
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content" id="chapter1-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item active" onclick="loadProgrammingProblem(1)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold"&gt;1&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题1：数据库表设计&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;25分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c1')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;A&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题1&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c2')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;B&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题2&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节2：关系数据库理论 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter2')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"&gt;&lt;/i&gt;
                  关系数据库理论
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter2-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c3')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;C&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题3&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c4')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;D&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题4&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节3：SQL语言 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter3')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"&gt;&lt;/i&gt;
                  SQL语言
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter3-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(2)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;2&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题2：SQL查询练习&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c5')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;E&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题5&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c6')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;F&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题6&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节4：数据库设计 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter4')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"&gt;&lt;/i&gt;
                  数据库设计
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/1&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter4-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c7')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;G&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题7&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节5：数据库管理 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter5')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"&gt;&lt;/i&gt;
                  数据库管理
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/4&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter5-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(3)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;3&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题3：事务处理&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-hard"&gt;困难&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;25分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(4)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;4&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题4：索引优化&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;20分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c8')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;H&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题8&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c9')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;I&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题9&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节6：数据库应用开发 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter6')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"&gt;&lt;/i&gt;
                  数据库应用开发
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter6-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(5)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;5&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题5：Python数据库操作&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c10')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;J&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题10&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

bi_chapters = '''            &lt;h2 class="section-title"&gt;商务智能题库&lt;/h2&gt;

            &lt;!-- 章节列表 --&gt;
            &lt;div class="space-y-6"&gt;
              &lt;!-- 章节1：商务智能基础 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter1')"&gt;
                  &lt;i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"&gt;&lt;/i&gt;
                  商务智能基础
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content" id="chapter1-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item active" onclick="loadChoiceQuestion('c1')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;A&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题1&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c2')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;B&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题2&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节2：数据仓库设计 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter2')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"&gt;&lt;/i&gt;
                  数据仓库设计
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/5&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter2-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(1)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;1&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题1：数据仓库建模&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;25分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(2)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;2&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题2：ETL实现&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c3')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;C&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题3&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c4')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;D&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题4&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c5')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;E&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题5&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节3：OLAP分析 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter3')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"&gt;&lt;/i&gt;
                  OLAP分析
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter3-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(3)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;3&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题3：OLAP多维分析&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;20分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c6')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;F&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题6&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c7')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;G&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题7&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节4：数据可视化 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter4')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"&gt;&lt;/i&gt;
                  数据可视化
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter4-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(4)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;4&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题4：数据可视化&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;20分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c8')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;H&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题8&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节5：商业决策支持 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter5')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"&gt;&lt;/i&gt;
                  商业决策支持
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter5-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(5)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;5&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题5：商业决策支持&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-hard"&gt;困难&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c9')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;I&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题9&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节6：综合项目实践 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter6')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"&gt;&lt;/i&gt;
                  综合项目实践
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/1&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter6-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c10')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;J&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题10&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

sc_chapters = '''            &lt;h2 class="section-title"&gt;供应链分析题库&lt;/h2&gt;

            &lt;!-- 章节列表 --&gt;
            &lt;div class="space-y-6"&gt;
              &lt;!-- 章节1：供应链管理基础 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter1')"&gt;
                  &lt;i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"&gt;&lt;/i&gt;
                  供应链管理基础
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content" id="chapter1-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item active" onclick="loadChoiceQuestion('c1')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;A&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题1&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c2')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;B&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题2&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节2：需求预测分析 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter2')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"&gt;&lt;/i&gt;
                  需求预测分析
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter2-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(1)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;1&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题1：需求预测分析&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;25分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c3')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;C&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题3&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c4')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;D&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题4&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节3：库存优化 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter3')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"&gt;&lt;/i&gt;
                  库存优化
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter3-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(2)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;2&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题2：库存优化管理&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c5')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;E&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题5&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c6')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;F&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题6&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节4：供应商评估 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter4')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"&gt;&lt;/i&gt;
                  供应商评估
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter4-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(3)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;3&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题3：供应商评估分析&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;20分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c7')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;G&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题7&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节5：物流优化 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter5')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"&gt;&lt;/i&gt;
                  物流优化
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter5-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(4)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;4&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题4：物流路线优化&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;20分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c8')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;H&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题8&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c9')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;I&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题9&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;

              &lt;!-- 章节6：综合案例分析 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter6')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"&gt;&lt;/i&gt;
                  综合案例分析
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/2&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter6-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(5)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;5&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;问题5：供应链综合分析&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-hard"&gt;困难&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c10')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;J&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;选择题10&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

def main():
    print("=" * 60)
    print("开始更新章节导航")
    print("=" * 60)
    
    # 更新三个文件的章节导航
    update_navigation('database-principles.html', '数据库原理', db_chapters)
    update_navigation('business-intelligence.html', '商务智能', bi_chapters)
    update_navigation('supply-chain-analysis.html', '供应链分析', sc_chapters)
    
    print("=" * 60)
    print("所有课程章节导航更新完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()

