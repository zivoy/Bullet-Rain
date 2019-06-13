import cx_Freeze
import os

executables = [cx_Freeze.Executable("main.py")]

os.environ['TCL_LIBRARY'] = r'D:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Python36\tcl\tk8.6'
cx_Freeze.setup(
    name="Bullet Rain",
    options={"build_exe": {"packages": ["pygame", "random"],
                           "include_files": ["gameClasses.py", "gameFunctions.py", "gameVariables.py", "settings.json",
                                             "kunstler.ttf", "settings.py", "stage.py", "vgafix.fon", "images",
                                             "sounds"]}},
    executables=executables

)

# python setup.py build
# python setup.py bdist_msi
