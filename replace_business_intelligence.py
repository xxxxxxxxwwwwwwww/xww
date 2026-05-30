#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将供应链分析内容替换为商务智能内容"""
import os

def main():
    input_file = '/workspace/courses/business-intelligence.html'
    backup_file = '/workspace/courses/business-intelligence-backup-before-replace.html'
    
    # 备份当前文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已备份到: {backup_file}")
    
    # 替换标题
    content = content.replace('<title>供应链分析 - Xww的课程页面</title>', 
                              '<title>商务智能分析 - Xww的课程页面</title>')
    
    # 替换导航栏标题
    content = content.replace('供应链分析', '商务智能分析')
    
    # 替换知识点模块标题
    content = content.replace('模块一：供应链基础概念', '模块一：商务智能基础概念')
    content = content.replace('模块二：供应链规划与优化', '模块二：数据仓库与OLAP')
    content = content.replace('模块三：供应链数字化转型', '模块三：数据分析与挖掘')
    
    # 替换知识点内容
    old_content1 = '''            <div id="topic-1" class="topic-content hidden">
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">1. 什么是供应链管理？</h4>
              <p class="text-gray-300 mb-4">
                供应链管理（Supply Chain Management, SCM）是对从供应商到最终客户的整个供应链流程进行规划、协调和控制的管理活动。
                其目标是在正确的时间、正确的地点，以最低的成本提供正确数量的正确产品。
              </p>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">2. 供应链的核心组成部分</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-truck mr-2"></i>供应商</h5>
                  <p class="text-gray-400 text-sm">提供原材料和零部件的组织或个人</p>
                </div>
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-industry mr-2"></i>制造商</h5>
                  <p class="text-gray-400 text-sm">将原材料转化为成品的组织</p>
                </div>
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-warehouse mr-2"></i>分销商</h5>
                  <p class="text-gray-400 text-sm">存储和配送产品的中间环节</p>
                </div>
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-users mr-2"></i>零售商</h5>
                  <p class="text-gray-400 text-sm">直接面向消费者销售的渠道</p>
                </div>
              </div>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">3. 供应链的关键指标</h4>
              <ul class="list-disc list-inside text-gray-300 space-y-2 mb-4">
                <li><strong>交付周期（Lead Time）</strong>：从下单到收货的时间</li>
                <li><strong>库存周转率</strong>：销售成本与平均库存的比率</li>
                <li><strong>准时交付率</strong>：按时交付订单的比例</li>
                <li><strong>供应链总成本</strong>：采购、制造、物流等总成本</li>
              </ul>
            </div>'''
    
    new_content1 = '''            <div id="topic-1" class="topic-content hidden">
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">1. 什么是商务智能？</h4>
              <p class="text-gray-300 mb-4">
                商务智能（Business Intelligence, BI）是将企业中现有的数据转化为知识，帮助企业做出明智业务经营决策的技术和过程。
                通过数据分析、报表和可视化工具，帮助企业洞察市场趋势、优化运营效率。
              </p>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">2. 商务智能的核心组成部分</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-database mr-2"></i>数据仓库</h5>
                  <p class="text-gray-400 text-sm">集中存储企业数据的核心系统</p>
                </div>
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-line-chart mr-2"></i>OLAP分析</h5>
                  <p class="text-gray-400 text-sm">多维数据分析引擎</p>
                </div>
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-bar-chart mr-2"></i>数据可视化</h5>
                  <p class="text-gray-400 text-sm">图表展示数据洞察</p>
                </div>
                <div class="bg-dark-gray p-4 rounded-lg">
                  <h5 class="font-semibold text-gray-200 mb-2"><i class="fa fa-file-text-o mr-2"></i>报表系统</h5>
                  <p class="text-gray-400 text-sm">定期生成业务报表</p>
                </div>
              </div>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">3. 商务智能的关键价值</h4>
              <ul class="list-disc list-inside text-gray-300 space-y-2 mb-4">
                <li><strong>数据驱动决策</strong>：基于数据而非经验进行决策</li>
                <li><strong>运营效率提升</strong>：优化业务流程，降低成本</li>
                <li><strong>市场趋势洞察</strong>：发现市场机会和风险</li>
                <li><strong>绩效监控</strong>：实时跟踪关键业务指标</li>
              </ul>
            </div>'''
    
    content = content.replace(old_content1, new_content1)
    
    old_content2 = '''            <div id="topic-2" class="topic-content hidden">
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">1. 需求预测</h4>
              <p class="text-gray-300 mb-4">
                需求预测是供应链规划的起点。通过历史数据分析、市场趋势研究，预测未来一段时间内的产品需求量，
                为生产计划、库存管理提供依据。
              </p>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">2. 库存优化策略</h4>
              <ul class="list-disc list-inside text-gray-300 space-y-2 mb-4">
                <li><strong>ABC分类法</strong>：将物品按重要性分为A、B、C三类进行差异化管理</li>
                <li><strong>EOQ模型</strong>：经济订货批量模型，计算最优订货量</li>
                <li><strong>安全库存</strong>：应对不确定性的缓冲库存</li>
                <li><strong>JIT管理</strong>：准时制生产，追求零库存</li>
              </ul>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">3. 物流网络规划</h4>
              <p class="text-gray-300 mb-4">
                物流网络规划确定仓库、配送中心的数量和位置，优化运输路线，
                在服务水平和物流成本之间取得平衡。
              </p>
            </div>'''
    
    new_content2 = '''            <div id="topic-2" class="topic-content hidden">
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">1. 数据仓库架构</h4>
              <p class="text-gray-300 mb-4">
                数据仓库是一个面向主题、集成、相对稳定、反映历史变化的数据集合，
                用于支持管理决策。数据通常从多个业务系统抽取、转换、加载（ETL）而来。
              </p>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">2. 维度建模</h4>
              <ul class="list-disc list-inside text-gray-300 space-y-2 mb-4">
                <li><strong>星型模型</strong>：事实表连接多个维度表的简单结构</li>
                <li><strong>雪花模型</strong>：规范化的维度表结构</li>
                <li><strong>事实星座</strong>：多个事实表共享维度表</li>
                <li><strong>维度层次</strong>：时间、地理位置等维度的层级结构</li>
              </ul>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">3. OLAP分析</h4>
              <p class="text-gray-300 mb-4">
                OLAP（联机分析处理）支持复杂的多维分析操作，包括钻取（Drill-down）、
                上卷（Roll-up）、切片（Slice）、切块（Dice）和旋转（Pivot）。
              </p>
            </div>'''
    
    content = content.replace(old_content2, new_content2)
    
    old_content3 = '''            <div id="topic-3" class="topic-content hidden">
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">1. 数字化转型的必要性</h4>
              <p class="text-gray-300 mb-4">
                在数字经济时代，传统供应链面临响应速度慢、透明度低、协同困难等挑战。
                数字化转型通过物联网、大数据、人工智能等技术，重构供应链运营模式。
              </p>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">2. 核心技术应用</h4>
              <ul class="list-disc list-inside text-gray-300 space-y-2 mb-4">
                <li><strong>物联网（IoT）</strong>：实时追踪物流和库存</li>
                <li><strong>区块链</strong>：供应链溯源和透明度</li>
                <li><strong>人工智能</strong>：智能预测和优化</li>
                <li><strong>云计算</strong>：供应链协同平台</li>
              </ul>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">3. 实现路径</h4>
              <p class="text-gray-300 mb-4">
                从数据采集开始，逐步实现业务数字化、流程自动化、决策智能化，
                最终构建敏捷、弹性、智能的数字化供应链。
              </p>
            </div>'''
    
    new_content3 = '''            <div id="topic-3" class="topic-content hidden">
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">1. 数据分析方法</h4>
              <p class="text-gray-300 mb-4">
                数据分析从简单到复杂可分为描述性分析、诊断性分析、预测性分析和规范性分析四个层次，
                帮助企业从理解过去到预测未来、优化决策。
              </p>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">2. 数据挖掘技术</h4>
              <ul class="list-disc list-inside text-gray-300 space-y-2 mb-4">
                <li><strong>分类预测</strong>：客户流失预测、信用评分</li>
                <li><strong>聚类分析</strong>：客户分群、市场细分</li>
                <li><strong>关联规则</strong>：购物篮分析、产品推荐</li>
                <li><strong>时序预测</strong>：销售预测、需求预测</li>
              </ul>
              <h4 class="text-lg font-semibold text-cyan-400 mb-3">3. 可视化最佳实践</h4>
              <p class="text-gray-300 mb-4">
                选择合适的图表类型（柱状图、折线图、散点图、热力图等），
                保持简洁清晰，突出关键信息，讲述数据故事。
              </p>
            </div>'''
    
    content = content.replace(old_content3, new_content3)
    
    # 替换题目
    old_choice_questions = '''const choiceQuestions = [
      {
        id: 'cq1',
        question: '供应链管理的核心目标是什么？',
        options: ['提高产品质量', '在正确的时间、正确的地点，以最低的成本提供正确的产品', '扩大市场份额', '增加销售额'],
        answer: 1,
        explanation: '供应链管理的核心目标是在正确的时间、正确的地点，以最低的成本提供正确数量的正确产品。'
      },
      {
        id: 'cq2',
        question: 'ABC分类法中，A类物品通常占总价值的多少比例？',
        options: ['5-10%', '30-40%', '60-70%', '80-90%'],
        answer: 3,
        explanation: 'ABC分类法中，A类物品通常占物品数量的10-20%，但占总价值的80-90%，需要重点管理。'
      },
      {
        id: 'cq3',
        question: 'EOQ模型是用来计算什么的？',
        options: ['最大库存水平', '经济订货批量', '安全库存量', '再订货点'],
        answer: 1,
        explanation: 'EOQ（Economic Order Quantity）即经济订货批量模型，用于计算最优的订货数量，使订货成本和持有成本之和最小。'
      },
      {
        id: 'cq4',
        question: 'JIT管理理念追求的目标是什么？',
        options: ['最大化库存', '零库存', '定期补货', '批量生产'],
        answer: 1,
        explanation: 'JIT（Just-In-Time）准时制管理追求的目标是零库存，只在需要的时候生产或采购需要的数量。'
      }
    ]'''
    
    new_choice_questions = '''const choiceQuestions = [
      {
        id: 'cq1',
        question: '商务智能的核心目标是什么？',
        options: ['开发更多软件', '将数据转化为知识，支持业务决策', '增加数据存储量', '提高网速'],
        answer: 1,
        explanation: '商务智能的核心目标是将企业数据转化为知识，帮助企业做出明智的业务经营决策。'
      },
      {
        id: 'cq2',
        question: '数据仓库的特点不包括以下哪项？',
        options: ['面向主题', '集成', '易变', '反映历史变化'],
        answer: 2,
        explanation: '数据仓库的特点包括：面向主题、集成、相对稳定、反映历史变化。"易变"不符合数据仓库的特点。'
      },
      {
        id: 'cq3',
        question: '星型模型的结构是怎样的？',
        options: ['多个维度表相互连接', '一个事实表连接多个维度表', '只有一个表', '层级嵌套结构'],
        answer: 1,
        explanation: '星型模型由一个事实表和多个维度表组成，事实表在中心，维度表围绕在四周，形似星星。'
      },
      {
        id: 'cq4',
        question: 'OLAP操作中，从汇总数据深入到细节数据的操作称为？',
        options: ['上卷', '钻取', '切片', '旋转'],
        answer: 1,
        explanation: '钻取（Drill-down）是从汇总数据深入到细节数据，上卷（Roll-up）相反，是从细节数据聚合到汇总数据。'
      }
    ]'''
    
    content = content.replace(old_choice_questions, new_choice_questions)
    
    # 替换编程题
    old_coding_questions = '''const codingQuestions = [
      {
        id: 'code1',
        title: '库存周转率计算',
        description: '编写一个函数 calculate_inventory_turnover，计算库存周转率。库存周转率 = 销售成本 / 平均库存。其中平均库存 = (期初库存 + 期末库存) / 2。',
        starterCode: `def calculate_inventory_turnover(cost_of_goods_sold, beginning_inventory, ending_inventory):
    """
    计算库存周转率
    
    Args:
        cost_of_goods_sold: 销售成本
        beginning_inventory: 期初库存
        ending_inventory: 期末库存
    
    Returns:
        库存周转率
    """
    pass`,
        testCases: [
          { input: [1000000, 200000, 300000], expected: 4.0 },
          { input: [500000, 100000, 100000], expected: 5.0 },
          { input: [200000, 50000, 30000], expected: 5.0 }
        ]
      },
      {
        id: 'code2',
        title: 'ABC分类',
        description: '编写一个函数 abc_classification，根据物品的价值进行ABC分类。A类：价值累计前20%；B类：20%-50%；C类：50%-100%。返回一个字典，键为物品ID，值为类别（"A", "B", "C"）。',
        starterCode: `def abc_classification(items):
    """
    ABC分类
    
    Args:
        items: 字典，键为物品ID，值为价值
    
    Returns:
        字典，键为物品ID，值为类别（"A", "B", "C"）
    """
    pass`,
        testCases: [
          { input: [{'item1': 50, 'item2': 30, 'item3': 15, 'item4': 5}], expected: {'item1': 'A', 'item2': 'A', 'item3': 'B', 'item4': 'C'} },
          { input: [{'a': 100}], expected: {'a': 'A'} },
          { input: [{'x': 10, 'y': 20, 'z': 30, 'w': 40}], expected: {'w': 'A', 'z': 'A', 'y': 'B', 'x': 'C'} }
        ]
      }
    ]'''
    
    new_coding_questions = '''const codingQuestions = [
      {
        id: 'code1',
        title: '销售增长率计算',
        description: '编写一个函数 calculate_growth_rate，计算销售增长率。增长率 = (本期销售额 - 上期销售额) / 上期销售额 × 100%。',
        starterCode: `def calculate_growth_rate(current_period, previous_period):
    """
    计算销售增长率
    
    Args:
        current_period: 本期销售额
        previous_period: 上期销售额
    
    Returns:
        销售增长率（百分比，如10表示10%）
    """
    pass`,
        testCases: [
          { input: [1100000, 1000000], expected: 10.0 },
          { input: [900000, 1000000], expected: -10.0 },
          { input: [200000, 160000], expected: 25.0 }
        ]
      },
      {
        id: 'code2',
        title: '数据聚合统计',
        description: '编写一个函数 aggregate_sales，对销售数据进行聚合统计。输入是一个列表，每个元素是包含"product"、"region"、"amount"的字典。返回按产品和地区分组的销售总额。',
        starterCode: `def aggregate_sales(sales_data):
    """
    聚合销售数据
    
    Args:
        sales_data: 销售数据列表，每个元素是字典
    
    Returns:
        嵌套字典，第一层键为产品，第二层键为地区，值为销售总额
    """
    pass`,
        testCases: [
          { input: [[{'product': 'A', 'region': '华东', 'amount': 100}, {'product': 'A', 'region': '华东', 'amount': 200}, {'product': 'B', 'region': '华北', 'amount': 150}]], expected: {'A': {'华东': 300}, 'B': {'华北': 150}} }
        ]
      }
    ]'''
    
    content = content.replace(old_coding_questions, new_coding_questions)
    
    # 写入文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 商务智能课程内容替换完成！")
    print(f"  - 标题已更新为：商务智能分析")
    print(f"  - 知识点模块已更新")
    print(f"  - 选择题已更新")
    print(f"  - 编程题已更新")
    print(f"\n可以打开文件检查: {input_file}")

if __name__ == '__main__':
    main()
