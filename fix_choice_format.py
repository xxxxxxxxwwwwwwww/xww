#!/usr/bin/env python3
"""
修复选择题格式和隐藏代码编辑器中的代码
"""

from pathlib import Path

file_path = Path('/workspace/courses/data-analysis-tech.html')

# 读取文件
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复选择题数据格式
# 将简单字符串数组改为包含label和text的对象数组
new_choice_questions = '''    const choiceQuestions = [
      // 第一章：NumPy数组基础
      {
        id: 'chapter1_0',
        question: '在NumPy中，创建数组的基本函数是？',
        options: [
          {label: 'A', text: 'array()'},
          {label: 'B', text: 'create()'},
          {label: 'C', text: 'make()'},
          {label: 'D', text: 'new()'}
        ],
        answer: 'A',
        explanation: 'NumPy使用np.array()函数创建数组。',
        difficulty: 'easy',
        chapter: 1,
        title: 'NumPy基础知识'
      },
      {
        id: 'chapter2_0',
        question: 'NumPy数组的哪个属性返回数组的维度数？',
        options: [
          {label: 'A', text: 'size'},
          {label: 'B', text: 'shape'},
          {label: 'C', text: 'ndim'},
          {label: 'D', text: 'dtype'}
        ],
        answer: 'C',
        explanation: 'ndim属性返回数组的维度数，shape返回形状，size返回元素总数，dtype返回数据类型。',
        difficulty: 'easy',
        chapter: 2,
        title: 'NumPy高级特性'
      },
      {
        id: 'chapter3_0',
        question: 'Pandas中用于存储一维数据的结构是？',
        options: [
          {label: 'A', text: 'DataFrame'},
          {label: 'B', text: 'Series'},
          {label: 'C', text: 'Panel'},
          {label: 'D', text: 'Table'}
        ],
        answer: 'B',
        explanation: 'Series是Pandas的一维数据结构，DataFrame是二维的表格结构。',
        difficulty: 'easy',
        chapter: 3,
        title: 'Pandas数据结构'
      },
      {
        id: 'chapter4_0',
        question: '读取CSV文件使用的Pandas函数是？',
        options: [
          {label: 'A', text: 'pd.load_csv()'},
          {label: 'B', text: 'pd.read_csv()'},
          {label: 'C', text: 'pd.open_csv()'},
          {label: 'D', text: 'pd.import_csv()'}
        ],
        answer: 'B',
        explanation: '使用pd.read_csv()函数读取CSV文件。',
        difficulty: 'easy',
        chapter: 4,
        title: '文件格式选择'
      },
      {
        id: 'chapter5_0',
        question: 'DataFrame中缺失值的表示方法是？',
        options: [
          {label: 'A', text: 'null'},
          {label: 'B', text: 'None'},
          {label: 'C', text: 'NaN'},
          {label: 'D', text: 'NA'}
        ],
        answer: 'C',
        explanation: 'NumPy和Pandas使用NaN（Not a Number）表示缺失值。',
        difficulty: 'easy',
        chapter: 5,
        title: '数据清洗方法'
      },
      {
        id: 'chapter6_0',
        question: '哪个方法可以计算DataFrame的描述性统计？',
        options: [
          {label: 'A', text: 'df.summary()'},
          {label: 'B', text: 'df.describe()'},
          {label: 'C', text: 'df.statistics()'},
          {label: 'D', text: 'df.analyze()'}
        ],
        answer: 'B',
        explanation: 'describe()方法提供数据的计数、均值、标准差、最小值、最大值和分位数等统计信息。',
        difficulty: 'medium',
        chapter: 6,
        title: '探索性分析技术'
      },
      {
        id: 'chapter7_0',
        question: '在数据可视化中，折线图最适合展示什么类型的数据？',
        options: [
          {label: 'A', text: '分类比较'},
          {label: 'B', text: '趋势变化'},
          {label: 'C', text: '部分与整体关系'},
          {label: 'D', text: '数据分布'}
        ],
        answer: 'B',
        explanation: '折线图最适合展示数据随时间变化的趋势。',
        difficulty: 'easy',
        chapter: 7,
        title: '可视化最佳实践'
      },
      {
        id: 'chapter8_0',
        question: '在Pandas中，按列分组聚合使用的方法是？',
        options: [
          {label: 'A', text: 'df.sort()'},
          {label: 'B', text: 'df.filter()'},
          {label: 'C', text: 'df.groupby()'},
          {label: 'D', text: 'df.aggregate()'}
        ],
        answer: 'C',
        explanation: 'groupby()方法用于按一个或多个列分组，然后进行聚合计算。',
        difficulty: 'medium',
        chapter: 8,
        title: '聚合函数'
      },
      {
        id: 'chapter9_0',
        question: '将字符串转换为日期时间的Pandas函数是？',
        options: [
          {label: 'A', text: 'pd.to_date()'},
          {label: 'B', text: 'pd.to_datetime()'},
          {label: 'C', text: 'pd.parse_date()'},
          {label: 'D', text: 'pd.date_convert()'}
        ],
        answer: 'B',
        explanation: 'pd.to_datetime()函数将字符串或其他格式转换为datetime类型。',
        difficulty: 'medium',
        chapter: 9,
        title: '时间序列方法'
      },
      {
        id: 'chapter10_0',
        question: '在机器学习中，将数据划分为训练集和测试集的目的是？',
        options: [
          {label: 'A', text: '减少数据量'},
          {label: 'B', text: '提高计算速度'},
          {label: 'C', text: '评估模型泛化能力'},
          {label: 'D', text: '简化数据结构'}
        ],
        answer: 'C',
        explanation: '使用训练集训练模型，测试集评估模型的泛化能力。',
        difficulty: 'medium',
        chapter: 10,
        title: '机器学习概念'
      }
    ];'''

# 替换选择题数据
import re
pattern = r'const choiceQuestions = \[.*?\];'
content = re.sub(pattern, new_choice_questions, content, flags=re.DOTALL)

# 2. 隐藏代码编辑器中的代码，只显示 "# 请编写代码"
# 找到所有的 code 字段并替换
content = re.sub(r"'code': `[^`]+`", "'code': `# 请编写代码\\n`", content)
content = re.sub(r'code: `[^`]+`', 'code: `# 请编写代码\\n`', content)

# 写入文件
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成！")
print("1. 选择题格式已修复")
print("2. 代码编辑器中的代码已隐藏，只显示 '# 请编写代码'")
