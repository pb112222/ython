"""
Configuration and constants for PlayBeat Digital.
"""

from pathlib import Path

# Output directory
DIST_DIR = Path("dist")

# Page metadata
PAGE_TITLE_SUFFIX = "— PlayBeat Digital"

# List of all pages to generate
PAGES_CONFIG = [
    "index", "games", "gift-cards", "software", "ai-tools",
    "game-items", "accounts", "subscriptions", "top-up", "trending",
    "best-value", "outsource", "our-team", "faq", "contact",
    "my-account", "privacy", "terms", "refund"
]

# Product categories for filtering
CATEGORIES = {
    "games": ["Action", "RPG", "Strategy", "Sports", "Indie", "Sandbox", "Space"],
    "giftcards": ["PlayStation", "Xbox", "Steam", "Google Play", "Apple", "Amazon", "Nintendo", "Roblox"],
    "software": ["OS", "Design", "Security", "Productivity", "VPN", "Utility"],
    "aitools": ["AI Assistant", "AI Image", "AI Video", "AI Voice", "AI Search"],
    "gameitems": ["Skin", "Weapon", "Character", "Currency", "Emote", "Bundle", "Melee"],
    "accounts": ["Streaming", "Music", "Design", "Education", "Writing"],
    "subscriptions": ["Gaming", "Creative", "Streaming", "Security", "Productivity"],
}

# Trust features
TRUST_FEATURES = [
    {"icon": "⚡", "title": "Instant Delivery", "desc": "Keys sent in seconds"},
    {"icon": "🔒", "title": "256-bit SSL", "desc": "Bank-grade security"},
    {"icon": "✅", "title": "Verified Products", "desc": "100% authentic keys"},
    {"icon": "🌍", "title": "Global Access", "desc": "Available in 100+ countries"},
    {"icon": "💬", "title": "24/7 Support", "desc": "Real humans, always on"},
]
