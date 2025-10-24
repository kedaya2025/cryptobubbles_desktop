# Crypto Bubbles Desktop

<div align="center">

![Crypto Bubbles](logo64.png)

A desktop wrapper for [cryptobubbles.net](https://cryptobubbles.net/) - Interactive cryptocurrency bubble chart visualization.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com)

</div>

## ✨ Features

- 🖥️ **Standalone Desktop App** - No browser required
- 🌐 **Full Website Access** - Direct access to cryptobubbles.net
- 📊 **Complete Functionality** - All original features preserved
- 🎨 **Native Experience** - Native window with custom icon
- ⚡ **Lightweight** - Minimal resource usage
- 🔒 **No Dependencies** - Packaged as single executable (optional)

## 📸 Screenshot

The app displays real-time cryptocurrency market data with:
- Bubble size representing market cap
- Color indicating 24h price change (green = up, red = down)
- Interactive hover information
- Time period selection (hour, day, week, month, year)

## 🚀 Quick Start

### Running from Source

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
python crypto_bubbles_app.py
```

### Using Pre-built Executable (Windows)

Download the latest release from the [Releases](../../releases) page and run `CryptoBubbles.exe` directly.

## 🔨 Building Executable

### Windows

```bash
# Install PyInstaller
pip install pyinstaller

# Build with custom icon
python -m PyInstaller --onefile --windowed --name=CryptoBubbles --icon=logo.ico --clean crypto_bubbles_app.py
```

The executable will be created in the `dist/` folder.

### Build Script

For convenience, use the provided build script:

```bash
python build_exe.py
```

## 📋 System Requirements

- **Python:** 3.7 or higher
- **OS:** Windows 7+, macOS 10.10+, or Linux
- **Network:** Internet connection required
- **Memory:** 2GB RAM recommended
- **Disk Space:** ~50MB

## 🛠️ Technical Stack

- **[pywebview](https://pywebview.flowrl.com/)** - Lightweight web view wrapper
- **Backend Support:**
  - Windows: EdgeHTML / MSHTML
  - macOS: WebKit
  - Linux: GTK WebKit2

## 📁 Project Structure

```
crypto-bubbles-desktop/
├── crypto_bubbles_app.py   # Main application
├── build_exe.py            # Build script for executable
├── convert_icon.py         # Icon conversion utility
├── logo64.png              # Application icon (PNG)
├── logo.ico                # Application icon (ICO)
├── requirements.txt        # Python dependencies
├── 刷新图标缓存.bat         # Icon cache refresh (Windows)
└── README.md               # This file
```

## 🔧 Icon Customization

To use your own icon:

1. Replace `logo64.png` with your icon (64x64 or larger)
2. Convert to ICO format:
```bash
python convert_icon.py
```
3. Rebuild the executable

## 🐛 Troubleshooting

### Icon Not Showing (Windows)

If the executable shows the wrong icon:
1. Run `刷新图标缓存.bat` as administrator
2. Or restart Windows Explorer
3. Or restart your computer

### Application Won't Start

- Check your internet connection
- Ensure firewall allows the application
- Try running as administrator

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Crypto Bubbles](https://cryptobubbles.net/) - Original website
- [pywebview](https://pywebview.flowrl.com/) - Desktop wrapper framework

## ⚠️ Disclaimer

This is an unofficial desktop wrapper. All cryptocurrency data is provided by cryptobubbles.net. This project is not affiliated with or endorsed by Crypto Bubbles.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<div align="center">
Made with ❤️ for the crypto community
</div>
