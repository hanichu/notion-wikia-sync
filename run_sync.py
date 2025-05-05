# Entrypoint script

from notion_wikia_translator.sync_engine import sync

if __name__ == "__main__":
    sync()
