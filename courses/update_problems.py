import re

# 读取原始文件
with open('data-analysis-tech.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 新的题库数据
new_problems = """    const problems = [
      {
        id: 1,
        title: "问题1：数据分析流程",
        description: `编写一个程序，模拟完整的数据分析流程。

<strong>输入：</strong>
一个包含销售数据的CSV文件

<strong>输出：</strong>
分析报告摘要

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>读取数据文件</li>
  <li>数据清洗和预处理</li>
  <li>基本统计分析</li>
  <li>输出分析报告</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import pandas as pd
import numpy as np

# 模拟数据
data = {
    '日期': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    '销售额': [1000, 1500, np.nan, 1800, 2000],
    '客户数': [20, 30, 25, np.nan, 40],
    '产品类别': ['A', 'B', 'A', 'C', 'B']
}
df = pd.DataFrame(data)

# 步骤1: 数据读取与概览
print("=== 步骤1: 数据概览 ===")
print(f"数据形状: {df.shape}")
print(df.head())

# 步骤2: 数据清洗
print("\\n=== 步骤2: 数据清洗 ===")
print("缺失值统计:")
print(df.isnull().sum())

# 填充缺失值
df['销售额'] = df['销售额'].fillna(df['销售额'].mean())
df['客户数'] = df['客户数'].fillna(df['客户数'].median())
print("\\n清洗后数据:")
print(df)

# 步骤3: 统计分析
print("\\n=== 步骤3: 统计分析 ===")
print("基本统计:")
print(df.describe())

print("\\n按类别汇总:")
print(df.groupby('产品类别')['销售额'].sum())

# 步骤4: 生成报告
print("\\n=== 步骤4: 分析报告 ===")
print(f"总销售额: {df['销售额'].sum():.2f}")
print(f"日均销售额: {df['销售额'].mean():.2f}")
print(f"客户总数: {df['客户数'].sum():.0f}")`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用Pandas读取和处理数据</p>
<p>2. 识别并处理缺失值</p>
<p>3. 进行基本统计分析和分组汇总</p>
<p>4. 生成简洁的分析报告</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
import numpy as np

# 模拟数据
data = {
    '日期': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    '销售额': [1000, 1500, np.nan, 1800, 2000],
    '客户数': [20, 30, 25, np.nan, 40],
    '产品类别': ['A', 'B', 'A', 'C', 'B']
}
df = pd.DataFrame(data)

# 步骤1: 数据概览
print("=== 步骤1: 数据概览 ===")
print(f"数据形状: {df.shape}")
print(df.head())

# 步骤2: 数据清洗
df['销售额'] = df['销售额'].fillna(df['销售额'].mean())
df['客户数'] = df['客户数'].fillna(df['客户数'].median())

# 步骤3: 统计分析
print("\\n=== 步骤3: 统计分析 ===")
print(df.describe())

# 步骤4: 生成报告
print("\\n=== 步骤4: 分析报告 ===")
print(f"总销售额: {df['销售额'].sum():.2f}")
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter1-basics')">第一章：数据分析概述</a></li>
  <li>数据分析流程</li>
  <li>CRISP-DM方法论</li>
</ul>`
      },
      {
        id: 2,
        title: "问题2：缺失值处理",
        description: `编写一个程序，使用Pandas处理DataFrame中的缺失值。

<strong>输入：</strong>
一个包含缺失值的DataFrame

<strong>输出：</strong>
处理后的DataFrame，其中缺失值已被适当处理

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>识别并统计缺失值</li>
  <li>使用合适的方法填充缺失值（如均值、中位数或众数）</li>
  <li>返回处理后的DataFrame</li>
</ul>`,
        difficulty: "easy",
        time: "15分钟",
        code: `# 请编写代码
import pandas as pd
import numpy as np

# 创建示例数据
data = {
    '姓名': ['张三', '李四', '王五', np.nan, '赵六'],
    '年龄': [25, 30, np.nan, 35, 40],
    '性别': ['男', '女', '男', np.nan, '女'],
    '工资': [5000, 6000, 5500, np.nan, 7000]
}
df = pd.DataFrame(data)

# 识别缺失值
print("缺失值统计:")
print(df.isnull().sum())

# 处理缺失值
df['年龄'] = df['年龄'].fillna(df['年龄'].mean())
df['工资'] = df['工资'].fillna(df['工资'].median())
df['性别'] = df['性别'].fillna(df['性别'].mode()[0])
df['姓名'] = df['姓名'].fillna('未知')

print("\\n处理后的数据:")
print(df)`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用Pandas的isnull()和sum()方法识别并统计缺失值</p>
<p>2. 根据数据类型选择合适的填充方法：数值型数据使用均值或中位数，分类型数据使用众数</p>
<p>3. 使用fillna()方法填充缺失值</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
import numpy as np

data = {
    '姓名': ['张三', '李四', '王五', np.nan, '赵六'],
    '年龄': [25, 30, np.nan, 35, 40],
    '性别': ['男', '女', '男', np.nan, '女'],
    '工资': [5000, 6000, 5500, np.nan, 7000]
}
df = pd.DataFrame(data)

print("缺失值统计:")
print(df.isnull().sum())

df['年龄'] = df['年龄'].fillna(df['年龄'].mean())
df['工资'] = df['工资'].fillna(df['工资'].median())
df['性别'] = df['性别'].fillna(df['性别'].mode()[0])
df['姓名'] = df['姓名'].fillna('未知')
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2-preprocessing')">第二章：数据准备与清洗</a></li>
  <li>缺失值处理方法</li>
  <li>数据质量评估</li>
</ul>`
      },
      {
        id: 3,
        title: "问题3：异常值检测",
        description: `编写一个程序，使用IQR方法检测数据中的异常值。

<strong>输入：</strong>
一个包含可能异常值的数据集

<strong>输出：</strong>
检测到的异常值

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算四分位数和IQR</li>
  <li>定义异常值边界</li>
  <li>检测并返回异常值</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import pandas as pd
import numpy as np

# 创建示例数据
np.random.seed(42)
data = np.random.normal(100, 10, 100)
data = np.append(data, [50, 180, 185])  # 添加异常值
df = pd.DataFrame({'数值': data})

# 方法1: IQR检测
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_iqr = df[(df < lower_bound) | (df > upper_bound)]
print("IQR方法检测到的异常值:")
print(outliers_iqr)

# 方法2: Z-score检测
z_scores = np.abs((df - df.mean()) / df.std())
outliers_z = df[z_scores > 3]
print("\\nZ-score方法检测到的异常值:")
print(outliers_z)`,
        analysis: `
<h4>解题思路</h4>
<p>1. 计算数据的第一四分位数(Q1)和第三四分位数(Q3)</p>
<p>2. 计算四分位距(IQR) = Q3 - Q1</p>
<p>3. 定义异常值边界：下界 = Q1 - 1.5 * IQR，上界 = Q3 + 1.5 * IQR</p>
<p>4. 检测并返回超出边界的值作为异常值</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.normal(100, 10, 100)
data = np.append(data, [50, 180, 185])
df = pd.DataFrame({'数值': data})

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df < lower_bound) | (df > upper_bound)]
print("异常值:", outliers)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2-preprocessing')">第二章：数据准备与清洗</a></li>
  <li>异常值检测方法</li>
  <li>统计方法应用</li>
</ul>`
      },
      {
        id: 4,
        title: "问题4：SQL查询实战",
        description: `编写SQL查询语句，从数据库中提取所需数据。

<strong>输入：</strong>
包含订单表(orders)和客户表(customers)的数据库

<strong>输出：</strong>
查询结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>查询2024年1月的订单</li>
  <li>关联客户表获取客户信息</li>
  <li>按客户分组统计订单金额</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `-- 请编写SQL查询

-- 1. 查询2024年1月的订单
SELECT * 
FROM orders 
WHERE order_date >= '2024-01-01' AND order_date < '2024-02-01';

-- 2. 关联客户表查询订单详情
SELECT 
    o.order_id,
    o.order_date,
    o.amount,
    c.name AS customer_name,
    c.email
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date >= '2024-01-01';

-- 3. 按客户分组统计
SELECT 
    c.name AS customer_name,
    COUNT(o.order_id) AS order_count,
    SUM(o.amount) AS total_amount,
    AVG(o.amount) AS avg_amount
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
HAVING COUNT(o.order_id) > 5
ORDER BY total_amount DESC;`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用WHERE子句过滤特定日期范围的订单</p>
<p>2. 使用JOIN语句关联订单表和客户表</p>
<p>3. 使用GROUP BY分组统计，HAVING过滤分组结果</p>
<p>4. 使用ORDER BY对结果排序</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
-- 查询2024年1月订单并关联客户信息
SELECT 
    o.order_id,
    o.order_date,
    o.amount,
    c.name AS customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date >= '2024-01-01' 
  AND o.order_date < '2024-02-01';
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter3-tools')">第三章：核心工具实操</a></li>
  <li>SQL查询语法</li>
  <li>多表连接</li>
</ul>`
      },
      {
        id: 5,
        title: "问题5：描述性统计分析",
        description: `编写一个程序，对数据进行描述性统计分析。

<strong>输入：</strong>
一个包含数值型数据的DataFrame

<strong>输出：</strong>
数据的基本统计信息

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>计算基本统计量（均值、中位数、标准差等）</li>
  <li>计算相关性矩阵</li>
</ul>`,
        difficulty: "easy",
        time: "10分钟",
        code: `# 请编写代码
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '年龄': [20, 25, 30, 35, 40, 45, 50, 55],
    '收入': [5000, 6000, 8000, 10000, 12000, 15000, 18000, 20000],
    '消费': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]
})

# 基本统计信息
print("基本统计信息:")
print(df.describe())

# 中位数
print("\\n中位数:")
print(df.median())

# 标准差
print("\\n标准差:")
print(df.std())

# 相关性矩阵
print("\\n相关性矩阵:")
print(df.corr())`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用DataFrame的describe()方法获取基本统计信息</p>
<p>2. 使用median()方法计算中位数</p>
<p>3. 使用std()方法计算标准差</p>
<p>4. 使用corr()方法计算相关性矩阵</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd

df = pd.DataFrame({
    '年龄': [20, 25, 30, 35, 40],
    '收入': [5000, 6000, 8000, 10000, 12000],
    '消费': [1000, 1500, 2000, 2500, 3000]
})

print("基本统计:")
print(df.describe())
print("\\n相关性:")
print(df.corr())
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter4-statistics')">第四章：统计分析方法</a></li>
  <li>描述性统计</li>
  <li>相关性分析</li>
</ul>`
      },
      {
        id: 6,
        title: "问题6：假设检验",
        description: `编写一个程序，进行独立样本t检验。

<strong>输入：</strong>
两组独立样本数据

<strong>输出：</strong>
检验结果（t值和p值）

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>生成两组模拟数据</li>
  <li>进行独立样本t检验</li>
  <li>解释检验结果</li>
</ul>`,
        difficulty: "medium",
        time: "20分钟",
        code: `# 请编写代码
import numpy as np
from scipy import stats

# 生成两组模拟数据
np.random.seed(42)
group1 = np.random.normal(50, 10, 30)  # 对照组
group2 = np.random.normal(55, 10, 30)  # 实验组

print("组1描述统计:")
print(f"均值: {group1.mean():.2f}, 标准差: {group1.std():.2f}")

print("\\n组2描述统计:")
print(f"均值: {group2.mean():.2f}, 标准差: {group2.std():.2f}")

# 独立样本t检验
t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"\\nt值: {t_stat:.4f}")
print(f"p值: {p_value:.4f}")

# 解释结果
alpha = 0.05
if p_value < alpha:
    print(f"p值({p_value:.4f}) < α({alpha})，拒绝原假设，两组均值存在显著差异")
else:
    print(f"p值({p_value:.4f}) >= α({alpha})，接受原假设，两组均值无显著差异")`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用numpy生成两组符合正态分布的模拟数据</p>
<p>2. 使用scipy.stats.ttest_ind进行独立样本t检验</p>
<p>3. 根据p值判断是否拒绝原假设</p>
<p>4. 输出检验结果和解释</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import numpy as np
from scipy import stats

np.random.seed(42)
group1 = np.random.normal(50, 10, 30)
group2 = np.random.normal(55, 10, 30)

t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t值: {t_stat:.4f}, p值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("拒绝原假设，存在显著差异")
else:
    print("接受原假设，无显著差异")
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter4-statistics')">第四章：统计分析方法</a></li>
  <li>推断统计</li>
  <li>假设检验</li>
</ul>`
      },
      {
        id: 7,
        title: "问题7：线性回归",
        description: `编写一个程序，使用线性回归预测销售数据。

<strong>输入：</strong>
包含广告投入和销售额的数据集

<strong>输出：</strong>
回归模型和预测结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>构建线性回归模型</li>
  <li>评估模型性能</li>
  <li>进行预测</li>
</ul>`,
        difficulty: "medium",
        time: "25分钟",
        code: `# 请编写代码
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 创建示例数据
np.random.seed(42)
data = pd.DataFrame({
    '广告投入': np.linspace(1, 10, 50),
    '销售额': np.linspace(10, 100, 50) + np.random.normal(0, 5, 50)
})

X = data[['广告投入']].values
y = data['销售额'].values

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"回归系数: {model.coef_[0]:.2f}")
print(f"截距: {model.intercept_:.2f}")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

# 预测新数据
new_data = np.array([[12]])
prediction = model.predict(new_data)
print(f"\\n广告投入12万时的预测销售额: {prediction[0]:.2f}万")`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用sklearn的LinearRegression创建线性回归模型</p>
<p>2. 使用train_test_split划分训练集和测试集</p>
<p>3. 使用fit()方法训练模型</p>
<p>4. 使用predict()方法进行预测</p>
<p>5. 使用MSE和R²评估模型性能</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    '广告投入': [1, 2, 3, 4, 5],
    '销售额': [10, 20, 30, 40, 50]
})

X = data[['广告投入']]
y = data['销售额']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

print(f"系数: {model.coef_[0]:.2f}")
print(f"预测: {model.predict([[6]])[0]:.2f}")
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter4-statistics')">第四章：统计分析方法</a></li>
  <li>回归分析</li>
  <li>机器学习基础</li>
</ul>`
      },
      {
        id: 8,
        title: "问题8：K-Means聚类",
        description: `编写一个程序，使用K-Means算法对客户进行聚类分析。

<strong>输入：</strong>
包含客户消费数据的数据集

<strong>输出：</strong>
聚类结果

<strong>要求：</strong>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li>使用肘部法确定最佳K值</li>
  <li>进行K-Means聚类</li>
  <li>分析聚类结果</li>
</ul>`,
        difficulty: "hard",
        time: "30分钟",
        code: `# 请编写代码
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# 创建示例数据
np.random.seed(42)
data = pd.DataFrame({
    '消费金额': np.random.randint(100, 1000, 100),
    '购买频率': np.random.randint(1, 20, 100)
})

# 使用肘部法确定最佳K值
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(data)
    inertia.append(kmeans.inertia_)

print("不同K值的惯性:")
for k, val in enumerate(inertia, 1):
    print(f"K={k}: {val:.2f}")

# 使用K=3进行聚类
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data['聚类标签'] = kmeans.fit_predict(data)

print("\\n聚类中心:")
print(pd.DataFrame(kmeans.cluster_centers_, columns=data.columns[:-1]))

print("\\n各簇数量:")
print(data['聚类标签'].value_counts())`,
        analysis: `
<h4>解题思路</h4>
<p>1. 使用肘部法选择最佳聚类数K</p>
<p>2. 使用KMeans进行聚类</p>
<p>3. 分析聚类中心和各簇数量</p>
<p>4. 为数据添加聚类标签</p>
<h4>代码示例</h4>
<div class="bg-dark p-3 rounded-lg font-mono text-sm">
  <pre class="text-cyan-300">
import pandas as pd
from sklearn.cluster import KMeans

data = pd.DataFrame({
    '消费金额': [100, 200, 500, 800, 900],
    '购买频率': [1, 2, 5, 8, 10]
})

kmeans = KMeans(n_clusters=3, n_init=10)
data['聚类标签'] = kmeans.fit_predict(data)
print(data)
  </pre>
</div>
<h4>知识点</h4>
<ul class="list-disc list-inside space-y-1 mt-2">
  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter5-advanced')">第五章：高级数据分析方法</a></li>
  <li>聚类分析</li>
  <li>K-Means算法</li>
</ul>`
      }
    ];
"""

# 新的选择题数据
new_choice_questions = """    const choiceQuestions = [
      {
        id: 'c1',
        chapter: 1,
        title: "选择题1：数据分析定义",
        question: "数据分析的核心目标是什么？",
        options: [
          { label: 'A', text: '收集数据' },
          { label: 'B', text: '清洗数据' },
          { label: 'C', text: '提取洞察支持决策' },
          { label: 'D', text: '存储数据' }
        ],
        answer: 'C',
        analysis: "数据分析的核心目标是从数据中提取有价值的洞察，为决策提供支持。收集、清洗和存储数据都是数据分析过程中的步骤，而非最终目标。",
        difficulty: "easy"
      },
      {
        id: 'c2',
        chapter: 1,
        title: "选择题2：CRISP-DM方法论",
        question: "CRISP-DM方法论包含几个阶段？",
        options: [
          { label: 'A', text: '4个' },
          { label: 'B', text: '5个' },
          { label: 'C', text: '6个' },
          { label: 'D', text: '7个' }
        ],
        answer: 'C',
        analysis: "CRISP-DM方法论包含6个阶段：业务理解、数据理解、数据准备、建模、评估、部署。这是数据挖掘项目的标准流程。",
        difficulty: "easy"
      },
      {
        id: 'c3',
        chapter: 2,
        title: "选择题3：缺失值处理",
        question: "对于数值型数据的缺失值，以下哪种处理方法最合适？",
        options: [
          { label: 'A', text: '直接删除' },
          { label: 'B', text: '用均值或中位数填充' },
          { label: 'C', text: '用0填充' },
          { label: 'D', text: '用最大值填充' }
        ],
        answer: 'B',
        analysis: "对于数值型数据，使用均值或中位数填充缺失值是常用且合适的方法。均值适用于正态分布数据，中位数适用于偏态分布数据。",
        difficulty: "easy"
      },
      {
        id: 'c4',
        chapter: 2,
        title: "选择题4：异常值检测",
        question: "IQR方法中，异常值的判定标准是什么？",
        options: [
          { label: 'A', text: '超出均值±1倍标准差' },
          { label: 'B', text: '超出Q1-1.5×IQR或Q3+1.5×IQR' },
          { label: 'C', text: '超出均值±2倍标准差' },
          { label: 'D', text: '超出中位数±1倍IQR' }
        ],
        answer: 'B',
        analysis: "IQR方法中，异常值定义为小于Q1-1.5×IQR或大于Q3+1.5×IQR的值。Q1是第一四分位数，Q3是第三四分位数，IQR=Q3-Q1。",
        difficulty: "medium"
      },
      {
        id: 'c5',
        chapter: 3,
        title: "选择题5：SQL查询",
        question: "在SQL中，用于从多个表中获取数据的关键字是？",
        options: [
          { label: 'A', text: 'SELECT' },
          { label: 'B', text: 'JOIN' },
          { label: 'C', text: 'WHERE' },
          { label: 'D', text: 'GROUP BY' }
        ],
        answer: 'B',
        analysis: "JOIN关键字用于将两个或多个表按照共同的列连接在一起。SELECT用于选择列，WHERE用于过滤行，GROUP BY用于分组。",
        difficulty: "easy"
      },
      {
        id: 'c6',
        chapter: 3,
        title: "选择题6：Pandas操作",
        question: "在Pandas中，以下哪个方法用于查看数据的前几行？",
        options: [
          { label: 'A', text: 'describe()' },
          { label: 'B', text: 'info()' },
          { label: 'C', text: 'head()' },
          { label: 'D', text: 'shape()' }
        ],
        answer: 'C',
        analysis: "head()方法用于查看DataFrame的前几行（默认前5行）。describe()显示统计摘要，info()显示数据信息，shape是属性不是方法。",
        difficulty: "easy"
      },
      {
        id: 'c7',
        chapter: 4,
        title: "选择题7：描述性统计",
        question: "以下哪个统计量不受极端值影响？",
        options: [
          { label: 'A', text: '均值' },
          { label: 'B', text: '标准差' },
          { label: 'C', text: '中位数' },
          { label: 'D', text: '极差' }
        ],
        answer: 'C',
        analysis: "中位数是数据排序后位于中间位置的值，不受极端值影响。均值、标准差和极差都容易受到极端值的影响。",
        difficulty: "easy"
      },
      {
        id: 'c8',
        chapter: 4,
        title: "选择题8：假设检验",
        question: "p值小于0.05表示什么？",
        options: [
          { label: 'A', text: '接受原假设' },
          { label: 'B', text: '拒绝原假设' },
          { label: 'C', text: '无法判断' },
          { label: 'D', text: '需要更多数据' }
        ],
        answer: 'B',
        analysis: "当p值小于显著性水平（通常是0.05）时，我们拒绝原假设，认为存在显著差异。p值表示在原假设成立的情况下观察到当前数据的概率。",
        difficulty: "medium"
      },
      {
        id: 'c9',
        chapter: 5,
        title: "选择题9：机器学习类型",
        question: "K-Means属于哪种机器学习类型？",
        options: [
          { label: 'A', text: '监督学习' },
          { label: 'B', text: '无监督学习' },
          { label: 'C', text: '强化学习' },
          { label: 'D', text: '半监督学习' }
        ],
        answer: 'B',
        analysis: "K-Means是一种无监督学习算法，它不需要标注数据，而是自动从数据中发现模式和结构，将相似的数据点分组到同一个簇中。",
        difficulty: "easy"
      },
      {
        id: 'c10',
        chapter: 5,
        title: "选择题10：回归分析",
        question: "线性回归的目标是什么？",
        options: [
          { label: 'A', text: '分类' },
          { label: 'B', text: '预测连续数值' },
          { label: 'C', text: '聚类' },
          { label: 'D', text: '降维' }
        ],
        answer: 'B',
        analysis: "线性回归用于预测连续数值型变量。分类是分类算法的目标，聚类是无监督学习的目标，降维是如PCA等方法的目标。",
        difficulty: "easy"
      },
      {
        id: 'c11',
        chapter: 6,
        title: "选择题11：数据可视化",
        question: "展示时间趋势最合适的图表类型是？",
        options: [
          { label: 'A', text: '饼图' },
          { label: 'B', text: '柱状图' },
          { label: 'C', text: '折线图' },
          { label: 'D', text: '散点图' }
        ],
        answer: 'C',
        analysis: "折线图最适合展示数据随时间的变化趋势。饼图适合展示占比，柱状图适合比较类别，散点图适合展示两个变量的关系。",
        difficulty: "easy"
      },
      {
        id: 'c12',
        chapter: 6,
        title: "选择题12：报告撰写",
        question: "数据分析报告的核心部分是什么？",
        options: [
          { label: 'A', text: '封面' },
          { label: 'B', text: '执行摘要' },
          { label: 'C', text: '分析结果' },
          { label: 'D', text: '结论建议' }
        ],
        answer: 'D',
        analysis: "结论建议是报告的核心，包含分析的核心发现和针对业务问题的具体行动建议。执行摘要提供概览，分析结果提供详细数据支持。",
        difficulty: "medium"
      },
      {
        id: 'c13',
        chapter: 7,
        title: "选择题13：RFM分析",
        question: "RFM分析中的R代表什么？",
        options: [
          { label: 'A', text: 'Recency（最近购买时间）' },
          { label: 'B', text: 'Frequency（购买频率）' },
          { label: 'C', text: 'Monetary（购买金额）' },
          { label: 'D', text: 'Revenue（收入）' }
        ],
        answer: 'A',
        analysis: "RFM是客户价值分析的常用方法：R代表Recency（最近一次购买时间），F代表Frequency（购买频率），M代表Monetary（购买金额）。",
        difficulty: "easy"
      },
      {
        id: 'c14',
        chapter: 7,
        title: "选择题14：转化率",
        question: "转化率的计算公式是？",
        options: [
          { label: 'A', text: '访问数 / 购买数' },
          { label: 'B', text: '购买数 / 访问数' },
          { label: 'C', text: '购买数 / 曝光数' },
          { label: 'D', text: '点击数 / 曝光数' }
        ],
        answer: 'B',
        analysis: "转化率 = 购买数 / 访问数 × 100%。它衡量的是访问用户中有多少比例完成了购买行为。",
        difficulty: "easy"
      },
      {
        id: 'c15',
        chapter: 8,
        title: "选择题15：职业发展",
        question: "数据分析师最核心的技能是什么？",
        options: [
          { label: 'A', text: '编程能力' },
          { label: 'B', text: '统计知识' },
          { label: 'C', text: '业务理解能力' },
          { label: 'D', text: '可视化能力' }
        ],
        answer: 'C',
        analysis: "虽然技术技能很重要，但业务理解能力是数据分析师最核心的技能。能够将业务问题转化为分析问题，并将分析结果转化为业务洞察，才是数据分析的核心价值。",
        difficulty: "medium"
      }
    ];
"""

# 找到problems数组的位置并替换
problems_pattern = r"(\s+)const problems = \[.*?^\1\];\s*$"
content = re.sub(problems_pattern, new_problems, content, flags=re.MULTILINE | re.DOTALL)

# 找到choiceQuestions数组的位置并替换
choice_pattern = r"(\s+)const choiceQuestions = \[.*?^\1\];\s*$"
content = re.sub(choice_pattern, new_choice_questions, content, flags=re.MULTILINE | re.DOTALL)

# 写入更新后的文件
with open('data-analysis-tech.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("题库更新完成！")
print(f"编程题目数量: {len(new_problems.split('id: ')) - 1}")
print(f"选择题数量: {len(new_choice_questions.split('id: ')) - 1}")
