from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge')
    page=browser.new_page()
    widths=[320,390,480,600,760,768,820,1024,1440,1920]
    results=[]
    for width in widths:
        page.set_viewport_size({'width':width,'height':1000})
        page.goto('http://127.0.0.1:4173/',wait_until='networkidle')
        dimensions=page.evaluate('''() => ({viewport:innerWidth, content:document.documentElement.scrollWidth, image:[document.querySelector('.hero-portrait img').naturalWidth,document.querySelector('.hero-portrait img').naturalHeight], greeting:getComputedStyle(document.querySelector('.hero-greeting')).fontFamily})''')
        assert dimensions['content']==width,dimensions
        results.append(dimensions)
        if width==1440: page.screenshot(path='tmp/preview/desktop-hero.png')
        if width==390: page.screenshot(path='tmp/preview/mobile-hero.png')
    print(json.dumps(results,indent=2))
    browser.close()
