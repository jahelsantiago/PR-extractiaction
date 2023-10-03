from github.Repository import Repository
from github.PullRequestComment import PullRequestComment
from github.PaginatedList import PaginatedList

def get_all_comments_from_repository(repository: Repository) -> PaginatedList[PullRequestComment]:
    pull_requests = repository.get_pulls(state='all')
    for pr in pull_requests:
        print(f"Getting comments from PR #{pr.number}")
        comments = pr.get_review_comments()
        for comment in comments:
            yield comment

def getCommentAttributes(comment: PullRequestComment):
    return {
        "id": comment.id,
        "body": comment.body,
        "diff_hunk": comment.diff_hunk,
        "path": comment.path,
        "position": comment.position,
        "original_position": comment.original_position,
        "commit_id": comment.commit_id,
        "original_commit_id": comment.original_commit_id,
        "html_url": comment.html_url,
        "pull_request_url": comment.pull_request_url,
    }

def getUserComments(repository: Repository, comment_author: str):
    user_comments = []
    comments = get_all_comments_from_repository(repository)
    for comment in comments:
        if comment.user.login == comment_author:
            user_comments.append(getCommentAttributes(comment))
    return user_comments
