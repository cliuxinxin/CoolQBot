import configparser
from github import Github

class Robot():
    def __init__(self):
        self.config = self.get_config()
        self.auth_key = self.get_auth_key(self.config)
        self.g = self.connect_github(self.auth_key)
        self.repo  = self.get_repo(self.g,self.config)
        self.issues = self.get_issues(self.repo)
        self.issues_dict = self.init_issue_cache(self.issues)


    def get_config(self,configfile='config.ini'):
        config = configparser.ConfigParser()
        config.read(configfile)
        return config

    def get_auth_key(self,config):
        return '118092e115ea248917a3d662d35d12f19e47a438'

    def get_repo(self,g,config):
        repo_name =  'cliuxinxin/topics'
        repo = g.get_repo(repo_name) 
        return repo

    def init_issue_cache(self,issues):
        issues_dict = {}
        for issue in issues:
            if issues_dict.get(issue.title):
                pass
            else:
                issues_dict[issue.title] = issue.number
        return issues_dict

    def connect_github(self,auth_key):
        g = Github(auth_key)
        return g

    def get_issues(self,repo):
        issues = repo.get_issues()
        return issues

    def create_issue(self,title):
        if self.issues_dict.get(title):
            issue = self.repo.get_issue(number=self.issues_dict[title])
        else:
            issue = self.repo.create_issue(title) 
            self.issues_dict[issue.title] = issue.number
        return issue

    def get_comments(self,issue):
        return  issue.get_comments()

    def create_comment(self,issue,comment_content):
        comment = issue.create_comment("This is bird")
        return comment

    def create_comment_by_issue_number(self,issue_number,comment_content):
        issue = self.repo.get_issue(number=issue_number)
        comment = issue.create_comment(comment_content)
        return comment

    def test(self):
        issue = self.create_issue("This is test third issue")
        comment = self.create_comment(issue,"This is bird")
        for isu in self.issues:
            print(isu.title)

if __name__ == "__main__":
    robot = Robot()
    robot.test()