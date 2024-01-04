#!/usr/bin/python3
exec('import ctypes;ctypes.CDLL("libc.so.6").write(1, b"#pythoniscool\\n", 14)')
