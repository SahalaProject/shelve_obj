from setuptools import setup, find_packages

setup(
    name="okk",
    version="0.3.1",
    author="liyubin",
    author_email="1399393088@qq.com",
    description="原injson，判断两个json的差异，并返回最后差异结果",
    # long_description=open("README.rst").read(),
    license="Apache License, Version 2.0",
    url="https://github.com/SahalaProject",
    # packages=['injson-ok'],
    # package_data={'injson-ok': ['*.py']},
    py_modules=['injson-ok'],
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3"
    ],
    entry_points={

    }
)

# 加密 pyarmor-7 obfuscate injson_ok11.py

# 步骤：

# 1.setup.py放在被打包同级
# 本地打包项目文件
# python setup.py sdist

# 2.上传项目到pypi服务器
# pip install twine
# twine upload dist/name.tar.gz

# 3.下载上传的库
# pip install name
