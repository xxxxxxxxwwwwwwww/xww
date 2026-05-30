#!/bin/bash

echo "=== 供应链考试文件诊断 ==="
echo ""
echo "1. 检查文件是否存在："
ls -lh /workspace/courses/supply-chain-analysis-exam.html

echo ""
echo "2. 检查文件大小是否正常："
wc -l /workspace/courses/supply-chain-analysis-exam.html

echo ""
echo "3. 检查HTML结构是否完整："
grep -c "</html>" /workspace/courses/supply-chain-analysis-exam.html
grep -c "<script>" /workspace/courses/supply-chain-analysis-exam.html
grep -c "</script>" /workspace/courses/supply-chain-analysis-exam.html

echo ""
echo "4. 检查关键元素："
grep -c 'id="start-exam"' /workspace/courses/supply-chain-analysis-exam.html
grep -c "addEventListener.*start-exam" /workspace/courses/supply-chain-analysis-exam.html
grep -c "function startExam" /workspace/courses/supply-chain-analysis-exam.html

echo ""
echo "5. 检查DOMContentLoaded事件："
grep -c "DOMContentLoaded" /workspace/courses/supply-chain-analysis-exam.html

echo ""
echo "=== 诊断完成 ==="
