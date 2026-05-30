#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新商务智能分析课程详细知识点"""
import os

def main():
    input_file = '/workspace/courses/business-intelligence.html'
    backup_file = '/workspace/courses/business-intelligence-detailed-backup.html'
    
    print("开始更新商务智能分析详细知识点...")
    
    # 备份当前文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已备份到: {backup_file}")
    
    # 查找知识内容区域
    start_marker = '      <!-- 知识点标签页 -->'
    end_marker = '  </div>\n\n  <script>'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("❌ 错误：未找到知识点内容标记")
        print(f"  start_marker 位置: {start_idx}")
        print(f"  end_marker 位置: {end_idx}")
        return
    
    # 生成完整的详细知识点内容
    new_knowledge = '''      <!-- 知识点标签页 -->
      <div id="knowledge" class="tab-content hidden">
        <div class="py-6">
          <h2 class="text-2xl font-bold text-cyan-400 mb-6">📚 商务智能分析 - 详细知识点</h2>
          
          <div class="space-y-4">
            <!-- 第1章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-book text-cyan-400"></i>
                  第1章 商务智能基础认知
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">1.1 商务智能概念、价值与应用场景</h4>
                    <div class="text-sm text-gray-300 space-y-3">
                      <p><strong>什么是商务智能？</strong></p>
                      <p>商务智能（BI）是将企业数据转化为知识，帮助做出明智业务决策的技术和过程。</p>
                      <div class="bg-dark-gray p-3 rounded">
                        <p class="font-semibold text-yellow-400 mb-2">📊 BI核心价值</p>
                        <ul class="list-disc list-inside text-gray-400 text-sm space-y-1">
                          <li>数据驱动决策：从经验决策转向基于数据的科学决策</li>
                          <li>提升运营效率：优化业务流程，降低成本</li>
                          <li>发现市场机会：挖掘客户需求，识别增长机会</li>
                          <li>风险预警管理：及时发现潜在风险</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">1.2 数据→信息→知识→决策</h4>
                    <div class="text-sm text-gray-300">
                      <div class="grid grid-cols-4 gap-3 text-center mb-4">
                        <div>
                          <div class="w-12 h-12 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-1">📝</div>
                          <strong class="text-blue-400 text-sm">数据</strong>
                          <p class="text-xs text-gray-400">原始事实</p>
                        </div>
                        <div>
                          <div class="w-12 h-12 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-1">📊</div>
                          <strong class="text-green-400 text-sm">信息</strong>
                          <p class="text-xs text-gray-400">有意义数据</p>
                        </div>
                        <div>
                          <div class="w-12 h-12 bg-yellow-600 rounded-full flex items-center justify-center mx-auto mb-1">💡</div>
                          <strong class="text-yellow-400 text-sm">知识</strong>
                          <p class="text-xs text-gray-400">规律模式</p>
                        </div>
                        <div>
                          <div class="w-12 h-12 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-1">🎯</div>
                          <strong class="text-purple-400 text-sm">决策</strong>
                          <p class="text-xs text-gray-400">行动选择</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">1.3 BI核心架构</h4>
                    <div class="text-sm text-gray-300 space-y-3">
                      <div class="bg-dark-gray p-3 rounded">
                        <div class="flex items-center gap-2 mb-2">
                          <div class="w-8 h-8 bg-blue-600 rounded flex items-center justify-center"><i class="fa fa-database"></i></div>
                          <strong class="text-blue-400">数据源层</strong>
                        </div>
                        <p class="text-gray-400 text-xs">业务数据库、ERP、CRM、日志文件、外部数据</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded">
                        <div class="flex items-center gap-2 mb-2">
                          <div class="w-8 h-8 bg-green-600 rounded flex items-center justify-center"><i class="fa fa-refresh"></i></div>
                          <strong class="text-green-400">ETL层</strong>
                        </div>
                        <p class="text-gray-400 text-xs">Extract抽取→Transform转换→Load加载</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded">
                        <div class="flex items-center gap-2 mb-2">
                          <div class="w-8 h-8 bg-yellow-600 rounded flex items-center justify-center"><i class="fa fa-server"></i></div>
                          <strong class="text-yellow-400">数据仓库层</strong>
                        </div>
                        <p class="text-gray-400 text-xs">集中存储，支持OLAP分析</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded">
                        <div class="flex items-center gap-2 mb-2">
                          <div class="w-8 h-8 bg-purple-600 rounded flex items-center justify-center"><i class="fa fa-search"></i></div>
                          <strong class="text-purple-400">分析层</strong>
                        </div>
                        <p class="text-gray-400 text-xs">OLAP、数据挖掘、机器学习</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded">
                        <div class="flex items-center gap-2 mb-2">
                          <div class="w-8 h-8 bg-emerald-600 rounded flex items-center justify-center"><i class="fa fa-bar-chart"></i></div>
                          <strong class="text-emerald-400">可视化层</strong>
                        </div>
                        <p class="text-gray-400 text-xs">报表、看板、仪表板</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第2章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-line-chart text-cyan-400"></i>
                  第2章 业务理解与数据分析思维
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">2.1 四种分析层次</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-blue-500">
                        <strong class="text-blue-400">📊 描述性分析</strong>
                        <p class="text-gray-400 text-xs mt-1">回答：发生了什么？</p>
                        <p class="text-gray-500 text-xs">示例：5月销售额1000万</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-yellow-500">
                        <strong class="text-yellow-400">🔍 诊断性分析</strong>
                        <p class="text-gray-400 text-xs mt-1">回答：为什么发生？</p>
                        <p class="text-gray-500 text-xs">示例：增长来自华东地区</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-orange-500">
                        <strong class="text-orange-400">🔮 预测性分析</strong>
                        <p class="text-gray-400 text-xs mt-1">回答：将要发生什么？</p>
                        <p class="text-gray-500 text-xs">示例：预计6月销售1200万</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-green-500">
                        <strong class="text-green-400">🎯 规范性分析</strong>
                        <p class="text-gray-400 text-xs mt-1">回答：应该怎么做？</p>
                        <p class="text-gray-500 text-xs">示例：建议加大营销投入</p>
                      </div>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">2.2 维度拆解</h4>
                    <div class="grid grid-cols-1 md:grid-cols-5 gap-2 text-xs">
                      <div class="bg-dark-gray p-2 rounded text-center">
                        <div class="text-blue-400 text-lg">📅</div>
                        <strong class="text-blue-400">时间</strong>
                        <p class="text-gray-500">年/季/月/周/日</p>
                      </div>
                      <div class="bg-dark-gray p-2 rounded text-center">
                        <div class="text-green-400 text-lg">🌍</div>
                        <strong class="text-green-400">地区</strong>
                        <p class="text-gray-500">国家/区域/省/市</p>
                      </div>
                      <div class="bg-dark-gray p-2 rounded text-center">
                        <div class="text-yellow-400 text-lg">📦</div>
                        <strong class="text-yellow-400">产品</strong>
                        <p class="text-gray-500">分类/品牌/价格带</p>
                      </div>
                      <div class="bg-dark-gray p-2 rounded text-center">
                        <div class="text-purple-400 text-lg">📱</div>
                        <strong class="text-purple-400">渠道</strong>
                        <p class="text-gray-500">线上/线下/APP</p>
                      </div>
                      <div class="bg-dark-gray p-2 rounded text-center">
                        <div class="text-emerald-400 text-lg">👥</div>
                        <strong class="text-emerald-400">用户</strong>
                        <p class="text-gray-500">新老/等级/画像</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第3章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-database text-cyan-400"></i>
                  第3章 数据库与SQL数据查询
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">3.1 SQL基础语法</h4>
                    <div class="bg-dark-gray p-3 rounded font-mono text-xs">
                      <pre class="text-cyan-300">-- SELECT查询
SELECT user_id, name, amount 
FROM orders 
WHERE amount > 100 
ORDER BY amount DESC 
LIMIT 10;

-- 聚合函数
SELECT 
  COUNT(*) AS total,
  SUM(amount) AS sum_amount,
  AVG(amount) AS avg_amount
FROM orders
GROUP BY user_id
HAVING SUM(amount) > 1000;</pre>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">3.2 JOIN多表查询</h4>
                    <div class="bg-dark-gray p-3 rounded font-mono text-xs">
                      <pre class="text-cyan-300">-- INNER JOIN
SELECT o.order_id, u.name, o.amount
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id;

-- LEFT JOIN
SELECT u.name, COUNT(o.order_id) AS order_count
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.name;</pre>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">3.3 窗口函数</h4>
                    <div class="bg-dark-gray p-3 rounded font-mono text-xs">
                      <pre class="text-cyan-300">-- ROW_NUMBER, RANK, DENSE_RANK
SELECT 
  user_id, amount,
  ROW_NUMBER() OVER(ORDER BY amount DESC) AS rn,
  RANK() OVER(ORDER BY amount DESC) AS rk
FROM orders;

-- LAG/LEAD 同比环比
SELECT 
  date, amount,
  LAG(amount, 1) OVER(ORDER BY date) AS prev,
  (amount - LAG(amount, 1) OVER(ORDER BY date)) 
  / LAG(amount, 1) OVER(ORDER BY date) AS growth_rate
FROM daily_sales;</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第4章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-cubes text-cyan-400"></i>
                  第4章 数据仓库与ETL数据处理
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">4.1 维度建模</h4>
                    <div class="text-sm text-gray-300 space-y-2">
                      <div class="bg-dark-gray p-3 rounded">
                        <strong class="text-blue-400">星型模型 Star Schema</strong>
                        <p class="text-gray-400 text-xs mt-1">事实表在中心，连接多个维度表</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded">
                        <strong class="text-green-400">雪花模型 Snowflake Schema</strong>
                        <p class="text-gray-400 text-xs mt-1">维度表规范化，层级结构</p>
                      </div>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">4.2 数据分层</h4>
                    <div class="text-sm text-gray-300 space-y-2">
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-yellow-500">
                        <strong>ODS 操作数据层</strong>
                        <p class="text-gray-400 text-xs">原始数据，基本清洗</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-blue-500">
                        <strong>DWD 明细数据层</strong>
                        <p class="text-gray-400 text-xs">清洗后的明细数据</p>
                      </div>
                      <div class="bg-dark-gray p-3 rounded border-l-4 border-green-500">
                        <strong>DWS 汇总数据层</strong>
                        <p class="text-gray-400 text-xs">轻度汇总，按主题组织</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第5章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-file-excel-o text-cyan-400"></i>
                  第5章 Excel高级商务数据分析
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4 text-sm text-gray-300">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">5.1 高级函数</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                      <div class="bg-dark-gray p-2 rounded"><code class="text-cyan-400">VLOOKUP/XLOOKUP</code> - 查找匹配</div>
                      <div class="bg-dark-gray p-2 rounded"><code class="text-cyan-400">SUMIFS/COUNTIFS</code> - 多条件统计</div>
                      <div class="bg-dark-gray p-2 rounded"><code class="text-cyan-400">INDEX/MATCH</code> - 高级查找</div>
                      <div class="bg-dark-gray p-2 rounded"><code class="text-cyan-400">IFS/SWITCH</code> - 多条件判断</div>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">5.2 数据透视表</h4>
                    <p class="text-gray-400 text-xs">快速汇总分析大量数据，支持行、列、值、筛选器四个区域</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第6章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-bar-chart text-cyan-400"></i>
                  第6章 主流BI可视化工具
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4 text-sm text-gray-300">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">6.1 Power BI</h4>
                    <div class="text-xs space-y-2 text-gray-400">
                      <p>• Power Query：数据清洗和转换</p>
                      <p>• Power Pivot：数据建模</p>
                      <p>• DAX：数据分析表达式</p>
                      <p>• Power View：数据可视化</p>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">6.2 图表选型</h4>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                      <div class="bg-dark-gray p-2 rounded">📊 柱形图 - 类别对比</div>
                      <div class="bg-dark-gray p-2 rounded">📈 折线图 - 趋势变化</div>
                      <div class="bg-dark-gray p-2 rounded">🥧 饼图 - 占比分析</div>
                      <div class="bg-dark-gray p-2 rounded">🔵 散点图 - 相关性</div>
                      <div class="bg-dark-gray p-2 rounded">🗺️ 地图 - 地理位置</div>
                      <div class="bg-dark-gray p-2 rounded">🎯 漏斗图 - 转化分析</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第7章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-calculator text-cyan-400"></i>
                  第7章 统计学基础与商务分析模型
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4 text-sm text-gray-300">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">7.1 RFM用户分层模型</h4>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs">
                      <div class="bg-dark-gray p-2 rounded">
                        <strong class="text-blue-400">R Recency</strong>
                        <p class="text-gray-400">最近一次消费</p>
                      </div>
                      <div class="bg-dark-gray p-2 rounded">
                        <strong class="text-green-400">F Frequency</strong>
                        <p class="text-gray-400">消费频率</p>
                      </div>
                      <div class="bg-dark-gray p-2 rounded">
                        <strong class="text-yellow-400">M Monetary</strong>
                        <p class="text-gray-400">消费金额</p>
                      </div>
                    </div>
                  </div>
                  
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">7.2 ABC分类</h4>
                    <div class="text-xs text-gray-400 space-y-1">
                      <p>• A类：20%的商品贡献80%的销售额，重点管理</p>
                      <p>• B类：30%的商品贡献15%的销售额，常规管理</p>
                      <p>• C类：50%的商品贡献5%的销售额，简化管理</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第8章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-pie-chart text-cyan-400"></i>
                  第8章 数据可视化与BI看板设计
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4 text-sm text-gray-300">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">8.1 看板设计原则</h4>
                    <div class="text-xs text-gray-400 space-y-1">
                      <p>✓ 重点突出：核心KPI放在显眼位置</p>
                      <p>✓ 逻辑清晰：从宏观到微观层层深入</p>
                      <p>✓ 配色协调：不超过3-5种主色</p>
                      <p>✓ 交互友好：支持钻取、筛选、联动</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第9章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-code text-cyan-400"></i>
                  第9章 Python商务智能分析
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-4 text-sm text-gray-300">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3">9.1 核心库</h4>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                      <div class="bg-dark-gray p-2 rounded"><strong class="text-blue-400">Pandas</strong> - 数据处理</div>
                      <div class="bg-dark-gray p-2 rounded"><strong class="text-green-400">NumPy</strong> - 数值计算</div>
                      <div class="bg-dark-gray p-2 rounded"><strong class="text-yellow-400">Matplotlib/Seaborn</strong> - 可视化</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 第10章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-briefcase text-cyan-400"></i>
                  第10章 行业实战项目
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-3 text-sm text-gray-300">
                  <div class="bg-dark-gray p-3 rounded">📊 项目一：电商销售BI分析</div>
                  <div class="bg-dark-gray p-3 rounded">💰 项目二：企业经营财务分析</div>
                  <div class="bg-dark-gray p-3 rounded">👥 项目三：用户运营分析</div>
                  <div class="bg-dark-gray p-3 rounded">📦 项目四：供应链库存分析</div>
                </div>
              </div>
            </div>

            <!-- 第11章 -->
            <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
              <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
                <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
                  <i class="fa fa-rocket text-cyan-400"></i>
                  第11章 商务智能综合应用与职业拓展
                </h3>
                <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
              </div>
              <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
                <div class="space-y-3 text-sm text-gray-300">
                  <div class="bg-dark-gray p-3 rounded">⚡ 自动化报表、定时刷新、数据预警</div>
                  <div class="bg-dark-gray p-3 rounded">🌐 大数据与BI结合：Hive、Spark基础</div>
                  <div class="bg-dark-gray p-3 rounded">📋 数据治理、指标体系搭建</div>
                  <div class="bg-dark-gray p-3 rounded">🎯 BI岗位方向、求职技能清单</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
'''
    
    # 替换内容
    content = content[:start_idx] + new_knowledge + '\n' + content[end_idx:]
    
    # 保存文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✅ 商务智能分析详细知识点更新完成！")

if __name__ == '__main__':
    main()
