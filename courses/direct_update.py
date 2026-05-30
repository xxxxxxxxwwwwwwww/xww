
import re

def replace_section_in_file(target_file, source_file):
    """
    从源文件读取更新后的problems和choiceQuestions部分，替换目标文件中的相应部分
    """
    # 读取源文件和目标文件
    with open(source_file, 'r', encoding='utf-8') as f:
        source_content = f.read()
    
    with open(target_file, 'r', encoding='utf-8') as f:
        target_content = f.read()
    
    # 提取源文件中的内容
    problems_start = source_content.find('    // 问题数据\n    const problems = [')
    choices_end = source_content.find('    // 初始化\n    const', problems_start)
    updated_data = source_content[problems_start:choices_end]
    
    # 提取题库章节标题和右侧注释之间的内容作为参考
    left_start = target_content.find('            &lt;h2 class="section-title"&gt;', 
                                   target_content.find('题库标签页'))
    right_start = target_content.find('          &lt;!-- 右侧：问题、代码编辑器、运行结果、答案解析 --&gt;', left_start)
    
    # 替换数据部分
    old_problems_start = target_content.find('    // 问题数据\n    const problems = [')
    old_choices_end = target_content.find('    // 初始化\n    const', old_problems_start)
    
    target_content = target_content[:old_problems_start] + updated_data + target_content[old_choices_end:]
    
    # 写入更新后的文件
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(target_content)
    
    print(f"成功更新 {target_file} 的题目数据！")

def main():
    print("=" * 60)
    print("开始更新课程题库")
    print("=" * 60)
    
    # 更新数据库原理
    replace_section_in_file('database-principles.html', 'database-principles-updated.html')
    
    # 更新商务智能
    replace_section_in_file('business-intelligence.html', 'business-intelligence-updated.html')
    
    # 更新供应链分析
    replace_section_in_file('supply-chain-analysis.html', 'supply-chain-updated.html')
    
    print("=" * 60)
    print("所有课程题目数据更新完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()

