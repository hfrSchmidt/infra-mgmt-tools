import io
import os

import setuptools


# Package metadata.

name = "infra-mgmt-tools"
description = "infrastructure management tools"
# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 3 - Alpha"
dependencies = [
  "python-freeipa >= 1.0"
]


# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(package_root, "infra/usermgmt/version.py")) as fp:
  exec(fp.read(), version)
version = version["__version__"]

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
  readme = readme_file.read()

# Only include packages under the 'infra' namespace. Do not include tests,
# benchmarks, etc.
packages = [
  package for package in setuptools.find_packages() if package.startswith("infra")
]

# Determine which namespaces are needed.
namespaces = ["infra"]
if "infra.usermgmt" in packages:
  namespaces.append("infra.usermgmt")


setuptools.setup(
  name=name,
  version=version,
  description=description,
  long_description=readme,
  author="Hendrik Schmidt",
  author_email="",
  license="MIT",
  url="https://github.com/hfrschmidt/infra-mgmt-tools",
  classifiers=[
      release_status,
      "Intended Audience :: System Administrators",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Operating System :: POSIX :: Linux",
      "Topic :: System :: Systems Administration",
  ],
  packages=packages,
  namespace_packages=namespaces,
  install_requires=dependencies,
  python_requires=">=3.7",
  include_package_data=True,
  zip_safe=False,
)
