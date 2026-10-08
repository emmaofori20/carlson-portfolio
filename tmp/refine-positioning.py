from pathlib import Path
p=Path('index.html')
html=p.read_text(encoding='utf-8-sig')
old='<div class="hero-identity"><p class="identity-title">Research<br>assistant</p><p class="identity-note">Laboratory experience, 2022–2023<br>Machine learning internship, 2023–2024</p></div>'
new='<div class="hero-identity"><p class="identity-title"><span>Data Analytics</span><span>&amp; Research</span><span>Professional</span></p><p class="identity-note"><span>Station Manager — More Fuel Limited</span><span>Research • Analytics • Operations</span><span class="role-date">CV date: October 2025</span></p></div>'
assert old in html
html=html.replace(old,new)
html=html.replace('Water quality. Data analytics. Biotechnology.','Data Analytics. Research. Operations.')
html=html.replace('A foundation in data.<br> A perspective shaped<br> by laboratory research.','A foundation in data.<br> Experience across research<br> and business operations.')
html=html.replace('Computing, chemistry<br>and a curiosity for<br>what the data can tell us.','Data, research<br>and the operations<br>that bring them together.')
html=html.replace("I'm Nathaniel Carlson Appiah. My background brings together data analytics and computing, laboratory research, and agricultural biotechnology education.","I'm Nathaniel Carlson Appiah. My multidisciplinary background brings together station management and business operations, data analytics and machine learning, laboratory research and water analysis, and agricultural biotechnology education.")
html=html.replace("I've worked with water-quality data during an internship at GSSTI and with experimental procedures as a Research Assistant. Alongside research, my experience includes operations, administration, inventory management and client relationships.","My most recently listed role is Station Manager at More Fuel Limited, with October 2025 recorded in my CV. That experience includes station operations, sales, inventory management and client relationships. The CV does not specify an end date or confirm that the role is ongoing.")
html=html.replace('<a class="text-link download-link"',"<p>Earlier, I contributed to water-quality machine learning during an internship at GSSTI (October 2023 – September 2024) and worked as a Research Assistant in laboratory research and water analysis (November 2022 – September 2023). My academic background includes Agricultural Biotechnology.</p><a class=\"text-link download-link\"",1)
html=html.replace("Nathaniel Carlson Appiah's research portfolio: water-quality machine learning, laboratory research, data analytics and a background in agricultural biotechnology.","Nathaniel Carlson Appiah's portfolio: data analytics, machine learning, laboratory research, water analysis, station management and business operations, with an agricultural biotechnology background.")
p.write_text(html,encoding='utf-8')
p=Path('styles.css')
css=p.read_text(encoding='utf-8-sig')
css=css.replace('.hero-identity{position:absolute;right:var(--gutter);bottom:123px}', '.hero-identity{position:absolute;right:var(--gutter);bottom:123px;width:min(24vw,340px)}')
css=css.replace('.identity-title{font-size:clamp(44px,4.2vw,68px);font-weight:700;line-height:.94;letter-spacing:-.025em}', '.identity-title{font-size:clamp(36px,3.4vw,54px);font-weight:700;line-height:.98;letter-spacing:-.025em}.identity-title span,.identity-note span{display:block}.identity-title span{white-space:nowrap}.identity-note .role-date{margin-top:7px;color:var(--muted);font-size:.9em}')
css=css.replace('.hero-identity{bottom:125px}.identity-title{font-size:45px}.identity-note{font-size:14px;max-width:175px}', '.hero-identity{bottom:125px;width:22vw}.identity-title{font-size:clamp(28px,3.5vw,38px)}.identity-note{font-size:14px;max-width:none}')
css=css.replace('.hero-identity{position:relative;right:auto;bottom:auto;margin-top:28px;display:flex;gap:30px;align-items:end}.identity-title{font-size:40px}.identity-note{font-size:15px;max-width:180px;margin-top:0}', '.hero-identity{position:relative;right:auto;bottom:auto;margin-top:28px;display:block;width:auto}.identity-title{font-size:40px}.identity-note{font-size:16px;max-width:none;margin-top:16px}')
css=css.replace('.hero-identity{gap:15px}.identity-title{font-size:36px}.identity-note{font-size:13px}', '.identity-title{font-size:36px}.identity-note{font-size:15px}')
p.write_text(css,encoding='utf-8')
