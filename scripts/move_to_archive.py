# -*- coding: utf-8 -*-
import shutil
import os
import sys

# 设置输出编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 要移动的文件列表
files_to_move = [
    '活书简单介绍.md',
    '活书.md',
    '活书项目商业计划书.md',
    '活书MVP.md',
    '活书MVP技术文档.md',
    '活书MVP1.0.md',
    '活书MVP1.1.md',
    '活书MVP2.0.md',
    '活书内部思考.md',
    '《KAIROS活书 - 可行性方案》V1.0.md'
]

archive_dir = '99_归档'

# 确保归档目录存在
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)

# 移动文件
moved = []
not_found = []

for filename in files_to_move:
    if os.path.exists(filename):
        try:
            dest = os.path.join(archive_dir, filename)
            shutil.move(filename, dest)
            moved.append(filename)
            print(f"[OK] Moved: {filename}")
        except Exception as e:
            print(f"[ERROR] Failed to move {filename}: {e}")
    else:
        not_found.append(filename)
        print(f"[WARN] Not found: {filename}")

print(f"\n总计: 移动 {len(moved)} 个文件")
if not_found:
    print(f"未找到: {len(not_found)} 个文件")

