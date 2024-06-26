# Quantinuum Docs Sphinx Theme

This theme is based on [furo](https://pradyunsg.me/furo/).

### Build the sphinx theme locally
```
./build.sh # Outputs sphinx theme files in /dist.
```

### Install the theme from release branch
```bash
pip install git+https://github.com/aidanCQ/qui-sphinx.git@dist
```
```bash
poetry add git+https://github.com/aidanCQ/qui-sphinx.git@dist
```

### Configure the theme in sphinx

In `conf.py` add:

```python
html_theme_options = {
 ...,
 "navTextLinks": [
        {
            "title": string,
            "href": string,
        },
    ],
 "navProductName": string,
 "navIconLinks": [
     {
         "title": string,
         "href": string,
         "iconImageURL": string (i.e. "/_static/github.svg"),
     },
 ],
}
extensions = [
    ...,
    "quantinuum_docs_theme",
]

html_theme = "quantinuum_docs_theme"
```
