"""
BLC 黑电平校正 RGB 分析工具
用于 ISP 调试第一步：计算 sensor 黑电平参数

使用方法：
1. 把 sensor 用黑布盖住（无光环境）
2. 拍一张照片
3. 运行脚本，弹出窗口选择图片
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog


def analyze_rgb(image_path):
    """分析图片 RGB 值，用于 BLC 黑电平校正"""
    img = cv2.imread(image_path)
    if img is None:
        print(f"错误：无法读取图片 {image_path}")
        return
    
    # BGR 通道（OpenCV 默认顺序）
    b_channel = img[:,:,0]
    g_channel = img[:,:,1]
    r_channel = img[:,:,2]
    
    # 计算各通道平均值
    r_avg = np.mean(r_channel)
    g_avg = np.mean(g_channel)
    b_avg = np.mean(b_channel)
    
    print("=" * 50)
    print("RGB 通道分析结果")
    print("=" * 50)
    print(f"R 通道平均值: {r_avg:.2f}")
    print(f"G 通道平均值: {g_avg:.2f}")
    print(f"B 通道平均值: {b_avg:.2f}")
    print("=" * 50)
    print("BLC 计算公式: BLC值 = RGB值 × (-16)")
    print("=" * 50)
    print(f"建议 BLC_R:  {int(r_avg * -16)}")
    print(f"建议 BLC_G:  {int(g_avg * -16)}")
    print(f"建议 BLC_B:  {int(b_avg * -16)}")
    print("=" * 50)


def select_file():
    """弹出文件选择窗口"""
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    file_path = filedialog.askopenfilename(
        title="选择图片文件",
        filetypes=[
            ("图片文件", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("所有文件", "*.*")
        ]
    )
    
    root.destroy()
    return file_path


if __name__ == "__main__":
    print("正在打开文件选择窗口...")
    image_path = select_file()
    
    if image_path:
        print(f"已选择: {image_path}")
        analyze_rgb(image_path)
    else:
        print("未选择文件")
