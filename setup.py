from glob import glob

import os as opsys

import platform

from setuptools import setup, Extension, Command, Distribution

from wheel.bdist_wheel import bdist_wheel

class bdist_fbx_wheel(bdist_wheel):
    description = "Builds FBX for Python"

    user_options = bdist_wheel.user_options + [

        ('os=', None, 'The operating system to build for'),
        ('arch=', None, 'The arch to build for'),
        ('python=', None, 'The python version to build for'),
    ]

    def initialize_options(self):
        super().initialize_options()

        self.os = None
        self.arch = None
        self.python = None

    def finalize_options(self):
        assert self.os in ("linux", "windows")
        assert self.arch in ("x86", "x64")
        assert self.python in ("2", "3")

        real_arch = self.arch if self.arch == "x86" else "x86_64"

        if self.os == "windows":
            if self.arch == "x86":
                self.plat_name = "win_32"
            if self.arch == "x64":
                self.plat_name = "win_amd64"

        if self.os == "linux":
            self.plat_name = f"{self.os}_{real_arch}"

        self.plat_name_supplied = True
        self.python_tag = f"py{self.python}"
        self.root_is_pure = False
        self.universal = False

        self.bdist_dir = f"build/{self.os}/{self.arch}/{self.python}"
        self.data_dir = "python_fbx_bindings"

        package_files = [opsys.path.abspath(path) for path in glob(f"bin/{self.os}/Python{self.python}*{self.arch}*/*")]
        print(f"Initializing FBX packages {package_files}")

        if package_files:
            self.distribution.data_files = [('lib/site-packages/python_fbx_bindings', package_files)]

        self.distribution.platforms = [self.os]

        super().finalize_options()

    def run(self):
        super().run()


if __name__ == "__main__":
    setup(
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Topic :: Artistic Software',
            'Topic :: Multimedia :: Graphics :: 3D Modeling',
            'Topic :: Software Development :: Libraries'
        ],
        cmdclass={
            "bdist_fbx_wheel": bdist_fbx_wheel
        }
    )