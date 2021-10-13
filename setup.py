application_title = "Hello App"
main_python_file = "main.py"

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "Win32":
    base = "Win32GUI"

includes = ["atexit","re"]
setup(
        name = application_title,
        version = "0.1",
        description = "Hello Test",
        options = {"build_exe" : {"includes" : includes}},
        executables = [Executable(main_python_file, base=base)])

