from pathlib import Path
p=Path('styles.css')
css=p.read_text(encoding='utf-8')
css=css.replace('.hero{min-height:0;padding-top:486px;padding-bottom:113px}', '.hero{min-height:0;padding-top:545px;padding-bottom:113px}')
css=css.replace('.hero{min-height:0;padding-top:434px;padding-bottom:110px}', '.hero{min-height:0;padding-top:487px;padding-bottom:110px}')
p.write_text(css,encoding='utf-8')
