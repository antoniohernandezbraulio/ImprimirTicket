import cx_Freeze

executables = [cx_Freeze.Executable("printCode.py",
                                   base = "Win32GUI",
                                   icon = None)]

build_exe_options = {"packages": [],
                     "include_files":["confCode.py"]}

cx_Freeze.setup(
    name = "printCode",
    version = "1.0",
    description = "printCode",
    options = {"build_exe": build_exe_options},
    executables = executables
    )