def clean_img_url_for_slug(url:str) -> str:
    parts = url['src'].split('/')
    slug = parts[3]
    return slug