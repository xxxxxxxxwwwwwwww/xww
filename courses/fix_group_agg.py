#!/usr/bin/env python3
# 修复分组聚合分析课程文件

import re

# 读取购物篮分析模板
with open('/workspace/courses/market-basket-analysis.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 更新页面标题
content = content.replace('购物篮分析 - Xww的课程页面', '分组聚合分析 - Xww的课程页面')

# 2. 更新考试链接
content = content.replace('market-basket-analysis-exam.html', 'group-aggregation-exam.html')

# 3. 更新题库标题
content = content.replace('购物篮分析题库', '分组聚合分析题库')

# 4. 更新知识点导航按钮
content = content.replace('模块1：购物篮分析基础', '模块1：分组聚合基础')
content = content.replace('模块2：Apriori算法', '模块2：高级聚合分析')
content = content.replace('模块3：结果可视化与应用', '模块3：业务应用与案例')

# 5. 更新模块ID
content = content.replace('data-target="module1-overview"', 'data-target="module1-basics"')
content = content.replace('data-target="module2-apriori"', 'data-target="module2-advanced"')
content = content.replace('data-target="module3-visualization"', 'data-target="module3-applications"')

content = content.replace('id="module1-overview"', 'id="module1-basics"')
content = content.replace('id="module2-apriori"', 'id="module2-advanced"')
content = content.replace('id="module3-visualization"', 'id="module3-applications"')

# 6. 更新模块标题
content = content.replace('<i class="fa fa-shopping-cart"></i> 模块1：购物篮分析基础', '<i class="fa fa-table"></i> 模块1：分组聚合基础')
content = content.replace('<i class="fa fa-link"></i> 模块2：Apriori算法', '<i class="fa fa-bar-chart"></i> 模块2：高级聚合分析')
content = content.replace('<i class="fa fa-line-chart"></i> 模块3：结果可视化与应用', '<i class="fa fa-pie-chart"></i> 模块3：业务应用与案例')

# 7. 更新模块内容简介
content = content.replace('购物篮分析（Market Basket Analysis）是一种数据挖掘技术，用于发现顾客购买的商品之间的关联关系', '分组聚合分析是数据分析中的核心技术，用于按指定维度对数据进行分组并进行聚合计算')
content = content.replace('关联规则学习、Apriori算法、频繁项集挖掘', 'groupby操作、聚合函数、透视表')
content = content.replace('商品推荐、交叉销售、促销策略', '数据汇总、统计分析、业务报表')

# 8. 更新编程题数据
content = content.replace('问题1：数据加载与探索', '问题1：数据加载与分组')
content = content.replace('问题2：支持度与置信度计算', '问题2：聚合函数使用')
content = content.replace('问题3：Apriori算法实现', '问题3：多维度聚合')
content = content.replace('问题4：关联规则生成', '问题4：透视表与交叉表')

# 9. 更新选择题内容
content = content.replace('选择题1：购物篮分析概念', '选择题1：分组聚合概念')
content = content.replace('购物篮分析主要用于发现什么？', '分组聚合分析的主要作用是什么？')
content = content.replace('商品之间的关联关系', '数据按维度分组后的聚合统计')
content = content.replace('选择题2：支持度概念', '选择题2：groupby概念')
content = content.replace('支持度(Support)表示什么？', 'groupby的作用是什么？')
content = content.replace('同时购买X和Y的交易比例', '按指定列对数据进行分组')
content = content.replace('选择题3：置信度概念', '选择题3：聚合函数')
content = content.replace('置信度(Confidence)表示什么？', '以下哪个不是常用的聚合函数？')
content = content.replace('购买X的顾客中购买Y的概率', 'sort()')
content = content.replace('选择题4：Apriori原理', '选择题4：多列分组')
content = content.replace('Apriori算法的核心原理是什么？', '如何进行多列分组？')
content = content.replace('频繁项集的子集也是频繁的', 'df.groupby([\'列1\', \'列2\'])')
content = content.replace('选择题5：提升度含义', '选择题5：透视表')
content = content.replace('当提升度(Lift)大于1时，表示什么？', 'pivot_table的作用是什么？')
content = content.replace('X和Y是正相关的', '创建数据透视表')
content = content.replace('选择题6：业务应用', '选择题6：agg方法')
content = content.replace('购物篮分析最常见的业务应用是什么？', 'agg()方法的作用是什么？')
content = content.replace('商品推荐和交叉销售', '同时应用多个聚合函数')
content = content.replace('选择题7：货架摆放', '选择题7：transform')
content = content.replace('根据购物篮分析结果，关联度高的商品应该如何摆放？', 'transform()方法的特点是什么？')
content = content.replace('放在相邻位置', '保持原数据形状')
content = content.replace('选择题8：可视化方法', '选择题8：业务应用')
content = content.replace('以下哪种可视化方法最适合展示商品关联关系？', '分组聚合最常见的业务应用是什么？')
content = content.replace('网络图', '生成统计报表')

# 10. 更新选择题解析内容
content = content.replace('购物篮分析是一种数据挖掘技术', '分组聚合分析是数据分析的核心技术')
content = content.replace('支持度(Support(X→Y)) = P(X∩Y)', 'groupby用于按指定列分组数据')
content = content.replace('置信度(Confidence(X→Y)) = P(Y|X)', '常用聚合函数包括sum、mean、count等')
content = content.replace('Apriori算法基于先验原理', '多列分组使用列表形式')
content = content.replace('提升度(Lift) > 1表示X和Y是正相关的', 'pivot_table用于创建数据透视表')
content = content.replace('购物篮分析最常见的应用是商品推荐', 'agg()可以同时应用多个聚合函数')
content = content.replace('将关联度高的商品放在相邻位置', 'transform()保持原数据形状')

# 11. 更新getKnowledgeSection和getChapterName函数
content = content.replace("1: 'module1-overview'", "1: 'module1-basics'")
content = content.replace("2: 'module2-demand'", "2: 'module2-advanced'")
content = content.replace("3: 'module3-inventory'", "3: 'module3-applications'")

content = content.replace("1: '供应链概述'", "1: '分组聚合基础'")
content = content.replace("2: '需求预测'", "2: '高级聚合分析'")
content = content.replace("3: '库存管理'", "3: '业务应用与案例'")
content = content.replace("return names[chapter] || '供应链分析'", "return names[chapter] || '分组聚合分析'")

# 写入文件
with open('/workspace/courses/group-aggregation.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("分组聚合分析课程文件已修复完成！")