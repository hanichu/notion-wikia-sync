# Notion Wikia Sync Bot

This bot automatically syncs and translates Notion wiki content between English and Italian, using DeepL (Free) and Google Translate as fallback. It sends updates via Telegram.

## Features
- Syncs Notion databases and pages
- Bidirectional translation (EN <-> IT)
- Auto-fallback from DeepL to Google
- Hourly sync with cron
- Telegram alerts on success and error

## Setup
1. Clone the repo
2. Install dependencies with pip
3. Create `.env` with your API keys
4. Run `python3 run_sync.py` or set a cron job

## Environment Variables
- `NOTION_API_KEY`
- `DEEPL_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
