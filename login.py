# -*- coding = utf-8 -*-
"""
@File: login.py
@Author : Tianci
@Time : 2024/1/24 13:19
@Software : PyCharm
"""


class login(object):
    def __init__(self):
        self.username = input('Input your GitHub username:')
        self.password = input('Input your GitHub personal access token:')


info = login()