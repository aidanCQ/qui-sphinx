"""Bootstrap-based sphinx theme from the community."""

from pathlib import Path
from typing import Dict
from sphinx.application import Sphinx
from sphinx import version_info as sphinx_version
from pydata_sphinx_theme.utils import get_theme_options_dict
__version__ = "0.0.1"

def extend_html_context(app, pagename, templatename, context, doctree):
     # Add ``sphinx_version_info`` tuple for use in Jinja templates
     context['sphinx_version_info'] = sphinx_version
     context['theme_options'] = get_theme_options_dict(app);

def setup(app: Sphinx) -> Dict[str, str]:
    """Setup the Sphinx application."""
    here = Path(__file__).parent.resolve()
    theme_path = here / "theme" / "quantinuum_docs_theme"

    app.add_html_theme("quantinuum_docs_theme", str(theme_path))
    # Include component templates
    # app.config.templates_path.append(str(theme_path / "components"))


    # Extend the default context when rendering the templates.
    app.connect("html-page-context", extend_html_context)
    
    return {"parallel_read_safe": True, "parallel_write_safe": True}
