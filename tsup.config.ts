import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['ui/index.tsx'],
  outDir: './quantinuum_docs_theme/theme/quantinuum_docs_theme/static/',
  minify: true,
  skipNodeModulesBundle: false,
  target: "es2015",
  platform: "browser",
  format: ["iife"],
})
