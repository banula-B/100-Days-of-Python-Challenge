import json
import os

SETTINGS_FILE = "Resources/JSON files/settings.json"

# Default fallback settings
default_settings = {
    "theme": "dark",
    "volume": 80,
    "notifications_enabled": True,
    "auto_save_interval": 10
}


def load_settings():
    """Loads settings from a JSON file, or creates defaults if missing."""

    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("⚠️ Settings file corrupted! Resetting to defaults.")
            return default_settings.copy()

    else:
        print("📁 No settings file found. Using default configurations.")
        return default_settings.copy()


def save_settings(settings):
    """Saves the current settings dictionary directly back to the JSON file."""

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

    print("✅ Settings saved successfully!")


# Run the manager program
print("--- App Settings Manager ---")

current_settings = load_settings()

print(f"\nCurrent Configurations: {current_settings}")


# Let user modify a setting
new_volume = input(
    "\nEnter new volume level (0-100) or press Enter to keep current: "
).strip()

if new_volume.isdigit():
    current_settings["volume"] = int(new_volume)


new_theme = input(
    "Enter new theme (light/dark/system) or press Enter to keep current: "
).strip().lower()

if new_theme in ["light", "dark", "system"]:
    current_settings["theme"] = new_theme


# Save updates
save_settings(current_settings)