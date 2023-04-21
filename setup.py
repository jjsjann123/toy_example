from setuptools import setup, Extension, find_packages

packages = []
print("edit")


setup(
  package_dir = {"pkg2": "pkg_dir/pkg2/"},
  packages = ["pkg1", "pkg2"])
