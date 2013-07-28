"""
#########################################################################
Author: Shalin Shah
Project: DNA Cloud
Graduate Mentor: Dixita Limbachya
Mentor: Prof. Manish K Gupta
Date: 28 July 2013
Website: www.guptalab.org/dnacloud
This module is used to freeze the application.
#########################################################################
"""

from cx_Freeze import setup, Executable

includes = ["extraModules","panels","barcodeGenerator","encode","decode","HuffmanDictionary","pytxt2pdf"]
excludes = [
    '_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
    'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
    'Tkconstants', 'Tkinter'
]
include_files = ['barcode/','PIL/']

build_exe_options = {
                     "includes":includes, 
                     "excludes":excludes,
                     "include_files":include_files
}
 
exe = Executable(
    script="MainFrame.py",
    base="Win32GUI"
)
 
setup(
    name = "Dna-Cloud",
    version = "1",
    description = "Dna Cloud - Converter",
    options = {"build_exe": build_exe_options},
    executables = [exe]
)
