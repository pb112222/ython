"""
Utility functions for PlayBeat site generation.
"""

from pathlib import Path


def ensure_dist_dir(dist_path: Path) -> None:
    """Create dist directory if it doesn't exist."""
    dist_path.mkdir(exist_ok=True)


def copy_assets(dist_path: Path, asset_files: list) -> None:
    """Copy static assets (CSS, JS) to dist directory."""
    import shutil
    
    for filename in asset_files:
        src = Path(filename)
        if src.exists():
            dest = dist_path / filename
            shutil.copy(src, dest)
            print(f"  ✓ Copied {filename}")
        else:
            print(f"  ⚠  WARNING: {filename} not found — add it to the project root")


def generate_page_html(title: str, body: str, extra_js: str = "", extra_css: str = "", 
                       ticker: str = "", header: str = "", footer: str = "", modals: str = "") -> str:
    """
    Generate a complete HTML page from components.
    
    Args:
        title: Page title (suffix added automatically)
        body: Main page content
        extra_js: Additional JavaScript code
        extra_css: Additional CSS code
        ticker: Ticker component HTML
        header: Header component HTML
        footer: Footer component HTML
        modals: Modal dialogs HTML
    
    Returns:
        Complete HTML document as string
    """
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — PlayBeat Digital</title>
<link rel="stylesheet" href="shared.css">
{extra_css}
</head>
<body>

{ticker}
{header}

<main>
{body}
</main>

{footer}
{modals}

<script src="shared.js"></script>
{extra_js}
</body>
</html>
'''


def write_pages_to_disk(pages: dict, dist_path: Path) -> None:
    """
    Write all generated pages to disk.
    
    Args:
        pages: Dictionary of {filename: html_content}
        dist_path: Output directory path
    """
    for filename, content in pages.items():
        filepath = dist_path / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"  ✓ {filename}")
