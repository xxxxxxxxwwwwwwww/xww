#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 完全重构考试页面，复制 business-intelligence-exam.html 的成功经验

print("=== 重构考试页面 ===\n")

# 读取参考文件和目标文件
with open('business-intelligence-exam.html', 'r', encoding='utf-8') as f:
    ref_content = f.read()

with open('data-analysis-exam.html', 'r', encoding='utf-8') as f:
    exam_content = f.read()

# 定义新的考试题目数据
new_data = '''  <script>
    // 考试题目数据
    const examProblems = [
      {
        id: 1,
        title: "编程题：数据分析综合应用",
        description: `综合运用所学知识，完成一个完整的数据分析任务。

<strong>背景：</strong>
一家电商公司提供了2024年1月的销售数据，请对这份数据进行完整的分析和处理。

<strong>数据：</strong>
包含以下字段：订单ID、客户ID、订单日期、商品类别、销量、单价

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>读取并理解数据结构</li>
  <li>识别和处理数据中的缺失值和异常值</li>
  <li>计算每日、每类别的销售总额和平均单价</li>
  <li>输出分析结果</li>
</ul>`,
        difficulty: "medium",
        code: "# 请编写代码",
        answer: "",
        score: 10
      }
    ];

    // 考试选择题数据
    const examChoiceQuestions = [
      {
        id: 11,
        type: "choice",
        title: "选择题1：数据分析定义",
        question: "数据分析的核心目标是什么？",
        options: {
          A: "删除数据",
          B: "提取有用信息和形成结论",
          C: "只生成图表",
          D: "存储大量数据"
        },
        answer: "B",
        score: 10
      },
      {
        id: 12,
        type: "choice",
        title: "选择题2：CRISP-DM方法论",
        question: "CRISP-DM方法论中，哪个阶段是数据分析项目的核心？",
        options: {
          A: "业务理解",
          B: "数据理解",
          C: "数据建模",
          D: "部署实施"
        },
        answer: "C",
        score: 10
      },
      {
        id: 13,
        type: "choice",
        title: "选择题3：缺失值处理",
        question: "在Pandas中，检测缺失值的方法是？",
        options: {
          A: "df.missing()",
          B: "df.isna() 或 df.isnull()",
          C: "df.check_null()",
          D: "df.empty()"
        },
        answer: "B",
        score: 10
      },
      {
        id: 14,
        type: "choice",
        title: "选择题4：异常值检测",
        question: "使用IQR方法检测异常值时，通常使用多少倍IQR作为阈值？",
        options: {
          A: "0.5倍",
          B: "1倍",
          C: "1.5倍",
          D: "3倍"
        },
        answer: "C",
        score: 10
      },
      {
        id: 15,
        type: "choice",
        title: "选择题5：SQL查询",
        question: "SQL中，哪个关键字用于去除查询结果中的重复记录？",
        options: {
          A: "TOP",
          B: "UNIQUE",
          C: "DISTINCT",
          D: "GROUP BY"
        },
        answer: "C",
        score: 10
      },
      {
        id: 16,
        type: "choice",
        title: "选择题6：描述性统计",
        question: "描述数据集中趋势的指标不包括以下哪项？",
        options: {
          A: "均值",
          B: "中位数",
          C: "标准差",
          D: "众数"
        },
        answer: "C",
        score: 10
      },
      {
        id: 17,
        type: "choice",
        title: "选择题7：假设检验",
        question: "在假设检验中，p值表示什么？",
        options: {
          A: "原假设成立的概率",
          B: "在原假设成立的前提下，观察到当前或更极端结果的概率",
          C: "备择假设成立的概率",
          D: "犯第二类错误的概率"
        },
        answer: "B",
        score: 10
      },
      {
        id: 18,
        type: "choice",
        title: "选择题8：机器学习",
        question: "K-Means聚类算法属于哪种类型的机器学习？",
        options: {
          A: "监督学习",
          B: "无监督学习",
          C: "强化学习",
          D: "半监督学习"
        },
        answer: "B",
        score: 10
      },
      {
        id: 19,
        type: "choice",
        title: "选择题9：数据可视化",
        question: "以下哪种图表最适合展示数据的分布情况？",
        options: {
          A: "饼图",
          B: "柱状图",
          C: "直方图",
          D: "折线图"
        },
        answer: "C",
        score: 10
      }
    ];'''

# 替换题目数据部分
# 找到参考文件中的题目数据开始和结束位置
ref_start = ref_content.find('// 考试题目数据')
ref_end = ref_content.find('// 合并所有考试题目', ref_start) + len('// 合并所有考试题目')

# 找到我们文件中的题目数据部分
exam_start = exam_content.find('// 考试题目数据')
exam_end = exam_content.find('// 合并所有考试题目', exam_start) + len('// 合并所有考试题目')

# 替换题目数据
new_exam = exam_content[:exam_start] + new_data + exam_content[exam_end:]

# 写入更新后的文件
with open('data-analysis-exam.html', 'w', encoding='utf-8') as f:
    f.write(new_exam)

print("✓ 考试题目数据已更新")
print("\n=== 完成 ===")
