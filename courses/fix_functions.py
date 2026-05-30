
with open('customer-clustering.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 修复函数部分
old_functions = '''    // 获取知识点章节ID
    function getKnowledgeSection(chapter) {
      const sections = {
        1: 'module1-clustering-basics',
        2: 'module2-demand',
        3: 'module3-inventory',
        4: 'module4-logistics',
        5: 'module5-analysis',
        6: 'module6-risk'
      };
      return sections[chapter] || 'module1-clustering-basics';
    }

    // 获取章节名称
    function getChapterName(chapter) {
      const names = {
        1: '供应链概述',
        2: '需求预测',
        3: '库存管理',
        4: '物流优化',
        5: '供应链数据分析',
        6: '供应链风险与优化'
      };
      return names[chapter] || '供应链分析';
    }'''

new_functions = '''    // 获取知识点章节ID
    function getKnowledgeSection(chapter) {
      const sections = {
        1: 'module1-clustering-basics',
        2: 'module2-advanced-clustering',
        3: 'module3-clustering-applications'
      };
      return sections[chapter] || 'module1-clustering-basics';
    }

    // 获取章节名称
    function getChapterName(chapter) {
      const names = {
        1: '聚类分析基础',
        2: '高级聚类应用',
        3: '聚类结果应用'
      };
      return names[chapter] || '聚类分析';
    }'''

html = html.replace(old_functions, new_functions)

# 同时修复选择题的数据结构
# 让我们也更新一下选择题中的chapter字段
old_choice_data1 = "    const choiceQuestions = {"
# 让我们确保选择题有正确的chapter字段
# 我们需要检查并更新choiceQuestions

# 写入文件
with open('customer-clustering.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('函数修复完成！')
