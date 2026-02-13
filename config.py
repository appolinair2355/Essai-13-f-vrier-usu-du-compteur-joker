"""
Configuration du bot Telegram de prédiction Baccarat
"""
import os

def parse_channel_id(env_var: str, default: str) -> int:
    value = os.getenv(env_var) or default
    channel_id = int(value)
    # Convertit l'ID positif en format ID de canal Telegram négatif si nécessaire
    if channel_id > 0 and len(str(channel_id)) >= 10:
        channel_id = -channel_id
    return channel_id

# ID du canal source
SOURCE_CHANNEL_ID = parse_channel_id('SOURCE_CHANNEL_ID', os.getenv('SOURCE_CHANNEL_ID', '-1002682552255'))

# ID du canal de contrôle (Mirror)
CONTROL_CHANNEL_ID = parse_channel_id('CONTROL_CHANNEL_ID', os.getenv('CONTROL_CHANNEL_ID', '-1002674389383'))

# ID du canal de prédiction
PREDICTION_CHANNEL_ID = parse_channel_id('PREDICTION_CHANNEL_ID', os.getenv('PREDICTION_CHANNEL_ID', '-1002935867322'))

# Miroirs
MIRROR_PAIRS = {
    '♠️': '♦️',
    '♦️': '♠️',
    '❤️': '♣️',
    '♣️': '❤️'
}

ADMIN_ID = int(os.getenv('ADMIN_ID') or '0')

API_ID = int(os.getenv('API_ID') or '0')
API_HASH = os.getenv('API_HASH') or ''
BOT_TOKEN = os.getenv('BOT_TOKEN') or ''

PORT = int(os.getenv('PORT') or '10000')

# NOUVEAU MAPPING : La couleur qui précède la couleur manquante dans le cycle ♠️ → ❤️ → ♦️ → ♣️
# Cycle: ♠ -> ♥ -> ♦ -> ♣ -> ♠ (répète)
# Si ♣ manque, on joue la couleur qui précède (♦)
# Si ♠ manque, on joue la couleur qui précède (♣)
SUIT_MAPPING = {
    '♠': '♣',  # Pique manque -> Prédit Trèfle (précède ♠ dans le cycle)
    '♥': '♠',  # Cœur manque -> Prédit Pique (précède ♥ dans le cycle)
    '♦': '♥',  # Carreau manque -> Prédit Cœur (précède ♦ dans le cycle)
    '♣': '♦',  # Trèfle manque -> Prédit Carreau (précède ♣ dans le cycle)
}

# Séquence de prédiction : après avoir trouvé la couleur manquante, on prédit dans cet ordre cyclique
# Cycle des prédictions: ♠️, ❤️, ♦️, ♣️ (répète)
SUIT_SEQUENCE = ['♠', '♥', '♦', '♣']

# Intervalle entre les prédictions (+4 numéros)
PREDICTION_INTERVAL = 4

ALL_SUITS = ['♠', '♥', '♦', '♣']
SUIT_DISPLAY = {
    '♠': '♠️',
    '♥': '❤️',
    '♦': '♦️',
    '♣': '♣️'
}
