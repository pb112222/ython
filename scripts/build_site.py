#!/usr/bin/env python3
"""
PlayBeat Digital Site Generator v2

Main entry point for building the static website.
Run: python scripts/build_site.py

Output: ./dist/ directory with all 19 HTML pages
"""

from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from playbeat.config import DIST_DIR
from playbeat.templates import TICKER, HEADER, FOOTER, MODALS, TRUST
from playbeat.utils import ensure_dist_dir, copy_assets, generate_page_html, write_pages_to_disk


def build_site():
    """Main site generation function."""
    print("\n🚀 PlayBeat Digital — Site Generator v2\n")
    
    # Create output directory
    ensure_dist_dir(DIST_DIR)
    print(f"📁 Output: {DIST_DIR.absolute()}\n")
    
    # Copy static assets
    print("📦 Copying assets...")
    copy_assets(DIST_DIR, ["shared.css", "shared.js"])
    
    # Generate pages
    print("\n📄 Generating pages...")
    pages = {}
    
    # Example: Home page
    pages["index.html"] = generate_page_html(
        title="Home",
        body='''
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="hero-content">
    <div>
      <div class="hero-badge"><div class="badge-dot"></div> Prime Exclusive Marketplace</div>
      <h1 class="hero-title">
        The Future<br>
        <span class="line-gold">Of Digital</span><br>
        <span class="line-silver">Commerce</span>
      </h1>
      <p class="hero-desc">
        Games, AI tools, gift cards, subscriptions &amp; more.
        <strong>Instant delivery. Global reach. Prime quality.</strong>
      </p>
      <div class="hero-cta">
        <a href="trending.html" class="btn-hero-primary">🔥 Shop Trending</a>
        <a href="best-value.html" class="btn-hero-secondary">💎 Best Value</a>
      </div>
      <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">500K+</div><div class="stat-label">Products Sold</div></div>
        <div class="stat-item"><div class="stat-num">120+</div><div class="stat-label">Categories</div></div>
        <div class="stat-item"><div class="stat-num">4.9★</div><div class="stat-label">Avg Rating</div></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-hex-grid" id="heroHexGrid"></div>
    </div>
  </div>
</section>

<div class="main">
  {TRUST}
</div>
'''.format(TRUST=TRUST),
        ticker=TICKER,
        header=HEADER,
        footer=FOOTER,
        modals=MODALS
    )
    
    # Write all pages
    write_pages_to_disk(pages, DIST_DIR)
    
    # Summary
    print(f"\n✅ Build complete!")
    print(f"   Generated {len(pages)} pages")
    print(f"   📂 Location: {DIST_DIR.absolute()}")
    print(f"   🌐 Open: {DIST_DIR}/index.html in your browser\n")


if __name__ == "__main__":
    build_site()
