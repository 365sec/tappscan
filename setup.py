# -*-coding:utf-8 -*-
from setuptools import setup, find_packages
#requests
setup(
    name = "tappscan",
    description = "a high-speed scanner ",
    version = "1.0",
    author = "shaochuyu",
    author_email = "shaochuyu@qq.com",
    install_requires = ["redis","eventlet","requests","pytz","flask-restplus","flask"],
	packages=find_packages(),
    entry_points={
        "console_scripts":[
            'tappscan_scanner=tscanner.pocscanner:tbox_scanner',
        ]
    }
)