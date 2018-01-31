from urllib.parse import urlparse

def get_domain_name(urls):
    try:
        results = get_sub_domain_name(urls).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

def get_sub_domain_name(urls):
    try:
        return urlparse(urls).netloc
    except:
        return ''
