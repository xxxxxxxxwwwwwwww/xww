
with open('customer-clustering.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改页面标题
content = content.replace('&lt;title&gt;购物篮分析 - Xww的课程页面&lt;/title&gt;',
                        '&lt;title&gt;客户聚类分析 - Xww的课程页面&lt;/title&gt;')

# 2. 修改考试链接
content = content.replace('market-basket-analysis-exam.html',
                        'customer-clustering-exam.html')

# 3. 更新题库章节标题
content = content.replace('购物篮分析题库', '客户聚类分析题库')
content = content.replace('购物篮分析基础', '聚类分析基础')
content = content.replace('Apriori算法', '高级聚类应用')
content = content.replace('结果可视化与应用', '聚类结果应用')

# 4. 更新知识模块导航按钮
content = content.replace('模块1：购物篮分析基础', '模块1：聚类分析基础')
content = content.replace('module1-overview', 'module1-clustering-basics')
content = content.replace('模块2：Apriori算法', '模块2：高级聚类应用')
content = content.replace('module2-apriori', 'module2-advanced-clustering')
content = content.replace('模块3：结果可视化与应用', '模块3：聚类结果应用')
content = content.replace('module3-visualization', 'module3-clustering-applications')

# 5. 更新图标和内容
content = content.replace('&lt;i class="fa fa-shopping-cart"&gt;&lt;/i&gt;', 
                         '&lt;i class="fa fa-users"&gt;&lt;/i&gt;')
content = content.replace('&lt;i class="fa fa-code-fork"&gt;&lt;/i&gt;', 
                         '&lt;i class="fa fa-layer-group"&gt;&lt;/i&gt;')
content = content.replace('&lt;i class="fa fa-bar-chart"&gt;&lt;/i&gt;', 
                         '&lt;i class="fa fa-chart-pie"&gt;&lt;/i&gt;')

# 更新问题标题和描述
content = content.replace('问题1：交易数据加载与探索', '问题1：客户数据加载与探索')
content = content.replace('问题2：支持度与置信度计算', '问题2：K-Means聚类实现')
content = content.replace('问题3：Apriori频繁项集挖掘', '问题3：层次聚类与DBSCAN')

with open('customer-clustering.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('File updated successfully!')
