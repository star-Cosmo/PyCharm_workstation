"""
文件搜索工具
在指定目录中搜索包含特定文本的文件

使用方法：
1. 运行脚本
2. 输入目标目录路径
3. 输入要搜索的文本
"""

import os


def search_files(directory, search_text):
    """搜索文件中的文本"""
    results = []
    
    if not os.path.exists(directory):
        print(f"错误：目录不存在 - {directory}")
        return results
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            try:
                # 尝试以文本方式读取文件
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        if search_text in line:
                            results.append({
                                'file': filepath,
                                'line': line_num,
                                'content': line.strip()
                            })
            except Exception:
                # 跳过无法读取的文件（如二进制文件）
                continue
    
    return results


def main():
    print("=" * 50)
    print("文件搜索工具")
    print("=" * 50)
    
    directory = input("请输入目标目录路径: ").strip()
    if not directory:
        print("错误：目录路径不能为空")
        return
    
    search_text = input("请输入要搜索的文本: ").strip()
    if not search_text:
        print("错误：搜索文本不能为空")
        return
    
    print(f"\n正在搜索目录: {directory}")
    print(f"搜索文本: '{search_text}'")
    print("-" * 50)
    
    results = search_files(directory, search_text)
    
    if results:
        print(f"找到 {len(results)} 个匹配:")
        for result in results:
            print(f"\n文件: {result['file']}")
            print(f"行号: {result['line']}")
            print(f"内容: {result['content']}")
    else:
        print("未找到匹配项")
    
    print("-" * 50)
    print("搜索完成")


if __name__ == "__main__":
    main()
