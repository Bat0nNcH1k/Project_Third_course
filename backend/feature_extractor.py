import tldextract
import re
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    ext = tldextract.extract(url)

    features = {
        "qty_dot_url": url.count('.'),
        "qty_hyphen_url": url.count('-'),
        "qty_slash_url": url.count('/'),
        "qty_questionmark_url": url.count('?'),
        "qty_equal_url": url.count('='),
        "qty_at_url": url.count('@'),
        "qty_and_url": url.count('&'),
        "qty_exclamation_url": url.count('!'),
        "qty_space_url": url.count(' '),
        "qty_underline_url": url.count('_'),
        "qty_percent_url": url.count('%'),
        "qty_tilde_url": url.count('~'),
        "qty_comma_url": url.count(','),
        "qty_plus_url": url.count('+'),
        "qty_asterisk_url": url.count('*'),
        "qty_hashtag_url": url.count('#'),
        "qty_dollar_url": url.count('$'),
        "length_url": len(url),
        "domain_length": len(ext.domain),
        "qty_dot_domain": ext.domain.count('.'),
        "qty_hyphen_domain": ext.domain.count('-'),
        "qty_slash_domain": ext.domain.count('/'),
        "qty_questionmark_domain": ext.domain.count('?'),
        "qty_equal_domain": ext.domain.count('='),
        "domain_in_ip": 1 if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ext.domain) else 0,
        "email_in_url": 1 if re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", url) else 0,
        "url_shortened": 1 if re.match(r"(bit\.ly|goo\.gl|tinyurl\.com|ow\.ly)", ext.domain) else 0
    }

    return features