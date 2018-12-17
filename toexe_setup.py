from cx_Freeze import setup, Executable
import sys
import os

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

options = {
    'build_exe': 
    {
        "packages": ["PyQt5", "PIL"],
        "include_files": [
            ('tcl86t.dll',  os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll')),
            ('tk86t.dll', os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'))
            ],
        'includes': 'atexit',
    },
}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"
else:
    base = "Win64GUI"

executables = [Executable("testQt.py", base=base)]

setup(
    name = "bmpProcessor",
    options = options,
    version = "0.01",
    description = "Batch process bmp files",
    executables = executables
)