import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['ui/index.tsx'],
  outDir: 'static',
  minify: true,
  skipNodeModulesBundle: false,
  target: "es2015",
  platform: "browser",
  format: ["iife"],
})
