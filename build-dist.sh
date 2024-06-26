rm -rf ./dist
mkdir ./dist
cp -R ./quantinuum_docs_theme/ ./dist/quantinuum_docs_theme/
cp poetry.lock ./dist/poetry.lock
cp pyproject.toml ./dist/pyproject.toml 
cp README.md ./dist/README.md
