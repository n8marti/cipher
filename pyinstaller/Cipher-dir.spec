# -*- mode: python ; coding: utf-8 -*-
# Hacked hooks come from this link:
# https://github.com/gaphor/gaphor/pull/424/files/fa31b6e87b52c0412f8148a083b6785549b39fc6
# C:/msys64/mingw64/lib/python3.8/site-packages/_pyinstaller_hooks_contrib/hooks/:
#   - hook-gi.repository.HarfBuzz.py
#   - pre_safe_import_module/hook-gi.repository.HarfBuzz.py

block_cipher = None

import sys
sys.modules['FixTk'] = None

a = Analysis(['C:/msys64/home/Test/cipher/bin/cipher'],
             pathex=['C:/msys64/home/Test/cipher'],
             binaries=[],
             datas=[('C:/msys64/home/Test/cipher/data', 'data')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['FixTk',
		'tcl',
		'tk',
		'_tkinker',
		'tkinter',
		'Tkinter',
		'asyncio',
		'doctest',
		'email',
		'fcntl',
		'grp',
		'multiprocessing',
		'org',
		'posix',
		'pwd',
		'resource',
		'subprocess',
		'unittest',
		],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Get rid of unnecessary junk to shrink the app size.
a.datas = [i for i in a.datas if not os.path.dirname(i[1]).startswith("C:/ProgramData")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/bash-completion/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/doc/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/fontconfig/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/gettext")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/gtk-doc/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/icons/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/installed-tests/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/licenses/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/man/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/p11-kit/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/pki/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/sqlite/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/terminfo/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/themes/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/vala/")]
a.datas = [i for i in a.datas if not os.path.dirname(i[0]).startswith("share/xml/")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          name='Cipher',
          debug=False,
          exclude_binaries=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          console=False,
          icon='C:/msys64/home/Test/cipher/data/icons/cipher.ico')

coll = COLLECT(exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	upx_exclude=[],
	name='Cipher')