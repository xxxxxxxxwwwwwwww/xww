import re

# 读取文件
with open('data-analysis-tech.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 新的题目列表HTML
new_chapter_content = """              <!-- 章节1：数据分析基础 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter1')">
                  <i class="fa fa-chevron-down text-gray-400 transition-transform duration-300" id="chapter1-icon"></i>
                  数据分析基础
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content" id="chapter1-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item active" onclick="loadProgrammingProblem(1)">
                    <div class="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-gray-900 font-bold">1</div>
                    <div class="flex-1">
                      <div class="font-medium">数据分析流程</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(2)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">2</div>
                    <div class="flex-1">
                      <div class="font-medium">缺失值处理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">15分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(3)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">3</div>
                    <div class="flex-1">
                      <div class="font-medium">异常值检测</div>
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
                      <div class="font-medium">数据分析定义</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c2')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">B</div>
                    <div class="flex-1">
                      <div class="font-medium">CRISP-DM方法论</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节2：数据准备与清洗 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter2')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter2-icon"></i>
                  数据准备与清洗
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/4</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter2-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c3')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">C</div>
                    <div class="flex-1">
                      <div class="font-medium">缺失值处理</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c4')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">D</div>
                    <div class="flex-1">
                      <div class="font-medium">异常值检测</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节3：核心工具实操 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter3')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter3-icon"></i>
                  核心工具实操
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/4</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter3-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(4)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">4</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询实战</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c5')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">E</div>
                    <div class="flex-1">
                      <div class="font-medium">SQL查询</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c6')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">F</div>
                    <div class="flex-1">
                      <div class="font-medium">Pandas操作</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节4：统计分析方法 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter4')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter4-icon"></i>
                  统计分析方法
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/5</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter4-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(5)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">5</div>
                    <div class="flex-1">
                      <div class="font-medium">描述性统计分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-gray-400">10分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(6)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">6</div>
                    <div class="flex-1">
                      <div class="font-medium">假设检验</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">20分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadProgrammingProblem(7)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">7</div>
                    <div class="flex-1">
                      <div class="font-medium">线性回归</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-gray-400">25分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c7')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">G</div>
                    <div class="flex-1">
                      <div class="font-medium">描述性统计</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c8')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">H</div>
                    <div class="flex-1">
                      <div class="font-medium">假设检验</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节5：高级数据分析 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter5')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter5-icon"></i>
                  高级数据分析
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/3</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter5-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">编程题</div>
                  <div class="problem-item" onclick="loadProgrammingProblem(8)">
                    <div class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center font-bold">8</div>
                    <div class="flex-1">
                      <div class="font-medium">K-Means聚类</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-hard">困难</span>
                        <span class="text-xs text-gray-400">30分钟</span>
                      </div>
                    </div>
                  </div>
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-4">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c9')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">I</div>
                    <div class="flex-1">
                      <div class="font-medium">机器学习类型</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c10')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">J</div>
                    <div class="flex-1">
                      <div class="font-medium">回归分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节6：数据可视化 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter6')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter6-icon"></i>
                  数据可视化
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter6-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c11')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">K</div>
                    <div class="flex-1">
                      <div class="font-medium">数据可视化</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c12')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">L</div>
                    <div class="flex-1">
                      <div class="font-medium">报告撰写</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节7：行业实战案例 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter7')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter7-icon"></i>
                  行业实战案例
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/2</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter7-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c13')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">M</div>
                    <div class="flex-1">
                      <div class="font-medium">RFM分析</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c14')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">N</div>
                    <div class="flex-1">
                      <div class="font-medium">转化率</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-easy">简单</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 章节8：课程总结 -->
              <div class="chapter-item">
                <h3 class="topic-title" onclick="toggleChapter('chapter8')">
                  <i class="fa fa-chevron-right text-gray-400 transition-transform duration-300" id="chapter8-icon"></i>
                  课程总结
                  <span class="ml-auto text-xs text-gray-400">
                    <span class="chapter-progress">0/1</span>
                    <span class="progress-percentage">(0%)</span>
                  </span>
                </h3>
                <div class="chapter-content collapsed" id="chapter8-content">
                  <div class="text-xs text-gray-500 uppercase tracking-wider mb-2 mt-2">选择题</div>
                  <div class="problem-item" onclick="loadChoiceQuestion('c15')">
                    <div class="w-8 h-8 rounded-full bg-purple-700 flex items-center justify-center font-bold text-sm">O</div>
                    <div class="flex-1">
                      <div class="font-medium">职业发展</div>
                      <div class="flex items-center gap-2 mt-1">
                        <span class="difficulty-tag difficulty-medium">中等</span>
                        <span class="text-xs text-purple-400">选择题</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>"""

# 找到并替换题目列表区域
pattern = r"(<!-- 章节1：.*?-->\s*<div class=\"chapter-item\">.*?)</div>\s*</div>\s*</div>\s*</div>"
content = re.sub(pattern, new_chapter_content, content, flags=re.DOTALL)

# 写入更新后的文件
with open('data-analysis-tech.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("题目列表更新完成！")
