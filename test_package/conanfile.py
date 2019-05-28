# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    # def requirements(self):
    #     print(dir(self))
    #     print(dir(self.deps_cpp_info))
    #     print(dir(self.requires))
    #     print(self.requires.values())
    #     self.requires("vulkan_loader/{}@{}/{}".format(self.requires["vulkan_headers"].version, self.user, self.channel))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "test_package")
            self.run(bin_path, run_environment=True)
