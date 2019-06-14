import os

program_name = "Bullet Rain"
main_file = "main.py"
libraries_used = ["pygame", "random"]
files_needed = ["gameClasses.py", "gameFunctions.py", "gameVariables.py", "settings.json", "kunstler.ttf",
                "settings.py", "stage.py", "vgafix.fon", "images", "sounds"]
program_description = "Bullet Rain is a side-view platform based shooter game where two players " \
                      "go head to head in an epic battle for the glory!!!"
program_version = "0.1.4"

python_path = r"D:\Python36"


code = f"""\
import cx_Freeze

cx_Freeze.setup(
    name="{program_name}",
    version = "{program_version}",
    description = "{program_description}",
    options={{"build_exe": {{"packages": {libraries_used},
                           "include_files": {files_needed}}}}},
    executables=[cx_Freeze.Executable("{main_file}")]

)
"""

with open("setup.py", 'w') as setup_file:
    setup_file.write(code)


os.environ['TCL_LIBRARY'] = rf'{python_path}\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = rf'{python_path}\tcl\tk8.6'
os.system(rf"{python_path}\Scripts\pip.exe install cx_Freeze")

os.system(rf"{python_path}\python.exe setup.py build")
#os.system(rf"{python_path}\python.exe setup.py bdist_msi")  # for creating msi installer
#os.system(rf"{python_path}\python.exe setup.py bdist_dmg")  # only on mac create an installer

os.remove("setup.py")
