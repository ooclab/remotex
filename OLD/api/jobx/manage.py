#! /usr/bin/env python3
# coding: UTF-8

# 加载 Python 内置库
import os
import sys

# 加载开发路径
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'vendor'))


def main():
    import eva.management
    eva.management.main()


if __name__ == '__main__':
    os.environ.setdefault("EVA_SETTINGS_MODULE", "conf.settings")
    main()
