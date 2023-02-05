---
title: __introduction_page_title
---

{% set LC = page.file.dest_language|default("fr", true) %}

# Introduction

## {{ introduction.section_material[LC] }}

| Code | Description                                                                   |
|-----:|-------------------------------------------------------------------------------|
{%- for code, desc in material[LC].items() %}
| {{ code }} | {{ desc }} |
{%- endfor %}

## {{ introduction.section_protective[LC] }}

|  Code |  Description |
|------:| --------------|
{%- for code, desc in protection[LC].items() %}
| {{ code }} | {{ desc }} |
{%- endfor %}

## {{ introduction.section_colour_mark[LC] }}

|  Code | - |  Description |
|------:| :--: | --------------|
{%- for code, desc in colour_mark[LC].items() %}
| {{ code }} | <svg width="20" height="20"><circle stroke="black" stroke-width="1" cx="10" cy="10" r="9.5" fill="{{colour_mark.html_code[code]}}" /></svg> | {{ desc }} |
{%- endfor %}

