# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\BaiduNetdiskDownload\\python-demo\\develop_relate\\jiuyou\\src\\main\\python\\main.py'],
             pathex=['D:\\BaiduNetdiskDownload\\python-demo\\develop_relate\\jiuyou\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['d:\\python_data\\centyuan\\pyqt5\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['D:\\BaiduNetdiskDownload\\python-demo\\develop_relate\\jiuyou\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='九游合约_v1.1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , version='D:\\BaiduNetdiskDownload\\python-demo\\develop_relate\\jiuyou\\target\\PyInstaller\\version_info.py', icon='D:\\BaiduNetdiskDownload\\python-demo\\develop_relate\\jiuyou\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='九游合约_v1.1')
