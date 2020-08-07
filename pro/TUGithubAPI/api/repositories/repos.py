from core.rest_client import RestClient

class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)

    def list_your_repos(self, username, **kwargs):
    # def list_your_repos(self,**kwargs):
        # params={
        #     "visibility":visibility,
        #     "affiliation":affiliation,
        #     "type":type,
        #     "sort":sort,
        #     "direction":direction
        #
        #
        # }
        # return self.get("/user/repos",params = params)
        # return self.get("/user/repos", **kwargs)
        return self.get("/users/{}/repos".format(username), **kwargs)

    def list_organizition(self, org, **kwargs):
        return self.get("/orgs/{}/repos".format(org), **kwargs)

    def list_all_repositories(self, **kwargs):
        return self.get("/repositories", **kwargs)

    def create_user_repositories(self, **kwargs):
        return self.post("/user/repos",  **kwargs)

    def create_org_repositories(self, org, **kwargs):
        return self.post("/orgs/:{}/repos".format(org),  **kwargs)

    def get_a_repositories(self, owner, repos, **kwargs ):
        return self.get("/repos/{}/{}".format(owner, repos), **kwargs)

    def edit_repositories(self, owner, repos, **kwargs):
        return self.patch("/repos/{}/{}".format(owner, repos), **kwargs)

    def create_user_repo(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#create
        """
        return self.post("/user/repos", **kwargs)
