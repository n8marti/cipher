### Windows EXE
- Install MSYS2
- [...]

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
>s:
>cd \modem-check\src

```shell
# For testing the build process start with --onedir option.
> pyinstaller --clean --windowed --onedir --icon ./data/icons/cipher.ico --name Cipher.exe ./bin/cipher
# For distribution use --onefile option.
> pyinstaller --clean --windowed --onefile --icon ./data/icons/cipher.ico --name Cipher.exe ./bin/cipher

# === Standard version ===
>pyinstaller --clean -F -n "ModemCheck v0.6.exe" -i favicon.ico --uac-admin --win-private-assemblies __main__.py

# === Debug version ======
>pyinstaller --clean -F -n "ModemCheck(dbg) v0.6.exe" -i favicon.ico --uac-admin -d --win-private-assemblies __main__.py
```

### Linux executable
```bash
$ pyinstaller --clean --windowed --onefile --icon ./data/icons/cipher.svg --name Cipher ./bin/cipher

# === Standard version ===
(env) $ pyinstaller --clean -F -n "ModemCheck v0.6" __main__.py

# === Debug version ======
(env) $ pyinstaller --clean -F -n "ModemCheck(dbg) v0.6" -d __main__.py
```
