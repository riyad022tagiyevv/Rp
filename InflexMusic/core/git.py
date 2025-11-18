import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO

    # Token varsa istifadə edək
    if config.GIT_TOKEN:
        USER = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP = REPO_LINK.replace("https://", "")
        UPSTREAM_REPO = f"https://{USER}:{config.GIT_TOKEN}@{TEMP}"
    else:
        UPSTREAM_REPO = REPO_LINK

    try:
        repo = Repo()
        LOGGER(__name__).info("Git repo artıq mövcuddur.")
    except (GitCommandError, InvalidGitRepositoryError):
        LOGGER(__name__).info("Yeni git repo yaradılır...")
        repo = Repo.init()

        # REMOTE YARADILIR
        if "origin" not in repo.remotes:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        else:
            origin = repo.remote("origin")

        # FETCH
        try:
            origin.fetch()
        except Exception as e:
            LOGGER(__name__).error(f"Fetch error: {e}")
            return

        # BRANCH YOXLANIR
        if config.UPSTREAM_BRANCH not in origin.refs:
            LOGGER(__name__).error(
                f"❌ Branch tapılmadı: {config.UPSTREAM_BRANCH}\n"
                f"Repo-da olan branch-lar: {[ref.name for ref in origin.refs]}"
            )
            return

        # HEAD YARADILIR
        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH]
        ).set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        ).checkout(True)

        # PULL
        try:
            origin.pull(config.UPSTREAM_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")

        # REQUIREMENT QURULMASI
        install_req("pip3 install --no-cache-dir -r requirements.txt")

        LOGGER(__name__).info("Upstream-dən yeniləmələr çəkildi.")
