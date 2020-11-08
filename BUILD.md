### Windows EXE
- Install MSYS2 (msys2.org)
- Run Mingw64:
  - Update system ($ pacman -Suuy)
  - Install tools (see gtk.org/docs/installations/windows#using-gtk-from-msys2-packages)
  - Install UPX ($ pacman -S upx)
  - Install PyInstaller ($ pacman -S python-pip || $ pip install PyInstaller)
  - Build using spec file ($ pyinstaller pyinstaller/Cipher-dir.spec)

#### Old info?
- Install Python3
  - from: python.org/downloads/windows (~100 MB)
- Install pyinstaller
  - > pip install pyinstaller
- Install C++ Build Tools
  - from: visualstudio.microsoft.com/visual-cpp-build-tools (~80 MB)
  - from: VisualStudio Installer install C++ Build Tools (279 MB)
- Install PyGObject
  - > pip install PyGObject

### Linux ELF (needs work)
```bash
$ pyinstaller --clean --windowed --onefile --icon ./data/icons/cipher.svg --name Cipher ./bin/cipher

# === Standard version ===
(env) $ pyinstaller --clean -F -n "ModemCheck v0.6" __main__.py

# === Debug version ======
(env) $ pyinstaller --clean -F -n "ModemCheck(dbg) v0.6" -d __main__.py
```
