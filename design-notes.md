# Design direction

## Tokens
- Paper: #FAF9F6; ink: #111111; peach: #FFE3C0; cream: #F3E9D8; amber: #E8B768; secondary text: #595750.
- Cormorant Garamond italic: oversized greeting, section headings, contact invitation.
- Barlow Condensed bold: name and professional identity. Barlow Condensed regular: navigation and body copy, with comfortable size and line height.

## Composition
Desktop: centered portrait interrupts a broad italic greeting, with the name grounded left and research identity right. Body content is left aligned; a deliberately unequal project pair has a staggered baseline.

    brand             work / about / expertise            contact
                  oversized italic greeting
    short profile         PORTRAIT
    NATHANIEL             PORTRAIT             Research
    CARLSON APPIAH        PORTRAIT             assistant

    Selected research
    [ large water illustration ]      [ laboratory illustration ]
    Project and contribution          Research experience

    About / biography                 Education
    Expertise / three documented disciplines
    Contact / large invitation and real contact information

Mobile: greeting above and partly behind the portrait; the full name below the photograph; role and profile follow in readable document order. Work becomes one column. No fixed mobile navigation or hidden menu.

## Review against brief
The dramatic overlapping hero carries the expressive typography; supporting sections stay quiet. Revised the initial equal gallery into unequal, staggered research previews to avoid repeated card geometry. The second preview represents documented laboratory experience, explicitly distinguished from a separate project. No publication or availability claims are supported. Biotechnology appears as educational grounding, not claimed project experience. Current employment and degree completion are not inferred.

No reference screenshot was attached to the redesign request or found in the project. Composition follows the user's written reference description. The supplied assets/portrait.jpg is the actual owner photograph.

## Image asset provenance
Original portrait is preserved. Background extraction uses the built-in imagegen tool. Final prompt: Remove only the background, chairs, table, banner and room. Isolate the existing man from head through the visible lower torso on a genuinely transparent background. Preserve his exact face, skin tone, hair, expression, body proportions, crossed-arm pose, white shirt, printed shirt logo, hands and clothing; do not beautify, redraw, add, or invent any person or body parts. Retain the photographed subject as faithfully as possible. Crop away large empty space, create a clean natural cutout with accurate edges.

Research preview SVGs are abstract editorial illustrations created for this website, not scientific data, outputs, or photographs of the candidate's workplace.

## Final assets and verification
- Background-extracted portrait: assets/portrait-cutout.png, 1254 x 1254, transparent PNG. Original: assets/portrait.jpg, unchanged.
- Preview art: assets/water-study.svg and assets/laboratory-study.svg.
- Desktop, tablet and mobile screenshots reviewed; responsive page widths checked at 320, 390, 480, 600, 760, 768, 820, 1024, 1440 and 1920 pixels with no horizontal page overflow.
- Confirmed working in-page navigation, keyboard skip link, visible focus styles, expandable project contributions, valid PDF download, no broken images or JavaScript errors, and reduced-motion scroll behavior.
- Only the greeting and profile introduction animate on load. Disclosure controls use native HTML details elements; no JavaScript dependency is needed.
- Fonts load from Google Fonts with local serif and sans-serif fallbacks.
