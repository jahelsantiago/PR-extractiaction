from github import Github
from utils import getUserComments
import json

# Replace with your info
#-------------------------------------
github_access_token = "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"
repo_owner = "jahelsantiago"
repo_name = "frasier-testing"
user_to_extract_comments = "jahelsantiago"
#-------------------------------------



if __name__ == '__main__':
    github_instance = Github(github_access_token)
    repository = github_instance.get_repo(f"{repo_owner}/{repo_name}")

    user_comments = getUserComments(repository, user_to_extract_comments)
    user_comments_json = json.dumps(user_comments)

    with open(f"{user_to_extract_comments}-{repo_name}.json", 'w') as outfile:
        outfile.write(user_comments_json)