



from github import Github


#############################
repos = {}
username = "shrutigupta5555"
g = Github()
user = g.get_user(username)
for repo in user.get_repos():
    repos[repo.name] = repo.stargazers_count

Keymax = max(zip(repos.values(),repos.keys()))[1]

print(Keymax, repos[Keymax])
#############################

