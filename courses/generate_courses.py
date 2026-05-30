#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成三个课程文件的脚本
"""

import re

# 读取参考文件
with open('/workspace/courses/data-analysis-tech.html', 'r', encoding='utf-8') as f:
    template = f.read()

# ==================== 数据库原理与应用 ====================
db_content = template

# 更新标题
db_content = db_content.replace(
    '<title>数据分析技术 - Xww的课程页面</title>',
    '<title>数据库原理与应用 - Xww的课程页面</title>'
)

# 更新考试链接
db_content = db_content.replace(
    'href="data-analysis-exam.html"',
    'href="database-principles-exam.html"'
)

# 更新题库标题
db_content = db_content.replace(
    '<h2 class="section-title">数据分析技术题库</h2>',
    '<h2 class="section-title">数据库原理与应用题库</h2>'
)

# 更新章节导航
db_chapters = '''
              <!-- 章节1：数据库基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter1\')">
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
                      <div class="font-medium">创建数据库表</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">基本SELECT查询</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c1\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">数据库定义</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c2\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL全称</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节2：SQL查询基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter2\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  SQL查询基础
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
                      <div class="font-medium">WHERE条件过滤</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c3\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">WHERE子句</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c4\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">ORDER BY排序</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：高级SQL查询 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter3\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  高级SQL查询
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
                      <div class="font-medium">JOIN多表查询</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c5\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">JOIN类型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c6\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">聚合函数</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节4：数据修改与事务 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter4\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  数据修改与事务
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">INSERT插入数据</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(6)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">6</div>
                    <div class="flex-1">
                      <div class="font-medium">UPDATE更新数据</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(7)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">7</div>
                    <div class="flex-1">
                      <div class="font-medium">DELETE删除数据</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c7\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">事务ACID</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c8\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">UPDATE语句</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节5：索引与性能优化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter5\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  索引与性能优化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(8)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">8</div>
                    <div class="flex-1">
                      <div class="font-medium">创建与使用索引</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c9\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">I</div>
                    <div class="flex-1">
                      <div class="font-medium">索引类型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c10\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">查询优化</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节6：数据库设计 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter6\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"></i>
                  数据库设计
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter6-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c11\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">K</div>
                    <div class="flex-1">
                      <div class="font-medium">范式设计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c12\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">L</div>
                    <div class="flex-1">
                      <div class="font-medium">ER图设计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节7：数据库管理 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter7\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter7-icon"></i>
                  数据库管理
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter7-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c13\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">M</div>
                    <div class="flex-1">
                      <div class="font-medium">用户权限</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c14\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">N</div>
                    <div class="flex-1">
                      <div class="font-medium">备份恢复</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节8：课程总结 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter8\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter8-icon"></i>
                  课程总结
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/1</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter8-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c15\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">O</div>
                    <div class="flex-1">
                      <div class="font-medium">DBA技能</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
'''

# 替换章节导航部分 - 使用正则表达式找到并替换
pattern = r'<!-- 章节1：数据分析基础 -->.*?<!-- 章节8：课程总结 -->.*?</div>\s*</div>\s*</div>'
db_content = re.sub(pattern, db_chapters, db_content, flags=re.DOTALL)

# 更新 problems 数组
db_problems = '''    const problems = [
      {
        id: 1,
        title: '问题1：创建数据库表',
        description: `
          <p>使用Python和SQLite创建一个学生表，包含字段：学号、姓名、年龄、专业。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>创建名为 students 的表</li>
            <li>学号设为主键</li>
            <li>插入3条测试数据</li>
          </ul>
        `,
        difficulty: 'easy',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 sqlite3 连接数据库</p>
          <p>2. 使用 CREATE TABLE 语句创建表</p>
          <p>3. 使用 INSERT INTO 插入测试数据</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

# 连接数据库
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (student_id TEXT PRIMARY KEY, name TEXT, age INTEGER, major TEXT)''')

# 插入数据
students = [
    ('2024001', '张三', 20, '计算机科学'),
    ('2024002', '李四', 21, '软件工程'),
    ('2024003', '王五', 19, '数据科学')
]

cursor.executemany('INSERT OR REPLACE INTO students VALUES (?,?,?,?)', students)
conn.commit()

# 查询验证
cursor.execute('SELECT * FROM students')
print('学生表数据：')
for row in cursor.fetchall():
    print(row)

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter1-basics')">第一章：数据库基础</a></li>
            <li>CREATE TABLE 语句</li>
            <li>INSERT 语句</li>
          </ul>
        `
      },
      {
        id: 2,
        title: '问题2：基本SELECT查询',
        description: `
          <p>编写SQL查询从 students 表中获取所有计算机专业学生的信息。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>查询所有字段</li>
            <li>筛选专业为"计算机科学"的学生</li>
            <li>按年龄升序排序</li>
          </ul>
        `,
        difficulty: 'easy',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 SELECT * 查询所有字段</p>
          <p>2. 使用 WHERE 子句过滤专业</p>
          <p>3. 使用 ORDER BY 排序</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 执行查询
cursor.execute('''SELECT * FROM students 
                  WHERE major = '计算机科学' 
                  ORDER BY age ASC''')

print('计算机专业学生：')
for row in cursor.fetchall():
    print(f'学号: {row[0]}, 姓名: {row[1]}, 年龄: {row[2]}, 专业: {row[3]}')

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2-preprocessing')">第二章：SQL查询基础</a></li>
            <li>SELECT 查询</li>
            <li>WHERE 子句</li>
            <li>ORDER BY 排序</li>
          </ul>
        `
      },
      {
        id: 3,
        title: '问题3：WHERE条件过滤',
        description: `
          <p>查询年龄在20岁以上且专业不是"软件工程"的学生。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>使用比较运算符和逻辑运算符</li>
            <li>组合多个条件</li>
            <li>只显示姓名和专业</li>
          </ul>
        `,
        difficulty: 'medium',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 &gt; 比较运算符</p>
          <p>2. 使用 AND 逻辑运算符</p>
          <p>3. 使用 != 或 &lt;&gt; 表示不等于</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''SELECT name, major FROM students 
                  WHERE age &gt; 20 AND major != '软件工程' ''')

print('查询结果：')
for row in cursor.fetchall():
    print(f'姓名: {row[0]}, 专业: {row[1]}')

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2-preprocessing')">第二章：SQL查询基础</a></li>
            <li>WHERE 条件</li>
            <li>逻辑运算符</li>
          </ul>
        `
      },
      {
        id: 4,
        title: '问题4：JOIN多表查询',
        description: `
          <p>创建课程表和选课表，然后查询每个学生选了哪些课程。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>创建 courses 表和 enrollments 表</li>
            <li>插入测试数据</li>
            <li>使用 JOIN 连接查询</li>
          </ul>
        `,
        difficulty: 'medium',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 创建课程表和选课表</p>
          <p>2. 使用 INNER JOIN 连接三个表</p>
          <p>3. 通过外键关联</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建课程表
cursor.execute('''CREATE TABLE IF NOT EXISTS courses
                  (course_id TEXT PRIMARY KEY, course_name TEXT, credit INTEGER)''')

# 创建选课表
cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments
                  (student_id TEXT, course_id TEXT,
                   PRIMARY KEY (student_id, course_id))''')

# 插入测试数据
courses = [('CS101', 'Python编程', 4), ('CS102', '数据库原理', 3), ('CS103', '数据结构', 4)]
enrollments = [('2024001', 'CS101'), ('2024001', 'CS102'), ('2024002', 'CS101'), ('2024003', 'CS103')]

cursor.executemany('INSERT OR REPLACE INTO courses VALUES (?,?,?)', courses)
cursor.executemany('INSERT OR REPLACE INTO enrollments VALUES (?,?)', enrollments)
conn.commit()

# JOIN查询
cursor.execute('''SELECT s.name, c.course_name
                  FROM students s
                  JOIN enrollments e ON s.student_id = e.student_id
                  JOIN courses c ON e.course_id = c.course_id''')

print('学生选课情况：')
for row in cursor.fetchall():
    print(f'{row[0]} 选了 {row[1]}')

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter3-tools')">第三章：高级SQL查询</a></li>
            <li>JOIN 连接</li>
            <li>外键关系</li>
          </ul>
        `
      },
      {
        id: 5,
        title: '问题5：INSERT插入数据',
        description: `
          <p>向 students 表中插入两条新的学生记录。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>使用单条 INSERT 语句</li>
            <li>使用 executemany 批量插入</li>
            <li>查询验证插入结果</li>
          </ul>
        `,
        difficulty: 'easy',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 INSERT INTO 语句</p>
          <p>2. executemany 可以高效批量插入</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 批量插入
new_students = [
    ('2024004', '赵六', 22, '人工智能'),
    ('2024005', '钱七', 20, '网络安全')
]

cursor.executemany('INSERT OR REPLACE INTO students VALUES (?,?,?,?)', new_students)
conn.commit()

# 验证
cursor.execute('SELECT COUNT(*) FROM students')
print(f'学生总数: {cursor.fetchone()[0]}')

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter4-statistics')">第四章：数据修改与事务</a></li>
            <li>INSERT 语句</li>
            <li>批量插入</li>
          </ul>
        `
      },
      {
        id: 6,
        title: '问题6：UPDATE更新数据',
        description: `
          <p>将"张三"的专业更新为"人工智能"。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>使用 WHERE 子句定位记录</li>
            <li>使用 SET 子句更新字段</li>
            <li>查询验证更新结果</li>
          </ul>
        `,
        difficulty: 'medium',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 UPDATE 语句</p>
          <p>2. 注意一定要加 WHERE 条件</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 更新数据
cursor.execute('''UPDATE students 
                  SET major = '人工智能' 
                  WHERE name = '张三' ''')
conn.commit()

# 验证
cursor.execute("SELECT * FROM students WHERE name = '张三'")
print('更新后的张三：', cursor.fetchone())

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter4-statistics')">第四章：数据修改与事务</a></li>
            <li>UPDATE 语句</li>
            <li>事务提交</li>
          </ul>
        `
      },
      {
        id: 7,
        title: '问题7：DELETE删除数据',
        description: `
          <p>删除"钱七"的学生记录。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>使用 DELETE 语句</li>
            <li>使用 WHERE 子句指定要删除的记录</li>
            <li>查询验证删除结果</li>
          </ul>
        `,
        difficulty: 'medium',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 DELETE FROM 语句</p>
          <p>2. 注意一定要加 WHERE 条件，否则会删除所有数据</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 删除前先查看
cursor.execute("SELECT * FROM students WHERE name = '钱七'")
print('删除前：', cursor.fetchone())

# 删除数据
cursor.execute("DELETE FROM students WHERE name = '钱七'")
conn.commit()

# 验证
cursor.execute("SELECT * FROM students WHERE name = '钱七'")
print('删除后：', cursor.fetchone() or '已删除')

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter4-statistics')">第四章：数据修改与事务</a></li>
            <li>DELETE 语句</li>
            <li>数据安全</li>
          </ul>
        `
      },
      {
        id: 8,
        title: '问题8：创建与使用索引',
        description: `
          <p>在 students 表的 name 字段上创建索引，并比较查询性能。</p>
          <p><strong>要求</strong>：</p>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li>创建普通索引</li>
            <li>使用 EXPLAIN QUERY PLAN 查看执行计划</li>
            <li>比较索引前后的查询速度</li>
          </ul>
        `,
        difficulty: 'hard',
        code: '# 请编写代码',
        analysis: `
          <h4>解题思路</h4>
          <p>1. 使用 CREATE INDEX 创建索引</p>
          <p>2. 使用 EXPLAIN 分析查询计划</p>
          <p>3. 索引可以大幅提升查询速度</p>
          <h4>代码示例</h4>
          <div class="bg-dark p-3 rounded-lg font-mono text-sm">
            <pre class="text-cyan-300">
import sqlite3
import time

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建索引
cursor.execute('CREATE INDEX IF NOT EXISTS idx_students_name ON students(name)')
conn.commit()

# 查看执行计划
print('查询执行计划：')
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM students WHERE name = '张三'")
for row in cursor.fetchall():
    print(row)

print('\\n索引已创建在 name 字段上')

conn.close()
            </pre>
          </div>
          <h4>知识点</h4>
          <ul class="list-disc list-inside space-y-1 mt-2">
            <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter5-advanced')">第五章：索引与性能优化</a></li>
            <li>索引创建</li>
            <li>查询优化</li>
          </ul>
        `
      }
    ];'''

# 替换 problems 数组
db_content = re.sub(r'const problems = \[.*?\];', db_problems, db_content, flags=re.DOTALL)

# 更新 choiceQuestions 数组
db_choice_questions = '''    const choiceQuestions = [
      {
        id: 'c1',
        title: '选择题A：数据库定义',
        question: 'DBMS 的全称是什么？',
        options: [
          { label: 'A', text: 'Data Base Management System' },
          { label: 'B', text: 'Data Base Managing System' },
          { label: 'C', text: 'Database Management System' },
          { label: 'D', text: 'Database Manager System' }
        ],
        answer: 'C',
        analysis: "DBMS 是 Database Management System 的缩写，即数据库管理系统。",
        difficulty: "easy",
        chapter: 1
      },
      {
        id: 'c2',
        title: '选择题B：SQL全称',
        question: 'SQL 的全称是什么？',
        options: [
          { label: 'A', text: 'Structured Query Language' },
          { label: 'B', text: 'Simple Query Language' },
          { label: 'C', text: 'Standard Query Language' },
          { label: 'D', text: 'System Query Language' }
        ],
        answer: 'A',
        analysis: "SQL 是 Structured Query Language 的缩写，即结构化查询语言。",
        difficulty: "easy",
        chapter: 1
      },
      {
        id: 'c3',
        title: '选择题C：WHERE子句',
        question: 'WHERE 子句的作用是什么？',
        options: [
          { label: 'A', text: '指定要查询的表' },
          { label: 'B', text: '过滤查询结果' },
          { label: 'C', text: '对结果排序' },
          { label: 'D', text: '分组统计数据' }
        ],
        answer: 'B',
        analysis: "WHERE 子句用于指定过滤条件，只返回满足条件的记录。",
        difficulty: "easy",
        chapter: 2
      },
      {
        id: 'c4',
        title: '选择题D：ORDER BY排序',
        question: 'ORDER BY 默认的排序方式是？',
        options: [
          { label: 'A', text: '降序 DESC' },
          { label: 'B', text: '升序 ASC' },
          { label: 'C', text: '随机排序' },
          { label: 'D', text: '按插入顺序' }
        ],
        answer: 'B',
        analysis: "ORDER BY 默认按升序（ASC）排序，如果需要降序需要显式指定 DESC。",
        difficulty: "medium",
        chapter: 2
      },
      {
        id: 'c5',
        title: '选择题E：JOIN类型',
        question: '只返回两个表中匹配记录的 JOIN 类型是？',
        options: [
          { label: 'A', text: 'LEFT JOIN' },
          { label: 'B', text: 'RIGHT JOIN' },
          { label: 'C', text: 'INNER JOIN' },
          { label: 'D', text: 'FULL JOIN' }
        ],
        answer: 'C',
        analysis: "INNER JOIN 只返回两个表中在连接条件上匹配的记录。",
        difficulty: "easy",
        chapter: 3
      },
      {
        id: 'c6',
        title: '选择题F：聚合函数',
        question: '以下哪个不是 SQL 聚合函数？',
        options: [
          { label: 'A', text: 'COUNT()' },
          { label: 'B', text: 'SUM()' },
          { label: 'C', text: 'AVG()' },
          { label: 'D', text: 'UPPER()' }
        ],
        answer: 'D',
        analysis: "UPPER() 是字符串函数，用于转换为大写。COUNT、SUM、AVG 是聚合函数。",
        difficulty: "easy",
        chapter: 3
      },
      {
        id: 'c7',
        title: '选择题G：事务ACID',
        question: '事务的 ACID 特性中，I 代表什么？',
        options: [
          { label: 'A', text: 'Isolation（隔离性）' },
          { label: 'B', text: 'Integrity（完整性）' },
          { label: 'C', text: 'Index（索引）' },
          { label: 'D', text: 'Injection（注入）' }
        ],
        answer: 'A',
        analysis: "ACID 代表：Atomicity（原子性）、Consistency（一致性）、Isolation（隔离性）、Durability（持久性）。",
        difficulty: "easy",
        chapter: 4
      },
      {
        id: 'c8',
        title: '选择题H：UPDATE语句',
        question: 'UPDATE 语句中用于指定新值的关键字是？',
        options: [
          { label: 'A', text: 'CHANGE' },
          { label: 'B', text: 'MODIFY' },
          { label: 'C', text: 'SET' },
          { label: 'D', text: 'ALTER' }
        ],
        answer: 'C',
        analysis: "UPDATE 语句使用 SET 关键字来指定字段的新值。",
        difficulty: "medium",
        chapter: 4
      },
      {
        id: 'c9',
        title: '选择题I：索引类型',
        question: '以下关于索引的说法正确的是？',
        options: [
          { label: 'A', text: '索引越多越好' },
          { label: 'B', text: '索引会减慢写入速度' },
          { label: 'C', text: '索引不占用存储空间' },
          { label: 'D', text: '主键不是索引' }
        ],
        answer: 'B',
        analysis: "索引会加快查询速度，但会减慢写入（INSERT/UPDATE/DELETE）速度，因为需要同时更新索引。",
        difficulty: "easy",
        chapter: 5
      },
      {
        id: 'c10',
        title: '选择题J：查询优化',
        question: '以下哪个做法不利于查询优化？',
        options: [
          { label: 'A', text: '在 WHERE 条件字段上建索引' },
          { label: 'B', text: '使用 SELECT * 查询所有字段' },
          { label: 'C', text: '避免使用 LIKE %...' },
          { label: 'D', text: '合理使用 LIMIT' }
        ],
        answer: 'B',
        analysis: "使用 SELECT * 会查询不需要的字段，浪费带宽和内存，应该只查询需要的字段。",
        difficulty: "easy",
        chapter: 5
      },
      {
        id: 'c11',
        title: '选择题K：范式设计',
        question: '第一范式（1NF）要求？',
        options: [
          { label: 'A', text: '消除部分依赖' },
          { label: 'B', text: '消除传递依赖' },
          { label: 'C', text: '字段具有原子性' },
          { label: 'D', text: '每个表只有一个主键' }
        ],
        answer: 'C',
        analysis: "第一范式要求每个字段都是不可再分的最小数据单元，即具有原子性。",
        difficulty: "easy",
        chapter: 6
      },
      {
        id: 'c12',
        title: '选择题L：ER图设计',
        question: 'ER 图中菱形表示什么？',
        options: [
          { label: 'A', text: '实体' },
          { label: 'B', text: '属性' },
          { label: 'C', text: '关系' },
          { label: 'D', text: '主键' }
        ],
        answer: 'C',
        analysis: "ER 图中：矩形表示实体，椭圆表示属性，菱形表示关系。",
        difficulty: "medium",
        chapter: 6
      },
      {
        id: 'c13',
        title: '选择题M：用户权限',
        question: 'SQL 中用于授予用户权限的语句是？',
        options: [
          { label: 'A', text: 'ALLOW' },
          { label: 'B', text: 'GRANT' },
          { label: 'C', text: 'PERMIT' },
          { label: 'D', text: 'AUTHORIZE' }
        ],
        answer: 'B',
        analysis: "使用 GRANT 语句授予用户权限，使用 REVOKE 收回权限。",
        difficulty: "easy",
        chapter: 7
      },
      {
        id: 'c14',
        title: '选择题N：备份恢复',
        question: '数据库备份的主要目的是？',
        options: [
          { label: 'A', text: '提高查询速度' },
          { label: 'B', text: '防止数据丢失' },
          { label: 'C', text: '节省存储空间' },
          { label: 'D', text: '优化数据库结构' }
        ],
        answer: 'B',
        analysis: "数据库备份的主要目的是在数据丢失或损坏时能够恢复数据。",
        difficulty: "easy",
        chapter: 7
      },
      {
        id: 'c15',
        title: '选择题O：DBA技能',
        question: '以下哪个不是数据库管理员（DBA）的主要职责？',
        options: [
          { label: 'A', text: '数据库备份与恢复' },
          { label: 'B', text: '性能监控与优化' },
          { label: 'C', text: '编写前端页面' },
          { label: 'D', text: '用户权限管理' }
        ],
        answer: 'C',
        analysis: "编写前端页面是前端开发人员的职责，不是 DBA 的主要工作。",
        difficulty: "medium",
        chapter: 8
      }
    ];'''

# 替换 choiceQuestions 数组
db_content = re.sub(r'const choiceQuestions = \[.*?\];', db_choice_questions, db_content, flags=re.DOTALL)

# 更新知识点导航
db_knowledge_nav = '''          <div class="flex flex-wrap gap-3 mb-8 bg-dark-gray p-4 rounded-xl border border-gray-700">
            <button class="knowledge-nav active px-4 py-2 rounded-lg font-semibold transition" data-target="chapter1-basics">第一章：数据库基础</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter2-preprocessing">第二章：SQL查询基础</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter3-tools">第三章：高级SQL查询</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter4-statistics">第四章：数据修改与事务</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter5-advanced">第五章：索引与性能优化</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter6-visualization">第六章：数据库设计</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter7-cases">第七章：数据库管理</button>
            <button class="knowledge-nav px-4 py-2 rounded-lg hover:bg-gray-500 transition" data-target="chapter8-summary">第八章：课程总结</button>
          </div>'''

db_content = re.sub(r'<!-- 导航栏 -->.*?</div>', db_knowledge_nav, db_content, flags=re.DOTALL)

# 更新 getChapterName 函数
db_chapter_names = '''    function getChapterName(chapter) {
      const names = {
        1: '第一章：数据库基础',
        2: '第二章：SQL查询基础',
        3: '第三章：高级SQL查询',
        4: '第四章：数据修改与事务',
        5: '第五章：索引与性能优化',
        6: '第六章：数据库设计',
        7: '第七章：数据库管理',
        8: '第八章：课程总结'
      };
      return names[chapter] || '数据库原理';
    }'''

db_content = re.sub(r'function getChapterName\(chapter\) \{.*?\}', db_chapter_names, db_content, flags=re.DOTALL)

# 更新第一个问题的描述（默认显示的）
db_first_problem = '''      <div class="problem-description" id="problem-description">
        <p>使用Python和SQLite创建一个学生表，包含字段：学号、姓名、年龄、专业。</p>
        <p><strong>要求</strong>：</p>
        <ul class="list-disc list-inside space-y-1 mt-2">
          <li>创建名为 students 的表</li>
          <li>学号设为主键</li>
          <li>插入3条测试数据</li>
        </ul>
      </div>'''

db_content = re.sub(r'<div class="problem-description" id="problem-description">.*?</div>', db_first_problem, db_content, flags=re.DOTALL)

# 更新第一个问题的标题
db_content = db_content.replace(
    '<h3 class="text-xl font-bold text-gray-200" id="problem-title">问题1：缺失值处理</h3>',
    '<h3 class="text-xl font-bold text-gray-200" id="problem-title">问题1：创建数据库表</h3>'
)

# 更新第一个问题的难度标签
db_content = db_content.replace(
    '<span class="difficulty-tag difficulty-easy" id="difficulty-tag">简单</span>',
    '<span class="difficulty-tag difficulty-easy" id="difficulty-tag">简单</span>'
)

# 写入文件
with open('/workspace/courses/database-principles.html', 'w', encoding='utf-8') as f:
    f.write(db_content)

print("✓ database-principles.html 生成完成")


# ==================== 商务智能分析 ====================
bi_content = template

# 更新标题
bi_content = bi_content.replace(
    '<title>数据分析技术 - Xww的课程页面</title>',
    '<title>商务智能分析 - Xww的课程页面</title>'
)

# 更新考试链接
bi_content = bi_content.replace(
    'href="data-analysis-exam.html"',
    'href="business-intelligence-exam.html"'
)

# 更新题库标题
bi_content = bi_content.replace(
    '<h2 class="section-title">数据分析技术题库</h2>',
    '<h2 class="section-title">商务智能分析题库</h2>'
)

# 生成商务智能的章节导航
bi_chapters = '''
              <!-- 章节1：商务智能基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter1\')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  商务智能基础
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
                      <div class="font-medium">销售数据统计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">数据透视分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c1\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">BI定义</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c2\')">
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
              
              <!-- 章节2：数据ETL处理 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter2\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  数据ETL处理
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
                      <div class="font-medium">数据清洗转换</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c3\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">ETL含义</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c4\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">数据质量</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：多维数据分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter3\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  多维数据分析
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
                      <div class="font-medium">OLAP多维分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c5\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">OLAP操作</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion(\'c6\')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">维度建模</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节4：数据可视化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter(\'chapter4\')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  数据可视化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">销售趋势图表</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(6)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">6</div>
                    <div class="flex-1">
                      <div class="font-medium">产品占比饼图</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(7)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items