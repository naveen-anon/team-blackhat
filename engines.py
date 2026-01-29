import re
import math
from urllib.parse import urlparse

def url_structure_engine(url):
    reasons = []
    p = urlparse(url)

    if p.netloc.count('.') >= 4:
        reasons.append("Excessive subdomains")

    if "-" in p.netloc:
        reasons.append("Hyphenated domain")

    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
        reasons.append("IP-based URL")

    return result(reasons)

def keyword_engine(url):
    reasons = []
    keywords = ["login", "verify", "secure", "update", "account", "bank"]

    for k in keywords:
        if k in url.lower():
            reasons.append(f"Keyword: {k}")

    return result(reasons)

def entropy_engine(url):
    reasons = []

    def entropy(s):
        probs = [s.count(c)/len(s) for c in set(s)]
        return -sum(p * math.log2(p) for p in probs)

    e = entropy(url)
    if e > 4.2:
        reasons.append(f"High entropy ({round(e,2)})")

    return result(reasons)

def https_engine(url):
    reasons = []
    if not url.startswith("https://"):
        reasons.append("No HTTPS")
    return result(reasons)

def result(reasons):
    if len(reasons) >= 2:
        return "MALICIOUS", reasons
    elif len(reasons) == 1:
        return "SUSPICIOUS", reasons
    else:
        return "CLEAN", []
