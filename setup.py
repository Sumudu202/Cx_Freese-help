from cx_Freeze import setup, Executable
import scipy, os, PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.phonon import *
import numpy

includefiles_list=[]
scipy_path = os.path.dirname(scipy.__file__)
PyQt4_path1 = os.path.dirname(PyQt4.QtCore.__file__)
PyQt4_path2 = os.path.dirname(PyQt4.QtGui.__file__)
PyQt4_path3 = os.path.dirname(PyQt4.phonon.__file__)
numpy_path = os.path.dirname(numpy.__file__)

includefiles_list.append(scipy_path)
includefiles_list.append(PyQt4_path1)
includefiles_list.append(PyQt4_path2)
includefiles_list.append(PyQt4_path3)
includefiles_list.append(numpy_path)

# Dependencies are automatically detected, but it might need fine tuning.
buildOptions = dict(
    packages = ['sklearn.utils.sparsetools._graph_validation','cython','sip', 'pywt','pyqtgraph','mkl'],
    excludes = [],
    includes = [],
    include_files = includefiles_list
) 
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
 
executables = [
    Executable('AppName.py', base=base, icon="img/AppName.ico")
]

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "AppName",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]\AppName.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     "TARGETDIR",               # WkDir
     ),

	 ("ProgramMenuShortcut",        # Shortcut
     "ProgramMenuFolder",          # Directory_
     "AppName",     # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]\AppName.exe",   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}#, "Directory": directory_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

setup(
    name='AppName',
	author = "Name",
	author_email="example@gmail.com",
    version = '0.1',
    description = 'AppName',
    options = dict(build_exe = buildOptions, bdist_msi = bdist_msi_options),
    executables = executables
)
