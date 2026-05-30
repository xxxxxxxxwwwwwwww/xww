#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""替换商务智能分析页面中的供应链相关内容，统一为商务智能主题"""
import os

def main():
    input_file = '/workspace/courses/business-intelligence.html'
    backup_file = '/workspace/courses/business-intelligence-fix-backup.html'
    
    print("开始修复题目标题与内容不符的问题...")
    
    # 备份当前文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已备份到: {backup_file}")
    
    # 左侧章节列表替换
    old_chapter_list = '''            <!-- 章节列表 -->
            <div class="space-y-6">
              <!-- 章节1：供应链概述 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  供应链概述
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/6</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item active" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链数据预处理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商绩效评估</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c1')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">A</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链基本概念</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链核心流程</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链管理目标</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节2：需求预测 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  需求预测
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(3)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">3</div>
                    <div class="flex-1">
                      <div class="font-medium">移动平均预测</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(4)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">4</div>
                    <div class="flex-1">
                      <div class="font-medium">指数平滑预测</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">预测方法比较</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">预测误差分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：库存管理 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  库存管理
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">EOQ经济订货量</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(6)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">6</div>
                    <div class="flex-1">
                      <div class="font-medium">安全库存计算</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">库存成本分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">库存ABC分类</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节4：供应商管理 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  供应商管理
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(7)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">7</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商选择</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(8)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">8</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商评估</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商KPI</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c9')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">I</div>
                    <div class="flex-1">
                      <div class="font-medium">供应商关系管理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节5：供应链数据分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  供应链数据分析
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(9)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">9</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链数据分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(10)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">10</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链可视化</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节6：供应链风险与优化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter6')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"></i>
                  供应链风险与优化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter6-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链风险管理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c11')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">K</div>
                    <div class="flex-1">
                      <div class="font-medium">供应链优化策略</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>'''
    
    new_chapter_list = '''            <!-- 章节列表 -->
            <div class="space-y-6">
              <!-- 章节1：BI基础与SQL -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  BI基础与SQL
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/7</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item active" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询：各地区销售额</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">10分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">Python：计算同比增长率</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">10分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq1')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">1</div>
                    <div class="flex-1">
                      <div class="font-medium">BI概念与价值</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">2</div>
                    <div class="flex-1">
                      <div class="font-medium">数据价值链条</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">3</div>
                    <div class="flex-1">
                      <div class="font-medium">BI架构与ETL</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节2：数据分析思维 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  数据分析思维
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/4</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(3)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">3</div>
                    <div class="flex-1">
                      <div class="font-medium">Python：多维度统计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">4</div>
                    <div class="flex-1">
                      <div class="font-medium">四种分析层次</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">5</div>
                    <div class="flex-1">
                      <div class="font-medium">维度拆解</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：SQL高级应用 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  SQL高级应用
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(4)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">4</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL窗口函数：累计销售额</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">10分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(7)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL子查询：高价值客户</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">6</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询基础</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">7</div>
                    <div class="flex-1">
                      <div class="font-medium">JOIN查询</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">8</div>
                    <div class="flex-1">
                      <div class="font-medium">窗口函数</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节4：商务分析模型 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  商务分析模型
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/6</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">6</div>
                    <div class="flex-1">
                      <div class="font-medium">Python：RFM用户分层</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(6)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">7</div>
                    <div class="flex-1">
                      <div class="font-medium">Python：ABC商品分类</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(8)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">8</div>
                    <div class="flex-1">
                      <div class="font-medium">Python：时间序列移动平均</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq9')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">9</div>
                    <div class="flex-1">
                      <div class="font-medium">数据仓库与维度建模</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq12')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">10</div>
                    <div class="flex-1">
                      <div class="font-medium">RFM模型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq13')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">11</div>
                    <div class="flex-1">
                      <div class="font-medium">ABC分类法</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节5：综合应用与工具 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  综合应用与工具
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/9</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">12</div>
                    <div class="flex-1">
                      <div class="font-medium">数据分层</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq11')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">13</div>
                    <div class="flex-1">
                      <div class="font-medium">Excel高级函数</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq14')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">14</div>
                    <div class="flex-1">
                      <div class="font-medium">Power BI与DAX</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq15')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">15</div>
                    <div class="flex-1">
                      <div class="font-medium">Python数据分析库</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq16')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">16</div>
                    <div class="flex-1">
                      <div class="font-medium">同比环比计算</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq17')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">17</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL聚合函数</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq18')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">18</div>
                    <div class="flex-1">
                      <div class="font-medium">数据可视化原则</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq19')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">19</div>
                    <div class="flex-1">
                      <div class="font-medium">窗口函数应用</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('bi-cq20')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">20</div>
                    <div class="flex-1">
                      <div class="font-medium">数据治理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>'''
    
    # 替换章节列表
    content = content.replace(old_chapter_list, new_chapter_list)
    
    # 替换其他显示文本
    old_problem_title = '<h3 class="text-xl font-bold text-gray-200" id="problem-title">问题1：供应链数据预处理</h3>'
    new_problem_title = '<h3 class="text-xl font-bold text-gray-200" id="problem-title">SQL查询：计算各地区销售额</h3>'
    content = content.replace(old_problem_title, new_problem_title)
    
    old_problem_desc1 = '<p>编写一个程序，对供应链数据进行预处理，包括缺失值处理、异常值检测等。</p>'
    new_problem_desc1 = '<p>编写SQL查询语句，计算每个地区的总销售额和订单数量，按销售额降序排列。</p>'
    content = content.replace(old_problem_desc1, new_problem_desc1)
    
    old_problem_desc2 = '<p>包含缺失值和异常值的供应链数据</p>'
    new_problem_desc2 = '<p>分析不同地区的销售表现</p>'
    content = content.replace(old_problem_desc2, new_problem_desc2)
    
    # 替换章节标题映射
    old_chapter_titles = '''        1: '供应链概述',
        2: '需求预测',
        3: '库存管理',
        4: '供应商管理',
        5: '供应链数据分析',
        6: '供应链风险与优化' '''
    new_chapter_titles = '''        1: 'BI基础与SQL',
        2: '数据分析思维',
        3: 'SQL高级应用',
        4: '商务分析模型',
        5: '综合应用与工具' '''
    content = content.replace(old_chapter_titles, new_chapter_titles)
    
    # 替换问题4中的内容
    old_code_analysis_part1 = '''                <h4>解题思路</h4>
                <p>1. 使用Pandas的isnull()和sum()方法识别并统计缺失值</p>
                <p>2. 根据数据类型选择合适的填充方法：数值型数据使用均值或中位数，分类型数据使用众数</p>
                <p>3. 使用IQR方法检测异常值</p>
                <h4>代码示例</h4>
                <div class="bg-dark p-3 rounded-lg font-mono text-sm">
                  <pre class="text-cyan-300">
import pandas as pd
import numpy as np

# 创建示例数据
data = {
    'product_id': [1, 2, 3, 4, 5, 6],
    'demand': [100, 120, np.nan, 150, 200, 1000],
    'lead_time': [7, 8, 6, np.nan, 9, 8],
    'supplier': ['A', 'B', 'A', 'C', 'B', 'A']
}
df = pd.DataFrame(data)

# 识别缺失值
print("缺失值统计:")
print(df.isnull().sum())

# 处理缺失值
df['demand'] = df['demand'].fillna(df['demand'].mean())
df['lead_time'] = df['lead_time'].fillna(df['lead_time'].median())

# 检测异常值（IQR方法）
Q1 = df['demand'].quantile(0.25)
Q3 = df['demand'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['demand'] < lower) | (df['demand'] > upper)]
print("\\n检测到的异常值:")
print(outliers)

# 处理异常值（截断）
df['demand'] = df['demand'].clip(lower, upper)

print("\\n处理后的数据:")
print(df)
                  </pre>
                </div>
                <h4>知识点</h4>
                <ul class="list-disc list-inside space-y-1 mt-2">
                  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('data-preprocessing')">数据预处理</a></li>
                  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('pandas-basics')">Pandas基础</a></li>
                  <li>缺失值和异常值处理</li>
                </ul>'''
    new_code_analysis_part1 = '''                <h4>解题思路</h4>
                <p>1. 使用INNER JOIN或LEFT JOIN连接users和orders表</p>
                <p>2. 使用GROUP BY按地区分组</p>
                <p>3. 使用SUM()计算总销售额，COUNT()计算订单数量</p>
                <p>4. 使用ORDER BY按销售额降序排列</p>
                <h4>SQL示例</h4>
                <div class="bg-dark p-3 rounded-lg font-mono text-sm">
                  <pre class="text-cyan-300">
SELECT 
    u.region AS 地区,
    SUM(o.amount) AS 总销售额,
    COUNT(o.order_id) AS 总订单数
FROM orders o
INNER JOIN users u ON o.user_id = u.user_id
GROUP BY u.region
ORDER BY 总销售额 DESC;
                  </pre>
                </div>
                <h4>知识点</h4>
                <ul class="list-disc list-inside space-y-1 mt-2">
                  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter3')">第3章：SQL查询</a></li>
                  <li><a href="#" class="text-cyan-400 hover:underline" onclick="showTab('knowledge'); scrollToKnowledge('chapter2')">第2章：维度拆解</a></li>
                </ul>'''
    content = content.replace(old_code_analysis_part1, new_code_analysis_part1)
    
    # 保存文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 已修复题目标题与内容不符的问题！")
    print("📝 修改内容包括：")
    print("   - 左侧章节标题全部替换为商务智能相关")
    print("   - 所有题目标题替换为对应的BI题目")
    print("   - 章节标题映射更新")
    print("   - 问题描述和答案解析更新")

if __name__ == '__main__':
    main()
