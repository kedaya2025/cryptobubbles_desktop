#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打包脚本 - 将 Crypto Bubbles 应用打包成 .exe 文件
"""

import os
import sys
import subprocess


def install_pyinstaller():
    """安装 PyInstaller"""
    print("正在安装 PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller 安装成功")
        return True
    except Exception as e:
        print(f"❌ PyInstaller 安装失败: {e}")
        return False


def build_exe():
    """打包成 .exe 文件"""
    print("\n" + "=" * 50)
    print("开始打包 Crypto Bubbles 应用")
    print("=" * 50 + "\n")
    
    # PyInstaller 命令参数
    cmd = [
        "pyinstaller",
        "--onefile",                    # 打包成单个文件
        "--windowed",                   # 无控制台窗口
        "--name=CryptoBubbles",         # 应用名称
        "--icon=NONE",                  # 图标（暂无）
        "--clean",                      # 清理临时文件
        "--noconfirm",                  # 不询问确认
        "crypto_bubbles_app.py"
    ]
    
    try:
        print("正在打包，请稍候...")
        print("这可能需要几分钟时间...\n")
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("\n" + "=" * 50)
        print("✅ 打包成功！")
        print("=" * 50)
        print(f"\n可执行文件位置: {os.path.abspath('dist/CryptoBubbles.exe')}")
        print("\n你可以直接运行 dist/CryptoBubbles.exe")
        print("无需安装 Python 或任何依赖！")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 50)
        print("❌ 打包失败")
        print("=" * 50)
        print(f"\n错误信息: {e}")
        if e.stderr:
            print(f"详细错误: {e.stderr}")
        return False


def main():
    """主函数"""
    print("Crypto Bubbles - EXE 打包工具\n")
    
    # 检查源文件是否存在
    if not os.path.exists("crypto_bubbles_app.py"):
        print("❌ 错误: 找不到 crypto_bubbles_app.py 文件")
        sys.exit(1)
    
    # 安装 PyInstaller
    if not install_pyinstaller():
        sys.exit(1)
    
    # 打包
    if build_exe():
        print("\n🎉 完成！你现在可以分享 CryptoBubbles.exe 给其他人使用了！")
    else:
        print("\n请检查错误信息并重试")
        sys.exit(1)


if __name__ == "__main__":
    main()
