# Handles Notion API logic

import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))

def fetch_database_items(database_id):
    return notion.databases.query(database_id=database_id).get("results", [])

def create_or_update_page(parent_id, title, content_blocks):
    return notion.pages.create(
        parent={"page_id": parent_id},
        properties={
            "title": [{
                "text": {"content": title}
            }]
        },
        children=content_blocks
    )

def update_page_content(page_id, content_blocks):
    # You may want to clear or append—this is a placeholder
    notion.blocks.children.append(page_id, children=content_blocks)
