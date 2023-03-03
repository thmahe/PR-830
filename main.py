import yaml

with open('docs/_data/locales.yaml', 'r') as nav_y:
    locales = yaml.safe_load(nav_y.read())


def define_env(env):
    pass


def on_post_page_macros(env):
    lang = env.page.file.dest_language
    if lang == "":
        lang = 'fr'

    for key, val in locales['nav'].items():
        if key in env.page.markdown:
            env.raw_markdown = env.raw_markdown.replace(key, val[lang])
            env.page.title = val[lang]
            env.page.meta['title'] = val[lang]
