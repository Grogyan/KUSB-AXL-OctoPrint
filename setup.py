# setup.py
from setuptools import setup

plugin_identifier = "kusb_axl"
plugin_package = "octoprint_kusb_axl"
plugin_name = "OctoPrint-KUSB-AXL"
plugin_version = "0.1.0"
plugin_description = "Octoprint Plugin for the Klipper USB board"
plugin_author = "Your Name"
plugin_author_email = "grogyan@gmail.com"
plugin_url = "https://github.com/Grogyan/KUSB-AXL-OctoPrint"
plugin_license = "AGPLv3"

setup(
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    author_email=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    packages=[plugin_package],
    install_requires=["OctoPrint"],
    entry_points={
        "octoprint.plugin": [
            f"{plugin_identifier} = {plugin_package}"
        ]
    },
    package_data={
        plugin_package: ["templates/*", "static/*", "translations/*"]
    },
    zip_safe=False
)
