#!/usr/bin/env python3
"""zlink.ae SEO audit (office control C-SEO-01).

Usage:
  python3 tools/seo_audit.py            # audit the files in this repo
  python3 tools/seo_audit.py --live     # also fetch every sitemap URL from https://zlink.ae
Exit code 1 if any FAIL.
"""
import glob, json, os, re, sys, urllib.request
from html.parser import HTMLParser

SITE = "https://zlink.ae"
# claims that must never appear (office record: Z-Link holds no manufacturer approvals and no DCD fire approval)
FORBIDDEN = [r"(?<!not a Sika )approved applicator", r"certified applicator",
             r"DCD[- ]approved contractor", r"Civil Defence approved contractor", r"guaranteed (?:first|top|#1)"]
NAP = ["Office 201, Bay Square, Business Bay", "+971", "info@zlink.ae"]


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tags = []; s.links = []; s.imgs = []; s.h1 = 0; s.ld = []; s._ld = False; s.title = ''; s._t = False; s.meta = {}; s.canon = None; s.text = []
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == 'a' and a.get('href'): s.links.append(a['href'])
        if t == 'img': s.imgs.append(a)
        if t == 'h1': s.h1 += 1
        if t == 'title': s._t = True
        if t == 'meta' and a.get('name'): s.meta[a['name']] = a.get('content', '')
        if t == 'link' and a.get('rel') == 'canonical': s.canon = a.get('href')
        if t == 'script' and a.get('type') == 'application/ld+json': s._ld = True; s.ld.append('')
    def handle_endtag(s, t):
        if t == 'title': s._t = False
        if t == 'script': s._ld = False
    def handle_data(s, d):
        if s._t: s.title += d
        elif s._ld: s.ld[-1] += d
        else: s.text.append(d)


def url_of(path):
    rel = os.path.relpath(path, '.').replace(os.sep, '/')
    return SITE + '/' + (rel[:-10] if rel.endswith('index.html') else rel)


def main():
    live = '--live' in sys.argv
    fails, warns = [], []
    pages = [p for p in glob.glob('**/index.html', recursive=True) if not p.startswith(('tools', 'node_modules', '.git'))]
    sitemap = re.findall(r'<loc>([^<]+)</loc>', open('sitemap.xml').read())
    titles = {}
    if 'Sitemap: https://zlink.ae/sitemap.xml' not in open('robots.txt').read() or 'Disallow: /\n' in open('robots.txt').read():
        fails.append('robots.txt: sitemap line missing or site disallowed')
    for p in sorted(pages):
        u = url_of(p); src = open(p, encoding='utf-8').read(); x = P(); x.feed(src)
        tag = u.replace(SITE, '') or '/'
        t = x.title.strip()
        if not t or len(t) > 65: fails.append(f'{tag}: title length {len(t)} (need 1-65)')
        titles.setdefault(t, []).append(tag)
        dsc = x.meta.get('description', '')
        if not 70 <= len(dsc) <= 165: fails.append(f'{tag}: meta description length {len(dsc)} (need 70-165)')
        if x.canon != u: fails.append(f'{tag}: canonical {x.canon} != {u}')
        if x.h1 != 1: fails.append(f'{tag}: {x.h1} H1 tags (need exactly 1)')
        if u not in sitemap: fails.append(f'{tag}: not in sitemap.xml')
        for i in x.imgs:
            if i.get('alt') is None: fails.append(f'{tag}: image without alt attribute {i.get("src", "")[:60]}')
        if not x.ld: fails.append(f'{tag}: no JSON-LD')
        for b in x.ld:
            try: json.loads(b)
            except Exception as e: fails.append(f'{tag}: invalid JSON-LD ({e})')
        for l in x.links:
            if l.startswith('/') and not l.startswith('//'):
                path = l.split('#')[0]
                f = '.' + path + ('index.html' if path.endswith('/') else '')
                if not os.path.exists(f): fails.append(f'{tag}: broken internal link {l}')
        body = ' '.join(x.text)
        for pat in FORBIDDEN:
            if re.search(pat, body, re.I): fails.append(f'{tag}: forbidden claim matched /{pat}/')
        for n in NAP:
            if n not in src: warns.append(f'{tag}: NAP item missing "{n}"')
        m = src[src.find('<main'):src.find('</main>')] if '<main' in src else src
        words = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', m, flags=re.S)).split())
        if words < 300: warns.append(f'{tag}: thin content ({words} words)')
    for t, us in titles.items():
        if len(us) > 1: fails.append(f'duplicate title "{t}" on {us}')
    for s in sitemap:
        rel = s.replace(SITE, '')
        if not os.path.exists('.' + rel + ('index.html' if rel.endswith('/') else '')): fails.append(f'sitemap URL with no file: {s}')
    if live:
        for s in sitemap:
            try:
                r = urllib.request.urlopen(urllib.request.Request(s, headers={'User-Agent': 'zlink-seo-audit'}), timeout=20)
                if r.status != 200: fails.append(f'LIVE {s}: HTTP {r.status}')
            except Exception as e:
                fails.append(f'LIVE {s}: {e}')
    print(f'Pages: {len(pages)} · Sitemap URLs: {len(sitemap)}')
    for f in fails: print('FAIL', f)
    for w in warns: print('WARN', w)
    print('RESULT:', 'FAIL' if fails else ('PASS WITH NOTES' if warns else 'PASS'))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
