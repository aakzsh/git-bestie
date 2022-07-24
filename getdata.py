



from github import Github


#############################
def getHitRepo(username):
    try:
        repos = {}
        # username = ""
        g = Github()
        user = g.get_user(username)
        for repo in user.get_repos():
            repos[repo.name] = repo.stargazers_count

        isFull = False
        Keymax = sorted(repos.items(), key=lambda x: x[1], reverse=True)
        one = {}
        two = {}
        three = {}
        if len(Keymax)>2:
            
            isFull = True
            one = {'name': Keymax[0][0],'stars': Keymax[0][1] }
            two = {'name': Keymax[1][0],'stars': Keymax[1][1] }
            three = {'name': Keymax[2][0],'stars': Keymax[2][1] }
        else:
            isFull = False
            return "frr"
            
        # print(Keymax, repos[Keymax])

        # return (Keymax, repos[Keymax])
        return {'one': one, 'two': two, 'three': three}
    except:
        return "err"
#############################

