from os import environ, system, remove, listdir
from shutil import move, rmtree

program_name = "Bullet Rain"
main_file = "main.py"
libraries_used = ["pygame", "random"]
files_needed = ["gameClasses.py", "gameFunctions.py", "gameVariables.py", "settings.json", "kunstler.ttf",
                "settings.py", "stage.py", "vgafix.fon", "images", "sounds"]
program_description = "Bullet Rain is a side-view platform based shooter game where two players " \
                      "go head to head in an epic battle for the glory!!!"
program_version = "0.1.4"

python_path = r"C:\Users\Games\AppData\Local\Programs\Python\Python36"


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


environ['TCL_LIBRARY'] = rf'{python_path}\tcl\tcl8.6'
environ['TK_LIBRARY'] = rf'{python_path}\tcl\tk8.6'
libraries_used.append("cx_Freeze")
system(rf"{python_path}\python.exe -m pip install --upgrade pip")
for i in libraries_used:
    system(rf"{python_path}\Scripts\pip.exe install {i}")

#system(rf"{python_path}\python.exe setup.py build")  # for having just the exe
system(rf"{python_path}\python.exe setup.py bdist_msi")  # for creating msi installer
#system(rf"{python_path}\python.exe setup.py bdist_dmg")  # only on mac create an installer

remove("setup.py")

# this part down here leaves only the installer
for i in listdir("dist"):
    move(rf".\dist\{i}", rf".\{i}")
rmtree(r".\dist")
rmtree(r".\build")
