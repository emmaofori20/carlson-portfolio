from pathlib import Path
import json
from playwright.sync_api import sync_playwright
out = Path('tmp/preview')
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    page = browser.new_page()
    errors=[]
    page.on('pageerror', lambda e: errors.append(str(e)))
    results=[]
    for name, width, height in [('desktop',1440,1000),('tablet',768,1024),('mobile',390,844),('small-mobile',320,740)]:
        page.set_viewport_size({'width':width,'height':height})
        page.goto('http://127.0.0.1:4173/',wait_until='networkidle')
        page.evaluate('document.fonts.ready')
        page.screenshot(path=str(out / (name+'.png')),full_page=True)
        result=page.evaluate('''() => ({width:innerWidth, documentWidth:document.documentElement.scrollWidth, brokenImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src), fonts:document.fonts.check('600 20px "Barlow Condensed"'), anchors:[...document.querySelectorAll('a[href^="#"]')].every(a=>!!document.querySelector(a.getAttribute('href'))), overflowing:[...document.querySelectorAll('main *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1||e.getBoundingClientRect().left< -1).map(e=>e.className).slice(0,10)})''')
        result['viewport']=name
        results.append(result)
    page.get_by_text('Project contributions',exact=True).click()
    assert page.locator('.research-primary details').get_attribute('open') is not None
    page.get_by_role('link',name='Contact',exact=True).click()
    page.wait_for_timeout(700)
    assert page.url.endswith('#contact')
    page.goto('http://127.0.0.1:4173/')
    page.keyboard.press('Tab')
    assert page.locator('.skip-link').evaluate('(e)=>e===document.activeElement')
    page.emulate_media(reduced_motion='reduce')
    motion=page.locator('html').evaluate('(e)=>getComputedStyle(e).scrollBehavior')
    assert motion=='auto'
    pdf=page.request.get('http://127.0.0.1:4173/source/carlson.pdf')
    assert pdf.ok and pdf.body().startswith(b'%PDF')
    print(json.dumps({'viewports':results,'pageErrors':errors,'pdfDownload':'valid PDF','keyboardSkipLink':'passed','details':'passed','contactAnchor':'passed','reducedMotion':motion},indent=2))
    browser.close()

