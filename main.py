import yaml

dynamic_extra_var = 'works!'

with open('docs/_data/nav.yaml', 'r') as nav_y:
    nav = yaml.safe_load(nav_y.read())


def define_env(env):
    env.variables['dynamic_macros_var'] = 'works!'
    env.variables['dynamic_extra_var'] = dynamic_extra_var


def on_post_page_macros(env):
    lang = env.page.file.dest_language
    if lang == "":
        lang = 'fr'

    for key, val in nav.items():
        if key in env.page.markdown:
            env.raw_markdown = env.raw_markdown.replace(key, val[lang])
            env.page.title = val[lang]
            env.page.meta['title'] = val[lang]
