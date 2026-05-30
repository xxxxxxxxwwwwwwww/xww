
# 读取原始购物篮分析文件作为模板
with open('market-basket-analysis.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 进行主要替换
html = html.replace('购物篮分析', '客户聚类分析')
html = html.replace('market-basket-analysis-exam.html', 'customer-clustering-exam.html')
html = html.replace('module1-overview', 'module1-clustering-basics')
html = html.replace('module2-apriori', 'module2-advanced-clustering')
html = html.replace('module3-visualization', 'module3-clustering-applications')
html = html.replace('fa-shopping-cart', 'fa-users')
html = html.replace('fa-code-fork', 'fa-layer-group')
html = html.replace('fa-bar-chart', 'fa-chart-pie')

# 替换知识点内容
old_module1 = '''
            &lt;!-- 模块1：购物篮分析基础 --&gt;
            &lt;div id="module1-overview" class="knowledge-section"&gt;
              &lt;div class="bg-dark-gray rounded-xl p-6 border border-gray-700"&gt;
                &lt;h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2"&gt;
                  &lt;i class="fa fa-shopping-cart"&gt;&lt;/i&gt; 模块1：购物篮分析基础（8学时）
                &lt;/h3&gt;
                
                &lt;div class="grid md:grid-cols-2 gap-6"&gt;
                  &lt;!-- 购物篮分析概述 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-lightbulb-o text-yellow-400"&gt;&lt;/i&gt; 购物篮分析概述
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;购物篮分析（Market Basket Analysis）是一种数据挖掘技术，用于发现顾客购买的商品之间的关联关系。通过分析交易数据，找出哪些商品经常被一起购买，从而为商品摆放、促销策略等提供决策依据。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;🎯 核心应用&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;商品陈列优化、交叉销售、促销设计、库存管理、推荐系统等&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;📈 经典案例&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;啤酒与尿布的故事：超市发现周五下午买尿布的顾客常买啤酒&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
transactions = [
    ['面包', '牛奶'],
    ['面包', '牛奶', '啤酒'],
    ['牛奶', '尿布'],
]

support_A_B = 1/3  # 0.333
confidence_A_B = 1/2  # 0.5 (面包→牛奶)
support_B = 2/3
lift_A_B = 0.5 / (2/3)  # 0.75

print(f"支持度: {support_A_B:.3f}")
print(f"置信度: {confidence_A_B:.3f}")
print(f"提升度: {lift_A_B:.3f}")
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;

                  &lt;!-- 关联规则指标 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-link text-emerald-400"&gt;&lt;/i&gt; 关联规则指标
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;关联规则是形如 X→Y 的表达式，X称为前件，Y称为后件。关键指标包括支持度、置信度和提升度。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-2 flex items-center gap-2"&gt;
                          &lt;span&gt;📊&lt;/span&gt; 支持度 (Support)
                        &lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;Support(X→Y) = P(X∩Y)&lt;/p&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;表示同时购买X和Y的交易比例。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-2 flex items-center gap-2"&gt;
                          &lt;span&gt;🔗&lt;/span&gt; 置信度 (Confidence)
                        &lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;Confidence(X→Y) = P(Y|X)&lt;/p&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;表示购买X的顾客中购买Y的比例。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-pink-400 font-semibold mb-1"&gt;🎯 提升度 (Lift)&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;Lift(X→Y) = Confidence(X→Y) / P(Y)&lt;/p&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;表示关联规则的强度，&gt;1表示正相关。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

new_module1 = '''
            &lt;!-- 模块1：聚类分析基础 --&gt;
            &lt;div id="module1-clustering-basics" class="knowledge-section"&gt;
              &lt;div class="bg-dark-gray rounded-xl p-6 border border-gray-700"&gt;
                &lt;h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2"&gt;
                  &lt;i class="fa fa-users"&gt;&lt;/i&gt; 模块1：聚类分析基础（8学时）
                &lt;/h3&gt;
                
                &lt;div class="grid md:grid-cols-2 gap-6"&gt;
                  &lt;!-- 聚类分析概述 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-lightbulb-o text-yellow-400"&gt;&lt;/i&gt; 聚类分析概述
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;聚类分析（Clustering Analysis）是一种无监督学习技术，用于将相似的数据点分组到同一簇中。客户聚类通过分析客户特征，将客户划分为不同群体，帮助企业进行精准营销。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;🎯 核心应用&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;客户细分、精准营销、产品推荐、风险评估、用户画像等&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;📈 经典案例&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;RFM模型：通过最近购买、频率、金额将客户分为不同价值群体&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
import numpy as np
from sklearn.cluster import KMeans

# 客户特征数据：[消费金额, 消费频率, 最近购买天数]
customers = np.array([
    [1000, 10, 5],   # 高价值活跃客户
    [500, 5, 15],    # 中等价值客户
    [100, 2, 30],    # 低价值客户
    [2000, 20, 3],   # 高价值超级客户
    [300, 8, 20],    # 中等活跃客户
])

# K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(customers)

print("客户聚类结果:", labels)
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;

                  &lt;!-- 聚类算法指标 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-link text-emerald-400"&gt;&lt;/i&gt; 聚类评估指标
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;聚类评估主要关注簇内紧凑性和簇间分离度。关键指标包括轮廓系数、Davies-Bouldin指数和Calinski-Harabasz指数。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-2 flex items-center gap-2"&gt;
                          &lt;span&gt;📊&lt;/span&gt; 轮廓系数 (Silhouette)
                        &lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;范围[-1, 1]，越接近1表示聚类效果越好&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-2 flex items-center gap-2"&gt;
                          &lt;span&gt;🔗&lt;/span&gt; 肘部法则 (Elbow Method)
                        &lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;用于确定最佳聚类数K的方法&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-pink-400 font-semibold mb-1"&gt;🎯 距离度量&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;欧氏距离、曼哈顿距离、余弦相似度等&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

html = html.replace(old_module1, new_module1)

# 替换模块2
old_module2 = '''
            &lt;!-- 模块2：Apriori算法 --&gt;
            &lt;div id="module2-apriori" class="knowledge-section hidden"&gt;
              &lt;div class="bg-dark-gray rounded-xl p-6 border border-gray-700"&gt;
                &lt;h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2"&gt;
                  &lt;i class="fa fa-code-fork"&gt;&lt;/i&gt; 模块2：Apriori算法（8学时）
                &lt;/h3&gt;
                
                &lt;div class="grid md:grid-cols-2 gap-6"&gt;
                  &lt;!-- Apriori算法原理 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-lightbulb-o text-yellow-400"&gt;&lt;/i&gt; Apriori原理
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;Apriori算法是关联规则挖掘的经典算法，基于"频繁项集的所有非空子集也必须是频繁的"这一先验性质。算法通过逐层搜索的方式发现所有频繁项集。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;🔍 核心思想&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;如果一个项集是频繁的，那么它的所有子集也一定是频繁的；反之，如果一个项集是非频繁的，那么它的所有超集也一定是非频繁的。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;📋 算法步骤&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;1. 扫描数据库，生成1-项集；2. 迭代生成候选集并剪枝；3. 扫描数据库计算支持度；4. 重复直到没有新的频繁项集。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
# Apriori算法核心流程
transactions = [
    {'面包', '牛奶', '鸡蛋'},
    {'面包', '牛奶'},
    {'牛奶', '鸡蛋', '饼干'},
    {'面包', '饼干'},
    {'面包', '牛奶', '鸡蛋', '饼干'}
]

# 最小支持度阈值
min_support = 0.4

# 步骤1: 生成1-项集
def create_c1(transactions):
    c1 = []
    for transaction in transactions:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    return list(map(frozenset, c1))

c1 = create_c1(transactions)
print("1-项候选集:", c1)

# 步骤2: 扫描数据库计算支持度
def scan_db(transactions, ck, min_support):
    item_count = {}
    for transaction in transactions:
        for candidate in ck:
            if candidate.issubset(transaction):
                item_count[candidate] = item_count.get(candidate, 0) + 1
    
    num_transactions = float(len(transactions))
    frequent_itemsets = []
    support_data = {}
    
    for key in item_count:
        support = item_count[key] / num_transactions
        if support &gt;= min_support:
            frequent_itemsets.insert(0, key)
        support_data[key] = support
    
    return frequent_itemsets, support_data

L1, support_data = scan_db(transactions, c1, min_support)
print("1-项频繁集:", L1)
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;

                  &lt;!-- 关联规则生成 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-link text-emerald-400"&gt;&lt;/i&gt; 关联规则生成
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;从频繁项集中生成关联规则，需要满足最小置信度阈值。规则的形式为X→Y，其中X和Y是不相交的项集。&lt;/p&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
# 生成关联规则
def generate_rules(frequent_itemsets, support_data, min_conf=0.7):
    big_rule_list = []
    for i in range(1, len(frequent_itemsets)):
        for freq_set in frequent_itemsets[i]:
            H1 = [frozenset([item]) for item in freq_set]
            if (i &gt; 1):
                rules_from_conseq(freq_set, H1, support_data, big_rule_list, min_conf)
            else:
                calc_conf(freq_set, H1, support_data, big_rule_list, min_conf)
    return big_rule_list

def calc_conf(freq_set, H, support_data, brl, min_conf):
    pruned_H = []
    for conseq in H:
        conf = support_data[freq_set] / support_data[freq_set - conseq]
        if conf &gt;= min_conf:
            print(freq_set - conseq, '-&gt;', conseq, 'conf:', conf)
            brl.append((freq_set - conseq, conseq, conf))
            pruned_H.append(conseq)
    return pruned_H

# 示例：生成规则
# 假设有频繁项集L2, L3等
# rules = generate_rules([L1, L2, L3], support_data, min_conf=0.7)

# 计算提升度
def calculate_lift(support_XY, support_X, support_Y):
    """计算提升度"""
    return support_XY / (support_X * support_Y)

# 示例：计算提升度
support_milk_bread = 0.4  # 牛奶和面包同时出现的概率
support_milk = 0.8        # 牛奶出现的概率
support_bread = 0.6       # 面包出现的概率
lift = calculate_lift(support_milk_bread, support_milk, support_bread)
print(f"面包 -&gt; 牛奶 的提升度: {lift:.3f}")
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

new_module2 = '''
            &lt;!-- 模块2：高级聚类应用 --&gt;
            &lt;div id="module2-advanced-clustering" class="knowledge-section hidden"&gt;
              &lt;div class="bg-dark-gray rounded-xl p-6 border border-gray-700"&gt;
                &lt;h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2"&gt;
                  &lt;i class="fa fa-layer-group"&gt;&lt;/i&gt; 模块2：高级聚类应用（8学时）
                &lt;/h3&gt;
                
                &lt;div class="grid md:grid-cols-2 gap-6"&gt;
                  &lt;!-- K-Means算法原理 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-lightbulb-o text-yellow-400"&gt;&lt;/i&gt; K-Means算法原理
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;K-Means是最经典的聚类算法，通过迭代更新簇中心来最小化簇内平方和。算法简单高效，适合大规模客户数据聚类。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;🔍 核心思想&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;1. 随机选择K个初始簇中心；2. 将每个样本分配到最近的簇；3. 重新计算每个簇的中心；4. 重复直到收敛。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;📋 优缺点&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;优点：简单高效、易解释；缺点：需预先指定K、对初始值敏感、对异常值敏感。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
# K-Means核心实现
import numpy as np

def k_means(data, k, max_iter=100):
    # 1. 随机初始化簇中心
    centroids = data[np.random.choice(len(data), k, replace=False)]
    
    for _ in range(max_iter):
        # 2. 分配样本到最近的簇
        distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        
        # 3. 更新簇中心
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # 4. 检查收敛
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids

# 客户数据
customer_data = np.array([
    [1000, 10], [500, 5], [100, 2], 
    [2000, 20], [300, 8], [1500, 15]
])

labels, centers = k_means(customer_data, k=3)
print("聚类结果:", labels)
print("簇中心:", centers)
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;

                  &lt;!-- 其他聚类算法 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-link text-emerald-400"&gt;&lt;/i&gt; 其他聚类算法
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;除了K-Means，还有层次聚类、DBSCAN、高斯混合模型等多种聚类算法，各有适用场景。&lt;/p&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# DBSCAN：基于密度的聚类，能发现任意形状的簇
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(customer_data)

# 层次聚类：构建聚类树
hierarchical = AgglomerativeClustering(n_clusters=3)
hier_labels = hierarchical.fit_predict(customer_data)

# 高斯混合模型：概率模型，能给出样本属于各簇的概率
gmm = GaussianMixture(n_components=3, random_state=42)
gmm_labels = gmm.fit_predict(customer_data)
gmm_probs = gmm.predict_proba(customer_data)

print("DBSCAN标签:", dbscan_labels)
print("GMM概率:", gmm_probs.round(3))
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

html = html.replace(old_module2, new_module2)

# 替换模块3
old_module3 = '''
            &lt;!-- 模块3：结果可视化与应用 --&gt;
            &lt;div id="module3-visualization" class="knowledge-section hidden"&gt;
              &lt;div class="bg-dark-gray rounded-xl p-6 border border-gray-700"&gt;
                &lt;h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2"&gt;
                  &lt;i class="fa fa-bar-chart"&gt;&lt;/i&gt; 模块3：结果可视化与应用（8学时）
                &lt;/h3&gt;
                
                &lt;div class="grid md:grid-cols-2 gap-6"&gt;
                  &lt;!-- 关联规则可视化 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-pie-chart text-yellow-400"&gt;&lt;/i&gt; 关联规则可视化
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;将购物篮分析的结果以直观的图表形式展示，帮助业务人员理解商品之间的关联关系，支持决策制定。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;📊 网络图&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;用节点表示商品，边表示商品之间的关联，边的粗细表示支持度或置信度。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;📈 热力图&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;用颜色深浅表示商品组合的支持度或置信度，便于快速发现强关联。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
import pandas as pd

# 创建关联规则数据
rules_data = {
    'antecedent': ['面包', '牛奶', '鸡蛋', '面包', '饼干'],
    'consequent': ['牛奶', '面包', '牛奶', '鸡蛋', '牛奶'],
    'support': [0.4, 0.4, 0.3, 0.3, 0.2],
    'confidence': [0.8, 0.5, 0.75, 0.6, 0.5],
    'lift': [1.33, 0.83, 1.25, 1.0, 0.83]
}

rules_df = pd.DataFrame(rules_data)

print("关联规则表:")
print(rules_df)

# 筛选强关联规则
strong_rules = rules_df[(rules_df['support'] &gt;= 0.3) &amp; 
                        (rules_df['confidence'] &gt;= 0.6) &amp; 
                        (rules_df['lift'] &gt; 1)]
print("\\n强关联规则:")
print(strong_rules[['antecedent', 'consequent', 'support', 'confidence', 'lift']])

# 按提升度排序
sorted_rules = rules_df.sort_values('lift', ascending=False)
print("\\n按提升度排序:")
print(sorted_rules[['antecedent', 'consequent', 'lift']])
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;

                  &lt;!-- 业务应用场景 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-lightbulb-o text-emerald-400"&gt;&lt;/i&gt; 业务应用场景
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;购物篮分析在零售、电商、餐饮等行业有广泛应用，帮助企业优化营销策略、提升销售业绩。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;🛒 商品推荐&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;根据购物篮分析结果，为客户推荐关联商品，实现交叉销售。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;🏬 货架摆放&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;将关联度高的商品放在相邻位置，方便顾客购买。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-pink-400 font-semibold mb-1"&gt;🎯 促销活动&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;针对关联商品设计捆绑销售、满减优惠等促销活动。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
# 购物篮分析应用示例
def recommend_products(cart, rules, top_n=3):
    """
    根据购物篮和关联规则推荐商品
    """
    recommendations = []
    
    for _, rule in rules.iterrows():
        antecedent = set(rule['antecedent'].split(','))
        if antecedent.issubset(set(cart)):
            consequent = rule['consequent']
            if consequent not in cart:
                recommendations.append({
                    'product': consequent,
                    'confidence': rule['confidence'],
                    'lift': rule['lift']
                })
    
    # 按置信度和提升度排序
    recommendations.sort(key=lambda x: (x['confidence'], x['lift']), reverse=True)
    return recommendations[:top_n]

# 示例：购物车中有面包和鸡蛋
cart = ['面包', '鸡蛋']
recommendations = recommend_products(cart, rules_df)

print(f"当前购物篮: {cart}")
print("推荐商品:")
for rec in recommendations:
    print(f"  - {rec['product']} (置信度: {rec['confidence']:.2f}, 提升度: {rec['lift']:.2f})")
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

new_module3 = '''
            &lt;!-- 模块3：聚类结果应用 --&gt;
            &lt;div id="module3-clustering-applications" class="knowledge-section hidden"&gt;
              &lt;div class="bg-dark-gray rounded-xl p-6 border border-gray-700"&gt;
                &lt;h3 class="text-2xl font-bold text-cyan-400 mb-6 flex items-center gap-2"&gt;
                  &lt;i class="fa fa-chart-pie"&gt;&lt;/i&gt; 模块3：聚类结果应用（8学时）
                &lt;/h3&gt;
                
                &lt;div class="grid md:grid-cols-2 gap-6"&gt;
                  &lt;!-- 聚类结果可视化 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-pie-chart text-yellow-400"&gt;&lt;/i&gt; 聚类结果可视化
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;将客户聚类结果以直观图表展示，帮助业务人员理解不同客户群体的特征，支持营销决策。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;📊 散点图/气泡图&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;用不同颜色表示簇，点的大小表示客户价值，直观展示客户分布。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;📈 雷达图&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;展示各客户群在多维度特征上的差异，便于对比分析。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 客户数据与聚类结果
customer_df = pd.DataFrame({
    '消费金额': [1000, 500, 100, 2000, 300, 1500],
    '消费频率': [10, 5, 2, 20, 8, 15],
    '最近购买': [5, 15, 30, 3, 20, 7],
    '簇标签': [0, 1, 2, 0, 1, 0]
})

# 可视化聚类结果
plt.figure(figsize=(10, 6))
scatter = plt.scatter(customer_df['消费金额'], 
                     customer_df['消费频率'],
                     c=customer_df['簇标签'], 
                     cmap='viridis', s=100)
plt.xlabel('消费金额')
plt.ylabel('消费频率')
plt.title('客户聚类结果可视化')
plt.legend(*scatter.legend_elements(), title='客户群')
plt.colorbar(label='簇标签')
plt.grid(True, alpha=0.3)
plt.show()

# 各簇统计特征
cluster_stats = customer_df.groupby('簇标签').agg({
    '消费金额': 'mean',
    '消费频率': 'mean',
    '最近购买': 'mean'
}).round(2)
print("各客户群特征:")
print(cluster_stats)
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;

                  &lt;!-- 业务应用场景 --&gt;
                  &lt;div class="bg-dark p-5 rounded-lg border border-gray-700"&gt;
                    &lt;h4 class="text-lg font-semibold text-gray-200 mb-3 flex items-center gap-2"&gt;
                      &lt;i class="fa fa-lightbulb-o text-emerald-400"&gt;&lt;/i&gt; 业务应用场景
                    &lt;/h4&gt;
                    &lt;p class="text-gray-300 mb-4 text-sm leading-relaxed"&gt;客户聚类在电商、零售、金融、电信等行业有广泛应用，帮助企业实现精准营销和个性化服务。&lt;/p&gt;
                    
                    &lt;div class="space-y-3 mb-4"&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-emerald-400 font-semibold mb-1"&gt;🎯 精准营销&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;针对不同客户群设计差异化营销策略，提高营销ROI。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-yellow-400 font-semibold mb-1"&gt;💎 客户价值分层&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;识别高价值客户，提供VIP服务，进行重点维护。&lt;/p&gt;
                      &lt;/div&gt;
                      &lt;div class="bg-dark-gray p-3 rounded-lg"&gt;
                        &lt;h5 class="text-pink-400 font-semibold mb-1"&gt;🔮 流失预警&lt;/h5&gt;
                        &lt;p class="text-gray-400 text-sm"&gt;识别有流失风险的客户群，提前进行干预挽留。&lt;/p&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    
                    &lt;div class="bg-dark p-3 rounded font-mono text-sm"&gt;
                      &lt;pre class="text-cyan-300"&gt;
# RFM客户价值分析
def rfm_analysis(customer_data):
    """
    RFM模型：Recency最近购买, Frequency消费频率, Monetary消费金额
    """
    rfm = customer_data.copy()
    
    # 评分（5分制）
    rfm['R_score'] = pd.qcut(rfm['最近购买'], 5, labels=[5,4,3,2,1])
    rfm['F_score'] = pd.qcut(rfm['消费频率'], 5, labels=[1,2,3,4,5])
    rfm['M_score'] = pd.qcut(rfm['消费金额'], 5, labels=[1,2,3,4,5])
    
    # 合并RFM分数
    rfm['RFM_Score'] = rfm['R_score'].astype(str) + \
                      rfm['F_score'].astype(str) + \
                      rfm['M_score'].astype(str)
    
    # 客户群定义
    def segment_customer(row):
        if row['R_score'] &gt;= 4 and row['F_score'] &gt;= 4 and row['M_score'] &gt;= 4:
            return '高价值客户'
        elif row['R_score'] &gt;= 4 and row['F_score'] &gt;= 3:
            return '潜力客户'
        elif row['R_score'] &lt;= 2:
            return '流失风险客户'
        else:
            return '一般客户'
    
    rfm['客户群'] = rfm.apply(segment_customer, axis=1)
    return rfm

# 应用RFM分析
rfm_results = rfm_analysis(customer_df)
print("RFM分析结果:")
print(rfm_results[['消费金额', '消费频率', '最近购买', 'RFM_Score', '客户群']])
                      &lt;/pre&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt;
'''

html = html.replace(old_module3, new_module3)

# 现在更新JavaScript中的题目数据
old_problems_start = "  &lt;script&gt;\n    // 问题数据\n    const problems = ["
old_problems_end = "    // 选择题数据"

# 让我们创建新的题目数据
new_problems = '''  &lt;script&gt;
    // 问题数据
    const problems = [
      {
        id: 1,
        title: "问题1：客户数据加载与探索",
        description: `编写一个程序，加载客户数据并进行初步探索分析。
&lt;strong&gt;输入：&lt;/strong&gt;
客户数据集（包含消费金额、频率、最近购买等特征）
&lt;strong&gt;输出：&lt;/strong&gt;
数据统计信息和基本分析结果
&lt;strong&gt;要求：&lt;/strong&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;加载客户数据&lt;/li&gt;
  &lt;li&gt;统计客户数量和特征分布&lt;/li&gt;
  &lt;li&gt;分析客户价值分布&lt;/li&gt;
  &lt;li&gt;计算基本统计量&lt;/li&gt;
&lt;/ul&gt;`,
        difficulty: "easy",
        time: "20分钟",
        code: `# 请编写代码`,
        analysis: `
&lt;h4&gt;解题思路&lt;/h4&gt;
&lt;p&gt;1. 使用Pandas加载客户数据&lt;/p&gt;
&lt;p&gt;2. 统计基本信息：客户数、特征数、缺失值等&lt;/p&gt;
&lt;p&gt;3. 使用describe()分析数据分布&lt;/p&gt;
&lt;p&gt;4. 可视化关键特征&lt;/p&gt;
&lt;h4&gt;代码示例&lt;/h4&gt;
&lt;div class="bg-dark p-3 rounded-lg font-mono text-sm"&gt;
  &lt;pre class="text-cyan-300"&gt;
import pandas as pd
import numpy as np

# 客户数据
customer_data = {
    '客户ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    '消费金额': [1000, 500, 100, 2000, 300, 1500, 800, 600, 200, 1200],
    '消费频率': [10, 5, 2, 20, 8, 15, 12, 7, 3, 18],
    '最近购买': [5, 15, 30, 3, 20, 7, 10, 18, 25, 4],
    '客单价': [100, 100, 50, 100, 37.5, 100, 66.7, 85.7, 66.7, 66.7]
}

df = pd.DataFrame(customer_data)

# 基本统计
print("数据形状:", df.shape)
print("\\n数据预览:")
print(df.head())
print("\\n统计描述:")
print(df.describe())

# 客户价值分层
df['价值分层'] = pd.qcut(df['消费金额'], 3, labels=['低', '中', '高'])
print("\\n客户价值分布:")
print(df['价值分层'].value_counts())

# 计算RFM基础指标
print("\\n平均消费金额:", df['消费金额'].mean().round(2))
print("平均消费频率:", df['消费频率'].mean().round(2))
print("平均最近购买天数:", df['最近购买'].mean().round(2))
  &lt;/pre&gt;
&lt;/div&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module1-clustering-basics')"&gt;聚类分析基础&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;数据探索分析&lt;/li&gt;
  &lt;li&gt;描述性统计&lt;/li&gt;
&lt;/ul&gt;`
      },
      {
        id: 2,
        title: "问题2：K-Means聚类实现",
        description: `编写一个程序，实现K-Means聚类算法对客户进行分群。
&lt;strong&gt;输入：&lt;/strong&gt;
客户特征数据
&lt;strong&gt;输出：&lt;/strong&gt;
客户聚类结果和簇中心
&lt;strong&gt;要求：&lt;/strong&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;使用肘部法则确定K值&lt;/li&gt;
  &lt;li&gt;实现K-Means聚类&lt;/li&gt;
  &lt;li&gt;分析各客户群特征&lt;/li&gt;
&lt;/ul&gt;`,
        difficulty: "medium",
        time: "25分钟",
        code: `# 请编写代码`,
        analysis: `
&lt;h4&gt;解题思路&lt;/h4&gt;
&lt;p&gt;1. 数据标准化处理&lt;/p&gt;
&lt;p&gt;2. 使用肘部法则确定最佳聚类数&lt;/p&gt;
&lt;p&gt;3. 应用K-Means聚类&lt;/p&gt;
&lt;p&gt;4. 分析各簇特征&lt;/p&gt;
&lt;h4&gt;代码示例&lt;/h4&gt;
&lt;div class="bg-dark p-3 rounded-lg font-mono text-sm"&gt;
  &lt;pre class="text-cyan-300"&gt;
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 客户数据
X = np.array([
    [1000, 10, 5], [500, 5, 15], [100, 2, 30],
    [2000, 20, 3], [300, 8, 20], [1500, 15, 7],
    [800, 12, 10], [600, 7, 18], [200, 3, 25], [1200, 18, 4]
])

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 肘部法则确定K值
inertias = []
K_range = range(1, 10)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# 选择K=3进行聚类
kmeans_final = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans_final.fit_predict(X_scaled)
centers = scaler.inverse_transform(kmeans_final.cluster_centers_)

# 结果分析
df = pd.DataFrame(X, columns=['消费金额', '消费频率', '最近购买'])
df['簇标签'] = labels

print("聚类结果:")
print(df)
print("\\n簇中心:")
print(pd.DataFrame(centers, columns=['消费金额', '消费频率', '最近购买']))
print("\\n各簇客户数:")
print(df['簇标签'].value_counts().sort_index())
  &lt;/pre&gt;
&lt;/div&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module2-advanced-clustering')"&gt;K-Means算法&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;数据标准化&lt;/li&gt;
  &lt;li&gt;肘部法则&lt;/li&gt;
&lt;/ul&gt;`
      },
      {
        id: 3,
        title: "问题3：层次聚类与DBSCAN",
        description: `编写一个程序，使用层次聚类和DBSCAN进行客户分群。
&lt;strong&gt;输入：&lt;/strong&gt;
客户特征数据
&lt;strong&gt;输出：&lt;/strong&gt;
不同算法的聚类结果对比
&lt;strong&gt;要求：&lt;/strong&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;实现层次聚类&lt;/li&gt;
  &lt;li&gt;实现DBSCAN聚类&lt;/li&gt;
  &lt;li&gt;对比不同算法结果&lt;/li&gt;
&lt;/ul&gt;`,
        difficulty: "medium",
        time: "30分钟",
        code: `# 请编写代码`,
        analysis: `
&lt;h4&gt;解题思路&lt;/h4&gt;
&lt;p&gt;1. 使用不同聚类算法&lt;/p&gt;
&lt;p&gt;2. 比较聚类结果差异&lt;/p&gt;
&lt;p&gt;3. 评估各算法适用性&lt;/p&gt;
&lt;h4&gt;代码示例&lt;/h4&gt;
&lt;div class="bg-dark p-3 rounded-lg font-mono text-sm"&gt;
  &lt;pre class="text-cyan-300"&gt;
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 客户数据
X = np.array([
    [1000, 10, 5], [500, 5, 15], [100, 2, 30],
    [2000, 20, 3], [300, 8, 20], [1500, 15, 7],
    [800, 12, 10], [600, 7, 18], [200, 3, 25], [1200, 18, 4]
])

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 层次聚类
hier_clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
hier_labels = hier_clustering.fit_predict(X_scaled)

# DBSCAN聚类
dbscan = DBSCAN(eps=0.8, min_samples=2)
dbscan_labels = dbscan.fit_predict(X_scaled)

# 结果对比
results = pd.DataFrame({
    '原始索引': range(len(X)),
    '层次聚类': hier_labels,
    'DBSCAN': dbscan_labels
})

print("聚类结果对比:")
print(results)
print("\\n层次聚类 - 各簇大小:")
print(pd.Series(hier_labels).value_counts().sort_index())
print("\\nDBSCAN - 各簇大小 (-1表示噪声):")
print(pd.Series(dbscan_labels).value_counts().sort_index())

# 轮廓系数评估
if len(set(hier_labels)) &gt; 1:
    hier_silhouette = silhouette_score(X_scaled, hier_labels)
    print(f"\\n层次聚类轮廓系数: {hier_silhouette:.3f}")

valid_dbscan_labels = dbscan_labels[dbscan_labels != -1]
if len(set(valid_dbscan_labels)) &gt; 1:
    dbscan_silhouette = silhouette_score(X_scaled[dbscan_labels != -1], valid_dbscan_labels)
    print(f"DBSCAN轮廓系数: {dbscan_silhouette:.3f}")
  &lt;/pre&gt;
&lt;/div&gt;
&lt;h4&gt;知识点&lt;/h4&gt;
&lt;ul class="list-disc list-inside space-y-1 mt-2"&gt;
  &lt;li&gt;&lt;a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('module2-advanced-clustering')"&gt;高级聚类算法&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;层次聚类&lt;/li&gt;
  &lt;li&gt;DBSCAN&lt;/li&gt;
  &lt;li&gt;聚类评估&lt;/li&gt;
&lt;/ul&gt;`
      }
    ]

    // 选择题数据
'''

# 写入新文件
with open('customer-clustering.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("客户聚类分析页面生成成功！")
