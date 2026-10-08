from pathlib import Path
import re
p=Path('index.html')
html=p.read_text(encoding='utf-8-sig')
for code in [0x2013,0x2014,0x2022,0x2193,0x2191,0x00b7,0x2018,0x2019,0x201c,0x201d]:
    correct=chr(code)
    try: damaged=correct.encode('utf-8').decode('cp1252')
    except UnicodeDecodeError: continue
    html=html.replace(damaged,correct)
html=html.replace('<meta charset="utf-8">','<meta charset="UTF-8">')
html=re.sub(r'<div class="hero-identity">.*?</div>', '<div class="hero-identity"><p class="identity-title"><span>Data Analyst</span><span>&amp; Researcher</span></p><p class="identity-note">Experience in station management, laboratory research and machine learning.</p></div>', html, count=1)
html=re.sub(r'<p class="hero-description">.*?</p>', '<p class="hero-description"><span>A background in biotechnology.</span> <span>A career spanning data, research and operations.</span></p>',html,count=1)
html=html.replace('<span>Data Analytics. Research. Operations.</span>','<span>Biotechnology &middot; Data &middot; Business</span>')
html=html.replace('<h1 id="owner-name" class="hero-name"><span class="name-first">Nathaniel</span><span>Carlson Appiah</span></h1>', '<h1 id="owner-name" class="hero-name"><span class="name-first">Nathaniel</span> <span class="name-surname"><span>Carlson</span> <span>Appiah</span></span></h1>')
html=html.replace('(CV date: October 2025)','(October 2025, as listed in my CV)')
html=re.sub(r'[^\x00-\x7f]', lambda m:'&#x'+format(ord(m.group()),'X')+';',html)
assert 'CV date:' not in html
assert '&#xE2;' not in html
p.write_text(html,encoding='utf-8')
p=Path('styles.css')
css=p.read_text(encoding='utf-8-sig')
css=css.replace('.hero-description{position:absolute;top:300px;left:var(--gutter);font-size:23px;line-height:1.3;max-width:240px}', '.hero-description{position:absolute;top:245px;left:var(--gutter);font-size:21px;line-height:1.4;max-width:260px}.hero-description span{display:block}.hero-description span+span{margin-top:7px}')
css=css.replace('.identity-title{font-size:clamp(36px,3.4vw,54px);font-weight:700;line-height:.98;letter-spacing:-.025em}', '.identity-title{font-size:clamp(32px,3vw,46px);font-weight:600;line-height:1.04;letter-spacing:-.02em}')
css=css.replace('.identity-note .role-date{margin-top:7px;color:var(--muted);font-size:.9em}','')
css=css.replace('.identity-note{font-size:16px;line-height:1.4;margin-top:19px}', '.identity-note{font-size:18px;line-height:1.4;margin-top:17px;max-width:29ch}')
css=css.replace('.hero-description{top:255px;font-size:20px;max-width:185px}', '.hero-description{top:225px;font-size:18px;max-width:185px}')
css=css.replace('.identity-title{font-size:clamp(28px,3.5vw,38px)}.identity-note{font-size:14px;max-width:none}', '.identity-title{font-size:clamp(25px,3.1vw,34px)}.identity-note{font-size:16px;max-width:none}')
css=css.replace('.hero-name .name-first{font-size:.78em;margin-bottom:7px}', '.hero-name .name-first{font-size:.78em;margin-bottom:7px}.hero-name .name-surname{display:flex;gap:.18em}')
css=css.replace('.identity-title{font-size:40px}.identity-note{font-size:16px;max-width:none;margin-top:16px}', '.identity-title{font-size:30px}.identity-note{font-size:18px;max-width:30ch;margin-top:13px}')
css=css.replace('.identity-title{font-size:36px}.identity-note{font-size:15px}', '.identity-title{font-size:28px}.identity-note{font-size:17px}')
p.write_text(css,encoding='utf-8')
print('Repaired HTML punctuation; saved UTF-8 sources with entity-safe HTML. Updated only hero content/styles and the old CV-date label.')
