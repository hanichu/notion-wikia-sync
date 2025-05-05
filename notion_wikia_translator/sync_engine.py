from notion_wikia_translator import config, notion_helper, translator
from utils.telegram_notifier import send_telegram_message

def get_title_and_text_fields(properties):
    title_field = None
    text_field = None

    for key, value in properties.items():
        if value.get("type") == "title" and not title_field:
            title_field = key
        if value.get("type") == "rich_text" and not text_field:
            text_field = key
        if title_field and text_field:
            break
    return title_field, text_field

def sync():
    try:
        for pair in config.LANGUAGE_PAIRS:
            source_lang = pair['source']
            target_lang = pair['target']

            send_telegram_message(f"🔄 Syncing from {source_lang} to {target_lang}...")

            for db_key in config.DATABASES[source_lang]:
                source_db = config.DATABASES[source_lang][db_key]
                target_db = config.DATABASES[target_lang].get(db_key)

                print(f"▶️ Syncing table: {db_key}")
                print(f"   Source DB: {source_db}")
                items = notion_helper.fetch_database_items(source_db)
                print(f"   Found {len(items)} items")

                for item in items:
                    props = item.get("properties", {})
                    title_key, text_key = get_title_and_text_fields(props)

                    if not title_key or not text_key:
                        print("   ⚠️ Skipping row: title or text field not found")
                        continue

                    title_data = props.get(title_key, {}).get("title", [])
                    name = title_data[0]['text']['content'] if title_data else "Untitled"

                    desc_data = props.get(text_key, {}).get("rich_text", [])
                    description = desc_data[0]['text']['content'] if desc_data else ""

                    print(f"   - {name}: {description}")

                    if not description:
                        print("     ⏩ No description, skipping.")
                        continue

                    translated = translator.translate_text(description, source_lang, target_lang)
                    if translated:
                        print(f"     ✅ Translated: {translated}")
                        send_telegram_message(f"📄 Translated '{name}' from {source_lang} to {target_lang}")
                        # Placeholder: this is where you'd write to the IT DB or create page
                    else:
                        print("     ❌ Translation failed.")

        send_telegram_message("✅ ync completed successfully.")
    except Exception as error:
        send_telegram_message(f"⚠️ Error during sync:\n{str(error)}")
