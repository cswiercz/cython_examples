import numpy

import glob
import os
import shutil

from distutils.core import setup, Command
from distutils.extension import Extension
from Cython.Distutils import build_ext



# define extension (Cython) modules
ext_modules = [
    Extension('memoryview_pointers.matvec',
              sources=[os.path.join('memoryview_pointers','matvec.pyx'),
                       os.path.join('memoryview_pointers','matvec_doit.c')],
              include_dirs = [numpy.get_include()]),
]


class clean(Command):
    """Cleans *.pyc and debian trashs, so you should get the same copy as
    is in the VCS.
    """

    description = "remove build files"
    user_options = [("all", "a", "the same")]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        pass

    def run(self):
        # delete all files ending with certain extensions
        dir_setup = os.path.dirname(os.path.realpath(__file__))
        curr_dir = os.getcwd()
        for root, dirs, files in os.walk(dir_setup):
            for file in files:
                file = os.path.join(root, file)
                if file.endswith('.pyc') and os.path.isfile(file):
                    os.remove(file)
                if file.endswith('~') and os.path.isfile(file):
                    os.remove(file)

        os.chdir(dir_setup)

        # explicity remove files and directories from 'blacklist'
        blacklist = ['build', 'dist', 'doc/_build']
        for file in blacklist:
            if os.path.isfile(file):
                os.remove(file)
            elif os.path.isdir(file):
                shutil.rmtree(file)

        os.chdir(dir_setup)

        # delete temporary cython .c files. be careful to only delete
        # the .c files corresponding to .pyx files
        ext_sources = [f for ext in ext_modules for f in ext.sources]
        for file in ext_sources:
            file = os.path.join(dir_setup, file)
            if file.endswith('.pyx') and os.path.isfile(file):
                (root, ext) = os.path.splitext(file)
                file_c = root + '.c'
                if os.path.isfile(file_c):
                    os.remove(file_c)

        os.chdir(dir_setup)

        # delete cython .so modules
        ext_module_names = [ext.name for ext in ext_modules]
        for mod in ext_module_names:
            file = mod.replace('.', os.path.sep) + '.so'
            file = os.path.join(dir_setup, file)
            if os.path.isfile(file):
                os.remove(file)

        os.chdir(curr_dir)


setup(
    ext_modules = ext_modules,
    cmdclass = {'clean' : clean,
                'build_ext' : build_ext},
)
