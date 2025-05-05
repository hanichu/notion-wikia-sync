# Handles sync logic and sends Telegram notifications

from notion_wikia_translator import config, notion_helper, translator
from utils.telegram_notifier import send_telegram_message

def sync():
    try:
        for pair in config.LANGUAGE_PAIRS:
            source_lang = pair['source']
            target_lang = pair['target']

            send_telegram_message(f"🔄 Syncing from {source_lang} to {target_lang}...")

            for db_key in config.DATABASES[source_lang]:
                source_db = config.DATABASES[source_lang][db_key]
                target_db = config.DATABASES[target_lang][db_key]

                items = notion_helper.fetch_database_items(source_db)

                for item in items:
                    name = item['properties'].get("Name", {}).get("title", [{}])[0].get("text", {}).get("content", "")
                    description = item['properties'].get("Description", {}).get("rich_text", [{}])[0].get("text", {}).get("content", "")
                    translated_description = translator.translate_text(description, source_lang, target_lang)

                    if translated_description:
                        send_telegram_message(f"📄 Translated '{name}' from {source_lang} to {target_lang}")
                        # You can now call update or create functions here

        send_telegram_message("✅ Sync completed successfully.")

    except Exception as error:
        send_telegram_message(f"⚠️ Error during sync:\n{str(error)}")
