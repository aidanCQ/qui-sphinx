"""Bootstrap-based sphinx theme from the community."""

from pathlib import Path
from typing import Dict
from sphinx.application import Sphinx
from furo import _html_page_context

__version__ = "0.0.1"

def setup_my_func(app, pagename, templatename, context, doctree):
    context['user_config'] = app.config
    app.add_js_file("index.global.js", priority=200, loading_method="async")

def setup(app: Sphinx) -> Dict[str, str]:
    """Setup the Sphinx application."""
    here = Path(__file__).parent.resolve()
    theme_path = here / "theme" / "quantinuum_docs_theme"

    app.add_html_theme("quantinuum_docs_theme", str(theme_path))
    # Include component templates
    app.connect("html-page-context", setup_my_func)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
