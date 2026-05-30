import os

# 读取原始文件
with open('data-analysis-tech.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 读取新内容
with open('courses/chapter8-summary.html', 'r', encoding='utf-8') as f:
    new_content = f.read()

# 找到需要替换的范围
# 从678行（索引677）到2457行（索引2456），保留第678行之前的内容
before_content = ''.join(lines[:678])
after_content = ''.join(lines[2457:])

# 组合新文件
new_file = before_content + new_content + after_content

# 写入新文件
with open('data-analysis-tech.html', 'w', encoding='utf-8') as f:
    f.write(new_file)

print(f"文件更新完成！")
print(f"原始文件总行数: {len(lines)}")
print(f"新内容行数: {len(new_content.splitlines())}")
print(f"最终文件行数: {len(new_file.splitlines())}")
