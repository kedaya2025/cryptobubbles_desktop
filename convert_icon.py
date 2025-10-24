#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 PNG 图标转换为 ICO 格式
"""

from PIL import Image
import sys


def convert_png_to_ico(png_path, ico_path):
    """
    将 PNG 转换为 ICO
    
    Args:
        png_path: PNG 文件路径
        ico_path: 输出的 ICO 文件路径
    """
    try:
        print(f"正在转换 {png_path} 为 {ico_path}...")
        
        # 打开 PNG 图片
        img = Image.open(png_path)
        
        # 转换为 RGBA 模式（如果不是的话）
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # 创建多个尺寸的图标（Windows 标准）
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # 保存为 ICO 格式
        img.save(ico_path, format='ICO', sizes=icon_sizes)
        
        print(f"✅ 转换成功！ICO 文件已保存到: {ico_path}")
        return True
        
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        return False


def main():
    """主函数"""
    png_file = "logo64.png"
    ico_file = "logo.ico"
    
    print("=" * 50)
    print("PNG 转 ICO 工具")
    print("=" * 50 + "\n")
    
    if convert_png_to_ico(png_file, ico_file):
        print("\n现在可以重新打包应用了！")
    else:
        print("\n请确保已安装 Pillow 库: pip install Pillow")
        sys.exit(1)


if __name__ == "__main__":
    main()
