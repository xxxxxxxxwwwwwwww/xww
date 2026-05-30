
import re

# 配置数据
DB_PRINCIPLES_DATA = '''    // 问题数据
    const problems = [
        {
            id: 1,
            title: "数据库基本概念",
            difficulty: "easy",
            timeLimit: 25,
            description: "编写一个Python程序，模拟关系型数据库的基本概念。\\n\\n**输入**：\\n- 一组数据记录，包含多个字段\\n\\n**输出**：\\n- 按指定字段筛选和排序后的结果\\n\\n**要求**：\\n1. 定义数据表结构\\n2. 实现基本的查询功能\\n3. 输出格式化的查询结果",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 数据库基本概念模拟\\nclass DatabaseTable:\\n    def __init__(self, name, columns):\\n        self.name = name\\n        self.columns = columns\\n        self.data = []\\n    \\n    def insert(self, record):\\n        self.data.append(record)\\n    \\n    def select(self, conditions=None):\\n        result = []\\n        for record in self.data:\\n            if conditions is None or all(record.get(k) == v for k, v in conditions.items()):\\n                result.append(record)\\n        return result\\n    \\n    def sort_by(self, column):\\n        return sorted(self.data, key=lambda x: x[column])\\n\\n# 使用示例\\nusers = DatabaseTable('users', ['id', 'name', 'age'])\\nusers.insert({'id': 1, 'name': '张三', 'age': 25})\\nusers.insert({'id': 2, 'name': '李四', 'age': 30})\\n\\nprint(users.select({'age': 25}))\\nprint(users.sort_by('age'))"
        },
        {
            id: 2,
            title: "SQL查询实现",
            difficulty: "easy",
            timeLimit: 30,
            description: "模拟SQL SELECT查询的功能。\\n\\n**输入**：\\n- 数据表数据\\n- 查询条件\\n\\n**输出**：\\n- 查询结果\\n\\n**要求**：\\n1. 支持WHERE条件筛选\\n2. 支持ORDER BY排序\\n3. 支持指定列投影",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# SQL查询模拟器\\ndef sql_select(data, columns='*', where=None, order_by=None):\\n    result = data.copy()\\n    \\n    # WHERE条件筛选\\n    if where:\\n        filtered = []\\n        for record in result:\\n            match = True\\n            for field, value in where.items():\\n                if record.get(field) != value:\\n                    match = False\\n                    break\\n            if match:\\n                filtered.append(record)\\n        result = filtered\\n    \\n    # 排序\\n    if order_by:\\n        result = sorted(result, key=lambda x: x[order_by])\\n    \\n    # 投影\\n    if columns != '*':\\n        projected = []\\n        for record in result:\\n            projected_record = {col: record[col] for col in columns if col in record}\\n            projected.append(projected_record)\\n        result = projected\\n    \\n    return result\\n\\n# 测试数据\\ndata = [\\n    {'name': 'Apple', 'category': 'fruit', 'price': 5},\\n    {'name': 'Banana', 'category': 'fruit', 'price': 3},\\n    {'name': 'Carrot', 'category': 'vegetable', 'price': 2}\\n]\\n\\nprint(sql_select(data, where={'category': 'fruit'}, order_by='price'))"
        },
        {
            id: 3,
            title: "事务ACID特性",
            difficulty: "medium",
            timeLimit: 20,
            description: "模拟数据库事务的ACID特性。\\n\\n**要求**：\\n1. 实现事务的开始和提交\\n2. 实现回滚机制\\n3. 演示原子性和持久性",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 事务ACID特性模拟\\nclass Database:\\n    def __init__(self):\\n        self.data = {}\\n        self.transaction_log = []\\n        self.in_transaction = False\\n    \\n    def begin_transaction(self):\\n        self.in_transaction = True\\n        self.transaction_log = self.data.copy()\\n    \\n    def commit(self):\\n        if self.in_transaction:\\n            self.in_transaction = False\\n            self.transaction_log = []\\n            print('事务提交成功')\\n    \\n    def rollback(self):\\n        if self.in_transaction:\\n            self.data = self.transaction_log.copy()\\n            self.in_transaction = False\\n            print('事务已回滚')\\n    \\n    def set(self, key, value):\\n        self.data[key] = value\\n    \\n    def get(self, key):\\n        return self.data.get(key)\\n\\n# 演示事务\\ndb = Database()\\ndb.begin_transaction()\\ndb.set('balance', 100)\\ndb.set('balance', 150)\\ndb.rollback()  # 回滚到事务前状态\\nprint(db.get('balance'))  # 输出None，因为被回滚"
        },
        {
            id: 4,
            title: "索引结构实现",
            difficulty: "medium",
            timeLimit: 20,
            description: "实现简单的数据库索引结构，提高查询效率。\\n\\n**要求**：\\n1. 实现B树或哈希索引\\n2. 支持插入和查找\\n3. 对比有索引和无索引的查询性能",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 数据库索引实现\\nclass HashIndex:\\n    def __init__(self):\\n        self.index = {}\\n    \\n    def insert(self, key, record_id):\\n        if key not in self.index:\\n            self.index[key] = []\\n        self.index[key].append(record_id)\\n    \\n    def search(self, key):\\n        return self.index.get(key, [])\\n    \\n    def delete(self, key, record_id):\\n        if key in self.index:\\n            if record_id in self.index[key]:\\n                self.index[key].remove(record_id)\\n\\n# 使用示例\\nindex = HashIndex()\\nindex.insert('张三', 1)\\nindex.insert('李四', 2)\\nindex.insert('张三', 3)\\n\\nprint('查找\\'张三\\':', index.search('张三'))  # 输出 [1, 3]"
        },
        {
            id: 5,
            title: "数据库综合应用",
            difficulty: "hard",
            timeLimit: 30,
            description: "设计一个简单的学生成绩管理系统的数据库。\\n\\n**要求**：\\n1. 设计ER图（文字描述）\\n2. 定义数据表结构\\n3. 实现基本的增删改查功能\\n4. 编写示例SQL查询",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 学生成绩管理系统数据库设计\\n# ER图设计：\\n# - 学生(student): 学号, 姓名, 班级\\n# - 课程(course): 课程号, 课程名, 学分\\n# - 成绩(score): 学号, 课程号, 成绩\\n\\n# 创建表的SQL示例（文字描述）\\n# CREATE TABLE student (\\n#     id INT PRIMARY KEY,\\n#     name VARCHAR(50),\\n#     class VARCHAR(20)\\n# );\\n\\n# 简单的Python实现\\nclass StudentDB:\\n    def __init__(self):\\n        self.students = {}  # {id: {name, class}}\\n        self.courses = {}   # {id: {name, credit}}\\n        self.scores = []    # [{student_id, course_id, score}]\\n    \\n    def add_student(self, sid, name, cls):\\n        self.students[sid] = {'name': name, 'class': cls}\\n    \\n    def add_course(self, cid, name, credit):\\n        self.courses[cid] = {'name': name, 'credit': credit}\\n    \\n    def add_score(self, sid, cid, score):\\n        self.scores.append({'student_id': sid, 'course_id': cid, 'score': score})\\n    \\n    def get_student_scores(self, sid):\\n        return [s for s in self.scores if s['student_id'] == sid]\\n\\n# 使用示例\\ndb = StudentDB()\\ndb.add_student(1, '张三', '一班')\\ndb.add_course(101, '数学', 4)\\ndb.add_score(1, 101, 90)\\n\\nprint(db.get_student_scores(1))"
        }
    ];

    // 选择题数据
    const choiceQuestions = [
        {
            id: 'c1',
            chapter: 1,
            title: "数据模型概念",
            difficulty: "easy",
            description: "以下哪个不是常用的数据模型？",
            options: [
                "层次模型",
                "网状模型",
                "关系模型",
                "树状模型"
            ],
            correctIndex: 3,
            explanation: "常用的数据模型包括层次模型、网状模型和关系模型。树状模型不是标准的数据模型分类。"
        },
        {
            id: 'c2',
            chapter: 1,
            title: "数据库系统组成",
            difficulty: "medium",
            description: "数据库系统的核心是？",
            options: [
                "数据库",
                "数据库管理系统",
                "应用程序",
                "数据库管理员"
            ],
            correctIndex: 1,
            explanation: "数据库管理系统(DBMS)是数据库系统的核心，负责管理和维护数据库。"
        },
        {
            id: 'c3',
            chapter: 2,
            title: "关系代数运算",
            difficulty: "medium",
            description: "从关系中选择满足条件的元组的操作称为？",
            options: [
                "投影",
                "选择",
                "连接",
                "除"
            ],
            correctIndex: 1,
            explanation: "选择(SELECT)操作是从关系中选择满足条件的元组，是行方向的筛选。"
        },
        {
            id: 'c4',
            chapter: 2,
            title: "关系完整性",
            difficulty: "medium",
            description: "实体完整性要求主属性？",
            options: [
                "不能为空",
                "必须唯一",
                "不能为空且必须唯一",
                "可以重复"
            ],
            correctIndex: 2,
            explanation: "实体完整性要求主属性不能取空值且必须唯一，这样才能唯一标识元组。"
        },
        {
            id: 'c5',
            chapter: 3,
            title: "SQL语言分类",
            difficulty: "easy",
            description: "SQL语言中，CREATE TABLE属于？",
            options: [
                "数据查询语言",
                "数据操纵语言",
                "数据定义语言",
                "数据控制语言"
            ],
            correctIndex: 2,
            explanation: "CREATE TABLE属于数据定义语言(DDL)，用于定义数据库结构。"
        },
        {
            id: 'c6',
            chapter: 3,
            title: "SQL查询语法",
            difficulty: "easy",
            description: "SQL查询语句的正确执行顺序是？",
            options: [
                "SELECT → FROM → WHERE → GROUP BY → ORDER BY",
                "FROM → WHERE → SELECT → GROUP BY → ORDER BY",
                "FROM → WHERE → GROUP BY → SELECT → ORDER BY",
                "SELECT → FROM → GROUP BY → WHERE → ORDER BY"
            ],
            correctIndex: 2,
            explanation: "SQL查询的逻辑执行顺序是：FROM → WHERE → GROUP BY → SELECT → ORDER BY。"
        },
        {
            id: 'c7',
            chapter: 4,
            title: "规范化设计",
            difficulty: "medium",
            description: "第一范式要求属性是？",
            options: [
                "不可再分",
                "部分依赖于主键",
                "完全依赖于主键",
                "不传递依赖"
            ],
            correctIndex: 0,
            explanation: "第一范式要求每个属性都是原子的，不可再分。"
        },
        {
            id: 'c8',
            chapter: 5,
            title: "事务特性",
            difficulty: "easy",
            description: "事务的ACID特性中，I代表？",
            options: [
                "原子性",
                "一致性",
                "隔离性",
                "持久性"
            ],
            correctIndex: 2,
            explanation: "ACID中I代表Isolation(隔离性)，保证并发事务互不干扰。"
        },
        {
            id: 'c9',
            chapter: 5,
            title: "并发控制",
            difficulty: "medium",
            description: "解决并发操作带来的数据不一致问题主要通过？",
            options: [
                "封锁机制",
                "恢复机制",
                "索引机制",
                "优化机制"
            ],
            correctIndex: 0,
            explanation: "封锁机制是并发控制的主要方法，防止多个事务同时修改同一数据。"
        },
        {
            id: 'c10',
            chapter: 6,
            title: "数据库设计",
            difficulty: "medium",
            description: "数据库设计的六个阶段中，首先进行的是？",
            options: [
                "概念结构设计",
                "需求分析",
                "逻辑结构设计",
                "物理结构设计"
            ],
            correctIndex: 1,
            explanation: "数据库设计首先要进行需求分析，了解用户需求。"
        }
    ];
'''

BUSINESS_INTELLIGENCE_DATA = '''    // 问题数据
    const problems = [
        {
            id: 1,
            title: "数据仓库维度建模",
            difficulty: "easy",
            timeLimit: 25,
            description: "设计一个简单的销售数据仓库星型模型。\\n\\n**要求**：\\n1. 设计事实表和维度表\\n2. 支持时间、产品、地区维度分析\\n3. 实现基本的数据聚合查询",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 数据仓库星型模型模拟\\nclass DataWarehouse:\\n    def __init__(self):\\n        # 维度表\\n        self.dim_time = {}    # {time_id: {date, year, month, quarter}}\\n        self.dim_product = {} # {product_id: {name, category, price}}\\n        self.dim_region = {}  # {region_id: {name, city, province}}\\n        # 事实表\\n        self.fact_sales = []  # [{time_id, product_id, region_id, quantity, amount}]\\n    \\n    def add_time(self, time_id, date, year, month, quarter):\\n        self.dim_time[time_id] = {'date': date, 'year': year, 'month': month, 'quarter': quarter}\\n    \\n    def add_product(self, product_id, name, category, price):\\n        self.dim_product[product_id] = {'name': name, 'category': category, 'price': price}\\n    \\n    def add_region(self, region_id, name, city, province):\\n        self.dim_region[region_id] = {'name': name, 'city': city, 'province': province}\\n    \\n    def add_sale(self, time_id, product_id, region_id, quantity, amount):\\n        self.fact_sales.append({\\n            'time_id': time_id,\\n            'product_id': product_id,\\n            'region_id': region_id,\\n            'quantity': quantity,\\n            'amount': amount\\n        })\\n    \\n    def query_by_year(self, year):\\n        total = 0\\n        for sale in self.fact_sales:\\n            time = self.dim_time[sale['time_id']]\\n            if time['year'] == year:\\n                total += sale['amount']\\n        return total\\n\\n# 使用示例\\ndw = DataWarehouse()\\ndw.add_time(1, '2024-01-01', 2024, 1, 1)\\ndw.add_product(1, '笔记本电脑', '电子产品', 5000)\\ndw.add_region(1, '华东区', '上海', '上海')\\ndw.add_sale(1, 1, 1, 10, 50000)\\n\\nprint(f'2024年销售额: {dw.query_by_year(2024)}')"
        },
        {
            id: 2,
            title: "ETL过程实现",
            difficulty: "easy",
            timeLimit: 30,
            description: "实现一个简单的ETL（抽取-转换-加载）流程。\\n\\n**要求**：\\n1. 从数据源抽取原始数据\\n2. 进行数据清洗和转换\\n3. 加载到目标数据结构",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# ETL流程实现\\ndef extract(source_data):\\n    '''抽取数据''',\\n    print('正在抽取数据...')\\n    return source_data\\n\\ndef transform(raw_data):\\n    '''转换数据''',\\n    print('正在转换数据...')\\n    transformed = []\\n    for record in raw_data:\\n        # 清洗：去除空值\\n        if not record.get('name') or not record.get('value'):\\n            continue\\n        # 转换：格式化日期\\n        if 'date' in record:\\n            record['date'] = record['date'].replace('/', '-')\\n        # 转换：大写转换\\n        if 'status' in record:\\n            record['status'] = record['status'].upper()\\n        transformed.append(record)\\n    return transformed\\n\\ndef load(transformed_data, target):\\n    '''加载数据''',\\n    print('正在加载数据...')\\n    target.extend(transformed_data)\\n    print(f'成功加载 {len(transformed_data)} 条记录')\\n\\n# 测试ETL流程\\nsource = [\\n    {'name': 'A产品', 'value': 100, 'date': '2024/01/01', 'status': 'active'},\\n    {'name': None, 'value': 200, 'date': '2024/01/02', 'status': 'inactive'},\\n    {'name': 'B产品', 'value': None, 'date': '2024/01/03', 'status': 'active'}\\n]\\ntarget = []\\n\\n# 执行ETL\\nraw = extract(source)\\ntransformed = transform(raw)\\nload(transformed, target)\\nprint('目标数据:', target)"
        },
        {
            id: 3,
            title: "OLAP多维分析",
            difficulty: "medium",
            timeLimit: 20,
            description: "实现OLAP的基本操作：切片、切块、钻取。\\n\\n**要求**：\\n1. 支持按维度切片\\n2. 支持多维度切块\\n3. 支持数据聚合",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# OLAP多维分析实现\\nclass OLAPCubes:\\n    def __init__(self):\\n        self.data = []\\n    \\n    def add_data(self, record):\\n        self.data.append(record)\\n    \\n    def slice(self, dimension, value):\\n        '''切片：固定一个维度''',\\n        return [r for r in self.data if r[dimension] == value]\\n    \\n    def dice(self, conditions):\\n        '''切块：多个维度条件''',\\n        result = self.data\\n        for dim, val in conditions.items():\\n            result = [r for r in result if r[dim] == val]\\n        return result\\n    \\n    def rollup(self, group_by, measure):\\n        '''上卷：按维度聚合''',\\n        aggregations = {}\\n        for record in self.data:\\n            key = tuple(record[dim] for dim in group_by)\\n            if key not in aggregations:\\n                aggregations[key] = 0\\n            aggregations[key] += record[measure]\\n        return aggregations\\n\\n# 使用示例\\ncube = OLAPCubes()\\ncube.add_data({'year': 2024, 'region': '华东', 'product': '电脑', 'sales': 10000})\\ncube.add_data({'year': 2024, 'region': '华东', 'product': '手机', 'sales': 8000})\\ncube.add_data({'year': 2024, 'region': '华北', 'product': '电脑', 'sales': 9000})\\n\\nprint('切片-华东区:', cube.slice('region', '华东'))\\nprint('上卷-按年份:', cube.rollup(['year'], 'sales'))"
        },
        {
            id: 4,
            title: "数据可视化",
            difficulty: "medium",
            timeLimit: 20,
            description: "编写程序生成简单的数据可视化描述（文本式）。\\n\\n**要求**：\\n1. 支持柱状图的文本表示\\n2. 支持趋势图的文本表示\\n3. 输出美观的可视化结果",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 文本数据可视化\\ndef text_bar_chart(data, title='柱状图'):\\n    print(f'=== {title} ===')\\n    max_value = max(data.values()) if data else 1\\n    for label, value in data.items():\\n        bar_length = int((value / max_value) * 40)\\n        bar = '█' * bar_length\\n        print(f'{label:10} | {bar} {value}')\\n\\ndef text_line_chart(data, title='趋势图'):\\n    print(f'=== {title} ===')\\n    months = list(data.keys())\\n    values = list(data.values())\\n    \\n    # 简单的文本趋势展示\\n    print('月份: ' + '  '.join(months))\\n    print('数值: ' + '  '.join(str(v) for v in values))\\n    \\n    # 变化箭头\\n    print('趋势: ', end='')\\n    for i in range(1, len(values)):\\n        if values[i] > values[i-1]:\\n            print('↑ ', end='')\\n        elif values[i] < values[i-1]:\\n            print('↓ ', end='')\\n        else:\\n            print('→ ', end='')\\n    print()\\n\\n# 测试可视化\\nsales = {'1月': 120, '2月': 150, '3月': 130, '4月': 180, '5月': 160}\\ntext_bar_chart(sales, '月度销售额')\\nprint()\\ntext_line_chart(sales, '销售趋势')"
        },
        {
            id: 5,
            title: "商业决策支持",
            difficulty: "hard",
            timeLimit: 30,
            description: "综合运用BI技术，为零售业务提供决策支持。\\n\\n**要求**：\\n1. 分析销售数据\\n2. 识别热销产品\\n3. 发现销售趋势\\n4. 提供建议报告",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 商业决策支持系统\\nclass DecisionSupport:\\n    def __init__(self, sales_data):\\n        self.sales = sales_data\\n    \\n    def analyze_products(self):\\n        '''产品分析''',\\n        product_sales = {}\\n        for s in self.sales:\\n            product = s['product']\\n            product_sales[product] = product_sales.get(product, 0) + s['amount']\\n        return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)\\n    \\n    def analyze_trends(self):\\n        '''趋势分析''',\\n        monthly = {}\\n        for s in self.sales:\\n            month = s['date'][:7]\\n            monthly[month] = monthly.get(month, 0) + s['amount']\\n        return monthly\\n    \\n    def generate_report(self):\\n        '''生成决策报告''',\\n        print('=' * 50)\\n        print('商业智能决策报告')\\n        print('=' * 50)\\n        \\n        products = self.analyze_products()\\n        print('\\\\n热销产品TOP 3:')\\n        for i, (p, s) in enumerate(products[:3], 1):\\n            print(f'{i}. {p}: ¥{s:,}')\\n        \\n        trends = self.analyze_trends()\\n        print('\\\\n月度销售趋势:')\\n        for month, amount in sorted(trends.items()):\\n            print(f'{month}: ¥{amount:,}')\\n        \\n        print('\\\\n建议:')\\n        if products:\\n            print(f'- 重点推广热销产品: {products[0][0]}')\\n            print(f'- 考虑促销低销量产品: {products[-1][0]}')\\n\\n# 测试数据\\ndata = [\\n    {'product': '笔记本', 'date': '2024-01-15', 'amount': 5000},\\n    {'product': '笔记本', 'date': '2024-02-20', 'amount': 5500},\\n    {'product': '手机', 'date': '2024-01-10', 'amount': 3000},\\n    {'product': '平板', 'date': '2024-02-05', 'amount': 2000}\\n]\\n\\nds = DecisionSupport(data)\\nds.generate_report()"
        }
    ];

    // 选择题数据
    const choiceQuestions = [
        {
            id: 'c1',
            chapter: 1,
            title: "BI概念",
            difficulty: "easy",
            description: "BI的全称是？",
            options: [
                "Business Intelligence",
                "Big Data",
                "Business Integration",
                "Business Information"
            ],
            correctIndex: 0,
            explanation: "BI是Business Intelligence(商业智能)的缩写。"
        },
        {
            id: 'c2',
            chapter: 1,
            title: "BI系统目标",
            difficulty: "medium",
            description: "商业智能系统的核心目标是？",
            options: [
                "存储大量数据",
                "支持决策制定",
                "生成报表",
                "处理事务"
            ],
            correctIndex: 1,
            explanation: "商业智能的核心目标是通过数据分析支持更好的决策制定。"
        },
        {
            id: 'c3',
            chapter: 2,
            title: "数据仓库特点",
            difficulty: "easy",
            description: "以下哪个不是数据仓库的特点？",
            options: [
                "面向主题",
                "集成的",
                "可更新的",
                "随时间变化的"
            ],
            correctIndex: 2,
            explanation: "数据仓库的数据是相对稳定的，主要用于查询分析，不频繁更新。"
        },
        {
            id: 'c4',
            chapter: 2,
            title: "星型模型",
            difficulty: "medium",
            description: "星型模型由什么组成？",
            options: [
                "一个事实表和多个维度表",
                "多个事实表和一个维度表",
                "只有事实表",
                "只有维度表"
            ],
            correctIndex: 0,
            explanation: "星型模型由一个中心事实表和多个围绕它的维度表组成。"
        },
        {
            id: 'c5',
            chapter: 2,
            title: "缓慢变化维",
            difficulty: "medium",
            description: "处理维度数据变化的技术称为？",
            options: [
                "渐变维度",
                "快速维度",
                "静态维度",
                "动态维度"
            ],
            correctIndex: 0,
            explanation: "处理维度数据缓慢变化的技术称为缓慢变化维(SCD)。"
        },
        {
            id: 'c6',
            chapter: 3,
            title: "OLAP操作",
            difficulty: "easy",
            description: "从较低层次细节数据汇总到较高层次称为？",
            options: [
                "切片",
                "切块",
                "上卷",
                "下钻"
            ],
            correctIndex: 2,
            explanation: "上卷(Roll-up)是从细节数据汇总到更高层次的聚合数据。"
        },
        {
            id: 'c7',
            chapter: 3,
            title: "MOLAP与ROLAP",
            difficulty: "medium",
            description: "MOLAP使用什么存储数据？",
            options: [
                "关系数据库",
                "多维数组",
                "文档数据库",
                "图数据库"
            ],
            correctIndex: 1,
            explanation: "MOLAP(多维OLAP)使用多维数组存储数据。"
        },
        {
            id: 'c8',
            chapter: 4,
            title: "数据可视化",
            difficulty: "easy",
            description: "比较不同类别数据的大小适合用？",
            options: [
                "折线图",
                "柱状图",
                "饼图",
                "散点图"
            ],
            correctIndex: 1,
            explanation: "柱状图适合比较不同类别数据的数量大小。"
        },
        {
            id: 'c9',
            chapter: 5,
            title: "KPI指标",
            difficulty: "medium",
            description: "KPI指的是？",
            options: [
                "关键绩效指标",
                "知识过程集成",
                "关键流程改进",
                "知识产品创新"
            ],
            correctIndex: 0,
            explanation: "KPI是Key Performance Indicator(关键绩效指标)的缩写。"
        },
        {
            id: 'c10',
            chapter: 6,
            title: "BI发展趋势",
            difficulty: "medium",
            description: "当前BI发展的重要趋势不包括？",
            options: [
                "自助BI",
                "增强分析",
                "数据孤岛",
                "嵌入式BI"
            ],
            correctIndex: 2,
            explanation: "数据孤岛是需要解决的问题，不是发展趋势。趋势是自助BI、增强分析、嵌入式BI等。"
        }
    ];
'''

SUPPLY_CHAIN_DATA = '''    // 问题数据
    const problems = [
        {
            id: 1,
            title: "需求预测分析",
            difficulty: "easy",
            timeLimit: 25,
            description: "使用移动平均法进行简单的需求预测。\\n\\n**要求**：\\n1. 实现简单移动平均(SMA)\\n2. 实现加权移动平均(WMA)\\n3. 对比预测误差",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 需求预测分析\\nimport statistics\\n\\ndef simple_moving_average(data, period):\\n    '''简单移动平均''',\\n    if len(data) < period:\\n        return None\\n    sma = []\\n    for i in range(period, len(data) + 1):\\n        window = data[i-period:i]\\n        sma.append(sum(window) / period)\\n    return sma\\n\\ndef weighted_moving_average(data, weights):\\n    '''加权移动平均''',\\n    period = len(weights)\\n    if len(data) < period or sum(weights) != 1.0:\\n        return None\\n    wma = []\\n    for i in range(period, len(data) + 1):\\n        window = data[i-period:i]\\n        forecast = sum(w * x for w, x in zip(weights, window))\\n        wma.append(forecast)\\n    return wma\\n\\ndef calculate_error(actual, forecast):\\n    '''计算预测误差''',\\n    if not actual or not forecast:\\n        return None\\n    errors = [a - f for a, f in zip(actual, forecast)]\\n    mae = sum(abs(e) for e in errors) / len(errors)\\n    return {'MAE': mae}\\n\\n# 测试数据\\nsales = [100, 110, 105, 120, 115, 130, 125]\\nweights = [0.5, 0.3, 0.2]\\n\\nprint('历史销售:', sales)\\nprint('SMA(3):', simple_moving_average(sales, 3))\\nprint('WMA:', weighted_moving_average(sales, weights))"
        },
        {
            id: 2,
            title: "库存优化管理",
            difficulty: "easy",
            timeLimit: 30,
            description: "实现经济订货量(EOQ)模型计算。\\n\\n**要求**：\\n1. 计算EOQ\\n2. 计算订货点\\n3. 模拟库存变化",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 库存优化管理\\nimport math\\n\\ndef calculate_eoq(demand, order_cost, holding_cost):\\n    '''经济订货量EOQ''',\\n    # EOQ = sqrt(2DS/H)\\n    # D: 年需求量, S: 订货成本, H: 年持有成本\\n    eoq = math.sqrt(2 * demand * order_cost / holding_cost)\\n    return round(eoq)\\n\\ndef calculate_reorder_point(daily_demand, lead_time):\\n    '''订货点''',\\n    return daily_demand * lead_time\\n\\ndef simulate_inventory(eoq, reorder_point, daily_demand, days=30):\\n    '''模拟库存变化''',\\n    inventory = eoq  # 初始库存\\n    inventory_history = [inventory]\\n    \\n    for day in range(1, days + 1):\\n        inventory -= daily_demand\\n        # 检查是否需要补货\\n        if inventory <= reorder_point:\\n            inventory += eoq\\n            print(f'第{day}天: 库存过低，补货{eoq}单位')\\n        inventory_history.append(inventory)\\n    \\n    return inventory_history\\n\\n# 参数设置\\nannual_demand = 12000    # 年需求\\norder_cost = 50         # 每次订货成本\\nholding_cost = 2.4      # 年单位持有成本\\ndaily_demand = 12000 / 365\\nlead_time = 3           # 提前期（天）\\n\\neoq = calculate_eoq(annual_demand, order_cost, holding_cost)\\nrop = calculate_reorder_point(daily_demand, lead_time)\\n\\nprint(f'经济订货量(EOQ): {eoq}')\\nprint(f'订货点(ROP): {rop:.0f}')\\nprint('\\n库存模拟(30天):')\\nsimulate_inventory(eoq, rop, daily_demand, days=30)"
        },
        {
            id: 3,
            title: "供应商评估分析",
            difficulty: "medium",
            timeLimit: 20,
            description: "对供应商进行多维度综合评估。\\n\\n**要求**：\\n1. 设定评估指标（质量、成本、交付）\\n2. 计算各供应商得分\\n3. 进行排名和选择",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 供应商评估分析\\nclass SupplierEvaluator:\\n    def __init__(self, weights):\\n        '''weights: {quality: 0.4, cost: 0.3, delivery: 0.3}''',\\n        self.weights = weights\\n        self.suppliers = []\\n    \\n    def add_supplier(self, name, quality_score, cost_score, delivery_score):\\n        self.suppliers.append({\\n            'name': name,\\n            'quality': quality_score,\\n            'cost': cost_score,\\n            'delivery': delivery_score\\n        })\\n    \\n    def evaluate(self):\\n        '''评估所有供应商''',\\n        results = []\\n        for s in self.suppliers:\\n            total_score = (\\n                s['quality'] * self.weights['quality'] +\\n                s['cost'] * self.weights['cost'] +\\n                s['delivery'] * self.weights['delivery']\\n            )\\n            results.append({\\n                'name': s['name'],\\n                'quality': s['quality'],\\n                'cost': s['cost'],\\n                'delivery': s['delivery'],\\n                'total': round(total_score, 2)\\n            })\\n        # 按总分排序\\n        results.sort(key=lambda x: x['total'], reverse=True)\\n        return results\\n    \\n    def print_report(self):\\n        '''打印评估报告''',\\n        print('=' * 70)\\n        print('供应商综合评估报告')\\n        print('=' * 70)\\n        print(f'指标权重: 质量={self.weights[\"quality\"]}, 成本={self.weights[\"cost\"]}, 交付={self.weights[\"delivery\"]}')\\n        print('-' * 70)\\n        print(f'{'排名':<4} {'供应商':<10} {'质量':<6} {'成本':<6} {'交付':<6} {'总分':<8}')\\n        print('-' * 70)\\n        \\n        results = self.evaluate()\\n        for i, r in enumerate(results, 1):\\n            print(f'{i:<4} {r[\"name\"]:<10} {r[\"quality\"]:<6} {r[\"cost\"]:<6} {r[\"delivery\"]:<6} {r[\"total\"]:<8}')\\n        print('=' * 70)\\n\\n# 使用示例\\nevaluator = SupplierEvaluator({'quality': 0.4, 'cost': 0.3, 'delivery': 0.3})\\nevaluator.add_supplier('供应商A', 90, 85, 88)\\nevaluator.add_supplier('供应商B', 85, 92, 80)\\nevaluator.add_supplier('供应商C', 88, 80, 92)\\nevaluator.print_report()"
        },
        {
            id: 4,
            title: "物流路线优化",
            difficulty: "medium",
            timeLimit: 20,
            description: "实现简单的车辆路线规划。\\n\\n**要求**：\\n1. 计算两点间距离\\n2. 寻找最短配送路线\\n3. 计算总配送距离",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 物流路线优化\\nimport math\\nfrom itertools import permutations\\n\\ndef calculate_distance(point1, point2):\\n    '''计算两点间距离（欧氏距离）''',\\n    x1, y1 = point1\\n    x2, y2 = point2\\n    return math.sqrt((x2-x1)**2 + (y2-y1)**2)\\n\\ndef find_shortest_route(depot, customers):\\n    '''寻找最短路线（旅行商问题简化版）''',\\n    n = len(customers)\\n    shortest_distance = float('inf')\\n    best_route = None\\n    \\n    # 尝试所有可能的路线\\n    for perm in permutations(range(n)):\\n        total_distance = 0\\n        # 从仓库出发\\n        current = depot\\n        for idx in perm:\\n            total_distance += calculate_distance(current, customers[idx])\\n            current = customers[idx]\\n        # 返回仓库\\n        total_distance += calculate_distance(current, depot)\\n        \\n        if total_distance < shortest_distance:\\n            shortest_distance = total_distance\\n            best_route = perm\\n    \\n    return best_route, shortest_distance\\n\\ndef print_route(depot, customers, route):\\n    '''打印路线''',\\n    print('最佳配送路线:')\\n    print(f'仓库 → ', end='')\\n    for idx in route:\\n        print(f'客户{idx+1} → ', end='')\\n    print('仓库')\\n\\n# 测试数据\\ndepot = (0, 0)  # 仓库坐标\\ncustomers = [(10, 5), (3, 8), (15, 3)]  # 客户坐标\\n\\nroute, distance = find_shortest_route(depot, customers)\\nprint_route(depot, customers, route)\\nprint(f'总配送距离: {distance:.2f}')"
        },
        {
            id: 5,
            title: "供应链综合分析",
            difficulty: "hard",
            timeLimit: 30,
            description: "综合分析供应链各环节，发现优化机会。\\n\\n**要求**：\\n1. 整合需求预测、库存、供应商、物流数据\\n2. 识别供应链瓶颈\\n3. 提供整体优化建议",
            initialCode: "# 请编写代码\\n",
            sampleSolution: "# 供应链综合分析系统\\nclass SupplyChainAnalyzer:\\n    def __init__(self):\\n        self.demand_data = []\\n        self.inventory_data = {}\\n        self.supplier_data = []\\n        self.logistics_data = []\\n    \\n    def load_demand(self, sales):\\n        self.demand_data = sales\\n    \\n    def load_inventory(self, inventory):\\n        self.inventory_data = inventory\\n    \\n    def load_suppliers(self, suppliers):\\n        self.supplier_data = suppliers\\n    \\n    def analyze_demand(self):\\n        if not self.demand_data:\\n            return None\\n        avg_demand = sum(self.demand_data) / len(self.demand_data)\\n        variability = max(self.demand_data) - min(self.demand_data)\\n        return {'average': avg_demand, 'variability': variability}\\n    \\n    def analyze_inventory(self):\\n        if not self.inventory_data:\\n            return None\\n        total_stock = sum(self.inventory_data.values())\\n        turnover_rate = avg_demand * 12 / total_stock if total_stock &gt; 0 else 0\\n        return {'total_stock': total_stock, 'turnover_rate': turnover_rate}\\n    \\n    def identify_bottlenecks(self):\\n        bottlenecks = []\\n        demand_analysis = self.analyze_demand()\\n        \\n        if demand_analysis and demand_analysis['variability'] &gt; demand_analysis['average'] * 0.5:\\n            bottlenecks.append('需求波动大')\\n        \\n        if self.inventory_data.get('A产品', 0) &lt; 50:\\n            bottlenecks.append('A产品库存偏低')\\n        \\n        return bottlenecks\\n    \\n    def generate_report(self):\\n        print('=' * 60)\\n        print('供应链综合分析报告')\\n        print('=' * 60)\\n        \\n        demand_analysis = self.analyze_demand()\\n        if demand_analysis:\\n            print('\\\\n1. 需求分析:')\\n            print(f'   平均需求: {demand_analysis[\"average\"]:.1f}')\\n            print(f'   需求波动: {demand_analysis[\"variability\"]:.1f}')\\n        \\n        bottlenecks = self.identify_bottlenecks()\\n        print('\\\\n2. 瓶颈识别:')\\n        if bottlenecks:\\n            for b in bottlenecks:\\n                print(f'   - {b}')\\n        else:\\n            print('   未发现明显瓶颈')\\n        \\n        print('\\\\n3. 优化建议:')\\n        print('   - 加强需求预测准确性')\\n        print('   - 优化安全库存水平')\\n        print('   - 建立供应商备选方案')\\n        print('=' * 60)\\n\\n# 使用示例\\nanalyzer = SupplyChainAnalyzer()\\nanalyzer.load_demand([100, 110, 95, 120, 105, 115, 130, 125])\\nanalyzer.load_inventory({'A产品': 45, 'B产品': 100, 'C产品': 80})\\nanalyzer.generate_report()"
        }
    ];

    // 选择题数据
    const choiceQuestions = [
        {
            id: 'c1',
            chapter: 1,
            title: "供应链概念",
            difficulty: "easy",
            description: "供应链管理的英文缩写是？",
            options: [
                "SCM",
                "CRM",
                "ERP",
                "MRP"
            ],
            correctIndex: 0,
            explanation: "SCM是Supply Chain Management(供应链管理)的缩写。"
        },
        {
            id: 'c2',
            chapter: 1,
            title: "供应链目标",
            difficulty: "medium",
            description: "供应链管理的核心目标是？",
            options: [
                "降低成本",
                "提高速度",
                "总成本最小化和服务水平最大化",
                "增加库存"
            ],
            correctIndex: 2,
            explanation: "供应链管理的核心目标是在总成本最小化的同时实现服务水平最大化。"
        },
        {
            id: 'c3',
            chapter: 2,
            title: "需求预测方法",
            difficulty: "easy",
            description: "以下哪种是定性预测方法？",
            options: [
                "移动平均法",
                "指数平滑法",
                "德尔菲法",
                "回归分析法"
            ],
            correctIndex: 2,
            explanation: "德尔菲法是定性预测方法，其他都是定量方法。"
        },
        {
            id: 'c4',
            chapter: 2,
            title: "预测误差",
            difficulty: "medium",
            description: "MAE指的是？",
            options: [
                "平均绝对误差",
                "均方误差",
                "平均绝对百分比误差",
                "均方根误差"
            ],
            correctIndex: 0,
            explanation: "MAE是Mean Absolute Error(平均绝对误差)的缩写。"
        },
        {
            id: 'c5',
            chapter: 3,
            title: "ABC分类法",
            difficulty: "easy",
            description: "ABC分类法中，A类物品通常？",
            options: [
                "数量多，价值低",
                "数量少，价值高",
                "数量和价值都适中",
                "数量少，价值低"
            ],
            correctIndex: 1,
            explanation: "ABC分类中A类是数量少但价值高的重要物品，需要重点管理。"
        },
        {
            id: 'c6',
            chapter: 3,
            title: "安全库存",
            difficulty: "medium",
            description: "安全库存主要用于应对？",
            options: [
                "期望需求",
                "需求波动和供应不确定性",
                "固定订货量",
                "周期性需求"
            ],
            correctIndex: 1,
            explanation: "安全库存用于缓冲需求波动和供应不确定性带来的风险。"
        },
        {
            id: 'c7',
            chapter: 4,
            title: "供应商关系",
            difficulty: "medium",
            description: "与少数关键供应商建立长期合作关系称为？",
            options: [
                "交易型关系",
                "伙伴型关系",
                "竞争型关系",
                "分散型关系"
            ],
            correctIndex: 1,
            explanation: "伙伴型关系强调与关键供应商建立长期深度合作。"
        },
        {
            id: 'c8',
            chapter: 5,
            title: "物流模式",
            difficulty: "easy",
            description: "第三方物流的英文是？",
            options: [
                "1PL",
                "2PL",
                "3PL",
                "4PL"
            ],
            correctIndex: 2,
            explanation: "3PL是Third Party Logistics(第三方物流)的缩写。"
        },
        {
            id: 'c9',
            chapter: 5,
            title: "配送策略",
            difficulty: "medium",
            description: "JIT配送的主要特点是？",
            options: [
                "大批量少频次",
                "小批量多频次",
                "按周配送",
                "按月配送"
            ],
            correctIndex: 1,
            explanation: "JIT(准时制)配送特点是小批量、多频次，降低库存。"
        },
        {
            id: 'c10',
            chapter: 6,
            title: "供应链新技术",
            difficulty: "medium",
            description: "以下哪项技术常用于供应链可视化和追溯？",
            options: [
                "区块链",
                "虚拟现实",
                "增强现实",
                "量子计算"
            ],
            correctIndex: 0,
            explanation: "区块链技术提供了不可篡改的数据记录，适合供应链追溯。"
        }
    ];
'''

# 章节导航HTML模板
DB_CHAPTERS_HTML = '''            <h2 class="section-title">数据库原理题库</h2>

            <!-- 章节列表 -->
            <div class="space-y-6">
              <!-- 章节1：数据库基础概念 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  数据库基础概念
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item active" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">数据库基本概念</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c1')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">数据模型概念</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">数据库系统组成</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节2：关系数据库理论 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  关系数据库理论
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">关系代数运算</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">关系完整性</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节3：SQL语言 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  SQL语言
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询实现</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL语言分类</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询语法</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节4：数据库设计 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  数据库设计
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/1</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">规范化设计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节5：数据库管理 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  数据库管理
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/4</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(3)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">3</div>
                    <div class="flex-1">
                      <div class="font-medium">事务ACID特性</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(4)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">4</div>
                    <div class="flex-1">
                      <div class="font-medium">索引结构实现</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">事务特性</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
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
                </div>
              </div>

              <!-- 章节6：数据库应用开发 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter6')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"></i>
                  数据库应用开发
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter6-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">数据库综合应用</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">数据库设计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

BI_CHAPTERS_HTML = '''            <h2 class="section-title">商务智能题库</h2>

            <!-- 章节列表 -->
            <div class="space-y-6">
              <!-- 章节1：商务智能基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  商务智能基础
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item active" onclick="loadChoiceQuestion('c1')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">BI概念</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">BI系统目标</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节2：数据仓库设计 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  数据仓库设计
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">数据仓库维度建模</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">ETL过程实现</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">数据仓库特点</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">星型模型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">缓慢变化维</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节3：OLAP分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  OLAP分析
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
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
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">OLAP操作</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">MOLAP与ROLAP</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节4：数据可视化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  数据可视化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
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
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">数据可视化</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节5：商业决策支持 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  商业决策支持
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
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
                  <div class="problem-item" onclick="loadChoiceQuestion('c9')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">I</div>
                    <div class="flex-1">
                      <div class="font-medium">KPI指标</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节6：综合项目实践 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter6')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"></i>
                  综合项目实践
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/1</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter6-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">BI发展趋势</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

SC_CHAPTERS_HTML = '''            <h2 class="section-title">供应链分析题库</h2>

            <!-- 章节列表 -->
            <div class="space-y-6">
              <!-- 章节1：供应链管理基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  供应链管理基础
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item active" onclick="loadChoiceQuestion('c1')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链概念</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链目标</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节2：需求预测分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  需求预测分析
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">需求预测分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">需求预测方法</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">预测误差</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节3：库存优化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  库存优化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">库存优化管理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">ABC分类法</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">安全库存</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节4：供应商评估 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  供应商评估
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(3)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">3</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商评估分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商关系</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节5：物流优化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  物流优化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(4)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">4</div>
                    <div class="flex-1">
                      <div class="font-medium">物流路线优化</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">物流模式</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c9')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">I</div>
                    <div class="flex-1">
                      <div class="font-medium">配送策略</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 章节6：综合案例分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter6')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"></i>
                  综合案例分析
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter6-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链综合分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链新技术</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''


def update_html_file(file_path, new_data, new_chapters):
    """更新单个HTML文件"""
    print(f'正在更新: {file_path}')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 更新 problems 和 choiceQuestions 数组
    old_problems_start = content.find('    // 问题数据\n    const problems = [')
    old_choices_end = content.find('    // 初始化\n    const', old_problems_start)
    
    # 替换整个数据部分
    before_data = content[:old_problems_start]
    after_data = content[old_choices_end:]
    content = before_data + new_data + after_data
    
    # 2. 更新章节导航部分
    # 找到题库标签页中的章节标题开始处
    old_title_start = content.find('<h2 class="section-title">', content.find('题库标签页'))
    right_comment_start = content.find('<!-- 右侧：问题、代码编辑器、运行结果、答案解析 -->', old_title_start)
    
    content = content[:old_title_start] + new_chapters + content[right_comment_start:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'完成: {file_path}\n')


def main():
    print('='*60)
    print('开始更新课程题库')
    print('='*60)
    
    # 更新数据库原理
    update_html_file(
        'database-principles.html',
        DB_PRINCIPLES_DATA,
        DB_CHAPTERS_HTML
    )
    
    # 更新商务智能
    update_html_file(
        'business-intelligence.html',
        BUSINESS_INTELLIGENCE_DATA,
        BI_CHAPTERS_HTML
    )
    
    # 更新供应链分析
    update_html_file(
        'supply-chain-analysis.html',
        SUPPLY_CHAIN_DATA,
        SC_CHAPTERS_HTML
    )
    
    print('='*60)
    print('所有课程更新完成！')
    print('='*60)


if __name__ == '__main__':
    main()
