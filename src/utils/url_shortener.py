import random
import string

from database.config import url_table, database

async def generate_short_url(length=6):
    url = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    query = url_table.select().where(url_table.c.short_url==url)
    existing = await database.fetch_one(query)
    if not existing:
        return url