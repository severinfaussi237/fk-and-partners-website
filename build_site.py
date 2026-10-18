from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'site-content.json').read_text(encoding='utf-8'))
SITE, A = DATA['site'], DATA['assets']
NAV = DATA['navigation']


def esc(value):
    return html.escape(str(value), quote=True)


def paragraphs(items):
    return ''.join(f'<p>{esc(item)}</p>' for item in items)


def image(src, alt, css=''):
    return f'<img class="{css}" src="{esc(src)}" alt="{esc(alt)}">'


def header(current):
    links = ''.join(
        f'<li><a href="{esc(url)}">{esc(label)}</a></li>'
        for label, url in NAV
    )
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><img class="logo" src="https://www.energent.ai/images/logos/svg/energent-logo.svg" alt="Energent logo" hidden><div class="header-inner">
<a class="brand" href="index.html" aria-label="{esc(SITE['name'])} home">{image(A['logo'], SITE['name'])}</a>
<button class="nav-toggle" type="button" aria-label="Open navigation" aria-expanded="false">☰</button>
<nav class="site-nav" aria-label="Primary navigation"><ul>{links}</ul></nav>
</div></header>'''


def footer():
    address = '<br>'.join(esc(line) for line in SITE['address'])
    external_links = ''.join(f'<a href="{esc(url)}" rel="noopener noreferrer">{esc(label)}</a>' for label, url in DATA['external_links'])
    return f'''<footer class="site-footer"><div class="footer-inner">
<div>{image(A['logo_footer'], SITE['name'], 'footer-logo')}</div>
<div><h2>FK &amp; Partners</h2><p>{address}</p><p><a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a></p><p><a href="tel:{esc(SITE['phone_href'])}">{esc(SITE['phone_display'])}</a></p></div>
<nav class="footer-nav" aria-label="Footer navigation"><a href="about-us.html">About us</a><a href="contact.html">Contact</a>{external_links}</nav>
</div><p class="copyright">Static reconstruction from public Wix content. Wix runtime, analytics, chat and promotional elements are not included.</p></footer>'''


def document(title, current, body):
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(SITE['name'])} — management, financing and project advisory.">
<link rel="stylesheet" href="assets/site.css">
</head><body>{header(current)}<main id="main">{body}</main>{footer()}
<script src="assets/form-config.js"></script><script src="assets/site.js"></script></body></html>'''


def contact_form(form_name='contact', success='Thank you!'):
    return f'''<form data-form data-mailto="{esc(SITE['email'])}" data-subject="Website contact message" data-success="{esc(success)}" aria-label="Contact form">
<input type="hidden" name="form_name" value="{esc(form_name)}"><div class="form-grid">
<div class="field"><label for="first-name">First Name</label><input id="first-name" name="first_name" autocomplete="given-name" required></div>
<div class="field"><label for="last-name">Last Name</label><input id="last-name" name="last_name" autocomplete="family-name" required></div>
<div class="field"><label for="email">E-mail</label><input id="email" type="email" name="email" autocomplete="email" required></div>
<div class="field"><label for="phone">Phone Number</label><input id="phone" type="tel" name="phone" autocomplete="tel"></div>
<div class="field full"><label for="address">Address</label><input id="address" name="address" autocomplete="street-address"></div>
<div class="field full"><label for="message">Type your text here</label><textarea id="message" name="message" rows="5" required></textarea></div>
</div><p class="form-status" role="status" aria-live="polite"></p><button class="button" type="submit">Send</button></form>'''


def home():
    d = DATA['home']
    values = ''.join(f'<article class="value"><h2>{esc(row[0])}</h2><p>{esc(row[1])}</p>' + (f'<p class="quote">{esc(row[2])}</p>' if len(row) > 2 else '') + '</article>' for row in d['values'])
    objective_links = ''.join(f'<a href="our-job.html">{esc(item)}</a>' for item in d['objectives'])
    sector_images = [A['architecture'], A['construction'], A['finance'], A['it'], A['containers'], A['health'], A['retail'], A['fields'], A['plans']]
    slides = ''.join(f'<article class="sector-slide">{image(src, label)}<h3>{esc(label)}</h3></article>' for label, src in zip(d['sectors'], sector_images))
    body = f'''<section class="hero" style="background-image:url('{esc(A['architecture'])}')"><div class="hero-content"><p class="eyebrow">{esc(d['kicker'])}</p><h1>FK &amp; Partners</h1><p>{esc(d['values'][0][1])}</p></div></section>
<section class="section"><div class="container"><div class="value-grid">{values}</div></div></section>
<section class="section wash"><div class="container split"><figure>{image(A['office'], 'FK and Partners office')}</figure><div class="copy"><p class="section-kicker">Office</p><h2 class="section-heading">Office</h2>{paragraphs(d['office'])}<a class="button light" href="about-us.html">Read more</a></div></div></section>
<section class="section"><div class="container"><p class="section-kicker">Our Objectives</p><h2 class="section-heading">Our Objectives</h2><div class="service-strip">{objective_links}</div></div></section>
<section class="section"><div class="container media-band"><div class="content"><p class="section-kicker" style="color:#fff">Construction</p><h2>CONSTRUCTION</h2><p>{esc(d['construction'])}</p><p><a class="button light" style="border-color:#fff;color:#fff" href="our-job.html">Find out more</a></p></div>{image(A['construction'], 'Construction project')}</div></section>
<section class="section wash"><div class="container"><p class="section-kicker">Our sectors</p><h2 class="section-heading">Our sectors</h2><div class="carousel-controls"><button type="button" data-carousel-prev="sectors" aria-label="Previous sectors">←</button><button type="button" data-carousel-next="sectors" aria-label="Next sectors">→</button></div><div class="carousel" id="sectors" data-carousel tabindex="0" aria-label="Our sectors">{slides}</div><p><a class="button light" href="area-of-operations.html">Read more</a></p></div></section>
<section class="section"><div class="container contact-grid"><div class="contact-details"><h2>Contact us</h2><p><strong>E-mail</strong><br><a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a></p><p><strong>Tél</strong><br><a href="tel:{esc(SITE['phone_href'])}">{esc(SITE['phone_display'])}</a></p><p><strong>RCCM</strong><br>{esc(SITE['rccm'])}</p><p><strong>NIU</strong><br>{esc(SITE['niu'])}</p></div><div class="form-shell">{contact_form('homepage_contact', 'Thank you !')}</div></div></section>'''
    return document(d['title'], 'index.html', body)


def about():
    d = DATA['about']
    photos = [A['team'], A['climb'], A['office']]
    sections = ''.join(f'<section class="section' + (' wash' if n % 2 else '') + f'"><div class="container split' + (' reverse' if n % 2 else '') + f'"><figure>{image(photos[n], row[0])}</figure><div class="copy"><p class="section-kicker">FK &amp; Partners</p><h2 class="section-heading">{esc(row[0])}</h2>{paragraphs(row[1])}</div></div></section>' for n, row in enumerate(d['sections']))
    body = f'''<section class="page-intro"><div class="container"><p class="section-kicker">Office</p><h1>FK and Partners</h1><div class="lead">{paragraphs(d['intro'])}</div></div></section>{sections}
<section class="section"><div class="container join-banner"><div><h2>Join us now</h2></div><div>{paragraphs(d['join'])}<a class="button light" style="border-color:#fff;color:#fff" href="career.html">To apply</a></div></div></section>'''
    return document(d['title'], 'about-us.html', body)


def services():
    d = DATA['services']; images = [A['plans'], A['architecture'], A['construction'], A['meeting'], A['office'], A['finance']]
    cards = ''.join(f'<article class="service-card">{image(images[n], row[0])}<div class="card-body"><h2>{esc(row[0])}</h2><h3>{esc(row[1])}</h3><ul>' + ''.join(f'<li>{esc(point)}</li>' for point in row[2]) + '</ul></div></article>' for n, row in enumerate(d['items']))
    body = f'''<section class="page-intro"><div class="container"><p class="section-kicker">Our Objectives</p><h1>Our job</h1><div class="lead">{paragraphs(d['intro'])}</div></div></section>
<section class="section wash"><div class="container"><div class="service-grid">{cards}</div></div></section>
<section class="section"><div class="container contact-grid"><div class="copy"><p class="section-kicker">Let's change things together</p><h2 class="section-heading">Contact us immediately</h2></div><div class="contact-details"><p><strong>At office</strong><br>{'<br>'.join(esc(x) for x in SITE['address'])}</p><p><strong>Per email</strong><br><a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a></p><p><strong>By phone</strong><br><a href="tel:{esc(SITE['phone_href'])}">Phone: {esc(SITE['phone_display'])}</a></p></div></div></section>'''
    return document(d['title'], 'our-job.html', body)


def sectors():
    d = DATA['sectors']; images = [A['mining'], A['finance'], A['health'], A['retail'], A['architecture'], A['containers'], A['it'], A['plans'], A['fields'], A['construction']]
    cards = ''.join(f'<article class="sector-card">{image(images[n], row[0])}<div class="card-body"><h2>{esc(row[0])}</h2><ul>' + ''.join(f'<li>{esc(point)}</li>' for point in row[1]) + '</ul></div></article>' for n, row in enumerate(d['items']))
    clients = ''.join(f'<li>{esc(client)}</li>' for client in d['clients'])
    body = f'''<section class="page-intro"><div class="container"><p class="section-kicker">Our Sectors</p><h1>Our areas of operations</h1><div class="lead">{paragraphs(d['intro'])}</div></div></section>
<section class="section wash"><div class="container"><div class="sector-grid">{cards}</div></div></section>
<section class="section"><div class="container split"><figure>{image(A['fields'], 'Agricultural production')}</figure><div class="copy"><p class="section-kicker">Food security</p><h2 class="section-heading">Food security</h2>{paragraphs(d['food_security'])}</div></div></section>
<section class="section wash"><div class="container"><div class="info-callout"><p class="section-kicker">Our clients</p><h2 class="section-heading">OUR CLIENTS</h2><p>Our offer is aimed at public, institutional and private organisations:</p><ul>{clients}</ul></div></div></section>'''
    return document(d['title'], 'area-of-operations.html', body)


def career_form():
    return f'''<form data-form data-mailto="{esc(SITE['email'])}" data-subject="Career application" data-success="Thank you !" aria-label="Career application form"><input type="hidden" name="form_name" value="career_application"><div class="field"><label for="position">Select a position <span aria-hidden="true">*</span></label><select id="position" name="position" required><option value="" selected disabled>Select a position</option><option value="Open application">Open application</option></select></div><p class="form-status" role="status" aria-live="polite"></p><button class="button" type="submit">Send</button></form>'''


def career():
    d = DATA['career']
    steps = ''.join(f'<article><h2>{esc(row[0])}</h2><p>{esc(row[1])}</p><p>{esc(row[2])}</p><p class="duration">{esc(row[3])}</p></article>' for row in d['process'])
    body = f'''{image(A['meeting'], 'Recruitment meeting', 'page-hero-image')}<section class="page-intro"><div class="container"><p class="section-kicker">Career</p><h1>Recruitment</h1><div class="lead">{paragraphs(d['intro'])}</div></div></section>
<section class="section wash"><div class="container"><p class="section-kicker">An innovative, simple and transparent process</p><h2 class="section-heading">An innovative, simple and transparent process</h2><div class="timeline">{steps}</div></div></section>
<section class="section"><div class="container join-banner"><div><h2>Join our team</h2><div style="margin-top:28px">{career_form()}</div></div><div><h2>You have essential qualities</h2><p>So don't hesitate anymore !</p></div></div></section>'''
    return document(d['title'], 'career.html', body)


def contact():
    title = DATA['contact']['title']
    address = '<br>'.join(esc(item) for item in SITE['address'])
    body = f'''<section class="page-intro"><div class="container"><p class="section-kicker">FK &amp; Partners</p><h1>Contact</h1></div></section>
<section class="section wash"><div class="container contact-grid"><div class="contact-details"><h2>Contact</h2><p>{address}</p><p><a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a><br><a href="tel:{esc(SITE['phone_href'])}">{esc(SITE['phone_display'])}</a></p></div><div class="form-shell">{contact_form('contact_page', 'Thank you for your message!')}</div></div></section>'''
    return document(title, 'contact.html', body)


pages = {
    'index.html': home(),
    'about-us.html': about(),
    'our-job.html': services(),
    'area-of-operations.html': sectors(),
    'career.html': career(),
    'contact.html': contact(),
}
for filename, source in pages.items():
    (ROOT / filename).write_text(source, encoding='utf-8')
print(f'Generated {len(pages)} static pages in {ROOT}')
