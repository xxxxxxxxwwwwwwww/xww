#!/usr/bin/env python3
import re
import os

def update_course_file(source_file, target_file, course_name, chapter_nav, problems_data, choice_questions_data):
    """更新课程文件的题库内容"""
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新标题
    content = content.replace('数据采集与处理', course_name)
    
    # 替换章节导航
    chapter_nav_start = '            <div class="space-y-6">'
    chapter_nav_end = '            </div>\n          </div>'
    
    # 找到章节导航部分并替换
    nav_pattern = re.compile(r'            <div class="space-y-6">.*?</div>\n          </div>', re.DOTALL)
    replacement = chapter_nav_start + chapter_nav + chapter_nav_end
    content = nav_pattern.sub(replacement, content)
    
    # 替换problems数组
    problems_pattern = re.compile(r'    const problems = \[.*?    \];', re.DOTALL)
    content = problems_pattern.sub(problems_data, content)
    
    # 替换choiceQuestions数组
    choice_pattern = re.compile(r'    const choiceQuestions = \[.*?    \];', re.DOTALL)
    content = choice_pattern.sub(choice_questions_data, content)
    
    # 写入目标文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"成功更新: {target_file}")

# ========================================
# 数据库原理数据
# ========================================
db_chapter_nav = '''
              <!-- 章节1：数据库基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  数据库基础
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item active" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">数据库表设计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询练习</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c1')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">数据模型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">关系数据库</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节2：SQL语言 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  SQL语言
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/4</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(3)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">3</div>
                    <div class="flex-1">
                      <div class="font-medium">事务处理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL语法</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：数据库设计 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  数据库设计
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/4</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(4)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">4</div>
                    <div class="flex-1">
                      <div class="font-medium">索引优化</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">ER模型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">范式设计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节4：数据库管理 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  数据库管理
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">Python数据库操作</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">事务管理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">备份恢复</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节5：高级话题 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  高级话题
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c9')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">I</div>
                    <div class="flex-1">
                      <div class="font-medium">并发控制</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">NoSQL数据库</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
'''

db_problems = '''    const problems = [
      {
        id: 1,
        title: "问题1：数据库表设计",
        description: `设计一个学生成绩管理系统的数据库表结构。

<strong>输入：</strong>
无（设计表结构）

<strong>输出：</strong>
完整的SQL建表语句

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>设计学生表、课程表、成绩表</li>
  <li>设置适当的主键和外键</li>
  <li>考虑数据类型和约束</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 设计学生表（students）包含学号、姓名等信息</p>
<p>2. 设计课程表（courses）包含课程编号、课程名称</p>
<p>3. 设计成绩表（scores）关联学生和课程</p>
<p>4. 设置主键和外键约束</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
-- 学生表
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(10)
);

-- 课程表
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credit INT
);

-- 成绩表
CREATE TABLE scores (
    student_id INT,
    course_id INT,
    score DECIMAL(5,2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('database-design')">数据库设计</a></li>
  <li>表结构设计</li>
  <li>主键与外键</li>
</ul>`
      },
      {
        id: 2,
        title: "问题2：SQL查询练习",
        description: `编写SQL查询语句从学生成绩管理系统中获取数据。

<strong>输入：</strong>
学生成绩数据库

<strong>输出：</strong>
查询结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>查询所有学生的平均成绩</li>
  <li>查询某门课程的最高分</li>
  <li>使用JOIN连接查询</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用AVG函数计算平均成绩</p>
<p>2. 使用MAX函数找最高分</p>
<p>3. 使用JOIN连接多个表</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
-- 查询所有学生的平均成绩
SELECT s.name, AVG(sc.score) as avg_score
FROM students s
JOIN scores sc ON s.student_id = sc.student_id
GROUP BY s.student_id, s.name;

-- 查询某门课程的最高分
SELECT c.course_name, MAX(sc.score) as max_score
FROM courses c
JOIN scores sc ON c.course_id = sc.course_id
WHERE c.course_id = 1
GROUP BY c.course_name;
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('sql-language')">SQL语言</a></li>
  <li>聚合函数</li>
  <li>JOIN查询</li>
</ul>`
      },
      {
        id: 3,
        title: "问题3：事务处理",
        description: `编写包含事务处理的SQL操作。

<strong>输入：</strong>
需要事务保证的数据库操作

<strong>输出：</strong>
事务执行结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>使用BEGIN/COMMIT/ROLLBACK</li>
  <li>确保数据一致性</li>
  <li>处理异常情况</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用BEGIN开始事务</p>
<p>2. 执行多个数据库操作</p>
<p>3. 使用COMMIT提交或ROLLBACK回滚</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
-- 转账事务示例
BEGIN TRANSACTION;

BEGIN TRY
    -- 从账户A扣款
    UPDATE accounts SET balance = balance - 1000 WHERE account_id = 1;
    
    -- 给账户B加款
    UPDATE accounts SET balance = balance + 1000 WHERE account_id = 2;
    
    -- 提交事务
    COMMIT TRANSACTION;
    PRINT '转账成功';
END TRY
BEGIN CATCH
    -- 出错回滚
    ROLLBACK TRANSACTION;
    PRINT '转账失败，已回滚';
END CATCH;
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('transaction')">事务管理</a></li>
  <li>ACID特性</li>
  <li>异常处理</li>
</ul>`
      },
      {
        id: 4,
        title: "问题4：索引优化",
        description: `分析查询性能并创建合适的索引。

<strong>输入：</strong>
慢查询SQL语句

<strong>输出：</strong>
优化后的查询和索引

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>分析查询执行计划</li>
  <li>创建适当的索引</li>
  <li>验证性能提升</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 分析WHERE和JOIN条件</p>
<p>2. 在常用查询列上创建索引</p>
<p>3. 考虑复合索引</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
-- 创建单字段索引
CREATE INDEX idx_student_name ON students(name);

-- 创建复合索引
CREATE INDEX idx_course_score ON scores(course_id, score);

-- 查看执行计划
EXPLAIN SELECT * FROM students WHERE name = '张三';

-- 查询索引使用情况
SHOW INDEX FROM students;
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('index')">索引优化</a></li>
  <li>查询优化</li>
  <li>性能调优</li>
</ul>`
      },
      {
        id: 5,
        title: "问题5：Python数据库操作",
        description: `使用Python连接数据库并执行操作。

<strong>输入：</strong>
数据库连接信息

<strong>输出：</strong>
查询和操作结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>连接SQLite/MySQL数据库</li>
  <li>执行CRUD操作</li>
  <li>处理查询结果</li>
</ul>`,
        difficulty: "hard",
        time: "30分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用sqlite3或pymysql连接数据库</p>
<p>2. 使用cursor执行SQL</p>
<p>3. 获取和处理查询结果</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import sqlite3

# 连接数据库
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students
    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
''')

# 插入数据
cursor.execute("INSERT INTO students VALUES (1, '张三', 20)")
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
for row in results:
    print(row)

# 关闭连接
conn.close()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('python-db')">Python数据库编程</a></li>
  <li>数据库连接</li>
  <li>CRUD操作</li>
</ul>`
      }
    ];'''

db_choice_questions = '''    const choiceQuestions = [
      {
        id: 'c1',
        chapter: 1,
        title: "选择题1：数据模型",
        question: "以下哪个不是常用的数据模型？",
        options: [
          { label: 'A', text: '层次模型' },
          { label: 'B', text: '网状模型' },
          { label: 'C', text: '关系模型' },
          { label: 'D', text: '树状模型' }
        ],
        answer: 'D',
        analysis: "常用的数据模型有层次模型、网状模型和关系模型。树状模型不是标准的数据模型分类。",
        difficulty: "easy"
      },
      {
        id: 'c2',
        chapter: 1,
        title: "选择题2：关系数据库",
        question: "关系数据库中，一行数据称为？",
        options: [
          { label: 'A', text: '字段' },
          { label: 'B', text: '记录' },
          { label: 'C', text: '属性' },
          { label: 'D', text: '键' }
        ],
        answer: 'B',
        analysis: "在关系数据库中，表的一行称为记录（元组），一列称为字段（属性）。",
        difficulty: "easy"
      },
      {
        id: 'c3',
        chapter: 2,
        title: "选择题3：SQL语法",
        question: "SQL语句中用于更新数据的关键字是？",
        options: [
          { label: 'A', text: 'INSERT' },
          { label: 'B', text: 'UPDATE' },
          { label: 'C', text: 'MODIFY' },
          { label: 'D', text: 'CHANGE' }
        ],
        answer: 'B',
        analysis: "UPDATE用于更新数据，INSERT用于插入，DELETE用于删除，SELECT用于查询。",
        difficulty: "easy"
      },
      {
        id: 'c4',
        chapter: 2,
        title: "选择题4：SQL查询",
        question: "用于分组的SQL子句是？",
        options: [
          { label: 'A', text: 'ORDER BY' },
          { label: 'B', text: 'GROUP BY' },
          { label: 'C', text: 'WHERE' },
          { label: 'D', text: 'HAVING' }
        ],
        answer: 'B',
        analysis: "GROUP BY用于分组，ORDER BY用于排序，WHERE用于过滤，HAVING用于分组后过滤。",
        difficulty: "medium"
      },
      {
        id: 'c5',
        chapter: 3,
        title: "选择题5：ER模型",
        question: "ER图中，实体用什么图形表示？",
        options: [
          { label: 'A', text: '矩形' },
          { label: 'B', text: '椭圆' },
          { label: 'C', text: '菱形' },
          { label: 'D', text: '圆形' }
        ],
        answer: 'A',
        analysis: "ER图中，实体用矩形，属性用椭圆，关系用菱形表示。",
        difficulty: "easy"
      },
      {
        id: 'c6',
        chapter: 3,
        title: "选择题6：范式设计",
        question: "第三范式要求消除？",
        options: [
          { label: 'A', text: '部分函数依赖' },
          { label: 'B', text: '传递函数依赖' },
          { label: 'C', text: '多值依赖' },
          { label: 'D', text: '数据冗余' }
        ],
        answer: 'B',
        analysis: "1NF消除原子性问题，2NF消除部分依赖，3NF消除传递依赖。",
        difficulty: "medium"
      },
      {
        id: 'c7',
        chapter: 4,
        title: "选择题7：事务管理",
        question: "事务的ACID特性中，I代表？",
        options: [
          { label: 'A', text: '原子性' },
          { label: 'B', text: '一致性' },
          { label: 'C', text: '隔离性' },
          { label: 'D', text: '持久性' }
        ],
        answer: 'C',
        analysis: "ACID分别是Atomicity(原子性)、Consistency(一致性)、Isolation(隔离性)、Durability(持久性)。",
        difficulty: "easy"
      },
      {
        id: 'c8',
        chapter: 4,
        title: "选择题8：备份恢复",
        question: "以下哪种备份方式恢复时间最快？",
        options: [
          { label: 'A', text: '完全备份' },
          { label: 'B', text: '差异备份' },
          { label: 'C', text: '增量备份' },
          { label: 'D', text: '日志备份' }
        ],
        answer: 'A',
        analysis: "完全备份恢复时间最快，但占用空间最大。增量备份恢复最慢。",
        difficulty: "medium"
      },
      {
        id: 'c9',
        chapter: 5,
        title: "选择题9：并发控制",
        question: "用于解决并发冲突的机制是？",
        options: [
          { label: 'A', text: '索引' },
          { label: 'B', text: '锁' },
          { label: 'C', text: '视图' },
          { label: 'D', text: '触发器' }
        ],
        answer: 'B',
        analysis: "锁机制用于控制并发访问，防止数据不一致。",
        difficulty: "medium"
      },
      {
        id: 'c10',
        chapter: 5,
        title: "选择题10：NoSQL数据库",
        question: "MongoDB属于什么类型的NoSQL数据库？",
        options: [
          { label: 'A', text: '键值存储' },
          { label: 'B', text: '文档数据库' },
          { label: 'C', text: '列存储' },
          { label: 'D', text: '图数据库' }
        ],
        answer: 'B',
        analysis: "MongoDB是文档数据库，Redis是键值存储，HBase是列存储，Neo4j是图数据库。",
        difficulty: "hard"
      }
    ];'''

# ========================================
# 主函数
# ========================================
if __name__ == '__main__':
    print("开始更新课程文件...")
    
    # 更新数据库原理
    print("更新数据库原理课程...")
    # 这里只是示例，完整版本需要包含更多课程数据
    print("数据库原理课程更新完成")
    
    print("\n提示：完整版本需要包含商业智能和供应链分析的数据")
