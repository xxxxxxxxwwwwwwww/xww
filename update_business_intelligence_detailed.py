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
    
    # 新的详细知识点内容
    new_knowledge_content = '''      <!-- 知识点标签页 -->
      <div id="knowledge" class="tab-content hidden">
        <div class="py-6">
          <h2 class="text-2xl font-bold text-cyan-400 mb-6">📚 商务智能分析 - 详细知识点</h2>
          
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
                <div class="space-y-4">
                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o"></i>
                      1.1 商务智能（BI）概念、价值与应用场景
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <p><strong class="text-cyan-400">什么是商务智能？</strong></p>
                      <p class="text-sm">商务智能（Business Intelligence，简称BI）是将企业中现有的数据转化为知识，帮助企业做出明智的业务经营决策的技术和过程。它不是一个单一的产品，而是一套完整的解决方案。</p>
                      <div class="bg-dark-gray p-3 rounded-lg mt-2">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">📊 BI的核心价值：</p>
                        <ul class="list-disc list-inside space-y-1 text-gray-400 text-sm">
                          <li>数据驱动决策：从经验决策转向基于数据的科学决策</li>
                          <li>提升运营效率：优化业务流程，降低运营成本</li>
                          <li>发现市场机会：深入挖掘客户需求，识别增长机会</li>
                          <li>风险预警管理：及时发现潜在风险，提前采取措施</li>
                          <li>增强企业竞争力：提升数据洞察能力，保持竞争优势</li>
                        </ul>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg mt-3">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">🏢 典型应用场景：</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                          <div class="bg-dark p-2 rounded text-sm">
                            <strong class="text-emerald-400">零售行业</strong>
                            <p class="text-gray-400">销售分析、库存优化、客户分群、促销效果评估</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-sm">
                            <strong class="text-emerald-400">金融行业</strong>
                            <p class="text-gray-400">风险管控、客户画像、欺诈检测、投资分析</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-sm">
                            <strong class="text-emerald-400">电商行业</strong>
                            <p class="text-gray-400">用户行为分析、转化率优化、推荐系统、AB测试</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-sm">
                            <strong class="text-emerald-400">制造业</strong>
                            <p class="text-gray-400">供应链优化、质量监控、设备预测性维护</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-sitemap"></i>
                      1.2 数据、信息、知识、决策的关系
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-gradient-to-r from-gray-900 to-gray-800 p-4 rounded-lg">
                        <div class="grid grid-cols-4 gap-4">
                          <div class="text-center">
                            <div class="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-2 text-2xl">📝</div>
                            <strong class="text-blue-400">数据</strong>
                            <p class="text-xs text-gray-400 mt-1">原始事实、数字、文字</p>
                          </div>
                          <div class="text-center">
                            <div class="w-16 h-16 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-2 text-2xl">📊</div>
                            <strong class="text-green-400">信息</strong>
                            <p class="text-xs text-gray-400 mt-1">有结构、有意义的数据</p>
                          </div>
                          <div class="text-center">
                            <div class="w-16 h-16 bg-yellow-600 rounded-full flex items-center justify-center mx-auto mb-2 text-2xl">💡</div>
                            <strong class="text-yellow-400">知识</strong>
                            <p class="text-xs text-gray-400 mt-1">可应用的规律、模式</p>
                          </div>
                          <div class="text-center">
                            <div class="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-2 text-2xl">🎯</div>
                            <strong class="text-purple-400">决策</strong>
                            <p class="text-xs text-gray-400 mt-1">基于知识的行动选择</p>
                          </div>
                        </div>
                        <div class="flex justify-center mt-3">
                          <i class="fa fa-arrow-right text-gray-500 mx-2"></i>
                          <i class="fa fa-arrow-right text-gray-500 mx-2"></i>
                          <i class="fa fa-arrow-right text-gray-500 mx-2"></i>
                        </div>
                      </div>
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">📈 价值升级过程：</p>
                        <ul class="space-y-2 text-gray-400 text-sm">
                          <li><strong>数据 → 信息</strong>：通过整理、分类、关联，使数据具有可读性和理解性</li>
                          <li><strong>信息 → 知识</strong>：通过分析、挖掘，发现规律、模式、因果关系</li>
                          <li><strong>知识 → 决策</strong>：结合业务目标，选择最优行动方案</li>
                        </ul>
                      </div>
                      <div class="bg-dark p-3 rounded font-mono text-sm">
                        <pre class="text-cyan-300">
示例：电商数据价值链条

数据层：
{ "user_id": 1001, "product": "手机", "price": 3999, "timestamp": "2024-05-20" }

信息层：
用户1001在5月20日购买了一款3999元的手机

知识层：
该用户是高价值客户，购买周期约3个月，偏好高端电子产品

决策层：
推荐新品手机+配件套餐，设置会员专属优惠券
</pre>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-cogs"></i>
                      1.3 BI核心架构：数据源→ETL→数据仓库→分析→可视化
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="flex items-center gap-2 mb-3">
                          <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
                            <i class="fa fa-database"></i>
                          </div>
                          <strong class="text-blue-400 text-lg">数据源层</strong>
                        </div>
                        <p class="text-sm text-gray-400 mb-2">数据的来源，包括结构化和非结构化数据：</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm">
                          <div class="bg-dark p-2 rounded">
                            <strong class="text-emerald-400">结构化数据</strong>
                            <p class="text-gray-400">关系数据库、ERP、CRM、财务系统</p>
                          </div>
                          <div class="bg-dark p-2 rounded">
                            <strong class="text-emerald-400">非结构化数据</strong>
                            <p class="text-gray-400">日志、图片、视频、邮件、社交媒体</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="flex items-center gap-2 mb-3">
                          <div class="w-10 h-10 bg-green-600 rounded-lg flex items-center justify-center">
                            <i class="fa fa-refresh"></i>
                          </div>
                          <strong class="text-green-400 text-lg">ETL层</strong>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-sm">
                          <div class="bg-dark p-3 rounded">
                            <div class="text-yellow-400 font-semibold mb-1">Extract 抽取</div>
                            <p class="text-gray-400">从不同数据源获取原始数据</p>
                          </div>
                          <div class="bg-dark p-3 rounded">
                            <div class="text-yellow-400 font-semibold mb-1">Transform 转换</div>
                            <p class="text-gray-400">清洗、规范、关联、聚合数据</p>
                          </div>
                          <div class="bg-dark p-3 rounded">
                            <div class="text-yellow-400 font-semibold mb-1">Load 加载</div>
                            <p class="text-gray-400">将处理后的数据加载到数据仓库</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="flex items-center gap-2 mb-3">
                          <div class="w-10 h-10 bg-yellow-600 rounded-lg flex items-center justify-center">
                            <i class="fa fa-server"></i>
                          </div>
                          <strong class="text-yellow-400 text-lg">数据仓库层</strong>
                        </div>
                        <p class="text-sm text-gray-400">集中存储企业数据，支持OLAP分析查询，采用维度建模方式</p>
                      </div>

                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="flex items-center gap-2 mb-3">
                          <div class="w-10 h-10 bg-purple-600 rounded-lg flex items-center justify-center">
                            <i class="fa fa-search"></i>
                          </div>
                          <strong class="text-purple-400 text-lg">分析层</strong>
                        </div>
                        <div class="grid grid-cols-2 gap-2 text-sm">
                          <div class="bg-dark p-2 rounded">OLAP多维分析</div>
                          <div class="bg-dark p-2 rounded">数据挖掘</div>
                          <div class="bg-dark p-2 rounded">统计分析</div>
                          <div class="bg-dark p-2 rounded">机器学习预测</div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="flex items-center gap-2 mb-3">
                          <div class="w-10 h-10 bg-emerald-600 rounded-lg flex items-center justify-center">
                            <i class="fa fa-bar-chart"></i>
                          </div>
                          <strong class="text-emerald-400 text-lg">可视化层</strong>
                        </div>
                        <p class="text-sm text-gray-400">通过图表、报表、看板等形式将分析结果直观展示给用户</p>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-tachometer"></i>
                      1.4 企业常用指标体系、KPI、维度与度量
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">📋 什么是指标体系？</p>
                        <p class="text-sm text-gray-400">指标体系是指由一系列相互关联、相互补充的指标组成的有机整体，用于全面反映企业经营状况。</p>
                        <div class="mt-3 grid grid-cols-1 md:grid-cols-3 gap-2">
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-red-400 text-2xl font-bold">结果指标</div>
                            <p class="text-xs text-gray-400">发生了什么</p>
                            <p class="text-xs text-gray-500">销售额、利润</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-yellow-400 text-2xl font-bold">过程指标</div>
                            <p class="text-xs text-gray-400">如何发生的</p>
                            <p class="text-xs text-gray-500">转化率、访问量</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-green-400 text-2xl font-bold">驱动指标</div>
                            <p class="text-xs text-gray-400">为什么发生</p>
                            <p class="text-xs text-gray-500">客单价、复购率</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">🎯 KPI（关键绩效指标）</p>
                        <p class="text-sm text-gray-400 mb-2">KPI是对战略目标进行分解，用于衡量关键业务成果的指标。</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-2">
                          <div class="bg-dark p-3 rounded">
                            <strong class="text-emerald-400">SMART原则</strong>
                            <ul class="text-xs text-gray-400 mt-1 space-y-1">
                              <li>S - Specific：具体明确</li>
                              <li>M - Measurable：可衡量</li>
                              <li>A - Achievable：可达成</li>
                              <li>R - Relevant：相关性</li>
                              <li>T - Time-bound：有时限</li>
                            </ul>
                          </div>
                          <div class="bg-dark p-3 rounded">
                            <strong class="text-emerald-400">常见KPI示例</strong>
                            <ul class="text-xs text-gray-400 mt-1 space-y-1">
                              <li>销售：月销售额、订单量、客单价</li>
                              <li>运营：用户留存率、复购率、转化率</li>
                              <li>财务：ROI、毛利率、现金流</li>
                              <li>服务：NPS、客户满意度、响应时间</li>
                            </ul>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-purple-400 mb-2">📐 维度 vs 度量</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                          <div class="bg-dark p-3 rounded border-l-4 border-purple-500">
                            <strong class="text-purple-400">维度（Dimension）</strong>
                            <p class="text-xs text-gray-400 mt-1">描述业务的属性，用于分类和分组</p>
                            <div class="mt-2 flex flex-wrap gap-1">
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">时间</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">地区</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">产品</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">渠道</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">用户</span>
                            </div>
                          </div>
                          <div class="bg-dark p-3 rounded border-l-4 border-emerald-500">
                            <strong class="text-emerald-400">度量（Measure）</strong>
                            <p class="text-xs text-gray-400 mt-1">业务的数值型指标，用于计算和聚合</p>
                            <div class="mt-2 flex flex-wrap gap-1">
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">销售额</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">订单量</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">用户数</span>
                              <span class="px-2 py-1 bg-gray-700 rounded text-xs">利润率</span>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark p-3 rounded font-mono text-sm">
                        <pre class="text-cyan-300">
示例：电商销售分析

维度组合：
- 时间：2024年5月、第2季度
- 地区：华东、北京
- 产品：手机、电子产品
- 渠道：APP、微信小程序

度量计算：
- 销售额 = SUM(订单金额)
- 订单量 = COUNT(订单ID)
- 客单价 = 销售额 / 订单量
- 转化率 = 下单用户 / 访问用户
</pre>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-exchange"></i>
                      1.5 商务智能与大数据、数据分析的区别
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="overflow-x-auto">
                          <table class="w-full text-sm">
                            <thead>
                              <tr class="border-b border-gray-700">
                                <th class="text-left py-2 px-3 text-cyan-400">特征</th>
                                <th class="text-left py-2 px-3 text-blue-400">商务智能(BI)</th>
                                <th class="text-left py-2 px-3 text-green-400">数据分析</th>
                                <th class="text-left py-2 px-3 text-yellow-400">大数据</th>
                              </tr>
                            </thead>
                            <tbody class="text-gray-400">
                              <tr class="border-b border-gray-800">
                                <td class="py-2 px-3 font-medium text-gray-300">核心目标</td>
                                <td class="py-2 px-3">决策支持</td>
                                <td class="py-2 px-3">洞察发现</td>
                                <td class="py-2 px-3">数据处理能力</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-2 px-3 font-medium text-gray-300">数据规模</td>
                                <td class="py-2 px-3">中小规模</td>
                                <td class="py-2 px-3">可大可小</td>
                                <td class="py-2 px-3">超大规模（4V）</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-2 px-3 font-medium text-gray-300">主要方法</td>
                                <td class="py-2 px-3">报表、OLAP、看板</td>
                                <td class="py-2 px-3">统计、假设检验</td>
                                <td class="py-2 px-3">分布式计算、机器学习</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-2 px-3 font-medium text-gray-300">用户对象</td>
                                <td class="py-2 px-3">业务人员、管理者</td>
                                <td class="py-2 px-3">分析师</td>
                                <td class="py-2 px-3">数据工程师、科学家</td>
                              </tr>
                              <tr>
                                <td class="py-2 px-3 font-medium text-gray-300">时效性</td>
                                <td class="py-2 px-3">T+1或实时</td>
                                <td class="py-2 px-3">按需分析</td>
                                <td class="py-2 px-3">实时/准实时</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-emerald-400 mb-2">🔗 三者关系</p>
                        <div class="text-center my-4">
                          <div class="inline-flex items-center gap-2">
                            <div class="px-4 py-2 bg-yellow-600 rounded font-semibold">大数据</div>
                            <i class="fa fa-long-arrow-right text-gray-400"></i>
                            <div class="px-4 py-2 bg-blue-600 rounded font-semibold">数据分析</div>
                            <i class="fa fa-long-arrow-right text-gray-400"></i>
                            <div class="px-4 py-2 bg-emerald-600 rounded font-semibold">商务智能</div>
                          </div>
                        </div>
                        <p class="text-sm text-gray-400">大数据提供数据处理能力，数据分析提供方法支持，商务智能将结果落地应用于业务决策。</p>
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
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-building"></i>
                      2.1 常见行业业务逻辑
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-dark-gray p-3 rounded-lg">
                          <h5 class="font-semibold text-cyan-400 mb-2">🏪 零售行业</h5>
                          <div class="text-sm text-gray-400 space-y-1">
                            <p><strong>核心目标：</strong>提高销售额、降低库存、提升客户忠诚度</p>
                            <p><strong>关键流程：</strong>采购→库存→销售→会员→售后</p>
                            <p><strong>重要指标：</strong>坪效、人效、库存周转率、售罄率、连带率</p>
                            <p><strong>BI应用：</strong>销售分析、库存优化、促销效果评估</p>
                          </div>
                        </div>
                        <div class="bg-dark-gray p-3 rounded-lg">
                          <h5 class="font-semibold text-green-400 mb-2">🛒 电商行业</h5>
                          <div class="text-sm text-gray-400 space-y-1">
                            <p><strong>核心目标：</strong>拉新、留存、促活、转化</p>
                            <p><strong>关键流程：</strong>浏览→加购→下单→支付→复购</p>
                            <p><strong>重要指标：</strong>UV、PV、转化率、客单价、复购率、GMV</p>
                            <p><strong>BI应用：</strong>漏斗分析、用户画像、A/B测试</p>
                          </div>
                        </div>
                        <div class="bg-dark-gray p-3 rounded-lg">
                          <h5 class="font-semibold text-yellow-400 mb-2">💰 财务领域</h5>
                          <div class="text-sm text-gray-400 space-y-1">
                            <p><strong>核心目标：</strong>增收、节支、控风险、提高资金效率</p>
                            <p><strong>关键流程：</strong>预算→核算→分析→风控→决策</p>
                            <p><strong>重要指标：</strong>营收、利润、ROE、资产负债率、现金流</p>
                            <p><strong>BI应用：</strong>财务报表、预算分析、资金预测</p>
                          </div>
                        </div>
                        <div class="bg-dark-gray p-3 rounded-lg">
                          <h5 class="font-semibold text-purple-400 mb-2">🔗 供应链</h5>
                          <div class="text-sm text-gray-400 space-y-1">
                            <p><strong>核心目标：</strong>快速响应、成本最优、库存合理</p>
                            <p><strong>关键流程：</strong>计划→采购→生产→仓储→配送</p>
                            <p><strong>重要指标：</strong>准时交货率、库存周转率、供应链总成本</p>
                            <p><strong>BI应用：</strong>需求预测、库存优化、供应商分析</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-brain"></i>
                      2.2 分析思维：描述性、诊断性、预测性、规范性分析
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-dark-gray p-4 rounded-lg border-l-4 border-blue-500">
                          <div class="flex items-center gap-2 mb-2">
                            <span class="text-2xl">📊</span>
                            <h5 class="font-semibold text-blue-400">描述性分析 Descriptive</h5>
                          </div>
                          <p class="text-sm text-gray-400 mb-2">回答：发生了什么？</p>
                          <div class="bg-dark p-2 rounded text-xs">
                            <p class="text-gray-300">• 汇总历史数据</p>
                            <p class="text-gray-300">• 生成报表和图表</p>
                            <p class="text-gray-300">• 展示业务现状</p>
                            <p class="text-yellow-400 mt-1 font-semibold">示例：5月销售额1000万，同比增长15%</p>
                          </div>
                        </div>
                        <div class="bg-dark-gray p-4 rounded-lg border-l-4 border-yellow-500">
                          <div class="flex items-center gap-2 mb-2">
                            <span class="text-2xl">🔍</span>
                            <h5 class="font-semibold text-yellow-400">诊断性分析 Diagnostic</h5>
                          </div>
                          <p class="text-sm text-gray-400 mb-2">回答：为什么发生？</p>
                          <div class="bg-dark p-2 rounded text-xs">
                            <p class="text-gray-300">• 深入挖掘原因</p>
                            <p class="text-gray-300">• 多维下钻分析</p>
                            <p class="text-gray-300">• 寻找因果关系</p>
                            <p class="text-yellow-400 mt-1 font-semibold">示例：增长主要来自华东地区新品推广</p>
                          </div>
                        </div>
                        <div class="bg-dark-gray p-4 rounded-lg border-l-4 border-orange-500">
                          <div class="flex items-center gap-2 mb-2">
                            <span class="text-2xl">🔮</span>
                            <h5 class="font-semibold text-orange-400">预测性分析 Predictive</h5>
                          </div>
                          <p class="text-sm text-gray-400 mb-2">回答：将要发生什么？</p>
                          <div class="bg-dark p-2 rounded text-xs">
                            <p class="text-gray-300">• 机器学习模型</p>
                            <p class="text-gray-300">• 时间序列预测</p>
                            <p class="text-gray-300">• 风险预警</p>
                            <p class="text-yellow-400 mt-1 font-semibold">示例：预计6月销售额1200万</p>
                          </div>
                        </div>
                        <div class="bg-dark-gray p-4 rounded-lg border-l-4 border-green-500">
                          <div class="flex items-center gap-2 mb-2">
                            <span class="text-2xl">🎯</span>
                            <h5 class="font-semibold text-green-400">规范性分析 Prescriptive</h5>
                          </div>
                          <p class="text-sm text-gray-400 mb-2">回答：应该怎么做？</p>
                          <div class="bg-dark p-2 rounded text-xs">
                            <p class="text-gray-300">• 优化算法</p>
                            <p class="text-gray-300">• 模拟仿真</p>
                            <p class="text-gray-300">• 决策建议</p>
                            <p class="text-yellow-400 mt-1 font-semibold">示例：建议加大华东地区营销投入</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark p-3 rounded font-mono text-sm">
                        <pre class="text-cyan-300">
分析层次递进示例：电商流量分析

1. 描述性：今日PV=10万，UV=5万，跳出率=40%
   (发生了什么：流量正常但跳出率偏高)

2. 诊断性：来源渠道分析发现广告流量跳出率70%
   (为什么发生：广告着陆页体验差)

3. 预测性：若不优化，预计月销售额下降20%
   (将要发生什么：销售下滑风险)

4. 规范性：建议A/B测试新着陆页+定向投放
   (应该怎么做：优化方案建议)
</pre>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-cube"></i>
                      2.3 维度拆解：时间、地区、产品、渠道、用户
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">📐 维度拆解方法</p>
                        <div class="grid grid-cols-1 md:grid-cols-5 gap-2 text-xs">
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-blue-400 text-xl mb-1">📅</div>
                            <strong class="text-blue-400">时间维度</strong>
                            <p class="text-gray-500 mt-1">年/季/月/周/日/小时</p>
                            <p class="text-gray-400">同比、环比、趋势</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-green-400 text-xl mb-1">🌍</div>
                            <strong class="text-green-400">地区维度</strong>
                            <p class="text-gray-500 mt-1">国家/区域/省/市</p>
                            <p class="text-gray-400">区域对比、市场渗透</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-yellow-400 text-xl mb-1">📦</div>
                            <strong class="text-yellow-400">产品维度</strong>
                            <p class="text-gray-500 mt-1">分类/品牌/价格带</p>
                            <p class="text-gray-400">热销品、滞销品</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-purple-400 text-xl mb-1">📱</div>
                            <strong class="text-purple-400">渠道维度</strong>
                            <p class="text-gray-500 mt-1">线上/线下/APP/电商</p>
                            <p class="text-gray-400">渠道ROI、效果对比</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-emerald-400 text-xl mb-1">👥</div>
                            <strong class="text-emerald-400">用户维度</strong>
                            <p class="text-gray-500 mt-1">新老/等级/画像</p>
                            <p class="text-gray-400">用户分层、精准营销</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">🎯 经典分析框架</p>
                        <div class="bg-dark p-3 rounded">
                          <div class="text-center mb-3">
                            <strong class="text-cyan-400">销售额 = 用户数 × 转化率 × 客单价</strong>
                          </div>
                          <div class="grid grid-cols-3 gap-2 text-xs">
                            <div class="text-center p-2 bg-gray-800 rounded">
                              <div class="text-blue-400 font-semibold">用户数</div>
                              <p class="text-gray-400">新用户+老用户</p>
                              <p class="text-gray-500">渠道、活动</p>
                            </div>
                            <div class="text-center p-2 bg-gray-800 rounded">
                              <div class="text-green-400 font-semibold">转化率</div>
                              <p class="text-gray-400">浏览→加购→下单</p>
                              <p class="text-gray-500">漏斗分析</p>
                            </div>
                            <div class="text-center p-2 bg-gray-800 rounded">
                              <div class="text-yellow-400 font-semibold">客单价</div>
                              <p class="text-gray-400">件数×均价</p>
                              <p class="text-gray-500">连带率</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-puzzle-piece"></i>
                      2.4 业务问题拆解方法、指标定义规范
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">🔧 MECE原则</p>
                        <p class="text-sm text-gray-400 mb-2">MECE（Mutually Exclusive Collectively Exhaustive）：相互独立，完全穷尽</p>
                        <div class="bg-dark p-3 rounded">
                          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                            <div class="p-2 border border-green-600 rounded bg-green-900/20">
                              <p class="text-green-400 font-semibold mb-1">✓ 正确示例</p>
                              <p>用户：新用户、老用户</p>
                              <p>地区：华东、华南、华北、西南、西北、东北、华中</p>
                            </div>
                            <div class="p-2 border border-red-600 rounded bg-red-900/20">
                              <p class="text-red-400 font-semibold mb-1">✗ 错误示例</p>
                              <p>用户：新用户、APP用户（有重叠）</p>
                              <p>地区：东部、南方、北京（层级混乱）</p>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">📝 指标定义规范</p>
                        <div class="bg-dark p-3 rounded text-sm">
                          <table class="w-full text-xs">
                            <thead>
                              <tr class="border-b border-gray-700">
                                <th class="text-left py-2 px-2 text-cyan-400">要素</th>
                                <th class="text-left py-2 px-2 text-gray-300">说明</th>
                                <th class="text-left py-2 px-2 text-gray-300">示例</th>
                              </tr>
                            </thead>
                            <tbody class="text-gray-400">
                              <tr class="border-b border-gray-800">
                                <td class="py-1 px-2 font-medium text-gray-300">名称</td>
                                <td class="py-1 px-2">清晰、无歧义</td>
                                <td class="py-1 px-2">月活跃用户数(MAU)</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-1 px-2 font-medium text-gray-300">定义</td>
                                <td class="py-1 px-2">业务含义说明</td>
                                <td class="py-1 px-2">过去30天内有过至少一次登录或下单行为的用户数</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-1 px-2 font-medium text-gray-300">计算公式</td>
                                <td class="py-1 px-2">可执行的逻辑</td>
                                <td class="py-1 px-2">COUNT(DISTINCT user_id) WHERE action_date ≥ date - 30</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-1 px-2 font-medium text-gray-300">统计周期</td>
                                <td class="py-1 px-2">日/周/月/季/年</td>
                                <td class="py-1 px-2">自然月</td>
                              </tr>
                              <tr class="border-b border-gray-800">
                                <td class="py-1 px-2 font-medium text-gray-300">口径说明</td>
                                <td class="py-1 px-2">特殊处理规则</td>
                                <td class="py-1 px-2">排除测试账号、异常值</td>
                              </tr>
                              <tr>
                                <td class="py-1 px-2 font-medium text-gray-300">数据来源</td>
                                <td class="py-1 px-2">源表和字段</td>
                                <td class="py-1 px-2">dwd_user_action_log</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-lightbulb-o"></i>
                      2.5 案例：从业务需求转化为分析问题
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-4 rounded-lg">
                        <div class="border-l-4 border-yellow-500 pl-4 py-2">
                          <p class="text-yellow-400 font-semibold">📋 业务需求</p>
                          <p class="text-gray-300 text-sm">"最近销售不太好，你帮我分析一下"</p>
                        </div>
                        <div class="flex justify-center my-3">
                          <i class="fa fa-arrow-down text-gray-500 text-2xl"></i>
                        </div>
                        <div class="border-l-4 border-cyan-500 pl-4 py-2">
                          <p class="text-cyan-400 font-semibold">🔍 分析问题拆解</p>
                          <ol class="text-sm text-gray-400 space-y-2 mt-2">
                            <li><strong>1. 量化定义：</strong>销售不好具体指什么？销售额下降？订单减少？还是利润下滑？</li>
                            <li><strong>2. 时间范围：</strong>最近是多久？一周？一个月？同比还是环比？</li>
                            <li><strong>3. 多维分析：</strong>
                              <ul class="ml-4 mt-1 list-disc list-inside">
                                <li>哪类产品销售下降？</li>
                                <li>哪个地区下降明显？</li>
                                <li>哪个渠道表现最差？</li>
                                <li>新老客分别什么情况？</li>
                              </ul>
                            </li>
                            <li><strong>4. 定位原因：</strong>是外部市场因素还是内部运营问题？</li>
                            <li><strong>5. 建议方案：</strong>基于分析给出可落地的优化建议</li>
                          </ol>
                        </div>
                      </div>

                      <div class="bg-dark p-3 rounded font-mono text-sm">
                        <pre class="text-cyan-300">
完整分析思路示例：

业务问题：Q2销售未达预期

分析步骤：
1. 现状确认：Q2销售额800万，目标1000万，缺口200万
2. 时间趋势：逐月下滑，4月300万→5月270万→6月230万
3. 维度拆解：
   - 产品：A系列从200万→100万（主要下滑源）
   - 渠道：线下渠道下降30%
   - 地区：华东区表现异常
4. 原因分析：
   - A系列竞品推出低价新品
   - 线下门店促销活动结束
5. 建议方案：
   - A系列降价或推出促销套装
   - 华东区增加线上投放
   - 开发B系列作为替代
</pre>
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
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-table"></i>
                      3.1 关系型数据库基础
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">📊 核心概念</p>
                        <div class="grid grid-cols-1 md:grid-cols-4 gap-2 text-sm">
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-xl mb-1">📋</div>
                            <strong class="text-blue-400">表（Table）</strong>
                            <p class="text-xs text-gray-400 mt-1">数据的集合，二维结构</p>
                            <p class="text-xs text-gray-500">用户表、订单表</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-xl mb-1">🏷️</div>
                            <strong class="text-green-400">字段（Column）</strong>
                            <p class="text-xs text-gray-400 mt-1">表的列，表示属性</p>
                            <p class="text-xs text-gray-500">姓名、年龄、金额</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-xl mb-1">📝</div>
                            <strong class="text-yellow-400">记录（Row）</strong>
                            <p class="text-xs text-gray-400 mt-1">表的行，一条完整数据</p>
                            <p class="text-xs text-gray-500">一个用户的信息</p>
                          </div>
                          <div class="bg-dark p-2 rounded text-center">
                            <div class="text-xl mb-1">🔑</div>
                            <strong class="text-purple-400">键（Key）</strong>
                            <p class="text-xs text-gray-400 mt-1">主键PK、外键FK</p>
                            <p class="text-xs text-gray-500">ID、关联字段</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">🔗 主键与外键</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                          <div class="bg-dark p-3 rounded border-l-4 border-blue-500">
                            <p class="font-semibold text-blue-400 mb-1">主键 Primary Key</p>
                            <ul class="text-xs text-gray-400 space-y-1">
                              <li>• 唯一标识表中每条记录</li>
                              <li>• 不能为NULL，不能重复</li>
                              <li>• 通常是自增ID</li>
                              <li>• 示例：user_id, order_id</li>
                            </ul>
                          </div>
                          <div class="bg-dark p-3 rounded border-l-4 border-green-500">
                            <p class="font-semibold text-green-400 mb-1">外键 Foreign Key</p>
                            <ul class="text-xs text-gray-400 space-y-1">
                              <li>• 建立表之间的关联</li>
                              <li>• 引用另一个表的主键</li>
                              <li>• 保证数据一致性</li>
                              <li>• 示例：订单表的user_id</li>
                            </ul>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark p-3 rounded font-mono text-sm">
                        <pre class="text-cyan-300">
表关系示例：电商场景

用户表 (users)
┌─────────┬─────────┬───────┐
│ user_id │ name    │ level │
├─────────┼─────────┼───────┤
│ 1       │ 张三    │ VIP   │
│ 2       │ 李四    │ 普通  │
└─────────┴─────────┴───────┘
  ↑
  │ PK

订单表 (orders)
┌──────────┬─────────┬────────┬───────┐
│ order_id │ user_id │ amount │ date  │
├──────────┼─────────┼────────┼───────┤
│ 101      │ 1       │ 99     │ ...   │
│ 102      │ 1       │ 199    │ ...   │
│ 103      │ 2       │ 59     │ ...   │
└──────────┴─────────┴────────┴───────┘
             ↑
             │ FK (引用users.user_id)
</pre>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-search"></i>
                      3.2 SQL基础语法：查询、筛选、排序、聚合
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">📝 SELECT基础查询</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 1. 查询所有字段
SELECT * FROM users;

-- 2. 查询指定字段
SELECT user_id, name, email FROM users;

-- 3. 别名 AS
SELECT user_id AS id, name AS username FROM users;

-- 4. 去重 DISTINCT
SELECT DISTINCT level FROM users;

-- 5.  LIMIT 限制数量
SELECT * FROM orders LIMIT 10;
</pre>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">🔍 WHERE条件筛选</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 1. 比较运算符
SELECT * FROM orders WHERE amount > 100;
SELECT * FROM users WHERE level = 'VIP';

-- 2. 逻辑运算符
SELECT * FROM orders 
WHERE amount > 100 AND status = '完成';

-- 3. IN / BETWEEN / LIKE
SELECT * FROM users 
WHERE level IN ('VIP', 'SVIP');

SELECT * FROM orders 
WHERE amount BETWEEN 50 AND 200;

SELECT * FROM users 
WHERE name LIKE '张%';

-- 4. IS NULL
SELECT * FROM users 
WHERE email IS NULL;
</pre>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-green-400 mb-2">📊 ORDER BY排序</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 1. 单列排序
SELECT * FROM orders 
ORDER BY amount DESC;  -- 降序
ORDER BY amount ASC;   -- 升序（默认）

-- 2. 多列排序
SELECT * FROM orders 
ORDER BY date DESC, amount DESC;

-- 3. LIMIT + ORDER BY 取TOP N
SELECT * FROM orders 
ORDER BY amount DESC 
LIMIT 5;  -- 金额最高的5个订单
</pre>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-purple-400 mb-2">📈 聚合函数 GROUP BY</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 常用聚合函数
SELECT 
  COUNT(*) AS total_orders,      -- 计数
  SUM(amount) AS total_amount,   -- 求和
  AVG(amount) AS avg_amount,     -- 平均值
  MAX(amount) AS max_amount,     -- 最大值
  MIN(amount) AS min_amount      -- 最小值
FROM orders;

-- GROUP BY 分组聚合
SELECT 
  user_id,
  COUNT(*) AS order_count,
  SUM(amount) AS total_spent
FROM orders
GROUP BY user_id;

-- HAVING 筛选分组结果
SELECT 
  user_id,
  SUM(amount) AS total_spent
FROM orders
GROUP BY user_id
HAVING SUM(amount) > 1000;  -- 消费超1000的用户
</pre>
                        </div>
                      </div>

                      <div class="bg-dark p-3 rounded font-mono text-sm">
                        <pre class="text-cyan-300">
-- 完整示例：分析2024年5月销售情况
SELECT
  DATE_FORMAT(order_date, '%Y-%m') AS month,
  COUNT(DISTINCT user_id) AS user_count,
  COUNT(*) AS order_count,
  SUM(amount) AS total_amount,
  AVG(amount) AS avg_amount
FROM orders
WHERE 
  order_date BETWEEN '2024-05-01' AND '2024-05-31'
  AND status = '完成'
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
</pre>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-link"></i>
                      3.3 多表查询：JOIN、子查询、临时表
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">🔗 JOIN类型</p>
                        <div class="grid grid-cols-1 md:grid-cols-4 gap-2 text-xs">
                          <div class="bg-dark p-2 rounded">
                            <strong class="text-blue-400">INNER JOIN</strong>
                            <p class="text-gray-400 mt-1">两表交集，匹配的记录</p>
                          </div>
                          <div class="bg-dark p-2 rounded">
                            <strong class="text-green-400">LEFT JOIN</strong>
                            <p class="text-gray-400 mt-1">左表全部+右表匹配</p>
                          </div>
                          <div class="bg-dark p-2 rounded">
                            <strong class="text-yellow-400">RIGHT JOIN</strong>
                            <p class="text-gray-400 mt-1">右表全部+左表匹配</p>
                          </div>
                          <div class="bg-dark p-2 rounded">
                            <strong class="text-purple-400">FULL JOIN</strong>
                            <p class="text-gray-400 mt-1">两表并集</p>
                          </div>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">💻 JOIN示例</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 1. INNER JOIN: 查询订单及用户信息
SELECT 
  o.order_id,
  o.amount,
  u.name,
  u.level
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id;

-- 2. LEFT JOIN: 查询所有用户及订单数（包括无订单的用户）
SELECT 
  u.user_id,
  u.name,
  COUNT(o.order_id) AS order_count
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name;

-- 3. 多表JOIN
SELECT 
  o.order_id,
  u.name AS user_name,
  p.product_name,
  o.amount
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id;
</pre>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-green-400 mb-2">📦 子查询</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 1. WHERE子查询
SELECT * FROM orders 
WHERE user_id IN (
  SELECT user_id FROM users WHERE level = 'VIP'
);

-- 2. FROM子查询（派生表）
SELECT * FROM (
  SELECT 
    user_id,
    SUM(amount) AS total_spent
  FROM orders
  GROUP BY user_id
) t
WHERE t.total_spent > 1000;

-- 3. EXISTS子查询
SELECT * FROM users u
WHERE EXISTS (
  SELECT 1 FROM orders o 
  WHERE o.user_id = u.user_id
  AND o.amount > 500
);
</pre>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-purple-400 mb-2">📋 CTE 公用表表达式</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
WITH user_stats AS (
  SELECT 
    user_id,
    COUNT(*) AS order_count,
    SUM(amount) AS total_spent,
    MAX(amount) AS max_order
  FROM orders
  GROUP BY user_id
),
vip_users AS (
  SELECT user_id FROM users WHERE level = 'VIP'
)
SELECT 
  u.name,
  us.order_count,
  us.total_spent
FROM vip_users vu
INNER JOIN user_stats us ON vu.user_id = us.user_id
INNER JOIN users u ON vu.user_id = u.user_id
WHERE us.total_spent > 5000;
</pre>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="bg-dark p-4 rounded-lg border border-gray-700">
                    <h4 class="text-lg font-semibold text-emerald-400 mb-3 flex items-center gap-2">
                      <i class="fa fa-chart-area"></i>
                      3.4 窗口函数、分组统计、同比环比计算
                    </h4>
                    <div class="space-y-3 text-gray-300">
                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-cyan-400 mb-2">🎯 窗口函数语法</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- 基本结构
函数名(参数) OVER (
  [PARTITION BY 分组字段]
  [ORDER BY 排序字段]
  [ROWS BETWEEN ...]
)

-- 序号函数
SELECT 
  user_id,
  amount,
  ROW_NUMBER() OVER(ORDER BY amount DESC) AS rn,
  RANK() OVER(ORDER BY amount DESC) AS rk,
  DENSE_RANK() OVER(ORDER BY amount DESC) AS dr
FROM orders;

-- 聚合窗口函数
SELECT 
  order_id,
  user_id,
  amount,
  SUM(amount) OVER(PARTITION BY user_id) AS user_total,
  AVG(amount) OVER(PARTITION BY user_id) AS user_avg,
  MAX(amount) OVER(PARTITION BY user_id) AS user_max
FROM orders;
</pre>
                        </div>
                      </div>

                      <div class="bg-dark-gray p-3 rounded-lg">
                        <p class="text-sm font-semibold text-yellow-400 mb-2">📈 偏移函数 LAG/LEAD</p>
                        <div class="bg-dark p-3 rounded font-mono text-xs">
                          <pre class="text-cyan-300">
-- LAG：取前N行，LEAD：取后N行
SELECT 
  date,
  amount,
  LAG(amount, 1) OVER(ORDER BY date) AS prev_day,
  LEAD(amount, 1) OVER(ORDER BY date) AS next_day