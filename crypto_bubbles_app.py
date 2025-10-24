#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crypto Bubbles 网页封装器
将 https://cryptobubbles.net/ 封装成桌面应用
"""

import webview
import sys


class CryptoBubblesApp:
    """Crypto Bubbles 应用类"""
    
    def __init__(self):
        self.url = "https://cryptobubbles.net/"
        self.window = None
    
    def run(self):
        """运行应用"""
        print("=" * 50)
        print("Crypto Bubbles - 加密货币气泡图")
        print("正在启动应用...")
        print("=" * 50)
        
        # 创建窗口
        self.window = webview.create_window(
            title='Crypto Bubbles - 加密货币气泡图',
            url=self.url,
            width=1400,
            height=900,
            resizable=True,
            fullscreen=False,
            min_size=(800, 600),
            background_color='#1a1a1a'
        )
        
        # 启动应用
        webview.start(debug=False)


def main():
    """主函数"""
    try:
        app = CryptoBubblesApp()
        app.run()
    except KeyboardInterrupt:
        print("\n应用已关闭")
        sys.exit(0)
    except Exception as e:
        print(f"启动失败: {e}")
        print("\n提示: 请确保已安装 pywebview")
        print("安装命令: pip install pywebview")
        sys.exit(1)


if __name__ == "__main__":
    main()
