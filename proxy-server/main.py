"""My proxy server entry point"""
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from helpers.jenkins_helper import fetch_data
from helpers.shell_login_helper import get_session_xsrf_token

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/jenkins-search")
async def search(query: str):
    """Search Jenkins for the given query"""
    try:
        results = await fetch_data(query)
        return JSONResponse(content=results)
    except Exception as e:
        logger.error("Error during search: %s", str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
            ) from e


@app.get("/cloud-login")
async def wg_cloud_login():
    """Login to wg cloud"""
    response = get_session_xsrf_token()
    return JSONResponse(content=response)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
