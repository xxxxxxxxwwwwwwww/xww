#!/usr/bin/env python3
import re
import os

def replace_chapter_nav(content, course_data):
    """替换左侧章节导航"""
    chapter_nav_start = '            <h2 class="section-title">数据分析技术题库</h2>'
    chapter_nav_end = '            </div>\n          </div>\n\n          <!-- 右侧：题目展示区 -->'
    
    old_chapter_section = content.split(chapter_nav_start)[1].split(chapter_nav_end)[0]
    content = content.replace(old_chapter_section, course_data['chapter_nav'])
    content = content.replace('数据分析技术题库', course_data['title'])
    
    return content

def replace_problems(content, problems_data):
    """替换编程题数组"""
    problems_start = '    const problems = ['
    problems_end = '    ];\n\n    // 选择题数据'
    
    old_problems = content.split(problems_start)[1].split(problems_end)[0]
    content = content.replace(old_problems, problems_data)
    
    return content

def replace_choice_questions(content, choice_data):
    """替换选择题数组"""
    choice_start = '    const choiceQuestions = ['
    choice_end = '    ];\n\n    // 当前状态'
    
    old_choice = content.split(choice_start)[1].split(choice_end)[0]
    content = content.replace(old_choice, choice_data)
    
    return content

def update_title(content, new_title):
    """更新页面标题"""
    return content.replace('<title>数据分析技术 - Xww的课程页面</title>', f'<title>{new_title} - Xww的课程页面</title>')

# ==================== 数据库原理课程数据 ====================
database_data = {
    'title': '数据库原理题库',
    'chapter_nav': '''
            <!-- 章节列表 -->
            <div class="space-y-6">
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
''',

    'problems': '''
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
''',

    'choice_questions': '''
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
'''
}

# ==================== 商业智能课程数据 ====================
bi_data = {
    'title': '商业智能题库',
    'chapter_nav': '''
            <!-- 章节列表 -->
            <div class="space-y-6">
                            <!-- 章节1：BI基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  BI基础
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
                      <div class="font-medium">数据仓库建模</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">ETL实现</div>
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
                      <div class="font-medium">BI定义</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">数据仓库</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节2：OLAP与多维分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  OLAP与多维分析
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
                      <div class="font-medium">OLAP多维分析</div>
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
                      <div class="font-medium">OLAP概念</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">多维操作</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：数据可视化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  数据可视化
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
                      <div class="font-medium">数据可视化</div>
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
                      <div class="font-medium">图表选择</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">可视化原则</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节4：BI应用 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  BI应用
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
                      <div class="font-medium">商业决策支持</div>
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
                      <div class="font-medium">BI工具</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">报表设计</div>
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
                      <div class="font-medium">数据挖掘</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">机器学习应用</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
''',

    'problems': '''
      {
        id: 1,
        title: "问题1：数据仓库建模",
        description: "设计一个销售数据的数据仓库星型模型。",
        description: `设计一个销售数据的数据仓库星型模型。

<strong>输入：</strong>
业务需求描述

<strong>输出：</strong>
星型模型设计

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>设计事实表和维度表</li>
  <li>确定维度和度量</li>
  <li>考虑 Slowly Changing Dimensions</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 确定事实表（销售事实）</p>
<p>2. 设计维度表（时间、产品、客户、门店等）</p>
<p>3. 确定度量（销售额、数量等）</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
-- 时间维度表
CREATE TABLE dim_time (
    time_key INT PRIMARY KEY,
    date DATE,
    year INT,
    quarter INT,
    month INT,
    day INT,
    week_day INT
);

-- 产品维度表
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- 销售事实表
CREATE TABLE fact_sales (
    time_key INT,
    product_key INT,
    customer_key INT,
    store_key INT,
    quantity INT,
    amount DECIMAL(12,2),
    PRIMARY KEY (time_key, product_key, customer_key, store_key),
    FOREIGN KEY (time_key) REFERENCES dim_time(time_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('data-warehouse')">数据仓库</a></li>
  <li>星型模型</li>
  <li>维度建模</li>
</ul>`
      },
      {
        id: 2,
        title: "问题2：ETL实现",
        description: `编写ETL流程将数据从源系统加载到数据仓库。

<strong>输入：</strong>
源系统数据

<strong>输出：</strong>
清洗转换后的数据

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>抽取数据</li>
  <li>清洗和转换</li>
  <li>加载到目标表</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 读取源数据</p>
<p>2. 清洗去重、处理缺失值</p>
<p>3. 转换格式</p>
<p>4. 加载到目标表</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
from datetime import datetime

# 1. Extract - 抽取数据
source_data = pd.read_csv('source_sales.csv')

# 2. Transform - 转换清洗
# 去重
clean_data = source_data.drop_duplicates()

# 处理缺失值
clean_data = clean_data.fillna(0)

# 转换日期格式
clean_data['date'] = pd.to_datetime(clean_data['date'])

# 生成代理键
clean_data['time_key'] = clean_data['date'].dt.strftime('%Y%m%d').astype(int)

# 3. Load - 加载
clean_data.to_sql('fact_sales_staging', con=engine, if_exists='replace')
print(f"ETL完成，加载了{len(clean_data)}条记录")
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('etl')">ETL流程</a></li>
  <li>数据清洗</li>
  <li>数据转换</li>
</ul>`
      },
      {
        id: 3,
        title: "问题3：OLAP多维分析",
        description: "使用OLAP操作进行多维数据分析。",
        description: `使用OLAP操作进行多维数据分析。

<strong>输入：</strong>
多维数据立方体

<strong>输出：</strong>
分析结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>上卷(Roll-up)操作</li>
  <li>下钻(Drill-down)操作</li>
  <li>切片(Slice)和切块(Dice)</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 按维度层次进行聚合（上卷）</p>
<p>2. 从高层级到低层级（下钻）</p>
<p>3. 选择特定维度值（切片）</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

# 假设有销售数据
sales_data = pd.DataFrame({
    'year': [2023, 2023, 2023, 2024, 2024, 2024],
    'quarter': [1, 2, 3, 1, 2, 3],
    'region': ['华东', '华东', '华北', '华东', '华东', '华北'],
    'sales': [100, 150, 120, 130, 160, 140]
})

# 上卷：按年度统计
roll_up = sales_data.groupby('year')['sales'].sum()
print("按年度统计：")
print(roll_up)

# 切片：只看华东地区
slice_data = sales_data[sales_data['region'] == '华东']
print("\\n华东地区销售：")
print(slice_data)

# 切块：2023年+华东地区
dice_data = sales_data[(sales_data['year'] == 2023) & (sales_data['region'] == '华东')]
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('olap')">OLAP分析</a></li>
  <li>多维操作</li>
  <li>数据聚合</li>
</ul>`
      },
      {
        id: 4,
        title: "问题4：数据可视化",
        description: `创建BI仪表板所需的可视化图表。

<strong>输入：</strong>
业务指标数据

<strong>输出：</strong>
可视化图表

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>选择合适的图表类型</li>
  <li>KPI指标展示</li>
  <li>趋势和对比分析</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 确定关键指标</p>
<p>2. 选择合适的图表类型</p>
<p>3. 实现趋势和对比</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 示例数据
data = pd.DataFrame({
    'month': ['1月', '2月', '3月', '4月', '5月', '6月'],
    'revenue': [100, 120, 110, 130, 140, 160],
    'orders': [50, 60, 55, 65, 70, 80]
})

# 创建仪表板布局
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. KPI卡片
axes[0,0].text(0.5, 0.5, f'总营收:\\n{data["revenue"].sum()}', 
               fontsize=20, ha='center')
axes[0,0].axis('off')
axes[0,0].set_title('核心KPI', fontsize=14)

# 2. 营收趋势
axes[0,1].plot(data['month'], data['revenue'], marker='o', linewidth=2)
axes[0,1].set_title('营收趋势')
axes[0,1].grid(True, alpha=0.3)

# 3. 订单量趋势
axes[1,0].bar(data['month'], data['orders'], color='skyblue')
axes[1,0].set_title('订单量')

# 4. 营收vs订单散点图
axes[1,1].scatter(data['orders'], data['revenue'], s=100, alpha=0.6)
axes[1,1].set_title('订单与营收关系')
axes[1,1].set_xlabel('订单量')
axes[1,1].set_ylabel('营收')

plt.tight_layout()
plt.show()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('visualization')">数据可视化</a></li>
  <li>仪表板设计</li>
  <li>KPI展示</li>
</ul>`
      },
      {
        id: 5,
        title: "问题5：商业决策支持",
        description: `构建分析模型支持商业决策。

<strong>输入：</strong>
历史业务数据

<strong>输出：</strong>
决策建议和预测

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>销售预测</li>
  <li>客户分群</li>
  <li>决策建议</li>
</ul>`,
        difficulty: "hard",
        time: "30分钟",
        code: `# 请编写代码`,
        analysis: `
<h4>解题思路</h4>
<p>1. 分析历史数据</p>
<p>2. 构建预测模型</p>
<p>3. 输出决策建议</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# 历史销售数据
data = pd.DataFrame({
    'month': list(range(1, 13)),
    'sales': [100, 110, 105, 120, 130, 125, 140, 150, 145, 160, 170, 165],
    'promotion': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
})

# 训练预测模型
X = data[['month', 'promotion']]
y = data['sales']
model = LinearRegression()
model.fit(X, y)

# 预测下一季度
next_quarter = pd.DataFrame({
    'month': [13, 14, 15],
    'promotion': [0, 1, 0]
})

predictions = model.predict(next_quarter)

print("下一季度销售预测：")
for i, pred in enumerate(predictions, 1):
    print(f"第{12+i}月：{pred:.1f}")

# 决策建议
print("\\n决策建议：")
print("1. 在第14月安排促销活动")
print("2. 预计Q4销售额将增长15%")
print("3. 建议增加库存准备")
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('decision')">决策支持</a></li>
  <li>预测建模</li>
  <li>商业智能应用</li>
</ul>`
      }
''',

    'choice_questions': '''
      {
        id: 'c1',
        chapter: 1,
        title: "选择题1：BI定义",
        question: "商业智能(BI)的核心目标是？",
        options: [
          { label: 'A', text: '存储大量数据' },
          { label: 'B', text: '支持更好的商业决策' },
          { label: 'C', text: '自动化业务流程' },
          { label: 'D', text: '替代人工分析' }
        ],
        answer: 'B',
        analysis: "BI的核心目标是通过数据和分析支持更好的商业决策。",
        difficulty: "easy"
      },
      {
        id: 'c2',
        chapter: 1,
        title: "选择题2：数据仓库",
        question: "数据仓库的特点不包括？",
        options: [
          { label: 'A', text: '面向主题' },
          { label: 'B', text: '集成的' },
          { label: 'C', text: '实时更新' },
          { label: 'D', text: '时变的' }
        ],
        answer: 'C',
        analysis: "数据仓库是面向主题、集成、时变、非易失的，通常不是实时更新。",
        difficulty: "easy"
      },
      {
        id: 'c3',
        chapter: 2,
        title: "选择题3：OLAP概念",
        question: "OLAP相对于OLTP的特点是？",
        options: [
          { label: 'A', text: '处理大量简单查询' },
          { label: 'B', text: '复杂分析查询' },
          { label: 'C', text: '实时事务处理' },
          { label: 'D', text: '高并发写入' }
        ],
        answer: 'B',
        analysis: "OLAP用于复杂分析查询，OLTP用于事务处理。",
        difficulty: "easy"
      },
      {
        id: 'c4',
        chapter: 2,
        title: "选择题4：多维操作",
        question: "从季度数据查看月度数据的操作称为？",
        options: [
          { label: 'A', text: '上卷(Roll-up)' },
          { label: 'B', text: '下钻(Drill-down)' },
          { label: 'C', text: '切片(Slice)' },
          { label: 'D', text: '旋转(Pivot)' }
        ],
        answer: 'B',
        analysis: "下钻是从高层级数据查看更详细的低层级数据。",
        difficulty: "medium"
      },
      {
        id: 'c5',
        chapter: 3,
        title: "选择题5：图表选择",
        question: "展示占比关系最适合用？",
        options: [
          { label: 'A', text: '折线图' },
          { label: 'B', text: '柱状图' },
          { label: 'C', text: '饼图' },
          { label: 'D', text: '散点图' }
        ],
        answer: 'C',
        analysis: "饼图最适合展示占比关系，折线图看趋势，柱状图看对比，散点图看相关性。",
        difficulty: "easy"
      },
      {
        id: 'c6',
        chapter: 3,
        title: "选择题6：可视化原则",
        question: "数据可视化的首要原则是？",
        options: [
          { label: 'A', text: '美观炫丽' },
          { label: 'B', text: '准确传达信息' },
          { label: 'C', text: '使用丰富色彩' },
          { label: 'D', text: '3D效果' }
        ],
        answer: 'B',
        analysis: "可视化最重要的是准确有效地传达信息，美观是次要的。",
        difficulty: "medium"
      },
      {
        id: 'c7',
        chapter: 4,
        title: "选择题7：BI工具",
        question: "以下哪个不是主流BI工具？",
        options: [
          { label: 'A', text: 'Tableau' },
          { label: 'B', text: 'Power BI' },
          { label: 'C', text: 'Photoshop' },
          { label: 'D', text: 'FineReport' }
        ],
        answer: 'C',
        analysis: "Photoshop是图像编辑软件，不是BI工具。",
        difficulty: "easy"
      },
      {
        id: 'c8',
        chapter: 4,
        title: "选择题8：报表设计",
        question: "报表设计的最佳实践不包括？",
        options: [
          { label: 'A', text: '每页展示尽可能多的信息' },
          { label: 'B', text: '合理的信息层次' },
          { label: 'C', text: '突出重要数据' },
          { label: 'D', text: '清晰的标题和说明' }
        ],
        answer: 'A',
        analysis: "报表应该简洁明了，不要在一页堆积过多信息。",
        difficulty: "medium"
      },
      {
        id: 'c9',
        chapter: 5,
        title: "选择题9：数据挖掘",
        question: "从数据中发现规律和模式的过程称为？",
        options: [
          { label: 'A', text: '数据查询' },
          { label: 'B', text: '数据挖掘' },
          { label: 'C', text: '数据录入' },
          { label: 'D', text: '数据备份' }
        ],
        answer: 'B',
        analysis: "数据挖掘是从数据中发现规律和模式的过程。",
        difficulty: "medium"
      },
      {
        id: 'c10',
        chapter: 5,
        title: "选择题10：机器学习应用",
        question: "在BI中使用机器学习进行销售预测属于？",
        options: [
          { label: 'A', text: '描述性分析' },
          { label: 'B', text: '诊断性分析' },
          { label: 'C', text: '预测性分析' },
          { label: 'D', text: '规范性分析' }
        ],
        answer: 'C',
        analysis: "预测未来属于预测性分析。",
        difficulty: "hard"
      }
'''
}

# ==================== 供应链分析课程数据 ====================
supply_chain_data = {
    'title': '供应链分析题库',
    'chapter_nav': '''
            <!-- 章节列表 -->
            <div class="space-y-6">
                            <!-- 章节1：供应链基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-