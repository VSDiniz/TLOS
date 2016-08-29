# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 08:06:38 2016

@author: vini_
"""

import cx_Freeze

executables = [cx_Freeze.Executable("TLOS.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )