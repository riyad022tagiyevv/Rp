import asyncio
import shlex
from typing import Tuple

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
    # Heroku üçün Git tamamilə deaktiv edildi.
    LOGGER(__name__).info("Git yoxlanışı keçilir (Heroku üçün deaktiv).")

    try:
        install_req("pip3 install --no-cache-dir -r requirements.txt")
    except Exception as e:
        LOGGER(__name__).error(f"Requirements quraşdırılmadı: {e}")
