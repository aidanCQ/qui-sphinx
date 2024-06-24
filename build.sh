echo "🐍 Copying sphinx assets..."
rm -rf ./dist
mkdir ./dist
cp -R ./quantinuum_docs_theme ./dist
echo "🔨 Building UI assets..."
STATIC_DIR=./dist/quantinuum_docs_theme/theme/quantinuum_docs_theme/static
npm run build
cp ./node_modules/@cqcl/quantinuum-ui/dist/tokens.css ./static/tokens.css
npx tailwindcss --postcss ./postcss.config.cjs -i ./ui/index.css -o ./static/styles.css
cp -R ./static $STATIC_DIR
cp ./poetry.lock ./dist/poetry.lock
cp ./pyproject.toml ./dist/pyproject.toml
cp ./README.md ./dist/README.md
rm -rf ./static
echo ✅ "Done. Generated sphinx theme under /dist."

