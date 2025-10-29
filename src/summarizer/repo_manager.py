from git import Repo
from config import REPO_URL, REPO_PATH
import os

def clone_or_update_repo():
    if not os.path.exists(REPO_PATH):
        print("Cloning repo for the first time...")
        Repo.clone_from(REPO_URL, REPO_PATH)
    else:
        print("Updating existing repo...")
        repo = Repo(REPO_PATH)
        origin = repo.remotes.origin
        origin.pull()
    print("Repo ready at:", REPO_PATH)