/**
 * Webpack configuration for quantinuum-docs-theme.
 *
 * This script does a few primary things:
 *
 * - Generates a `webpack-macros.html` file that defines macros used
 *   to insert CSS / JS at various places in the main `layout.html` template.
 * - Compiles our translation files into .mo files so they can be bundled with the theme
 * - Compiles our SCSS and JS and places them in the _static/ folder
 * - Downloads and links FontAwesome and some JS libraries (Bootstrap, etc)
 */

const { resolve } = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CopyPlugin = require("copy-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

/*******************************************************************************
 * Compile our translation files
 */
const { exec } = require("child_process");
const localePath = resolve(__dirname, "src/quantinuum_docs_theme/locale");
const htmlWebpackPlugin = new HtmlWebpackPlugin();
const copyPlugin = new CopyPlugin();

module.exports = {
  mode: "production",
  devtool: "source-map",
  output: {filename: "scripts/[name].js", path: staticPath},
  optimization: {minimizer: ['...', new CssMinimizerPlugin()]},
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        {loader: MiniCssExtractPlugin.loader},
        {loader: "css-loader", options: { url: false }},
        {loader: "sass-loader",},
      ],
    }],
  },
  plugins: [htmlWebpackPlugin, copyPlugin, new MiniCssExtractPlugin({
    filename: "styles/[name].css"
  })],
  experiments: {
    topLevelAwait: true,
  },
};
