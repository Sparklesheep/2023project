# -*- coding = utf-8 -*-

class login(object):
    def __init__(self):
        self.username = input('Input your GitHub username:')
        self.password = input('Input your GitHub personal access token:')


info = login()
