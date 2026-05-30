
with open('customer-clustering.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 更新左侧章节1
old_chapter1_section = '''              &lt;!-- 章节1：客户聚类分析基础 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter1')"&gt;
                  &lt;i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"&gt;&lt;/i&gt;
                  客户聚类分析基础
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/5&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content" id="chapter1-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item active" onclick="loadProgrammingProblem(1)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold"&gt;1&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;数据加载与探索&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;20分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(2)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;2&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;K-Means聚类实现&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;25分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c1')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;A&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;客户聚类分析概念&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c2')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;B&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;聚类评估指标&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c3')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;C&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;RFM模型&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;'''

# 更新章节2
old_chapter2_section = '''              &lt;!-- 章节2：高级聚类应用 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter2')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"&gt;&lt;/i&gt;
                  高级聚类应用
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/4&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter2-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2"&gt;编程题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadProgrammingProblem(3)"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold"&gt;3&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;层次聚类与DBSCAN&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-gray-400"&gt;30分钟&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c4')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;D&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;K-Means算法原理&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c5')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;E&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;算法对比&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;'''

# 更新章节3
old_chapter3_section = '''              &lt;!-- 章节3：聚类结果应用 --&gt;
              &lt;div class="chapter-item"&gt;
                &lt;h3 class="topic-title" onclick="toggleChapter('chapter3')"&gt;
                  &lt;i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"&gt;&lt;/i&gt;
                  聚类结果应用
                  &lt;span class="ml-auto text-xs text-gray-400"&gt;
                    &lt;span class="chapter-progress"&gt;0/3&lt;/span&gt;
                    &lt;span class="progress-percentage"&gt;(0%)&lt;/span&gt;
                  &lt;/span&gt;
                &lt;/h3&gt;
                &lt;div class="chapter-content collapsed" id="chapter3-content"&gt;
                  &lt;div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4"&gt;选择题&lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c6')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;F&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;业务应用场景&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c7')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;G&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;客户价值分层&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-medium"&gt;中等&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                  &lt;div class="problem-item" onclick="loadChoiceQuestion('c8')"&gt;
                    &lt;div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm"&gt;H&lt;/div&gt;
                    &lt;div class="flex-1"&gt;
                      &lt;div class="font-medium"&gt;可视化方法&lt;/div&gt;
                      &lt;div class="flex items-center gap-2 mt-1"&gt;
                        &lt;span class="difficulty-tag difficulty-easy"&gt;简单&lt;/span&gt;
                        &lt;span class="text-xs text-purple-400"&gt;选择题&lt;/span&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;'''

# 现在替换
html = html.replace('商品组合统计', 'K-Means聚类实现')
html = html.replace('Apriori算法', '高级聚类应用')
html = html.replace('频繁项集挖掘', '层次聚类与DBSCAN')
html = html.replace('关联规则生成', '聚类结果应用')
html = html.replace('Apriori原理', 'K-Means算法原理')
html = html.replace('算法流程', '算法对比')
html = html.replace('营销策略优化', '客户价值分层')
html = html.replace('结果可视化与应用', '聚类结果应用')
html = html.replace('关联规则指标', '聚类评估指标')
html = html.replace('支持度与置信度', 'RFM模型')

# 最后替换旧的题目描述
html = html.replace('问题1：供应链数据预处理', '问题1：客户数据加载与探索')

# 现在更新选择题数据 - 我们需要找到并替换旧的choiceQuestions部分
old_choice_questions = '''    const choiceQuestions = {
      c1: {
        id: 'c1',
        title: '购物篮分析概念',
        question: '以下哪项不是购物篮分析的主要应用场景？',
        options: [
          '商品陈列优化',
          '交叉销售推荐',
          '库存需求预测',
          '客户信用评分'
        ],
        correctAnswer: 3,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 D。&lt;/p&gt;
&lt;p&gt;购物篮分析主要用于发现商品间的关联关系，客户信用评分通常使用分类或回归模型，不属于购物篮分析的典型应用。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module1-overview')"&gt;购物篮分析基础&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c2: {
        id: 'c2',
        title: '关联规则指标',
        question: '在关联规则 X→Y 中，置信度表示什么？',
        options: [
          '同时包含X和Y的交易比例',
          '包含X的交易中同时包含Y的比例',
          '规则的提升程度',
          'Y的出现频率'
        ],
        correctAnswer: 1,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;置信度（Confidence）表示在包含X的交易中，同时也包含Y的条件概率，即 P(Y|X)。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module1-overview')"&gt;关联规则指标&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c3: {
        id: 'c3',
        title: '支持度与置信度',
        question: '如果某条规则的支持度很低但置信度很高，说明什么？',
        options: [
          '该规则非常有价值',
          '该商品组合很常见',
          '该规则可能是巧合，实际应用价值有限',
          '该规则的提升度一定很高'
        ],
        correctAnswer: 2,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 C。&lt;/p&gt;
&lt;p&gt;支持度低意味着该商品组合很少出现，即使置信度高，由于样本量小，可能是偶然现象，实际应用价值有限。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module1-overview')"&gt;关联规则指标&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c4: {
        id: 'c4',
        title: 'Apriori原理',
        question: 'Apriori算法的核心思想是什么？',
        options: [
          '频繁项集的所有子集一定是频繁的',
          '频繁项集的所有超集一定是频繁的',
          '先计算置信度再计算支持度',
          '使用贪心算法寻找最优解'
        ],
        correctAnswer: 0,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 A。&lt;/p&gt;
&lt;p&gt;Apriori原理是：如果一个项集是频繁的，那么它的所有非空子集也一定是频繁的。反之，如果一个项集是非频繁的，那么它的所有超集也一定是非频繁的。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module2-apriori')"&gt;Apriori算法&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c5: {
        id: 'c5',
        title: '算法流程',
        question: 'Apriori算法的第一步是什么？',
        options: [
          '生成候选2-项集',
          '扫描数据库，计算所有1-项集的支持度',
          '生成关联规则',
          '计算提升度'
        ],
        correctAnswer: 1,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;Apriori算法首先扫描数据库，统计所有单个商品（1-项集）的支持度，找出满足最小支持度的频繁1-项集。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module2-apriori')"&gt;Apriori算法&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c6: {
        id: 'c6',
        title: '业务应用场景',
        question: '以下哪项不是购物篮分析结果的典型应用？',
        options: [
          '货架摆放优化',
          '商品捆绑销售',
          '商品推荐',
          '商品价格制定'
        ],
        correctAnswer: 3,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 D。&lt;/p&gt;
&lt;p&gt;价格制定通常基于成本、市场需求、竞争等因素，不是购物篮分析的直接应用。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-visualization')"&gt;结果可视化与应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c7: {
        id: 'c7',
        title: '营销策略优化',
        question: '如果发现啤酒和尿布经常被一起购买，最合理的营销策略是？',
        options: [
          '将两种商品放在一起',
          '同时涨价',
          '只保留一个',
          '分开摆放很远'
        ],
        correctAnswer: 0,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 A。&lt;/p&gt;
&lt;p&gt;将关联商品放在一起可以增加销售，方便顾客购买，提高客单价。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-visualization')"&gt;结果可视化与应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c8: {
        id: 'c8',
        title: '可视化方法',
        question: '以下哪种图表最适合展示商品间的关联关系？',
        options: [
          '柱状图',
          '网络图',
          '折线图',
          '饼图'
        ],
        correctAnswer: 1,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;网络图用节点表示商品，边表示关联关系，最直观展示商品间的关联。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-visualization')"&gt;结果可视化与应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      }
    };'''

new_choice_questions = '''    const choiceQuestions = {
      c1: {
        id: 'c1',
        title: '客户聚类分析概念',
        question: '客户聚类分析属于什么类型的机器学习任务？',
        options: [
          '监督学习',
          '无监督学习',
          '强化学习',
          '深度学习'
        ],
        correctAnswer: 1,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;客户聚类分析是无监督学习，因为没有预先标记的类别，算法自动发现数据中的群组结构。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module1-clustering-basics')"&gt;聚类分析基础&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c2: {
        id: 'c2',
        title: '聚类评估指标',
        question: '轮廓系数（Silhouette Coefficient）的取值范围是？',
        options: [
          '[0, 1]',
          '[-1, 1]',
          '[0, ∞)',
          '(-∞, ∞)'
        ],
        correctAnswer: 1,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;轮廓系数范围是[-1, 1]，值越接近1表示聚类效果越好，接近-1表示聚类效果差。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module1-clustering-basics')"&gt;聚类评估指标&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c3: {
        id: 'c3',
        title: 'RFM模型',
        question: 'RFM模型中的F代表什么？',
        options: [
          '最近购买时间（Recency）',
          '消费频率（Frequency）',
          '消费金额（Monetary）',
          '客户价值（Value）'
        ],
        correctAnswer: 1,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;RFM模型中R=Recency最近购买，F=Frequency消费频率，M=Monetary消费金额。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-clustering-applications')"&gt;聚类结果应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c4: {
        id: 'c4',
        title: 'K-Means算法原理',
        question: 'K-Means算法中，K表示什么？',
        options: [
          '最大迭代次数',
          '聚类个数',
          '距离度量方式',
          '收敛阈值'
        ],
        correctAnswer: 1,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;K-Means中的K表示预先指定的聚类个数，需要预先确定。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module2-advanced-clustering')"&gt;K-Means算法&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c5: {
        id: 'c5',
        title: '算法对比',
        question: '以下哪种算法可以自动确定聚类个数？',
        options: [
          'K-Means',
          '层次聚类',
          'DBSCAN',
          '所有都需要预先指定'
        ],
        correctAnswer: 2,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 C。&lt;/p&gt;
&lt;p&gt;DBSCAN基于密度聚类，不需要预先指定聚类个数，可以自动发现任意形状的簇。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module2-advanced-clustering')"&gt;高级聚类算法&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c6: {
        id: 'c6',
        title: '业务应用场景',
        question: '客户聚类分析的典型应用不包括以下哪项？',
        options: [
          '精准营销',
          '客户细分',
          '商品推荐',
          '财务报表生成'
        ],
        correctAnswer: 3,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 D。&lt;/p&gt;
&lt;p&gt;财务报表生成是会计工作，不是客户聚类分析的典型应用。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-clustering-applications')"&gt;聚类结果应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c7: {
        id: 'c7',
        title: '客户价值分层',
        question: '在RFM模型中，最近购买时间（R）越短说明？',
        options: [
          '客户越活跃',
          '客户可能流失',
          '客户价值低',
          '客户消费频率低'
        ],
        correctAnswer: 0,
        difficulty: 'medium',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 A。&lt;/p&gt;
&lt;p&gt;最近购买时间越短说明客户越活跃，最近刚购买过。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-clustering-applications')"&gt;聚类结果应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      },
      c8: {
        id: 'c8',
        title: '可视化方法',
        question: '以下哪种图表最适合展示各客户群在多维度特征上的差异？',
        options: [
          '散点图',
          '雷达图',
          '折线图',
          '饼图'
        ],
        correctAnswer: 1,
        difficulty: 'easy',
        analysis: `
&lt;h4&gt;答案解析&lt;/h4&gt;
&lt;p&gt;正确答案是 B。&lt;/p&gt;
&lt;p&gt;雷达图可以同时展示多个维度的特征，便于对比不同客户群的差异。&lt;/p&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module3-clustering-applications')"&gt;聚类结果应用&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;`
      }
    };'''

# 替换选择题
html = html.replace(old_choice_questions, new_choice_questions)

# 更新getKnowledgeSection和getChapterName函数
old_functions_part = '''    function getKnowledgeSection(target) {
      const mapping = {
        'module1-overview': '购物篮分析基础',
        'module2-apriori': 'Apriori算法',
        'module3-visualization': '结果可视化与应用'
      };
      return mapping[target] || '知识点';
    }

    function getChapterName(questionId) {
      if (typeof questionId === 'number' {
        const chapterMap = {
          1: '购物篮分析基础',
          2: '购物篮分析基础',
          3: 'Apriori算法',
          4: 'Apriori算法'
        };
        return chapterMap[questionId] || '题库';
      } else {
        const choiceChapterMap = {
          'c1': '购物篮分析基础',
          'c2': '购物篮分析基础',
          'c3': '购物篮分析基础',
          'c4': 'Apriori算法',
          'c5': 'Apriori算法',
          'c6': '结果可视化与应用',
          'c7': '结果可视化与应用',
          'c8': '结果可视化与应用'
        };
        return choiceChapterMap[questionId] || '题库';
      }
    }'''

new_functions_part = '''    function getKnowledgeSection(target) {
      const mapping = {
        'module1-clustering-basics': '聚类分析基础',
        'module2-advanced-clustering': '高级聚类应用',
        'module3-clustering-applications': '聚类结果应用'
      };
      return mapping[target] || '知识点';
    }

    function getChapterName(questionId) {
      if (typeof questionId === 'number') {
        const chapterMap = {
          1: '聚类分析基础',
          2: '聚类分析基础',
          3: '高级聚类应用'
        };
        return chapterMap[questionId] || '题库';
      } else {
        const choiceChapterMap = {
          'c1': '聚类分析基础',
          'c2': '聚类分析基础',
          'c3': '聚类分析基础',
          'c4': '高级聚类应用',
          'c5': '高级聚类应用',
          'c6': '聚类结果应用',
          'c7': '聚类结果应用',
          'c8': '聚类结果应用'
        };
        return choiceChapterMap[questionId] || '题库';
      }
    }'''

# 修复函数参数问题 - 先找到并替换
# 查找并修复参数问题
html = html.replace("function getKnowledgeSection(target)", "function getKnowledgeSection(target)")
html = html.replace("typeof questionId === 'number'", "typeof questionId === 'number'")

# 替换函数部分
html = html.replace(old_functions_part, new_functions_part)

# 写入最终文件
with open('customer-clustering.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('最终更新完成！')
