# Different repo to syncrhonize with
remote_repo_url = https://github.com/duftcola-dev/RepoA.git
repo_mame = RepoA
repo_branch = master
# File we wich so syncrhonize
file = prefect.sh

sync:
	- git remote add $(repo_mame) $(remote_repo_url)
	- git remote -v

update:

	- git fetch $(repo_mame)
	- git checkout --patch $(repo_mame)/$(repo_branch) ./$(file)

