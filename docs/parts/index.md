# __catalog_page_title

{% set LC = page.file.dest_language|default("fr", true) %}

## {{ part_category[LC]["hex_screw"] }} ({{ parts_hex_screws.keys() | length }})

| ![Size](../assets/images/hex_size.png) | ![Size](../assets/images/pitch.png) | ![Size](../assets/images/length.png) | ![Size](../assets/images/material.png) | ![Size](../assets/images/protection.png) | ![Size](../assets/images/quantity.png) |  |
| :--: | :--: | :--: | :--: | :--: | :--: | --: |
{%- for code, desc in parts_hex_screws.items() %}
{%- set item = code | replace(" ", "") %}
{{ desc.nominal_diameter }} | {{ desc.pitch }} | {{ desc.length }} | {{desc.material}} | {{desc.protection}} | {{ desc.quantity if desc.quantity != '1' else ' ' }} | [{{ code }}]({{ item }}) 
{%- endfor %}

## {{ part_category[LC]["hex_bolts"] }} ({{ parts_hex_bolts.keys() | length }})

| ![Size](../assets/images/hex_nut_diam.png) | ![Size](../assets/images/pitch.png) | ![Size](../assets/images/hex_nut_height.png) | ![Size](../assets/images/material.png) | ![Size](../assets/images/protection.png) | ![Size](../assets/images/quantity.png) |  |
| :--: | :--: | :--: | :--: | :--: | :--: | --: |
{%- for code, desc in parts_hex_bolts.items() %}
{%- set item = code | replace(" ", "") %}
{{ desc.diameter }} | {{ desc.pitch }} | {{ desc.height }} | {{desc.material}} | {{desc.protection}} | {{ desc.quantity if desc.quantity != '1' else ' ' }} | [{{ code }}]({{ item }}) 
{%- endfor %}