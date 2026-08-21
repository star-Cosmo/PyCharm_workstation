"""
批量文件重命名工具
用于批量重命名指定目录下的文件

使用方法：
1. 运行脚本
2. 输入目标目录路径
3. 输入要查找的文本
4. 输入替换文本
"""

import os
import sys


def batch_rename(directory, find_text, replace_text):
    """批量重命名文件"""
    if not os.path.exists(directory):
        print(f"错误：目录不存在 - {directory}")
        return 0
    
    count = 0
    for filename in os.listdir(directory):
        if find_text in filename:
            new_filename = filename.replace(find_text, replace_text)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            try:
                os.rename(old_path, new_path)
                print(f"已重命名: {filename} -> {new_filename}")
                count += 1
            except Exception as e:
                print(f"重命名失败: {filename} - {e}")
    
    return count


def main():
    print("=" * 50)
    print("批量文件重命名工具")
    print("=" * 50)
    
    directory = input("请输入目标目录路径: ").strip()
    if not directory:
        print("错误：目录路径不能为空")
        return
    
    find_text = input("请输入要查找的文本: ").strip()
    replace_text = input("请输入替换文本: ").strip()
    
    print(f"\n正在处理目录: {directory}")
    print(f"查找: '{find_text}' -> 替换: '{replace_text}'")
    print("-" * 50)
    
    count = batch_rename(directory, find_text, replace_text)
    
    print("-" * 50)
    print(f"完成！共重命名 {count} 个文件")


if __name__ == "__main__":
    main()
