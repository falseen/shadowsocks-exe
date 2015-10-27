# -*- mode: python -*-

block_cipher = None


a = Analysis(['ss\\shadowsocks\\local.py'],
             pathex=['ss'],
             binaries=[('libeay32.dll','')],
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=['path.py'],
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ss_local',
          debug=False,
          strip=None,
          upx=True,
          console=True )