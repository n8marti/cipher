# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import sys
sys.modules['FixTk'] = None

#a = Analysis(['../cipher/bin/cipher'],
a = Analysis(['C:/msys64/home/Test/cipher/bin/cipher'],
             #pathex=['C:/msys64/home/Test/cipher', 'C:/msys64/home/Test/cipher-build'],
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
		#'subprocess',
		#'threading',
		#'shutil',
		#'email',
		#'urllib',
		#'doctest',
		#'unittest',
		#'asyncio',
		#'multiprocessing'
		],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Get rid of all C:\ProgramData junk.
a.datas = [i for i in a.datas if not os.path.dirname(i[1]).startswith("C:/ProgramData")]
# Remove /share/doc stuff.
a.datas = [i for it in a.datas if not os.path.dirname(i[0]).startswith("share/doc/")]

for i in a.datas:
	print(i)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          #a.binaries,	# remove for onedir
          #a.zipfiles,	# remove for onedir
          #a.datas,	# remove for onedir
          [],
          name='Cipher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          #runtime_tmpdir=None, # remove for onedir
          console=True , icon='../cipher/data/icons/cipher.ico')
# Delete comments above and "coll" below to switch to "onefile" mode.
coll = COLLECT(exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	upx_exclude=[],
	name='Cipher')