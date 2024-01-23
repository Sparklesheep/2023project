# -*- coding = utf-8 -*-
"""
@File: spider.py
@Author : Tianci
@Time : 2024/1/23 14:15
@Software : PyCharm
"""

import requests


def get_commit_history(username, repo_name, page=1, per_page=30):
    base_url = f'https://api.github.com/repos/{username}/{repo_name}/commits'

    headers = {
        'User-Agent': 'sveltejs'
    }

    params = {'page': page, 'per_page': per_page}
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            commit_sha = commit['sha']
            commit_message = commit['commit']['message']
            commit_author = commit['commit']['author']['name']
            commit_date = commit['commit']['author']['date']

            print(f"SHA: {commit_sha}")
            print(f"Author: {commit_author}")
            print(f"Date: {commit_date}")
            print(f"Message: {commit_message}")
            print("\n" + "=" * 50 + "\n")

        # 检查是否还有更多的页面，如果有，递归调用获取下一页
        if 'Link' in response.headers:
            links = response.headers['Link'].split(', ')
            for link in links:
                if 'rel="next"' in link:
                    next_page_url = link.split(';')[0][1:-1]
                    get_commit_history(username, repo_name, page + 1, per_page)

    else:
        print(f"Error: {response.status_code}")
        print(f"Error Message: {response.text}")


if __name__ == "__main__":
    get_commit_history('sveltejs', 'svelte')
