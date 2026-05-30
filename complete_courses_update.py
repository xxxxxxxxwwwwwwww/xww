#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一次性完成剩余两个课程的题库更新
基于 supply-chain-analysis.html 的成功模板
"""

import os

def read_file(filepath):
    """读取文件内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """写入文件内容"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def create_database_course(template_content):
    """创建数据库原理课程"""
    content = template_content
    
    # 更新标题
    content = content.replace('供应链分析 - Xww的课程页面', '数据库原理与应用 - Xww的课程页面')
    content = content.replace('供应链分析题库', '数据库原理与应用题库')
    content = content.replace('data-collection-exam.html', 'database-principles-exam.html')
    
    # 更新章节导航
    chapter_updates = [
        ('供应链概述', '数据库基础'),
        ('需求预测', 'SQL语言'),
        ('库存管理', '数据库设计'),
        ('物流优化', '数据库管理'),
        ('供应链数据分析', '高级话题'),
        ('供应链风险与优化', '数据库安全')
    ]
    
    for old, new in chapter_updates:
        content = content.replace(old, new)
    
    # 更新模块标题
    module_updates = [
        ('模块1：供应链概述', '模块1：数据库基础'),
        ('模块2：需求预测', '模块2：SQL语言'),
        ('模块3：库存管理', '模块3：数据库设计'),
        ('模块4：物流优化', '模块4：数据库管理'),
        ('模块5：供应链数据分析', '模块5：高级话题'),
        ('模块6：供应链风险与优化', '模块6：数据库安全')
    ]
    
    for old, new in module_updates:
        content = content.replace(old, new)
    
    # 更新选择题和编程题内容 - 这里我们会简化处理，确保结构正确
    # 首先更新 problems 数组
    db_problems = """    // 问题数据
    const problems = [
      {
        id: 1,
        title: "问题1：数据库表设计",
        description: `设计一个学生选课系统的数据库表结构。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>创建学生表students（包含学号、姓名、性别、班级等字段）</li>
  <li>创建课程表courses（包含课程号、课程名、学分等字段）</li>
  <li>创建选课表enrollments（关联学生和课程，包含成绩字段）</li>
  <li>使用Python的sqlite3库实现</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import sqlite3

# 创建数据库连接
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建学生表


# 创建课程表


# 创建选课表


# 提交并关闭
conn.commit()
conn.close()`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用sqlite3创建数据库连接</p>
<p>2. 设计合理的表结构和字段类型</p>
<p>3. 设置适当的主键约束</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT,
        class_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        credit REAL
    )
''')

cursor.execute('''
    CREATE TABLE enrollments (
        student_id INTEGER,
        course_id INTEGER,
        score REAL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
''')

conn.commit()
conn.close()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>关系数据库设计</li>
  <li>主键与外键</li>
  <li>SQLite使用</li>
</ul>`,
        chapter: 1
      },
      {
        id: 2,
        title: "问题2：SQL查询练习",
        description: `编写SQL查询语句从学生选课数据库中查询数据。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>查询所有学生信息</li>
  <li>查询某个学生的选课情况</li>
  <li>查询某门课程的平均成绩</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写代码
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 查询所有学生


# 查询学号为1的学生选课情况


# 查询课程号为1的平均成绩


conn.close()`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用SELECT语句查询数据</p>
<p>2. 使用JOIN连接多个表</p>
<p>3. 使用聚合函数计算统计数据</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 查询所有学生
cursor.execute('SELECT * FROM students')
print('所有学生:')
for row in cursor.fetchall():
    print(row)

# 查询学号为1的学生选课情况
cursor.execute('''
    SELECT s.name, c.course_name, e.score
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    WHERE s.student_id = 1
''')
print('\\n学生选课情况:')
for row in cursor.fetchall():
    print(row)

# 查询课程号为1的平均成绩
cursor.execute('SELECT AVG(score) FROM enrollments WHERE course_id = 1')
avg_score = cursor.fetchone()[0]
print(f'\\n课程平均成绩: {avg_score}')

conn.close()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>SELECT查询</li>
  <li>JOIN连接</li>
  <li>聚合函数</li>
</ul>`,
        chapter: 1
      },
      {
        id: 3,
        title: "问题3：索引优化",
        description: `为数据库表创建合适的索引以提高查询性能。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>分析常用查询场景</li>
  <li>创建适当的索引</li>
  <li>对比索引创建前后的查询性能</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import sqlite3
import time

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建索引前查询
start = time.time()
cursor.execute('SELECT * FROM students WHERE name = ?', ('张三',))
time_before = time.time() - start

# 创建索引


# 创建索引后查询
start = time.time()
cursor.execute('SELECT * FROM students WHERE name = ?', ('张三',))
time_after = time.time() - start

print(f'索引前: {time_before:.6f}秒')
print(f'索引后: {time_after:.6f}秒')

conn.close()`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用CREATE INDEX创建索引</p>
<p>2. 在经常查询的字段上创建索引</p>
<p>3. 注意索引会增加写入时间</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import sqlite3
import time

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 创建索引
cursor.execute('CREATE INDEX IF NOT EXISTS idx_student_name ON students(name)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_enrollment_course ON enrollments(course_id)')

conn.commit()
print('索引创建完成')

conn.close()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>索引原理</li>
  <li>CREATE INDEX</li>
  <li>性能优化</li>
</ul>`,
        chapter: 3
      },
      {
        id: 4,
        title: "问题4：事务处理",
        description: `实现数据库事务操作，确保数据一致性。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>实现转账操作（从一个账户扣款，给另一个账户加款）</li>
  <li>使用事务确保操作的原子性</li>
  <li>处理异常情况并回滚</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import sqlite3

def transfer_funds(from_id, to_id, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    try:
        # 创建账户表（如果不存在）
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                balance REAL NOT NULL
            )
        ''')
        
        # 扣款
        
        
        # 加款
        
        
        conn.commit()
        print('转账成功')
    except Exception as e:
        conn.rollback()
        print(f'转账失败: {e}')
    finally:
        conn.close()

# 测试
transfer_funds(1, 2, 100)`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用conn.commit()提交事务</p>
<p>2. 使用conn.rollback()回滚事务</p>
<p>3. 异常处理确保数据一致性</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import sqlite3

def transfer_funds(from_id, to_id, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                balance REAL NOT NULL
            )
        ''')
        
        # 扣款
        cursor.execute('UPDATE accounts SET balance = balance - ? WHERE account_id = ?', 
                      (amount, from_id))
        
        # 检查余额
        cursor.execute('SELECT balance FROM accounts WHERE account_id = ?', (from_id,))
        balance = cursor.fetchone()[0]
        if balance < 0:
            raise ValueError('余额不足')
        
        # 加款
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_id = ?',
                      (amount, to_id))
        
        conn.commit()
        print('转账成功')
    except Exception as e:
        conn.rollback()
        print(f'转账失败: {e}')
    finally:
        conn.close()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>事务ACID特性</li>
  <li>commit/rollback</li>
  <li>异常处理</li>
</ul>`,
        chapter: 2
      },
      {
        id: 5,
        title: "问题5：Python数据库操作",
        description: `使用Python实现完整的CRUD（增删改查）操作。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>实现Create（创建）操作</li>
  <li>实现Read（读取）操作</li>
  <li>实现Update（更新）操作</li>
  <li>实现Delete（删除）操作</li>
</ul>`,
        difficulty: "hard",
        time: "30分钟",
        code: `# 请编写代码
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        pass  # 请实现
    
    def create(self, name, age):
        pass  # 请实现
    
    def read(self, id=None):
        pass  # 请实现
    
    def update(self, id, name, age):
        pass  # 请实现
    
    def delete(self, id):
        pass  # 请实现
    
    def close(self):
        self.conn.close()

# 使用示例
db = DatabaseManager('test.db')
# 测试代码
db.close()`,
        analysis: `
<h4>解题思路</h4>
<p>1. 封装数据库操作为类</p>
<p>2. 实现完整的CRUD操作</p>
<p>3. 使用参数化查询防止SQL注入</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        self.conn.commit()
    
    def create(self, name, age):
        self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def read(self, id=None):
        if id:
            self.cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
            return self.cursor.fetchone()
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
    
    def update(self, id, name, age):
        self.cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, id))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete(self, id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def close(self):
        self.conn.close()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>CRUD操作</li>
  <li>参数化查询</li>
  <li>数据库封装</li>
</ul>`,
        chapter: 4
      }
    ];"""

    # 替换 problems 数组
    # 找到原来的 problems 开始和结束位置
    problems_start = content.find('    // 问题数据\n    const problems = [')
    if problems_start == -1:
        problems_start = content.find('    // 问题数据\r\n    const problems = [')
    
    if problems_start != -1:
        # 找到 problems 数组结束位置（下一个 const 或 // 选择题数据）
        problems_end = content.find('    // 选择题数据', problems_start)
        if problems_end == -1:
            problems_end = content.find('    const choiceQuestions', problems_start)
        
        if problems_end != -1:
            content = content[:problems_start] + db_problems + content[problems_end:]
    
    # 更新选择题
    db_choice_questions = """    // 选择题数据
    const choiceQuestions = [
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
        analysis: "常用的数据模型有层次模型、网状模型、关系模型和面向对象模型。树状模型不是标准的数据模型分类。",
        difficulty: "easy"
      },
      {
        id: 'c2',
        chapter: 1,
        title: "选择题2：关系数据库",
        question: "关系数据库中，一行数据被称为什么？",
        options: [
          { label: 'A', text: '字段' },
          { label: 'B', text: '记录' },
          { label: 'C', text: '属性' },
          { label: 'D', text: '域' }
        ],
        answer: 'B',
        analysis: "在关系数据库中，表的一行称为记录或元组，一列称为字段或属性。",
        difficulty: "easy"
      },
      {
        id: 'c3',
        chapter: 2,
        title: "选择题3：SQL语法",
        question: "SQL语句中，用于查询数据的关键字是？",
        options: [
          { label: 'A', text: 'INSERT' },
          { label: 'B', text: 'UPDATE' },
          { label: 'C', text: 'SELECT' },
          { label: 'D', text: 'DELETE' }
        ],
        answer: 'C',
        analysis: "SELECT用于查询数据，INSERT插入，UPDATE更新，DELETE删除。",
        difficulty: "easy"
      },
      {
        id: 'c4',
        chapter: 2,
        title: "选择题4：SQL查询",
        question: "SQL中WHERE子句的作用是？",
        options: [
          { label: 'A', text: '指定查询的表' },
          { label: 'B', text: '过滤查询结果' },
          { label: 'C', text: '排序查询结果' },
          { label: 'D', text: '分组统计数据' }
        ],
        answer: 'B',
        analysis: "WHERE子句用于过滤查询条件，HAVING用于分组后过滤，ORDER BY用于排序，GROUP BY用于分组。",
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
        analysis: "ER图中：矩形表示实体，椭圆表示属性，菱形表示联系。",
        difficulty: "easy"
      },
      {
        id: 'c6',
        chapter: 3,
        title: "选择题6：范式设计",
        question: "第一范式要求满足什么条件？",
        options: [
          { label: 'A', text: '消除部分函数依赖' },
          { label: 'B', text: '消除传递函数依赖' },
          { label: 'C', text: '属性不可再分' },
          { label: 'D', text: '消除多值依赖' }
        ],
        answer: 'C',
        analysis: "1NF要求属性原子性（不可再分），2NF消除部分依赖，3NF消除传递依赖，BCNF消除主属性传递依赖。",
        difficulty: "medium"
      },
      {
        id: 'c7',
        chapter: 4,
        title: "选择题7：事务管理",
        question: "事务的ACID特性中，I代表什么？",
        options: [
          { label: 'A', text: '原子性' },
          { label: 'B', text: '一致性' },
          { label: 'C', text: '隔离性' },
          { label: 'D', text: '持久性' }
        ],
        answer: 'C',
        analysis: "ACID：Atomicity原子性，Consistency一致性，Isolation隔离性，Durability持久性。",
        difficulty: "easy"
      },
      {
        id: 'c8',
        chapter: 4,
        title: "选择题8：备份恢复",
        question: "以下哪种备份方式只备份上次备份后变化的数据？",
        options: [
          { label: 'A', text: '完全备份' },
          { label: 'B', text: '增量备份' },
          { label: 'C', text: '差异备份' },
          { label: 'D', text: '镜像备份' }
        ],
        answer: 'B',
        analysis: "增量备份只备份上次备份后的变化，差异备份备份上次完全备份后的变化。",
        difficulty: "medium"
      },
      {
        id: 'c9',
        chapter: 5,
        title: "选择题9：并发控制",
        question: "两个事务互相等待对方释放锁的现象称为？",
        options: [
          { label: 'A', text: '死锁' },
          { label: 'B', text: '活锁' },
          { label: 'C', text: '脏读' },
          { label: 'D', text: '幻读' }
        ],
        answer: 'A',
        analysis: "死锁是两个事务互相等待；活锁是事务永远等待；脏读是读取未提交数据；幻读是同一查询结果不同。",
        difficulty: "medium"
      },
      {
        id: 'c10',
        chapter: 5,
        title: "选择题10：NoSQL数据库",
        question: "以下哪个不是NoSQL数据库？",
        options: [
          { label: 'A', text: 'MongoDB' },
          { label: 'B', text: 'Redis' },
          { label: 'C', text: 'PostgreSQL' },
          { label: 'D', text: 'Cassandra' }
        ],
        answer: 'C',
        analysis: "PostgreSQL是关系型数据库，MongoDB（文档）、Redis（键值）、Cassandra（列族）都是NoSQL数据库。",
        difficulty: "hard"
      },
      {
        id: 'c11',
        chapter: 6,
        title: "选择题11：数据库安全",
        question: "SQL注入攻击主要利用了什么漏洞？",
        options: [
          { label: 'A', text: '弱密码' },
          { label: 'B', text: '未验证的用户输入' },
          { label: 'C', text: '网络监听' },
          { label: 'D', text: '物理访问' }
        ],
        answer: 'B',
        analysis: "SQL注入利用未经验证的用户输入构造恶意SQL语句，应使用参数化查询防止。",
        difficulty: "medium"
      },
      {
        id: 'c12',
        chapter: 6,
        title: "选择题12：权限管理",
        question: "SQL中，授予用户权限使用什么语句？",
        options: [
          { label: 'A', text: 'ADD PRIVILEGE' },
          { label: 'B', text: 'GRANT' },
          { label: 'C', text: 'ALLOW' },
          { label: 'D', text: 'PERMIT' }
        ],
        answer: 'B',
        analysis: "GRANT用于授予权限，REVOKE用于回收权限。",
        difficulty: "medium"
      }
    ];"""

    # 替换选择题
    choice_start = content.find('    // 选择题数据')
    if choice_start == -1:
        choice_start = content.find('    const choiceQuestions = [')
    
    if choice_start != -1:
        # 找到结束位置
        choice_end = content.find('    // 初始化', choice_start)
        if choice_end == -1:
            choice_end = content.find('    // 加载', choice_start)
        
        if choice_end != -1:
            content = content[:choice_start] + db_choice_questions + content[choice_end:]
    
    # 更新考试链接
    content = content.replace('data-collection-exam.html', 'database-principles-exam.html')
    
    return content

def create_bi_course(template_content):
    """创建商业智能课程"""
    content = template_content
    
    # 更新标题
    content = content.replace('供应链分析 - Xww的课程页面', '商业智能 - Xww的课程页面')
    content = content.replace('供应链分析题库', '商业智能题库')
    content = content.replace('data-collection-exam.html', 'business-intelligence-exam.html')
    
    # 更新章节导航
    chapter_updates = [
        ('供应链概述', 'BI概述'),
        ('需求预测', '数据仓库'),
        ('库存管理', 'OLAP分析'),
        ('物流优化', '数据可视化'),
        ('供应链数据分析', 'BI工具'),
        ('供应链风险与优化', 'BI实战')
    ]
    
    for old, new in chapter_updates:
        content = content.replace(old, new)
    
    # 更新模块标题
    module_updates = [
        ('模块1：供应链概述', '模块1：BI概述'),
        ('模块2：需求预测', '模块2：数据仓库'),
        ('模块3：库存管理', '模块3：OLAP分析'),
        ('模块4：物流优化', '模块4：数据可视化'),
        ('模块5：供应链数据分析', '模块5：BI工具'),
        ('模块6：供应链风险与优化', '模块6：BI实战')
    ]
    
    for old, new in module_updates:
        content = content.replace(old, new)
    
    # 更新 problems 数组
    bi_problems = """    // 问题数据
    const problems = [
      {
        id: 1,
        title: "问题1：数据可视化基础",
        description: `使用Matplotlib绘制销售数据图表。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>绘制月度销售额折线图</li>
  <li>添加标题和标签</li>
  <li>设置合适的图表样式</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写代码
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [100, 120, 90, 150, 130, 160]

# 绘制图表
`,
        analysis: `
<h4>解题思路</h4>
<p>1. 导入matplotlib.pyplot</p>
<p>2. 使用plot()绘制折线图</p>
<p>3. 添加标题和标签</p>
<p>4. 显示图表</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import matplotlib.pyplot as plt
import pandas as pd

months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [100, 120, 90, 150, 130, 160]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linewidth=2, markersize=8)
plt.title('月度销售额趋势', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额(万元)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>Matplotlib基础</li>
  <li>折线图绘制</li>
  <li>图表美化</li>
</ul>`,
        chapter: 1
      },
      {
        id: 2,
        title: "问题2：数据分析统计",
        description: `使用Pandas进行销售数据分析。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算总销售额</li>
  <li>计算月平均销售额</li>
  <li>找出销售额最高的月份</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写代码
import pandas as pd

data = {
    'month': ['1月', '2月', '3月', '4月', '5月', '6月'],
    'sales': [100, 120, 90, 150, 130, 160],
    'profit': [20, 25, 15, 30, 28, 35]
}
df = pd.DataFrame(data)

# 分析数据
`,
        analysis: `
<h4>解题思路</h4>
<p>1. 创建DataFrame</p>
<p>2. 使用sum()、mean()等聚合函数</p>
<p>3. 使用idxmax()找最大值位置</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

data = {
    'month': ['1月', '2月', '3月', '4月', '5月', '6月'],
    'sales': [100, 120, 90, 150, 130, 160],
    'profit': [20, 25, 15, 30, 28, 35]
}
df = pd.DataFrame(data)

total_sales = df['sales'].sum()
avg_sales = df['sales'].mean()
max_month = df.loc[df['sales'].idxmax(), 'month']

print(f'总销售额: {total_sales}万元')
print(f'月平均销售额: {avg_sales:.1f}万元')
print(f'销售额最高月份: {max_month}')
print('\\n完整统计:')
print(df.describe())
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>Pandas数据统计</li>
  <li>聚合函数</li>
  <li>数据索引</li>
</ul>`,
        chapter: 4
      },
      {
        id: 3,
        title: "问题3：多维度分析",
        description: `按产品类别和地区进行多维度销售分析。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>按产品类别分组统计销售</li>
  <li>按地区分组统计销售</li>
  <li>创建透视表</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import pandas as pd

data = {
    'product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'region': ['华东', '华东', '华南', '华南', '华北', '华北'],
    'sales': [100, 80, 90, 70, 110, 85]
}
df = pd.DataFrame(data)

# 多维度分析
`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用groupby()分组</p>
<p>2. 使用pivot_table()创建透视表</p>
<p>3. 聚合统计数据</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

data = {
    'product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'region': ['华东', '华东', '华南', '华南', '华北', '华北'],
    'sales': [100, 80, 90, 70, 110, 85]
}
df = pd.DataFrame(data)

# 按产品分组
print('按产品分组:')
print(df.groupby('product')['sales'].sum())

# 按地区分组
print('\\n按地区分组:')
print(df.groupby('region')['sales'].sum())

# 透视表
print('\\n销售透视表:')
pivot = df.pivot_table(values='sales', index='product', columns='region', aggfunc='sum')
print(pivot)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>groupby分组</li>
  <li>透视表</li>
  <li>多维度分析</li>
</ul>`,
        chapter: 3
      },
      {
        id: 4,
        title: "问题4：综合图表展示",
        description: `创建一个综合BI仪表板，包含多个图表。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>包含折线图（趋势）</li>
  <li>包含柱状图（对比）</li>
  <li>包含饼图（占比）</li>
</ul>`,
        difficulty: "medium",
        time: "25分钟",
        code: `# 请编写代码
import matplotlib.pyplot as plt
import pandas as pd

# 数据准备
months = ['1月', '2月', '3月', '4月']
sales = [100, 120, 90, 150]
products = ['产品A', '产品B', '产品C']
product_sales = [300, 250, 200]

# 创建综合图表
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图1: 折线图
`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用subplots()创建多子图布局</p>
<p>2. 分别绘制不同类型的图表</p>
<p>3. 调整布局使其美观</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import matplotlib.pyplot as plt
import pandas as pd

months = ['1月', '2月', '3月', '4月']
sales = [100, 120, 90, 150]
products = ['产品A', '产品B', '产品C']
product_sales = [300, 250, 200]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('销售分析仪表板', fontsize=16)

# 折线图
axes[0, 0].plot(months, sales, marker='o')
axes[0, 0].set_title('销售趋势')
axes[0, 0].grid(True, alpha=0.3)

# 柱状图
axes[0, 1].bar(products, product_sales, color=['#06b6d4', '#10b981', '#f59e0b'])
axes[0, 1].set_title('产品销售对比')

# 饼图
axes[1, 0].pie(product_sales, labels=products, autopct='%1.1f%%')
axes[1, 0].set_title('产品销售占比')

# 移除空图
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>子图布局</li>
  <li>多种图表类型</li>
  <li>BI仪表板</li>
</ul>`,
        chapter: 4
      },
      {
        id: 5,
        title: "问题5：销售预测",
        description: `使用简单的移动平均法进行销售预测。
<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算3个月移动平均</li>
  <li>预测下一个月的销量</li>
  <li>可视化实际值和预测值</li>
</ul>`,
        difficulty: "medium",
        time: "25分钟",
        code: `# 请编写代码
import pandas as pd
import matplotlib.pyplot as plt

data = [100, 120, 90, 150, 130, 160, 140, 180]
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月']

# 移动平均预测
`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用rolling()计算移动平均</p>
<p>2. 用最后一个平均值作为预测</p>
<p>3. 可视化对比</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
import matplotlib.pyplot as plt

data = [100, 120, 90, 150, 130, 160, 140, 180]
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月']

df = pd.DataFrame({'sales': data}, index=months)
df['ma3'] = df['sales'].rolling(window=3).mean()

# 预测
next_pred = df['ma3'].iloc[-1]
print(f'下个月预测销量: {next_pred:.1f}')

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['sales'], label='实际销售', marker='o')
plt.plot(df.index, df['ma3'], label='3月移动平均', linestyle='--')
plt.axhline(y=next_pred, color='red', linestyle=':', label=f'预测值: {next_pred:.1f}')
plt.title('销售预测')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>移动平均</li>
  <li>预测方法</li>
  <li>数据可视化</li>
</ul>`,
        chapter: 2
      }
    ];"""

    # 替换 problems 数组
    problems_start = content.find('    // 问题数据\n    const problems = [')
    if problems_start == -1:
        problems_start = content.find('    // 问题数据\r\n    const problems = [')
    
    if problems_start != -1:
        problems_end = content.find('    // 选择题数据', problems_start)
        if problems_end == -1:
            problems_end = content.find('    const choiceQuestions', problems_start)
        
        if problems_end != -1:
            content = content[:problems_start] + bi_problems + content[problems_end:]
    
    # 更新选择题
    bi_choice_questions = """    // 选择题数据
    const choiceQuestions = [
      {
        id: 'c1',
        chapter: 1,
        title: "选择题1：BI定义",
        question: "BI的全称是什么？",
        options: [
          { label: 'A', text: 'Business Information' },
          { label: 'B', text: 'Business Intelligence' },
          { label: 'C', text: 'Business Integration' },
          { label: 'D', text: 'Business Innovation' }
        ],
        answer: 'B',
        analysis: "BI是Business Intelligence的缩写，即商业智能，是一套完整的解决方案，用于有效集成企业现有数据。",
        difficulty: "easy"
      },
      {
        id: 'c2',
        chapter: 1,
        title: "选择题2：BI目标",
        question: "商业智能的主要目标是什么？",
        options: [
          { label: 'A', text: '数据收集' },
          { label: 'B', text: '数据存储' },
          { label: 'C', text: '辅助决策' },
          { label: 'D', text: '报表生成' }
        ],
        answer: 'C',
        analysis: "虽然BI也涉及数据收集、存储和报表，但其最终目标是支持更好的商业决策。",
        difficulty: "easy"
      },
      {
        id: 'c3',
        chapter: 2,
        title: "选择题3：数据仓库",
        question: "数据仓库的特点不包括以下哪项？",
        options: [
          { label: 'A', text: '面向主题' },
          { label: 'B', text: '集成的' },
          { label: 'C', text: '易变的' },
          { label: 'D', text: '时变的' }
        ],
        answer: 'C',
        analysis: "数据仓库特点：面向主题、集成的、非易失的、时变的。数据是相对稳定的，不是易变的。",
        difficulty: "medium"
      },
      {
        id: 'c4',
        chapter: 2,
        title: "选择题4：星型模型",
        question: "星型模型的核心是什么？",
        options: [
          { label: 'A', text: '维度表' },
          { label: 'B', text: '事实表' },
          { label: 'C', text: '雪花表' },
          { label: 'D', text: '汇总表' }
        ],
        answer: 'B',
        analysis: "星型模型由一个中心事实表和多个维度表组成，事实表是核心，包含度量值和外键。",
        difficulty: "medium"
      },
      {
        id: 'c5',
        chapter: 3,
        title: "选择题5：OLAP操作",
        question: "从汇总数据查看详细数据的操作称为？",
        options: [
          { label: 'A', text: '上卷（Roll-up）' },
          { label: 'B', text: '下钻（Drill-down）' },
          { label: 'C', text: '切片（Slice）' },
          { label: 'D', text: '切块（Dice）' }
        ],
        answer: 'B',
        analysis: "下钻是从汇总到详细，上卷是从详细到汇总，切片是选择一个维度值，切块是选择多个维度值。",
        difficulty: "medium"
      },
      {
        id: 'c6',
        chapter: 3,
        title: "选择题6：ROLAP与MOLAP",
        question: "MOLAP使用什么存储数据？",
        options: [
          { label: 'A', text: '关系数据库' },
          { label: 'B', text: '多维数组' },
          { label: 'C', text: '文本文件' },
          { label: 'D', text: 'NoSQL数据库' }
        ],
        answer: 'B',
        analysis: "MOLAP（多维OLAP）使用多维数组存储，ROLAP（关系OLAP）使用关系数据库存储。",
        difficulty: "medium"
      },
      {
        id: 'c7',
        chapter: 4,
        title: "选择题7：数据可视化",
        question: "比较多类别的数据时，最适合使用什么图表？",
        options: [
          { label: 'A', text: '折线图' },
          { label: 'B', text: '柱状图' },
          { label: 'C', text: '饼图' },
          { label: 'D', text: '散点图' }
        ],
        answer: 'B',
        analysis: "柱状图适合类别比较，折线图适合趋势，饼图适合占比，散点图适合相关性。",
        difficulty: "easy"
      },
      {
        id: 'c8',
        chapter: 4,
        title: "选择题8：图表选择",
        question: "展示各部分占总体的比例时，使用什么图表？",
        options: [
          { label: 'A', text: '折线图' },
          { label: 'B', text: '柱状图' },
          { label: 'C', text: '饼图' },
          { label: 'D', text: '箱线图' }
        ],
        answer: 'C',
        analysis: "饼图专门用于显示各部分占整体的比例关系。",
        difficulty: "easy"
      },
      {
        id: 'c9',
        chapter: 5,
        title: "选择题9：BI工具",
        question: "以下哪个不是主流的BI工具？",
        options: [
          { label: 'A', text: 'Tableau' },
          { label: 'B', text: 'Power BI' },
          { label: 'C', text: 'Photoshop' },
          { label: 'D', text: 'FineReport' }
        ],
        answer: 'C',
        analysis: "Photoshop是图像处理软件，不是BI工具。Tableau、Power BI、FineReport都是BI工具。",
        difficulty: "easy"
      },
      {
        id: 'c10',
        chapter: 5,
        title: "选择题10：ETL过程",
        question: "ETL的T代表什么？",
        options: [
          { label: 'A', text: 'Transform（转换）' },
          { label: 'B', text: 'Transfer（传输）' },
          { label: 'C', text: 'Translate（翻译）' },
          { label: 'D', text: 'Transport（运输）' }
        ],
        answer: 'A',
        analysis: "ETL：Extract抽取、Transform转换、Load加载。",
        difficulty: "medium"
      },
      {
        id: 'c11',
        chapter: 6,
        title: "选择题11：KPI",
        question: "KPI的全称是什么？",
        options: [
          { label: 'A', text: 'Key Process Indicator' },
          { label: 'B', text: 'Key Performance Indicator' },
          { label: 'C', text: 'Key Product Indicator' },
          { label: 'D', text: 'Key Profit Indicator' }
        ],
        answer: 'B',
        analysis: "KPI是Key Performance Indicator（关键绩效指标）。",
        difficulty: "easy"
      },
      {
        id: 'c12',
        chapter: 6,
        title: "选择题12：数据驱动决策",
        question: "数据驱动决策的第一步是？",
        options: [
          { label: 'A', text: '数据分析' },
          { label: 'B', text: '数据收集' },
          { label: 'C', text: '数据可视化' },
          { label: 'D', text: '决策执行' }
        ],
        answer: 'B',
        analysis: "数据驱动决策的流程：数据收集→数据整理→数据分析→数据可视化→决策。第一步是数据收集。",
        difficulty: "medium"
      }
    ];"""

    # 替换选择题
    choice_start = content.find('    // 选择题数据')
    if choice_start == -1:
        choice_start = content.find('    const choiceQuestions = [')
    
    if choice_start != -1:
        choice_end = content.find('    // 初始化', choice_start)
        if choice_end == -1:
            choice_end = content.find('    // 加载', choice_start)
        
        if choice_end != -1:
            content = content[:choice_start] + bi_choice_questions + content[choice_end:]
    
    # 更新考试链接
    content = content.replace('data-collection-exam.html', 'business-intelligence-exam.html')
    
    return content

def main():
    """主函数"""
    courses_dir = '/workspace/courses'
    
    # 读取已成功的模板
    template_path = os.path.join(courses_dir, 'supply-chain-analysis.html')
    template_content = read_file(template_path)
    print(f'读取模板成功: {template_path}')
    
    # 创建数据库原理课程
    print('\n正在创建数据库原理课程...')
    db_content = create_database_course(template_content)
    db_path = os.path.join(courses_dir, 'database-principles.html')
    write_file(db_path, db_content)
    print(f'数据库原理课程已保存: {db_path}')
    
    # 创建商业智能课程
    print('\n正在创建商业智能课程...')
    bi_content = create_bi_course(template_content)
    bi_path = os.path.join(courses_dir, 'business-intelligence.html')
    write_file(bi_path, bi_content)
    print(f'商业智能课程已保存: {bi_path}')
    
    print('\n✅ 所有课程更新完成！')
    print('\n已更新的课程:')
    print('  1. database-principles.html - 数据库原理与应用')
    print('  2. business-intelligence.html - 商业智能')
    print('  3. supply-chain-analysis.html - 供应链分析 (已完成)')

if __name__ == '__main__':
    main()
