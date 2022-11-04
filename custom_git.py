# any change in the git
import git

repo = git.Repo("./")

print(repo.git.status())
print(repo.git.branch())

repo.git.add('--all')
repo.git.commit("-m", "first commit")

repo.git.push("origin", "divyanshu")
