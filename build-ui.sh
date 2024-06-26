echo "🔨 Building UI assets..."
STATIC_DIR=./quantinuum_docs_theme/theme/quantinuum_docs_theme/static
npm run build
cp ./node_modules/@cqcl/quantinuum-ui/dist/tokens.css ./$STATIC_DIR/tokens.css
npx tailwindcss --postcss ./postcss.config.cjs -i ./ui/index.css -o ./$STATIC_DIR/tailwind.css
echo ✅ "Done. Added UI assets to theme"

