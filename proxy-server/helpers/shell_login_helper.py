"""Shell Helper"""
import subprocess
import re
import logging

logger = logging.getLogger(__name__)


SCRIPT_PATH = r"C:\wg-repos\wgc\examples\wgc_csrf_headers.py"

SESSION_REGEX = re.compile(r'wgcloud_dev_session=([^;]+)')
XSRF_REGEX = re.compile(r'XSRF-TOKEN=([^\n]+)')
ORIGIN_REGEX = re.compile(r'Origin:([^\n]+)')


def get_session_xsrf_token():
    """Execute command to run script"""
    process = subprocess.run(["python ", SCRIPT_PATH], capture_output=True, text=True, check=True)
    result = process.stdout

    if result:
        return {
            "wgcloud_dev_session": re.findall(SESSION_REGEX, result),
            "XSRF_Token": re.findall(XSRF_REGEX, result),
            "Origin": re.findall(ORIGIN_REGEX, result)
        }

    logger.error(process.stderr)
    return { "message": "result not found"}
