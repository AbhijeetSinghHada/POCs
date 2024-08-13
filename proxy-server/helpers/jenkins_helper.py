""" Helper file for jenkins search"""
import asyncio
import re
import logging
import aiohttp

logger = logging.getLogger(__name__)


jenkins_paths = [
    "microservices-master",
    "infrastructure-master",
    "cipra",
    "siem",
    "wg-firewan",
    "wg-wifi",
    "wg-xdr",
    "wgcloudnoida",
    "wgid",
    "panda",
    "tdr-master",
    "authpoint",
    "firebox-master",
    "platform",
    "dnswatch",
    "stagingprod-master",
    "testing-master",
    "eng-internal",
    "ndr",
]

JENKINS_BASE_PATH = "https://jenkins.infra.int.daas-watchguard.com"
REGEX = re.compile(r'name":"(.*?)"')


async def fetch_data(query: str):
    """Fetch data from Jenkins"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_from_path(session, path, query) for path in jenkins_paths]
        responses = await asyncio.gather(*tasks)
        return [res for res in responses if res]


async def fetch_from_path(session, path, query):
    """Fetch data from a specific Jenkins path"""
    url = f"{JENKINS_BASE_PATH}/{path}/search/suggest?query={query}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                suggestions = re.findall(REGEX, data)
                if suggestions:
                    return {"suggestions": suggestions, "path": path}
            else:
                logger.error("Error fetching data from %s: Status %s", url, response.status)
    except Exception as e:
        logger.error("Exception while fetching data from %s: %s", url, str(e))
    return None
