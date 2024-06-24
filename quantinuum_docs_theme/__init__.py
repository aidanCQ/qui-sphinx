"""Bootstrap-based sphinx theme from the community."""

from pathlib import Path
from typing import Dict
from sphinx.application import Sphinx

__version__ = "0.0.1"


def setup(app: Sphinx) -> Dict[str, str]:
    """Setup the Sphinx application."""
    here = Path(__file__).parent.resolve()
    theme_path = here / "theme" / "quantinuum_docs_theme"

    app.add_html_theme("quantinuum_docs_theme", str(theme_path))
    # Include component templates
    # app.config.templates_path.append(str(theme_path / "components"))

    return {"parallel_read_safe": True, "parallel_write_safe": True}
