"""
系统信息查看工具
获取当前系统的基本信息

使用方法：
直接运行脚本即可显示系统信息
"""

import platform
import sys
import os
from datetime import datetime


def get_system_info():
    """获取系统信息"""
    info = {
        "操作系统": platform.system(),
        "操作系统版本": platform.version(),
        "系统架构": platform.architecture()[0],
        "处理器": platform.processor(),
        "Python版本": platform.python_version(),
        "当前时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "当前用户": os.getenv("USERNAME", "未知"),
        "当前目录": os.getcwd(),
    }
    return info


def main():
    print("=" * 50)
    print("系统信息查看工具")
    print("=" * 50)
    
    info = get_system_info()
    
    for key, value in info.items():
        print(f"{key}: {value}")
    
    print("=" * 50)
    
    # 显示磁盘空间（仅Windows）
    if platform.system() == "Windows":
        try:
            import shutil
            total, used, free = shutil.disk_usage("C:\\")
            print(f"\nC盘空间:")
            print(f"  总空间: {total // (1024**3)} GB")
            print(f"  已使用: {used // (1024**3)} GB")
            print(f"  可用空间: {free // (1024**3)} GB")
        except Exception as e:
            print(f"无法获取磁盘信息: {e}")


if __name__ == "__main__":
    main()
