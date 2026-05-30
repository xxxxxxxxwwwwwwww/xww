#!/bin/bash

echo "========================================="
echo "检查data-analysis-tech.html文件"
echo "========================================="
echo ""

# 1. 检查HTML头部
echo "1. 检查HTML头部结构..."
if head -5 data-analysis-tech.html | grep -q "DOCTYPE html"; then
    echo "   ✓ HTML DOCTYPE声明存在"
else
    echo "   ✗ HTML DOCTYPE声明缺失"
fi

if head -5 data-analysis-tech.html | grep -q "UTF-8"; then
    echo "   ✓ UTF-8字符编码设置正确"
else
    echo "   ✗ UTF-8字符编码缺失"
fi

echo ""

# 2. 检查8个章节
echo "2. 检查8个章节是否存在..."
for i in {1..8}; do
    chapter_id="chapter${i}-"
    if grep -q "id=\"${chapter_id}" data-analysis-tech.html; then
        echo "   ✓ 第${i}章存在"
    else
        echo "   ✗ 第${i}章缺失"
    fi
done

echo ""

# 3. 检查导航按钮
echo "3. 检查导航按钮..."
nav_count=$(grep -c "data-target=\"chapter" data-analysis-tech.html)
echo "   找到 ${nav_count} 个章节导航按钮"
if [ $nav_count -eq 8 ]; then
    echo "   ✓ 导航按钮数量正确（8个）"
else
    echo "   ✗ 导航按钮数量错误（期望8个）"
fi

echo ""

# 4. 检查JavaScript代码
echo "4. 检查JavaScript代码..."
if grep -q "section.style.display = 'none'" data-analysis-tech.html; then
    echo "   ✓ 章节切换使用内联样式"
else
    echo "   ✗ 章节切换未使用内联样式"
fi

if grep -q "section.classList.add('hidden')" data-analysis-tech.html; then
    echo "   ✗ 发现使用CSS类的代码（应该使用内联样式）"
else
    echo "   ✓ 未使用CSS类进行切换"
fi

echo ""

# 5. 检查关键元素
echo "5. 检查关键元素..."
if grep -q "id=\"question-bank\"" data-analysis-tech.html; then
    echo "   ✓ 题库标签页存在"
fi

if grep -q "id=\"codeEditor\"" data-analysis-tech.html; then
    echo "   ✓ 代码编辑器存在"
fi

if grep -q "id=\"knowledge\"" data-analysis-tech.html; then
    echo "   ✓ 知识点标签页存在"
fi

echo ""

# 6. 统计文件信息
echo "6. 文件统计信息..."
line_count=$(wc -l < data-analysis-tech.html)
echo "   总行数: $line_count"
char_count=$(wc -c < data-analysis-tech.html)
echo "   总字符数: $char_count"

echo ""
echo "========================================="
echo "检查完成"
echo "========================================="
