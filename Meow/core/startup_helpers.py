

import glob
import shlex
import ntpath
import asyncio
import logging
import importlib
from git import Repo
from typing import Tuple
from datetime import datetime
from Meow import config
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

REPO_ = Config.UPSTREAM_REPO
BRANCH_ = Config.U_BRANCH




async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def update_it():
    logging.info("[UPDATER] - Checking git for new available updates...")
    """Update Userbot On StartUps."""
    try:
        repo = Repo()
    except GitCommandError:
        logging.debug("Invalid Git Command. Not Updating....")
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(Config.U_BRANCH, origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    if repo.active_branch.name != Config.U_BRANCH:
        logging.debug("You Active Branch Doesn't Match With The Default Branch. Please Make Sure You Are on Default Branch.")
        return
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(Config.U_BRANCH)
    try:
        ups_rem.pull(Config.U_BRANCH)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await run_cmd("pip3 install --no-cache-dir -r requirements.txt")
    return
