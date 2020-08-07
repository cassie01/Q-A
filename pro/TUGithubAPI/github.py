from api.repositories.repos import Repos

class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "http://api.github.com"
        # self.api_root_url = "https://github.com/login"
        self.repos = Repos(self.api_root_url, **kwargs )

if __name__ == '__main__':
    #1
    # r = Github(token= "b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos("cassie01")
    # print(x.text)

    # data = {"direction": "desc"}
    # x = r.repos.list_your_repos("zhangting85",params= data)
    # x = r.repos.list_your_repos(params= data)
    # task 1
    # x = r.repos.list_organizition("TestUpCommunity",params=data)
    # x = r.repos.list_all_repositories(params=data)
    # print(x.text)

    #2
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(visibility = 'private')
    # print(x.text)
    # #3
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(visibility='public')
    # print(x.text)
    # #4
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(visibility='all')
    # print(x.text)
    # #5
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(direction='desc')
    # print(x.text)
    # #6
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(sort='updated')
    # print(x.text)
    # #7
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(type='owner', visibility="all")
    # print(x.text)
    # #8
    # r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # x = r.repos.list_your_repos(type='owner', sort="pushed")
    # print(x.text)
    #密码登录
    # r = Github(username= "cassie01", password= "xd19941225")
    # x = r.repos.list_your_repos()
    # print(x.text)

    r = Github(token="b1ce8efe194ac368d1bb3fffc27d718d2021a700")
    # r = Github(username= "cassie01", password= "xd19941225")
    username = "cassie01"
    orgname = "TestUpCommunity"

    # case 1
    data = {
        "name" : "hello-world",
        "description":"this is your first repository",
        "homepage": "http://github.com",
        "private" : False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }
    x = r.repos.create_user_repositories(json=data)
    print(x.status_code)
    # print(x.text)
    assert x.status_code == 201



    #case 2
    # x = r.repos.create_user_repositories(json=data)

    # with open(r'C:\Users\mshacxiang\pro\TUGithubAPI\content.txt', 'a') as f:
    #     f.write(x.text)