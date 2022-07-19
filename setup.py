import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {"build_exe": {"includes": "atexit"}}

executables = [Executable("sand_txt.py", base=base)]

setup(
    name="Sand",
    version="1.1",
    description="Sample cx_Freeze PyQt5 script",
    options=options,
    executables=executables,
)