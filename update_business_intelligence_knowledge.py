#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新商务智能分析课程知识点"""
import os

def main():
    input_file = '/workspace/courses/business-intelligence.html'
    backup_file = '/workspace/courses/business-intelligence-knowledge-backup.html'
    
    print("开始更新商务智能分析知识点...")
    
    # 备份当前文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已备份到: {backup_file}")
    
    # 新的知识点内容 - 11个章节
    new_knowledge_content = '''  <!-- 知识点标签页内容 -->
  <div id="knowledge-content" class="tab-content hidden">
    <div class="bg-dark-gray rounded-lg p-6">
      <h2 class="text-2xl font-bold text-cyan-400 mb-6">📚 商务智能分析 - 知识点汇总</h2>
      
      <!-- 章节列表 -->
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">商务智能（BI）概念、价值与应用场景</strong>
                  <p class="text-sm text-gray-400 mt-1">BI是将企业数据转化为知识，帮助做出明智业务决策的技术和过程</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据、信息、知识、决策的关系</strong>
                  <p class="text-sm text-gray-400 mt-1">数据→信息→知识→决策的价值升级路径</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">BI核心架构</strong>
                  <p class="text-sm text-gray-400 mt-1">数据源 → ETL → 数据仓库 → 分析 → 可视化</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">企业常用指标体系、KPI、维度与度量</strong>
                  <p class="text-sm text-gray-400 mt-1">构建科学的指标体系，支撑业务监控和决策</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">商务智能与大数据、数据分析的区别</strong>
                  <p class="text-sm text-gray-400 mt-1">理解BI的定位：聚焦决策支持，而非纯粹的技术或数据处理</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">常见行业业务逻辑</strong>
                  <p class="text-sm text-gray-400 mt-1">零售、电商、财务、供应链、运营等行业的核心业务逻辑</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">分析思维：描述性、诊断性、预测性、规范性分析</strong>
                  <p class="text-sm text-gray-400 mt-1">从理解过去到预测未来的分析层次递进</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">维度拆解</strong>
                  <p class="text-sm text-gray-400 mt-1">时间、地区、产品、渠道、用户等多维度拆解方法</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">业务问题拆解方法、指标定义规范</strong>
                  <p class="text-sm text-gray-400 mt-1">MECE原则、指标定义标准化</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">案例：从业务需求转化为分析问题</strong>
                  <p class="text-sm text-gray-400 mt-1">实际案例演示业务到分析的转化过程</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">关系型数据库基础</strong>
                  <p class="text-sm text-gray-400 mt-1">表、字段、主键、外键等核心概念</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">SQL基础语法</strong>
                  <p class="text-sm text-gray-400 mt-1">查询、筛选、排序、聚合等基础操作</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">多表查询</strong>
                  <p class="text-sm text-gray-400 mt-1">JOIN、子查询、临时表的高级用法</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">窗口函数、分组统计、同比环比计算</strong>
                  <p class="text-sm text-gray-400 mt-1">ROW_NUMBER、RANK、LAG、LEAD等函数应用</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">实战：从业务库提取分析所需数据</strong>
                  <p class="text-sm text-gray-400 mt-1">实际业务场景的SQL查询练习</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据仓库概念、OLAP与OLTP区别</strong>
                  <p class="text-sm text-gray-400 mt-1">数据仓库的特点与OLAP分析系统</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">维度建模</strong>
                  <p class="text-sm text-gray-400 mt-1">星型模型、雪花模型、事实表/维度表设计</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">ETL流程</strong>
                  <p class="text-sm text-gray-400 mt-1">抽取（Extract）、清洗（Transform）、加载（Load）</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据清洗</strong>
                  <p class="text-sm text-gray-400 mt-1">缺失值、异常值、重复值处理方法</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据分层</strong>
                  <p class="text-sm text-gray-400 mt-1">ODS（操作数据层）、DWD（明细数据层）、DWS（汇总数据层）</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">高级函数</strong>
                  <p class="text-sm text-gray-400 mt-1">IF、SUMIFS、XLOOKUP等函数综合应用</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据透视表、切片器</strong>
                  <p class="text-sm text-gray-400 mt-1">快速汇总分析大量数据</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">Power Query数据清洗与合并</strong>
                  <p class="text-sm text-gray-400 mt-1">批量数据处理和转换</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">Excel基础可视化、动态报表制作</strong>
                  <p class="text-sm text-gray-400 mt-1">图表制作和动态交互报表</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">实战：销售/财务月度分析报表</strong>
                  <p class="text-sm text-gray-400 mt-1">完整的Excel数据分析报告案例</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">Power BI界面、数据源连接</strong>
                  <p class="text-sm text-gray-400 mt-1">Power BI Desktop基本操作和数据导入</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据建模、度量值DAX基础</strong>
                  <p class="text-sm text-gray-400 mt-1">DAX函数和数据分析表达式</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">常用图表制作与图表选型</strong>
                  <p class="text-sm text-gray-400 mt-1">根据数据特点选择合适的图表类型</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">交互式看板、筛选、钻取</strong>
                  <p class="text-sm text-gray-400 mt-1">打造交互式数据可视化看板</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">国产BI工具</strong>
                  <p class="text-sm text-gray-400 mt-1">FineBI、帆软Quick BI简介</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">基础统计</strong>
                  <p class="text-sm text-gray-400 mt-1">均值、中位数、方差、相关性等统计概念</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">常用经典模型</strong>
                  <div class="mt-2 space-y-2 pl-4">
                    <p>• <strong>RFM用户分层模型</strong>：Recency、Frequency、Monetary</p>
                    <p>• <strong>ABC分类</strong>、帕累托二八法则</p>
                    <p>• <strong>漏斗分析</strong>、杜邦财务分析</p>
                  </div>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">时间序列分析</strong>
                  <p class="text-sm text-gray-400 mt-1">趋势、同比、环比、简单预测方法</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">图表规范</strong>
                  <p class="text-sm text-gray-400 mt-1">折线、柱状、饼图、热力图、散点图适用场景</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">看板布局、配色、信息层级设计</strong>
                  <p class="text-sm text-gray-400 mt-1">专业的可视化设计原则</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">商务报表规范、数据故事化表达</strong>
                  <p class="text-sm text-gray-400 mt-1">用数据讲述业务故事</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">交互式分析设计</strong>
                  <p class="text-sm text-gray-400 mt-1">钻取与联动逻辑设计</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">优秀BI看板案例赏析</strong>
                  <p class="text-sm text-gray-400 mt-1">行业最佳实践案例</p>
                </div>
              </li>
            </ul>
          </div>
        </div>

        <!-- 第9章 -->
        <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
          <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
            <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
              <i class="fa fa-code text-cyan-400"></i>
              第9章 Python商务智能分析（进阶）
            </h3>
            <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
          </div>
          <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">Python数据分析库</strong>
                  <p class="text-sm text-gray-400 mt-1">Pandas（数据处理）、Numpy（数值计算）</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据清洗、透视、分组计算</strong>
                  <p class="text-sm text-gray-400 mt-1">使用Python进行高效数据处理</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">简单可视化</strong>
                  <p class="text-sm text-gray-400 mt-1">Matplotlib、Seaborn基础图表制作</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">基础机器学习</strong>
                  <p class="text-sm text-gray-400 mt-1">聚类、简单回归用于预测分析</p>
                </div>
              </li>
            </ul>
          </div>
        </div>

        <!-- 第10章 -->
        <div class="chapter-item border border-gray-700 rounded-lg overflow-hidden">
          <div class="chapter-header flex items-center justify-between p-4 bg-dark cursor-pointer hover:bg-gray-800 transition-colors" onclick="toggleChapter(this)">
            <h3 class="chapter-title text-lg font-semibold text-gray-200 flex items-center gap-2">
              <i class="fa fa-briefcase text-cyan-400"></i>
              第10章 行业实战项目（综合应用）
            </h3>
            <i class="fa fa-chevron-down text-gray-400 transition-transform"></i>
          </div>
          <div class="chapter-content p-4 bg-gray-800 border-t border-gray-700">
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">项目一：电商销售BI分析</strong>
                  <p class="text-sm text-gray-400 mt-1">销量、客单、渠道、复购等核心指标分析</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">项目二：企业经营财务分析</strong>
                  <p class="text-sm text-gray-400 mt-1">营收、成本、利润全面分析</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">项目三：用户运营分析</strong>
                  <p class="text-sm text-gray-400 mt-1">留存、转化、用户画像分析</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">项目四：供应链库存分析</strong>
                  <p class="text-sm text-gray-400 mt-1">周转、缺货预警分析</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">完整BI报告撰写+看板交付</strong>
                  <p class="text-sm text-gray-400 mt-1">从分析到交付的完整流程</p>
                </div>
              </li>
            </ul>
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
            <ul class="space-y-3 text-gray-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">自动化报表、定时刷新、数据预警</strong>
                  <p class="text-sm text-gray-400 mt-1">建立自动化数据监控体系</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">大数据与BI结合</strong>
                  <p class="text-sm text-gray-400 mt-1">Hive、Spark基础认知</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">数据治理、指标体系搭建</strong>
                  <p class="text-sm text-gray-400 mt-1">建立企业级数据标准</p>
                </div>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400">•</span>
                <div>
                  <strong class="text-gray-200">BI岗位方向、求职技能清单</strong>
                  <p class="text-sm text-gray-400 mt-1">职业发展规划和技能要求</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>'''
    
    # 查找并替换知识点内容
    # 查找知识内容标签的开始和结束位置
    start_marker = '<!-- 知识点标签页内容 -->'
    end_marker = '<!-- 题库标签页内容 -->'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("❌ 错误：未找到知识点内容标记")
        return
    
    # 替换内容
    content = content[:start_idx] + new_knowledge_content + '\n\n' + content[end_idx:]
    
    # 保存文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n" + "="*60)
    print("✅ 商务智能分析知识点更新完成！")
    print("="*60)
    print(f"\n📚 已更新内容：")
    print("  • 第1章 商务智能基础认知")
    print("  • 第2章 业务理解与数据分析思维")
    print("  • 第3章 数据库与SQL数据查询")
    print("  • 第4章 数据仓库与ETL数据处理")
    print("  • 第5章 Excel高级商务数据分析")
    print("  • 第6章 主流BI可视化工具")
    print("  • 第7章 统计学基础与商务分析模型")
    print("  • 第8章 数据可视化与BI看板设计")
    print("  • 第9章 Python商务智能分析（进阶）")
    print("  • 第10章 行业实战项目（综合应用）")
    print("  • 第11章 商务智能综合应用与职业拓展")
    print(f"\n📁 文件位置：{input_file}")
    print("💡 刷新浏览器即可查看更新后的内容")

if __name__ == '__main__':
    main()
