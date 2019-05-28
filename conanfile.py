# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
import shutil


class LibnameConan(ConanFile):
    name = "vulkan_portability"
    version = "0.2"
    description = "header files for the Vulkan Portability extension: VK_EXTX_portability_subset."
    topics = ("conan", "vulkan", "extension", "VK_EXTX_portability_subset", )
    url = "https://github.com/bincrafters/conan-vulkan_portability"
    homepage = "https://github.com/KhronosGroup/Vulkan-Portability"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "Apache-2.0"
    exports = ["LICENSE.md", ]
    no_copy_source = True

    _source_subfolder = "source_subfolder"

    def requirements(self):
        self.requires("vulkan_loader/1.1.106@{}/{}".format(self.user, self.channel))

    def source(self):
        source_url = "https://github.com/KhronosGroup/Vulkan-Portability/archive/v{}.tar.gz".format(self.version)
        sha256 = "2508a2dd0e111cb7d4636a54d454e7172ab33c48cba0e6e86e6fdb7cf48becb5"
        tools.get(source_url, sha256=sha256)
        os.rename("Vulkan-Portability-{}".format(self.version), self._source_subfolder)

    def package(self):
        shutil.copytree(src=os.path.join(self.source_folder, self._source_subfolder, "include"),
                        dst=os.path.join(self.package_folder, "include"))
        self.copy("LICENSE.md", dst="licenses")
        self.copy("COPYRIGHT.txt", src=self._source_subfolder, dst="licenses")
