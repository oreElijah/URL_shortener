from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from models.url_shortener import Url
from utils.url_shortener import generate_short_url
from database.config import url_table, database

router = APIRouter()

@router.post("/shortener", status_code=200)
async def shorten_url(url: Url):
    original_url = url.original_url
    short_url = await generate_short_url()
    query = url_table.insert().values(original_url=original_url, short_url=short_url)
    await database.execute(query)
    return {"short_url": f"{short_url}"}

@router.get("/get_original/{short_url}", status_code=200)
async def get_original_url(short_url: str):
    query = url_table.select().where(url_table.c.short_url == short_url)
    result = await database.fetch_one(query)
    if result:
        return {"original_url": result["original_url"]}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short_url does not exist")
    
@router.get("/{short_url}", status_code=200)
async def redirect_url(short_url: str):
    query = url_table.select().where(url_table.c.short_url == short_url)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short_url does not exist")
    return RedirectResponse(result["original_url"], status_code=status.HTTP_302_FOUND)