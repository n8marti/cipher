### Windows EXE
>s:
>cd \modem-check\src

```shell
> pyinstaller --clean --windowed --onefile --icon ./data/icons/cipher.svg --name Cipher.exe ./bin/cipher

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
