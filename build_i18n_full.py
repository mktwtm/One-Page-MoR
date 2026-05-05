# -*- coding: utf-8 -*-
"""
Complete i18n pass: add data-i18n attrs to every remaining element
and replace the T object with full EN / PT / ES translations.
"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\mtboh\OneDrive\My Documents\Antigravity\WTM\One Page MoR\wtm'

with open(f'{BASE}/index.html', encoding='utf-8') as f:
    h = f.read()

# ── simple attr injection ─────────────────────────────────────────────────────
def ia(html, search, attr, key, only_first=True):
    idx = html.find(search)
    if idx == -1:
        print(f'  MISS [{key}]: {search[:70]!r}')
        return html
    close = html.index('>', idx)
    tag = html[idx:close]
    if attr in tag:
        return html
    return html[:idx] + tag + f' {attr}="{key}"' + html[close:]

# ── inline text replacement (for elements without good opening-tag hook) ──────
def ir(html, old, new):
    if old not in html:
        print(f'  MISS ir: {old[:70]!r}')
        return html
    return html.replace(old, new, 1)

# ═══════════════════════════════════════════════════════════════════════════════
# S3 — COMMERCIAL
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<div class="eyebrow">Commercial impact</div>',
    '<div class="eyebrow" data-i18n="commercial.eyebrow">Commercial impact</div>')

h = ir(h,
    '<h2 class="h-section" style="margin-top:18px">\n          This is not a tax department problem. It is a revenue problem.\n        </h2>',
    '<h2 class="h-section" data-i18n="commercial.h2" style="margin-top:18px">\n          This is not a tax department problem. It is a revenue problem.\n        </h2>')

h = ir(h,
    '<p class="lead">\n          A U.S. SaaS vendor',
    '<p class="lead" data-i18n="commercial.lead">\n          A U.S. SaaS vendor')

# KPI rows — wrap the text in a span so we preserve the dot sibling
h = ir(h,
    "<p>When the Brazilian customer's tax cost increases, your <strong>churn rate rises</strong>",
    '<p data-i18n-html="commercial.kpi1">When the Brazilian customer\'s tax cost increases, your <strong>churn rate rises</strong>')
h = ir(h,
    '<p><strong>CAC increases</strong> as sales teams spend more time',
    '<p data-i18n-html="commercial.kpi2"><strong>CAC increases</strong> as sales teams spend more time')
h = ir(h,
    '<p><strong>Expansion revenue slows</strong>',
    '<p data-i18n-html="commercial.kpi3"><strong>Expansion revenue slows</strong>')
h = ir(h,
    '<p><strong>Enterprise deals stall</strong>',
    '<p data-i18n-html="commercial.kpi4"><strong>Enterprise deals stall</strong>')
h = ir(h,
    '<p>Local billing with WTM <strong>turns compliance into a growth lever</strong>',
    '<p data-i18n-html="commercial.kpi5">Local billing with WTM <strong>turns compliance into a growth lever</strong>')

# consequence cards
h = ir(h,
    '<h3 class="h-card">Churn risk</h3>\n          <p>Customers may cancel',
    '<h3 class="h-card" data-i18n="cc1.title">Churn risk</h3>\n          <p data-i18n="cc1.body">Customers may cancel')
h = ir(h,
    '<h3 class="h-card">CAC pressure</h3>\n          <p>Longer sales cycles driven',
    '<h3 class="h-card" data-i18n="cc2.title">CAC pressure</h3>\n          <p data-i18n="cc2.body">Longer sales cycles driven')
h = ir(h,
    '<h3 class="h-card">RFP disqualification</h3>',
    '<h3 class="h-card" data-i18n="cc3.title">RFP disqualification</h3>')
h = ir(h,
    '<p>Without local invoicing capability',
    '<p data-i18n="cc3.body">Without local invoicing capability')
h = ir(h,
    '<h3 class="h-card">Provider liability</h3>',
    '<h3 class="h-card" data-i18n="cc4.title">Provider liability</h3>')
h = ir(h,
    '<p>As the Netflix/CIDE precedent shows',
    '<p data-i18n="cc4.body">As the Netflix/CIDE precedent shows')

# ═══════════════════════════════════════════════════════════════════════════════
# S4 — CASE STUDIES
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<div class="eyebrow" style="color:#E59A8E">Real precedents</div>',
    '<div class="eyebrow" data-i18n="case.eyebrow" style="color:#E59A8E">Real precedents</div>')

h = ir(h,
    '<h2 class="h-section" style="margin-top:18px">\n        The companies that ignored',
    '<h2 class="h-section" data-i18n="case.h2" style="margin-top:18px">\n        The companies that ignored')

h = ir(h,
    '<span class="case-meta">Earnings impact &middot; Global investor event</span>',
    '<span class="case-meta" data-i18n="case1.meta">Earnings impact &middot; Global investor event</span>')

h = ir(h,
    '<p class="case-stat-label">Tax-related expense connected',
    '<p class="case-stat-label" data-i18n="case1.stat1label">Tax-related expense connected')

h = ir(h,
    '<div class="case-stat smaller">~10% drop</div>',
    '<div class="case-stat smaller" data-i18n="case1.stat2">~10% drop</div>')

h = ir(h,
    '<p class="case-stat-label">Share price decline',
    '<p class="case-stat-label" data-i18n="case1.stat2label">Share price decline')

h = ir(h,
    '<span>Brazil tax issues can become earnings issues.</span>',
    '<span data-i18n="case1.l1">Brazil tax issues can become earnings issues.</span>')
h = ir(h,
    '<span>Brazil tax issues can become investor-relations issues.</span>',
    '<span data-i18n="case1.l2">Brazil tax issues can become investor-relations issues.</span>')
h = ir(h,
    '<span>Board-level visibility increases once the exposure becomes material.</span>',
    '<span data-i18n="case1.l3">Board-level visibility increases once the exposure becomes material.</span>')

h = ir(h,
    '<span class="case-meta">Substance over form</span>',
    '<span class="case-meta" data-i18n="case2.meta">Substance over form</span>')

h = ir(h,
    '<blockquote>\n          Brazilian authorities may look beyond',
    '<blockquote data-i18n-html="case2.quote">\n          Brazilian authorities may look beyond')

h = ir(h,
    '<p class="case-quote-sub">The questions regulators ask',
    '<p class="case-quote-sub" data-i18n="case2.quotesub">The questions regulators ask')

h = ir(h,
    '<div class="eyebrow eyebrow-light" style="color:rgba(255,255,255,.5)">The lesson for every U.S. SaaS company</div>',
    '<div class="eyebrow eyebrow-light" data-i18n="case2.diveyebrow" style="color:rgba(255,255,255,.5)">The lesson for every U.S. SaaS company</div>')

h = ir(h,
    '<p style="font-size:14.5px;color:rgba(236,236,238,.7);line-height:1.65">\n            Brazilian tax issues are no longer',
    '<p data-i18n="case2.divbody" style="font-size:14.5px;color:rgba(236,236,238,.7);line-height:1.65">\n            Brazilian tax issues are no longer')

# ═══════════════════════════════════════════════════════════════════════════════
# S5 — QUOTE
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<span class="accent">you need the transaction to work.</span>',
    '<span class="accent" data-i18n="quote.line2">you need the transaction to work.</span>')

# ═══════════════════════════════════════════════════════════════════════════════
# S6 — SOLUTION
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<div class="eyebrow">WTM Merchant of Record</div>',
    '<div class="eyebrow" data-i18n="solution.eyebrow">WTM Merchant of Record</div>')

h = ir(h,
    '<h2 class="h-section" style="margin-top:18px">\n        A Merchant of Record built',
    '<h2 class="h-section" data-i18n="solution.h2" style="margin-top:18px">\n        A Merchant of Record built')

h = ir(h,
    '<p class="lead">\n        WTM operates as your local',
    '<p class="lead" data-i18n="solution.lead">\n        WTM operates as your local')

# MOR diagram columns
h = ir(h,
    '<span class="mor-col-label">01. Buyer</span>',
    '<span class="mor-col-label" data-i18n="mor.buyer.label">01. Buyer</span>')
h = ir(h,
    '<h4>Brazilian customer</h4>',
    '<h4 data-i18n="mor.buyer.title">Brazilian customer</h4>')

h = ir(h,
    '<span class="mor-col-label">02. Merchant of Record</span>',
    '<span class="mor-col-label" data-i18n="mor.wtm.label">02. Merchant of Record</span>')
h = ir(h,
    '<span class="wtm-badge">Active in Brazil</span>',
    '<span class="wtm-badge" data-i18n="mor.wtm.badge">Active in Brazil</span>')

h = ir(h,
    '<span class="mor-col-label">03. Seller (you)</span>',
    '<span class="mor-col-label" data-i18n="mor.seller.label">03. Seller (you)</span>')
h = ir(h,
    '<h4>Your business</h4>',
    '<h4 data-i18n="mor.seller.title">Your business</h4>')

# MOR lists — use data-i18n-html on the <ul> elements (3 of them)
h = ir(h,
    '<ul>\n          <li>Buys locally, in BRL</li>',
    '<ul data-i18n-html="mor.buyer.list">\n          <li>Buys locally, in BRL</li>')
h = ir(h,
    '<ul>\n          <li>Local billing &amp;',
    '<ul data-i18n-html="mor.wtm.list">\n          <li>Local billing &amp;')
h = ir(h,
    '<ul>\n          <li>Receives clean payment</li>',
    '<ul data-i18n-html="mor.seller.list">\n          <li>Receives clean payment</li>')

# ═══════════════════════════════════════════════════════════════════════════════
# S7 — COMPARE
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<div class="eyebrow">Comparison</div>',
    '<div class="eyebrow" data-i18n="compare.eyebrow">Comparison</div>')

h = ir(h,
    '<h2 class="h-section" style="margin-top:18px">Direct selling vs. selling through WTM.</h2>',
    '<h2 class="h-section" data-i18n="compare.h2" style="margin-top:18px">Direct selling vs. selling through WTM.</h2>')

# compare rows (topic, without, with) — without/with have lucide icons so use data-i18n-html
rows = [
    ('Tax handling',
     '<i data-lucide="x"></i>Buyer handles taxes manually, often incorrectly',
     '<i data-lucide="check"></i>WTM handles all collection and remittance',
     'compare.r1'),
    ('Local invoice',
     '<i data-lucide="x"></i>No Nota Fiscal — procurement friction',
     '<i data-lucide="check"></i>Compliant NF-e issued for every transaction',
     'compare.r2'),
    ('Tax credits (CBS/IBS)',
     '<i data-lucide="x"></i>No local credits generated for buyer',
     '<i data-lucide="check"></i>Buyer generates full CBS/IBS credits',
     'compare.r3'),
    ('Provider liability',
     '<i data-lucide="x"></i>You may carry retroactive liability',
     '<i data-lucide="check"></i>Exposure dramatically reduced via WTM structure',
     'compare.r4'),
    ('Churn risk',
     '<i data-lucide="x"></i>Tax cost increase → cancellations and downgrades',
     '<i data-lucide="check"></i>Compliant path removes churn driver',
     'compare.r5'),
    ('Enterprise deals',
     '<i data-lucide="x"></i>RFP disqualification without local billing',
     '<i data-lucide="check"></i>Full documentation for finance, tax and procurement',
     'compare.r6'),
    ('Sales cycle',
     '<i data-lucide="x"></i>Longer cycles; higher CAC from tax objections',
     '<i data-lucide="check"></i>Smoother buying experience; lower friction at close',
     'compare.r7'),
]
for (topic, wo, wi, pfx) in rows:
    h = ir(h,
        f'<div class="cr-topic">{topic}</div>',
        f'<div class="cr-topic" data-i18n="{pfx}.topic">{topic}</div>')
    h = ir(h,
        f'<div class="cr-without">{wo}</div>',
        f'<div class="cr-without" data-i18n-html="{pfx}.without">{wo}</div>')
    h = ir(h,
        f'<div class="cr-with">{wi}</div>',
        f'<div class="cr-with" data-i18n-html="{pfx}.with">{wi}</div>')

# ═══════════════════════════════════════════════════════════════════════════════
# S8 — BENEFITS
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<div class="eyebrow">Why WTM</div>',
    '<div class="eyebrow" data-i18n="benefits.eyebrow">Why WTM</div>')

h = ir(h,
    '<h2 class="h-section" style="margin-top:18px">Key benefits.</h2>',
    '<h2 class="h-section" data-i18n="benefits.h2" style="margin-top:18px">Key benefits.</h2>')

benefit_cards = [
    ('Protect margins',
     'Reduce exposure to unexpected tax costs and pricing distortion. Correct tax embedding prevents the hidden margin erosion that surprises at renewal time.',
     'b1'),
    ('Increase win rate',
     'Offer a local, compliant buying experience that eliminates RFP disqualification and removes procurement objections before they stall the deal.',
     'b2'),
    ('Reduce churn &amp; CAC',
     'A structured local buying path removes the primary driver of tax-related churn and shortens sales cycles — directly improving NRR and lowering acquisition costs.',
     'b3'),
    ('Scale safely to 2033',
     "Use WTM's local infrastructure to navigate the full transition period through 2033 and expand across the broader LATAM market with confidence.",
     'b4'),
]
for (title, body, pfx) in benefit_cards:
    h = ir(h,
        f'<h3 class="h-card">{title}</h3>',
        f'<h3 class="h-card" data-i18n="{pfx}.title">{title}</h3>')
    h = ir(h,
        f'<p>{body}</p>',
        f'<p data-i18n="{pfx}.body">{body}</p>')

# ═══════════════════════════════════════════════════════════════════════════════
# S9 — ACTION STEPS
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<h2 class="h-section" style="color:#fff;margin-top:18px">Act before the reform becomes fully operational.</h2>',
    '<h2 class="h-section" data-i18n="action.h2" style="color:#fff;margin-top:18px">Act before the reform becomes fully operational.</h2>')

h = ir(h,
    '<p class="lead">The first step is not to open an entity',
    '<p class="lead" data-i18n="action.lead">The first step is not to open an entity')

steps = [
    ('Step 01','Map your Brazil footprint',
     'Identify all Brazilian customers, revenue streams and current payment methods to understand the full scope of your exposure.', 'a1'),
    ('Step 02','Estimate customer tax exposure',
     'Assess how much tax each customer currently carries — and model how that burden changes through the transition to 2033.','a2'),
    ('Step 03','Identify accounts at risk',
     'Flag customers most likely to churn, downgrade or delay renewal as tax costs increase and compliance scrutiny rises.','a3'),
    ('Step 04','Review contract language',
     'Assess whether your current agreements adequately address tax responsibility, liability allocation and compliance obligations.','a4'),
    ('Step 05','Prepare local billing with WTM',
     'Design a compliant local buying path — local invoice, payment in BRL, full CBS/IBS support — ready before customers ask.','a5'),
    ('Step 06','Train your go-to-market teams',
     'Align sales, finance, legal and customer success teams on how to position Brazil compliance as a competitive advantage, not a cost.','a6'),
]
for (step_label, title, body, pfx) in steps:
    h = ir(h, f'<span class="step">{step_label}</span>', f'<span class="step" data-i18n="{pfx}.step">{step_label}</span>')
    h = ir(h, f'<h4>{title}</h4>', f'<h4 data-i18n="{pfx}.title">{title}</h4>')
    h = ir(h, f'<p>{body}</p>', f'<p data-i18n="{pfx}.body">{body}</p>')

# ═══════════════════════════════════════════════════════════════════════════════
# S10 — GLOBE
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<div class="eyebrow eyebrow-light" style="color:#A8DCE8">Global presence</div>',
    '<div class="eyebrow eyebrow-light" data-i18n="globe.eyebrow" style="color:#A8DCE8">Global presence</div>')
h = ir(h,
    '<h2 class="h-section" style="color:#fff;margin-top:18px">Operating where your customers need you.</h2>',
    '<h2 class="h-section" data-i18n="globe.h2" style="color:#fff;margin-top:18px">Operating where your customers need you.</h2>')
h = ir(h,
    '<p class="lead">WTM has on-the-ground infrastructure',
    '<p class="lead" data-i18n="globe.lead">WTM has on-the-ground infrastructure')

# ═══════════════════════════════════════════════════════════════════════════════
# S11 — CTA
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<span class="trust-text">Trusted by <strong>4,000+</strong> companies worldwide</span>',
    '<span class="trust-text" data-i18n-html="cta.trust">Trusted by <strong>4,000+</strong> companies worldwide</span>')

h = ir(h,
    '<p class="versatylo">\n      understand your brazil exposure',
    '<p class="versatylo" data-i18n-html="cta.tagline">\n      understand your brazil exposure')

h = ir(h,
    '<p class="lead" style="margin:12px auto 0">\n      Chosen by over 4,000',
    '<p class="lead" data-i18n="cta.leadtext" style="margin:12px auto 0">\n      Chosen by over 4,000')

h = ir(h,
    '<span class="cta-stat-label">Companies expanded</span>',
    '<span class="cta-stat-label" data-i18n="cta.stat1">Companies expanded</span>')
h = ir(h,
    '<span class="cta-stat-label">Years of expertise</span>',
    '<span class="cta-stat-label" data-i18n="cta.stat2">Years of expertise</span>')
h = ir(h,
    '<span class="cta-stat-label">Prepare now</span>',
    '<span class="cta-stat-label" data-i18n="cta.stat3">Prepare now</span>')

h = ir(h,
    '<p style="font-family:var(--font-heading);font-weight:600;font-size:1.1rem;color:#fff;margin-bottom:28px;text-wrap:balance;max-width:46ch;margin-left:auto;margin-right:auto">\n      Brazil is professionalizing',
    '<p data-i18n="cta.body" style="font-family:var(--font-heading);font-weight:600;font-size:1.1rem;color:#fff;margin-bottom:28px;text-wrap:balance;max-width:46ch;margin-left:auto;margin-right:auto">\n      Brazil is professionalizing')

h = ir(h,
    '<a href="#" class="btn btn-light">Talk to a specialist <i data-lucide="arrow-right"></i></a>',
    '<a href="#" class="btn btn-light" data-i18n-html="cta.btn1">Talk to a specialist <i data-lucide="arrow-right"></i></a>')
h = ir(h,
    '<a href="https://linkedin.com" target="_blank" rel="noopener" class="btn btn-ghost-light">Contact on LinkedIn</a>',
    '<a href="https://linkedin.com" target="_blank" rel="noopener" class="btn btn-ghost-light" data-i18n="cta.btn2">Contact on LinkedIn</a>')

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<p class="versatylo">empowering expansion.</p>',
    '<p class="versatylo" data-i18n="footer.tagline">empowering expansion.</p>')
h = ir(h,
    '<a href="#">Privacy policy</a>',
    '<a href="#" data-i18n="footer.privacy">Privacy policy</a>')
h = ir(h,
    '<a href="#">Terms of use</a>',
    '<a href="#" data-i18n="footer.terms">Terms of use</a>')
h = ir(h,
    '<a href="#">Contact</a>',
    '<a href="#" data-i18n="footer.contact">Contact</a>')
h = ir(h,
    '<span>© 2025 WTM. All rights reserved.</span>',
    '<span data-i18n="footer.copy">© 2025 WTM. All rights reserved.</span>')
h = ir(h,
    '<span>Brazil · USA · Canada · México · Peru · Uruguay · Portugal · UAE</span>',
    '<span data-i18n="footer.places">Brazil · USA · Canada · México · Peru · Uruguay · Portugal · UAE</span>')
h = ir(h,
    '<span>Empowering global business expansion since 2003.</span>',
    '<span data-i18n="footer.since">Empowering global business expansion since 2003.</span>')

# ═══════════════════════════════════════════════════════════════════════════════
# TAX section — remaining items
# ═══════════════════════════════════════════════════════════════════════════════
h = ir(h,
    '<p class="lead">\n        When a Brazilian company buys SaaS',
    '<p class="lead" data-i18n="tax.lead">\n        When a Brazilian company buys SaaS')

h = ir(h,
    '<div class="vat-title">Indirect tax layer',
    '<div class="vat-title" data-i18n="tax.vat.title">Indirect tax layer')
h = ir(h,
    '<span>Current indirect layer (PIS + COFINS + ISS)</span>',
    '<span data-i18n="tax.vat.cur">Current indirect layer (PIS + COFINS + ISS)</span>')
h = ir(h,
    '<span>Expected dual VAT layer (CBS + IBS)</span>',
    '<span data-i18n="tax.vat.fut">Expected dual VAT layer (CBS + IBS)</span>')
h = ir(h,
    '<p class="vat-foot">\n            IRRF, IOF and CIDE remain',
    '<p class="vat-foot" data-i18n="tax.vat.foot">\n            IRRF, IOF and CIDE remain')
h = ir(h,
    '<div class="tax-block-title">From 2027 onward, expect</div>',
    '<div class="tax-block-title" data-i18n="tax.expect.title">From 2027 onward, expect</div>')

expect_items = [
    'Higher tax visibility and digital reporting',
    'Broader cross-checking of international payments',
    'Stronger buyer-side pressure for compliant invoices',
    'CFO, tax and procurement teams demanding local billing',
]
for i, item in enumerate(expect_items, 1):
    h = ir(h,
        f'<li><i data-lucide="arrow-right"></i> {item}</li>',
        f'<li><i data-lucide="arrow-right"></i> <span data-i18n="tax.e{i}">{item}</span></li>')

h = ir(h,
    '<p class="tax-foot">\n          Many buyers do not handle',
    '<p class="tax-foot" data-i18n="tax.foot">\n          Many buyers do not handle')

# tax rows
tax_rows = [
    ('IOF — Foreign exchange tax','Automatically charged by bank or card issuer','tax.iof'),
    ('IRRF — Withholding income tax','On most international outbound payments','tax.irrf'),
    ('CIDE — Contribution on technology','Royalties, technical services, software remittances — reinforced by the Netflix/CIDE precedent','tax.cide'),
    ('PIS-importation','Federal social contribution on imports','tax.pis'),
    ('COFINS-importation','Federal social contribution on imports','tax.cofins'),
    ('ISS-importation','Municipal service tax on imported services','tax.iss'),
    ('Reporting obligations','REINF, DCTFWeb / MIT, corporate tax reporting','tax.rep'),
]
for (name, note, pfx) in tax_rows:
    h = ir(h,
        f'<span class="tax-name">{name}</span>',
        f'<span class="tax-name" data-i18n="{pfx}.name">{name}</span>')
    h = ir(h,
        f'<span class="tax-note">{note}</span>',
        f'<span class="tax-note" data-i18n="{pfx}.note">{note}</span>')

print('All data-i18n attrs applied')

# ═══════════════════════════════════════════════════════════════════════════════
# Replace the full T object
# ═══════════════════════════════════════════════════════════════════════════════

NEW_T = r"""  const T = {
    en: {
      /* NAV */
      'nav.tax':'Tax reform','nav.solution':'Solution','nav.benefits':'Benefits',
      'nav.next-steps':'Next steps','nav.cta':'Talk to a specialist',
      /* HERO */
      'hero.eyebrow':'Brazil tax reform · SaaS, AI & cloud · 2025–2033',
      'hero.h1':'Your current go-to-market for Brazil may not survive the <span class="accent">new tax model.</span>',
      'hero.lead':'Brazil is moving from a market where cross-border SaaS non-compliance was often invisible, to a market where tax friction can directly affect sales, renewals, expansion and customer experience. The 2027 transition has already started.',
      'hero.tagline':'empowering expansion. <em>without the tax surprise.</em>',
      'hero.cta1':'Talk to a specialist <i data-lucide="arrow-right"></i>',
      'hero.cta2':'Understand your exposure',
      /* TAX */
      'tax.eyebrow':'The tax reality',
      'tax.h2':"Brazil’s tax layer is larger than your customers realize — and it’s about to grow.",
      'tax.lead':"When a Brazilian company buys SaaS from a foreign supplier, it typically sees only the subscription price, the exchange rate, and an IOF charge. The full picture is far more complex.",
      'tax.block-title':'Current obligations on your Brazilian customers',
      'tax.iof.name':'IOF — Foreign exchange tax','tax.iof.note':'Automatically charged by bank or card issuer',
      'tax.irrf.name':'IRRF — Withholding income tax','tax.irrf.note':'On most international outbound payments',
      'tax.cide.name':'CIDE — Contribution on technology','tax.cide.note':'Royalties, technical services, software remittances — reinforced by the Netflix/CIDE precedent',
      'tax.pis.name':'PIS-importation','tax.pis.note':'Federal social contribution on imports',
      'tax.cofins.name':'COFINS-importation','tax.cofins.note':'Federal social contribution on imports',
      'tax.iss.name':'ISS-importation','tax.iss.note':'Municipal service tax on imported services',
      'tax.rep.name':'Reporting obligations','tax.rep.note':'REINF, DCTFWeb / MIT, corporate tax reporting',
      'tax.foot':'Many buyers do not handle these obligations correctly, creating a market distortion: foreign SaaS looked cheaper than it really was because customers were not internalizing the full tax burden.',
      'tax.vat.title':'Indirect tax layer — current vs. future reform',
      'tax.vat.cur':'Current indirect layer (PIS + COFINS + ISS)',
      'tax.vat.fut':'Expected dual VAT layer (CBS + IBS)',
      'tax.vat.foot':'IRRF, IOF and CIDE remain relevant alongside the new VAT structure. Foreign sellers will need to support compliance directly or through reliable local partners. Under the new VAT environment, taxes become more visible, more enforceable, and more important for customers that want to generate credits.',
      'tax.expect.title':'From 2027 onward, expect',
      'tax.e1':'Higher tax visibility and digital reporting',
      'tax.e2':'Broader cross-checking of international payments',
      'tax.e3':'Stronger buyer-side pressure for compliant invoices',
      'tax.e4':'CFO, tax and procurement teams demanding local billing',
      /* COMMERCIAL */
      'commercial.eyebrow':'Commercial impact',
      'commercial.h2':'This is not a tax department problem. It is a revenue problem.',
      'commercial.lead':'A U.S. SaaS vendor may think: “this is a Brazilian tax issue. My customer must deal with it.” That may be true legally — but commercially, it is incomplete.',
      'commercial.kpi1':'When the Brazilian customer’s tax cost increases, your <strong>churn rate rises</strong> — customers cancel, downgrade or migrate to locally compliant vendors.',
      'commercial.kpi2':'<strong>CAC increases</strong> as sales teams spend more time overcoming procurement and tax objections before closing.',
      'commercial.kpi3':'<strong>Expansion revenue slows</strong> — customers avoid adding seats, tokens or usage when total tax cost becomes unpredictable.',
      'commercial.kpi4':'<strong>Enterprise deals stall</strong> — larger customers require local invoices and tax-compliant documentation before signing.',
      'commercial.kpi5':'Local billing with WTM <strong>turns compliance into a growth lever</strong> — a structured, local buying experience that improves NRR and conversion.',
      'cc1.title':'Churn risk','cc1.body':'Customers may cancel, downgrade or migrate to locally compliant alternatives as tax costs become visible.',
      'cc2.title':'CAC pressure','cc2.body':'Longer sales cycles driven by procurement and tax objections translate directly into higher acquisition costs.',
      'cc3.title':'RFP disqualification','cc3.body':'Without local invoicing capability, you may be eliminated from enterprise procurement processes before negotiations begin.',
      'cc4.title':'Provider liability','cc4.body':'As the Netflix/CIDE precedent shows, tax issues in Brazil can escalate to earnings-level events and board-level risk.',
      /* CASES */
      'case.eyebrow':'Real precedents',
      'case.h2':"The companies that ignored Brazil’s tax exposure learned it on their earnings call.",
      'case1.meta':'Earnings impact · Global investor event',
      'case1.stat1label':'Tax-related expense connected to a dispute with Brazilian tax authorities, contributing to a major stock market reaction.',
      'case1.stat2':'~10% drop',
      'case1.stat2label':'Share price decline in a single trading session, representing approximately USD 33 billion in market value impact.',
      'case1.l1':'Brazil tax issues can become earnings issues.',
      'case1.l2':'Brazil tax issues can become investor-relations issues.',
      'case1.l3':'Board-level visibility increases once the exposure becomes material.',
      'case2.meta':'Substance over form',
      'case2.quote':'Brazilian authorities may look beyond labels such as <em>“payment facilitator”</em> or <em>“marketplace”</em> and analyze the economic substance of the flow.',
      'case2.quotesub':'The questions regulators ask: who charges the customer? Who is effectively responsible for the Brazilian tax treatment? Can the current structure withstand local scrutiny?',
      'case2.diveyebrow':'The lesson for every U.S. SaaS company',
      'case2.divbody':'Brazilian tax issues are no longer just local compliance problems. They can become earnings problems, investor-relations problems and board-level risk events — especially when Brazilian revenue grows but the vendor remains non-localized for billing and tax purposes.',
      /* QUOTE */
      'quote.line1':'you do not just need tax support.','quote.line2':'you need the transaction to work.',
      /* SOLUTION */
      'solution.eyebrow':'WTM Merchant of Record',
      'solution.h2':'A Merchant of Record built for both sides of the transaction.',
      'solution.lead':"WTM operates as your local Merchant of Record in Brazil, removing tax, payment and compliance complexity from your operation and from your customer’s buying process. The solution is not simply to pay more tax — it is to design a compliant buying experience.",
      'solution.tagline':'<i data-lucide="sparkles"></i> Most MoRs solve your problem. WTM solves the transaction.',
      'mor.buyer.label':'01. Buyer','mor.buyer.title':'Brazilian customer',
      'mor.buyer.list':'<li>Buys locally, in BRL</li><li>Receives a compliant Nota Fiscal</li><li>Generates CBS/IBS tax credits</li><li>Predictable total cost</li><li>No internal tax friction</li>',
      'mor.wtm.label':'02. Merchant of Record','mor.wtm.badge':'Active in Brazil',
      'mor.wtm.list':'<li>Local billing &amp; Nota Fiscal (NF-e)</li><li>Payment processing in BRL</li><li>Tax collection &amp; remittance</li><li>Full CBS/IBS compliance</li><li>REINF, DCTFWeb reporting</li><li>Reconciliation &amp; reporting</li>',
      'mor.seller.label':'03. Seller (you)','mor.seller.title':'Your business',
      'mor.seller.list':'<li>Receives clean payment</li><li>Zero Brazilian tax liability</li><li>No local entity required</li><li>Lower churn from Brazil</li><li>Scales across LATAM</li>',
      /* COMPARE */
      'compare.eyebrow':'Comparison','compare.h2':'Direct selling vs. selling through WTM.',
      'compare.h-without':'Without WTM','compare.h-with':'With WTM',
      'compare.r1.topic':'Tax handling','compare.r1.without':'<i data-lucide="x"></i>Buyer handles taxes manually, often incorrectly','compare.r1.with':'<i data-lucide="check"></i>WTM handles all collection and remittance',
      'compare.r2.topic':'Local invoice','compare.r2.without':'<i data-lucide="x"></i>No Nota Fiscal — procurement friction','compare.r2.with':'<i data-lucide="check"></i>Compliant NF-e issued for every transaction',
      'compare.r3.topic':'Tax credits (CBS/IBS)','compare.r3.without':'<i data-lucide="x"></i>No local credits generated for buyer','compare.r3.with':'<i data-lucide="check"></i>Buyer generates full CBS/IBS credits',
      'compare.r4.topic':'Provider liability','compare.r4.without':'<i data-lucide="x"></i>You may carry retroactive liability','compare.r4.with':'<i data-lucide="check"></i>Exposure dramatically reduced via WTM structure',
      'compare.r5.topic':'Churn risk','compare.r5.without':'<i data-lucide="x"></i>Tax cost increase → cancellations and downgrades','compare.r5.with':'<i data-lucide="check"></i>Compliant path removes churn driver',
      'compare.r6.topic':'Enterprise deals','compare.r6.without':'<i data-lucide="x"></i>RFP disqualification without local billing','compare.r6.with':'<i data-lucide="check"></i>Full documentation for finance, tax and procurement',
      'compare.r7.topic':'Sales cycle','compare.r7.without':'<i data-lucide="x"></i>Longer cycles; higher CAC from tax objections','compare.r7.with':'<i data-lucide="check"></i>Smoother buying experience; lower friction at close',
      /* BENEFITS */
      'benefits.eyebrow':'Why WTM','benefits.h2':'Key benefits.',
      'b1.title':'Protect margins','b1.body':'Reduce exposure to unexpected tax costs and pricing distortion. Correct tax embedding prevents the hidden margin erosion that surprises at renewal time.',
      'b2.title':'Increase win rate','b2.body':'Offer a local, compliant buying experience that eliminates RFP disqualification and removes procurement objections before they stall the deal.',
      'b3.title':'Reduce churn & CAC','b3.body':'A structured local buying path removes the primary driver of tax-related churn and shortens sales cycles — directly improving NRR and lowering acquisition costs.',
      'b4.title':'Scale safely to 2033','b4.body':"Use WTM’s local infrastructure to navigate the full transition period through 2033 and expand across the broader LATAM market with confidence.",
      /* ACTIONS */
      'action.eyebrow':'Strategic roadmap',
      'action.h2':'Act before the reform becomes fully operational.',
      'action.lead':'The first step is not to open an entity in Brazil or choose an unverified reseller. The first step is to map your current exposure and model how costs change from now through 2033.',
      'a1.step':'Step 01','a1.title':'Map your Brazil footprint','a1.body':'Identify all Brazilian customers, revenue streams and current payment methods to understand the full scope of your exposure.',
      'a2.step':'Step 02','a2.title':'Estimate customer tax exposure','a2.body':'Assess how much tax each customer currently carries — and model how that burden changes through the transition to 2033.',
      'a3.step':'Step 03','a3.title':'Identify accounts at risk','a3.body':'Flag customers most likely to churn, downgrade or delay renewal as tax costs increase and compliance scrutiny rises.',
      'a4.step':'Step 04','a4.title':'Review contract language','a4.body':'Assess whether your current agreements adequately address tax responsibility, liability allocation and compliance obligations.',
      'a5.step':'Step 05','a5.title':'Prepare local billing with WTM','a5.body':'Design a compliant local buying path — local invoice, payment in BRL, full CBS/IBS support — ready before customers ask.',
      'a6.step':'Step 06','a6.title':'Train your go-to-market teams','a6.body':'Align sales, finance, legal and customer success teams on how to position Brazil compliance as a competitive advantage, not a cost.',
      /* GLOBE */
      'globe.eyebrow':'Global presence',
      'globe.h2':'Operating where your customers need you.',
      'globe.lead':'WTM has on-the-ground infrastructure across the Americas, Europe and the Middle East — ensuring your Brazilian expansion is backed by a network that understands every market.',
      /* CTA */
      'cta.trust':'Trusted by <strong>4,000+</strong> companies worldwide',
      'cta.tagline':'understand your brazil exposure<br><span class="accent">before it becomes a sales problem.</span>',
      'cta.leadtext':'Chosen by over 4,000 companies that have expanded into new markets in a reliable and simplified way, with full compliance across their operations.',
      'cta.stat1':'Companies expanded','cta.stat2':'Years of expertise','cta.stat3':'Prepare now',
      'cta.body':'Brazil is professionalizing how foreign digital services are bought, taxed, documented and reported. The winners will be the companies that treat compliance as a competitive advantage.',
      'cta.btn1':'Talk to a specialist <i data-lucide="arrow-right"></i>','cta.btn2':'Contact on LinkedIn',
      /* FOOTER */
      'footer.tagline':'empowering expansion.','footer.privacy':'Privacy policy','footer.terms':'Terms of use','footer.contact':'Contact',
      'footer.copy':'© 2025 WTM. All rights reserved.',
      'footer.places':'Brazil · USA · Canada · México · Peru · Uruguay · Portugal · UAE',
      'footer.since':'Empowering global business expansion since 2003.',
    },

    pt: {
      /* NAV */
      'nav.tax':'Reforma tributária','nav.solution':'Solução','nav.benefits':'Benefícios',
      'nav.next-steps':'Próximos passos','nav.cta':'Falar com especialista',
      /* HERO */
      'hero.eyebrow':'Reforma tributária do Brasil · SaaS, IA & cloud · 2025–2033',
      'hero.h1':'Seu modelo de go-to-market para o Brasil pode não sobreviver ao <span class="accent">novo modelo fiscal.</span>',
      'hero.lead':'O Brasil está migrando de um mercado em que a não conformidade tributária de SaaS cross-border era frequentemente invisível, para um mercado em que a fricção fiscal pode afetar diretamente vendas, renovações, expansão e a experiência do cliente. A transição de 2027 já começou.',
      'hero.tagline':'expansão com poder. <em>sem a surpresa fiscal.</em>',
      'hero.cta1':'Falar com especialista <i data-lucide="arrow-right"></i>',
      'hero.cta2':'Entenda sua exposição',
      /* TAX */
      'tax.eyebrow':'A realidade tributária',
      'tax.h2':'A camada tributária do Brasil é maior do que seus clientes percebem — e está prestes a crescer.',
      'tax.lead':'Quando uma empresa brasileira compra SaaS de um fornecedor estrangeiro, normalmente vê apenas o preço da assinatura, a taxa de câmbio e a cobrança de IOF. O quadro completo é muito mais complexo.',
      'tax.block-title':'Obrigações atuais sobre seus clientes brasileiros',
      'tax.iof.name':'IOF — Imposto sobre Operações Financeiras','tax.iof.note':'Cobrado automaticamente pelo banco ou emissor do cartão',
      'tax.irrf.name':'IRRF — Imposto de Renda Retido na Fonte','tax.irrf.note':'Sobre a maioria dos pagamentos internacionais',
      'tax.cide.name':'CIDE — Contribuição sobre Tecnologia','tax.cide.note':'Royalties, serviços técnicos, remessas de software — reforçado pelo precedente Netflix/CIDE',
      'tax.pis.name':'PIS-importação','tax.pis.note':'Contribuição social federal sobre importações',
      'tax.cofins.name':'COFINS-importação','tax.cofins.note':'Contribuição social federal sobre importações',
      'tax.iss.name':'ISS-importação','tax.iss.note':'Imposto municipal sobre serviços importados',
      'tax.rep.name':'Obrigações acessórias','tax.rep.note':'REINF, DCTFWeb / MIT, declarações de imposto corporativo',
      'tax.foot':'Muitos compradores não cumprem essas obrigações corretamente, criando uma distorção de mercado: o SaaS estrangeiro parecia mais barato do que realmente era porque os clientes não internalizavam a carga tributária total.',
      'tax.vat.title':'Camada de imposto indireto — atual vs. reforma futura',
      'tax.vat.cur':'Camada indireta atual (PIS + COFINS + ISS)',
      'tax.vat.fut':'Camada VAT duplo esperada (CBS + IBS)',
      'tax.vat.foot':'IRRF, IOF e CIDE permanecem relevantes ao lado da nova estrutura de IVA. Vendedores estrangeiros precisarão suportar a conformidade diretamente ou por meio de parceiros locais confiáveis. No novo ambiente de IVA, os impostos tornam-se mais visíveis, mais aplicáveis e mais importantes para clientes que desejam gerar créditos.',
      'tax.expect.title':'A partir de 2027, espere',
      'tax.e1':'Maior visibilidade fiscal e reporte digital',
      'tax.e2':'Maior cruzamento de informações de pagamentos internacionais',
      'tax.e3':'Maior pressão dos compradores por notas fiscais conformes',
      'tax.e4':'Equipes de CFO, tributação e compras exigindo faturamento local',
      /* COMMERCIAL */
      'commercial.eyebrow':'Impacto comercial',
      'commercial.h2':'Isso não é um problema do departamento fiscal. É um problema de receita.',
      'commercial.lead':'Um fornecedor de SaaS americano pode pensar: “este é um problema tributário brasileiro. Meu cliente deve lidar com isso.” Isso pode ser verdade legalmente — mas comercialmente, está incompleto.',
      'commercial.kpi1':'Quando o custo tributário do cliente brasileiro aumenta, sua <strong>taxa de churn cresce</strong> — clientes cancelam, fazem downgrade ou migram para fornecedores localmente conformes.',
      'commercial.kpi2':'<strong>O CAC aumenta</strong> à medida que as equipes de vendas gastam mais tempo superando objeções de compras e tributárias antes de fechar.',
      'commercial.kpi3':'<strong>A receita de expansão desacelera</strong> — clientes evitam adicionar licenças, tokens ou uso quando o custo tributário total se torna imprevisível.',
      'commercial.kpi4':'<strong>Negócios enterprise ficam parados</strong> — clientes maiores exigem notas fiscais locais e documentação tributária conforme antes de assinar.',
      'commercial.kpi5':'Faturamento local com a WTM <strong>transforma a conformidade em alavanca de crescimento</strong> — uma experiência de compra estruturada e local que melhora o NRR e a conversão.',
      'cc1.title':'Risco de churn','cc1.body':'Clientes podem cancelar, fazer downgrade ou migrar para alternativas localmente conformes à medida que os custos tributários se tornam visíveis.',
      'cc2.title':'Pressão no CAC','cc2.body':'Ciclos de vendas mais longos impulsionados por objeções de compras e tributárias se traduzem diretamente em maiores custos de aquisição.',
      'cc3.title':'Desqualificação em RFPs','cc3.body':'Sem capacidade de faturamento local, você pode ser eliminado de processos de compras enterprise antes mesmo de começar as negociações.',
      'cc4.title':'Responsabilidade do fornecedor','cc4.body':'Como mostra o precedente Netflix/CIDE, questões tributárias no Brasil podem escalar para eventos de nível de lucros e risco no conselho.',
      /* CASES */
      'case.eyebrow':'Precedentes reais',
      'case.h2':'As empresas que ignoraram a exposição tributária do Brasil souberam disso em sua call de resultados.',
      'case1.meta':'Impacto nos resultados · Evento para investidores globais',
      'case1.stat1label':'Despesa relacionada a tributos conectada a uma disputa com as autoridades fiscais brasileiras, contribuindo para uma grande reação no mercado de ações.',
      'case1.stat2':'~10% de queda',
      'case1.stat2label':'Queda no preço das ações em uma única sessão de negociação, representando aproximadamente USD 33 bilhões de impacto no valor de mercado.',
      'case1.l1':'Questões tributárias no Brasil podem se tornar questões de resultados.',
      'case1.l2':'Questões tributárias no Brasil podem se tornar questões de relações com investidores.',
      'case1.l3':'A visibilidade no nível do conselho aumenta quando a exposição se torna material.',
      'case2.meta':'Substância sobre a forma',
      'case2.quote':'As autoridades brasileiras podem ir além de rótulos como <em>“facilitador de pagamentos”</em> ou <em>“marketplace”</em> e analisar a substância econômica do fluxo.',
      'case2.quotesub':'As perguntas que os reguladores fazem: quem cobra do cliente? Quem é efetivamente responsável pelo tratamento tributário brasileiro? A estrutura atual pode resistir ao escruínio local?',
      'case2.diveyebrow':'A lição para toda empresa de SaaS americana',
      'case2.divbody':'Questões tributárias no Brasil não são mais apenas problemas de conformidade local. Podem se tornar problemas de resultados, problemas de relações com investidores e eventos de risco no nível do conselho — especialmente quando a receita brasileira cresce, mas o fornecedor permanece sem localização para fins de faturamento e tributação.',
      /* QUOTE */
      'quote.line1':'você não precisa apenas de suporte tributário.','quote.line2':'você precisa que a transação funcione.',
      /* SOLUTION */
      'solution.eyebrow':'WTM Merchant of Record',
      'solution.h2':'Um Merchant of Record construído para os dois lados da transação.',
      'solution.lead':'A WTM opera como seu Merchant of Record local no Brasil, removendo a complexidade tributária, de pagamentos e de conformidade da sua operação e do processo de compra do seu cliente. A solução não é simplesmente pagar mais imposto — é projetar uma experiência de compra conforme.',
      'solution.tagline':'<i data-lucide="sparkles"></i> A maioria dos MoRs resolve o seu problema. A WTM resolve a transação.',
      'mor.buyer.label':'01. Comprador','mor.buyer.title':'Cliente brasileiro',
      'mor.buyer.list':'<li>Compra localmente, em BRL</li><li>Recebe uma Nota Fiscal conforme</li><li>Gera créditos tributários CBS/IBS</li><li>Custo total previsível</li><li>Sem fricção tributária interna</li>',
      'mor.wtm.label':'02. Merchant of Record','mor.wtm.badge':'Ativo no Brasil',
      'mor.wtm.list':'<li>Faturamento local &amp; Nota Fiscal (NF-e)</li><li>Processamento de pagamentos em BRL</li><li>Coleta e remessa de tributos</li><li>Conformidade total CBS/IBS</li><li>Reporte REINF, DCTFWeb</li><li>Conciliação &amp; relatórios</li>',
      'mor.seller.label':'03. Vendedor (você)','mor.seller.title':'Seu negócio',
      'mor.seller.list':'<li>Recebe pagamento limpo</li><li>Zero responsabilidade tributária brasileira</li><li>Sem necessidade de entidade local</li><li>Menor churn do Brasil</li><li>Escala por toda a LATAM</li>',
      /* COMPARE */
      'compare.eyebrow':'Comparação','compare.h2':'Venda direta vs. venda pela WTM.',
      'compare.h-without':'Sem a WTM','compare.h-with':'Com a WTM',
      'compare.r1.topic':'Gestão tributária','compare.r1.without':'<i data-lucide="x"></i>Comprador gerencia tributos manualmente, frequentemente de forma incorreta','compare.r1.with':'<i data-lucide="check"></i>WTM gerencia toda a coleta e remessa',
      'compare.r2.topic':'Nota Fiscal','compare.r2.without':'<i data-lucide="x"></i>Sem Nota Fiscal — fricção em compras','compare.r2.with':'<i data-lucide="check"></i>NF-e conforme emitida para cada transação',
      'compare.r3.topic':'Créditos tributários (CBS/IBS)','compare.r3.without':'<i data-lucide="x"></i>Nenhum crédito local gerado para o comprador','compare.r3.with':'<i data-lucide="check"></i>Comprador gera créditos CBS/IBS completos',
      'compare.r4.topic':'Responsabilidade do fornecedor','compare.r4.without':'<i data-lucide="x"></i>Você pode carregar responsabilidade retroativa','compare.r4.with':'<i data-lucide="check"></i>Exposição drasticamente reduzida pela estrutura WTM',
      'compare.r5.topic':'Risco de churn','compare.r5.without':'<i data-lucide="x"></i>Aumento do custo tributário → cancelamentos e downgrades','compare.r5.with':'<i data-lucide="check"></i>Caminho conforme elimina o driver de churn',
      'compare.r6.topic':'Negócios enterprise','compare.r6.without':'<i data-lucide="x"></i>Desqualificação em RFPs sem faturamento local','compare.r6.with':'<i data-lucide="check"></i>Documentação completa para finanças, tributação e compras',
      'compare.r7.topic':'Ciclo de vendas','compare.r7.without':'<i data-lucide="x"></i>Ciclos mais longos; CAC mais alto por objeções tributárias','compare.r7.with':'<i data-lucide="check"></i>Experiência de compra mais fluída; menor fricção no fechamento',
      /* BENEFITS */
      'benefits.eyebrow':'Por que a WTM','benefits.h2':'Principais benefícios.',
      'b1.title':'Proteja margens','b1.body':'Reduza a exposição a custos tributários inesperados e distorção de preços. A incorporação correta de impostos evita a erosão oculta de margem que surpreende no momento da renovação.',
      'b2.title':'Aumente a taxa de conversão','b2.body':'Ofereça uma experiência de compra local e conforme que elimina a desqualificação em RFPs e remove objeções de compras antes que elas travem o negócio.',
      'b3.title':'Reduza churn & CAC','b3.body':'Um caminho de compra local estruturado remove o principal driver de churn relacionado a tributos e encurta os ciclos de vendas — melhorando diretamente o NRR e reduzindo os custos de aquisição.',
      'b4.title':'Escale com segurança até 2033','b4.body':'Use a infraestrutura local da WTM para navegar pelo período de transição completo até 2033 e expandir por todo o mercado LATAM com confiança.',
      /* ACTIONS */
      'action.eyebrow':'Roteiro estratégico',
      'action.h2':'Aja antes que a reforma esteja totalmente operacional.',
      'action.lead':'O primeiro passo não é abrir uma entidade no Brasil ou escolher um revendedor não verificado. O primeiro passo é mapear sua exposição atual e modelar como os custos mudam agora até 2033.',
      'a1.step':'Passo 01','a1.title':'Mapeie sua presença no Brasil','a1.body':'Identifique todos os clientes brasileiros, fluxos de receita e métodos de pagamento atuais para entender o escopo completo da sua exposição.',
      'a2.step':'Passo 02','a2.title':'Estime a exposição tributária dos clientes','a2.body':'Avalie quanto de imposto cada cliente carrega atualmente — e modele como esse ônus muda durante a transição até 2033.',
      'a3.step':'Passo 03','a3.title':'Identifique contas em risco','a3.body':'Sinalize os clientes mais propensos a cancelar, fazer downgrade ou atrasar a renovação à medida que os custos tributários aumentam e o escruínio de conformidade cresce.',
      'a4.step':'Passo 04','a4.title':'Revise a linguagem contratual','a4.body':'Avalie se seus acordos atuais abordam adequadamente a responsabilidade tributária, a alocação de passivos e as obrigações de conformidade.',
      'a5.step':'Passo 05','a5.title':'Prepare o faturamento local com a WTM','a5.body':'Projete um caminho de compra local conforme — nota fiscal local, pagamento em BRL, suporte completo CBS/IBS — pronto antes que os clientes peçam.',
      'a6.step':'Passo 06','a6.title':'Treine suas equipes de go-to-market','a6.body':'Alinhe as equipes de vendas, finanças, jurídico e sucesso do cliente sobre como posicionar a conformidade no Brasil como uma vantagem competitiva, não um custo.',
      /* GLOBE */
      'globe.eyebrow':'Presença global',
      'globe.h2':'Operando onde seus clientes precisam de você.',
      'globe.lead':'A WTM tem infraestrutura local nas Américas, Europa e Oriente Médio — garantindo que sua expansão no Brasil seja apoiada por uma rede que entende cada mercado.',
      /* CTA */
      'cta.trust':'Confiada por <strong>4.000+</strong> empresas em todo o mundo',
      'cta.tagline':'entenda sua exposição no brasil<br><span class="accent">antes que se torne um problema de vendas.</span>',
      'cta.leadtext':'Escolhida por mais de 4.000 empresas que se expandiram para novos mercados de forma confiável e simplificada, com total conformidade em suas operações.',
      'cta.stat1':'Empresas expandidas','cta.stat2':'Anos de expertise','cta.stat3':'Prepare-se agora',
      'cta.body':'O Brasil está profissionalizando como os serviços digitais estrangeiros são comprados, tributados, documentados e reportados. Os vencedores serão as empresas que tratarem a conformidade como uma vantagem competitiva.',
      'cta.btn1':'Falar com especialista <i data-lucide="arrow-right"></i>','cta.btn2':'Contato no LinkedIn',
      /* FOOTER */
      'footer.tagline':'expansão com poder.','footer.privacy':'Política de privacidade','footer.terms':'Termos de uso','footer.contact':'Contato',
      'footer.copy':'© 2025 WTM. Todos os direitos reservados.',
      'footer.places':'Brasil · EUA · Canadá · México · Peru · Uruguai · Portugal · EAU',
      'footer.since':'Impulsionando a expansão global de negócios desde 2003.',
    },

    es: {
      /* NAV */
      'nav.tax':'Reforma tributaria','nav.solution':'Solución','nav.benefits':'Beneficios',
      'nav.next-steps':'Próximos pasos','nav.cta':'Hablar con especialista',
      /* HERO */
      'hero.eyebrow':'Reforma tributaria de Brasil · SaaS, IA & cloud · 2025–2033',
      'hero.h1':'Su modelo de go-to-market para Brasil puede no sobrevivir al <span class="accent">nuevo modelo fiscal.</span>',
      'hero.lead':'Brasil está pasando de un mercado donde el incumplimiento tributario de SaaS cross-border era frecuentemente invisible, a un mercado donde la fricción fiscal puede afectar directamente las ventas, renovaciones, expansión y la experiencia del cliente. La transición de 2027 ya comenzó.',
      'hero.tagline':'expansión con poder. <em>sin la sorpresa fiscal.</em>',
      'hero.cta1':'Hablar con especialista <i data-lucide="arrow-right"></i>',
      'hero.cta2':'Entienda su exposición',
      /* TAX */
      'tax.eyebrow':'La realidad tributaria',
      'tax.h2':'La capa tributaria de Brasil es mayor de lo que sus clientes perciben — y está a punto de crecer.',
      'tax.lead':'Cuando una empresa brasileña compra SaaS de un proveedor extranjero, normalmente solo ve el precio de la suscripción, el tipo de cambio y un cargo de IOF. El cuadro completo es mucho más complejo.',
      'tax.block-title':'Obligaciones actuales sobre sus clientes brasileños',
      'tax.iof.name':'IOF — Impuesto sobre Operaciones Financieras','tax.iof.note':'Cobrado automáticamente por el banco o emisor de la tarjeta',
      'tax.irrf.name':'IRRF — Impuesto sobre la Renta Retenido en la Fuente','tax.irrf.note':'Sobre la mayoría de los pagos internacionales',
      'tax.cide.name':'CIDE — Contribución sobre Tecnología','tax.cide.note':'Regalías, servicios técnicos, remesas de software — reforzado por el precedente Netflix/CIDE',
      'tax.pis.name':'PIS-importación','tax.pis.note':'Contribución social federal sobre importaciones',
      'tax.cofins.name':'COFINS-importación','tax.cofins.note':'Contribución social federal sobre importaciones',
      'tax.iss.name':'ISS-importación','tax.iss.note':'Impuesto municipal sobre servicios importados',
      'tax.rep.name':'Obligaciones de reporte','tax.rep.note':'REINF, DCTFWeb / MIT, declaraciones de impuesto corporativo',
      'tax.foot':'Muchos compradores no gestionan estas obligaciones correctamente, creando una distorsión de mercado: el SaaS extranjero parecía más barato de lo que realmente era porque los clientes no internalizaban la carga tributaria total.',
      'tax.vat.title':'Capa de impuesto indirecto — actual vs. reforma futura',
      'tax.vat.cur':'Capa indirecta actual (PIS + COFINS + ISS)',
      'tax.vat.fut':'Capa IVA dual esperada (CBS + IBS)',
      'tax.vat.foot':'El IRRF, el IOF y la CIDE siguen siendo relevantes junto con la nueva estructura de IVA. Los vendedores extranjeros necesitarán apoyar el cumplimiento directamente o a través de socios locales confiables. En el nuevo entorno de IVA, los impuestos se vuelven más visibles, más aplicables y más importantes para los clientes que desean generar créditos.',
      'tax.expect.title':'A partir de 2027, espere',
      'tax.e1':'Mayor visibilidad fiscal y reporte digital',
      'tax.e2':'Mayor cruce de información de pagos internacionales',
      'tax.e3':'Mayor presión de los compradores por facturas conformes',
      'tax.e4':'Equipos de CFO, tributación y compras exigiendo facturación local',
      /* COMMERCIAL */
      'commercial.eyebrow':'Impacto comercial',
      'commercial.h2':'Esto no es un problema del departamento fiscal. Es un problema de ingresos.',
      'commercial.lead':'Un proveedor de SaaS de EE.UU. puede pensar: “este es un problema tributario brasileño. Mi cliente debe manejarlo.” Eso puede ser cierto legalmente — pero comercialmente, está incompleto.',
      'commercial.kpi1':'Cuando el costo tributario del cliente brasileño aumenta, su <strong>tasa de churn crece</strong> — los clientes cancelan, hacen downgrade o migran a proveedores localmente conformes.',
      'commercial.kpi2':'<strong>El CAC aumenta</strong> a medida que los equipos de ventas pasan más tiempo superando objeciones de compras y tributarias antes de cerrar.',
      'commercial.kpi3':'<strong>Los ingresos de expansión se desaceleran</strong> — los clientes evitan agregar licencias, tokens o uso cuando el costo tributario total se vuelve impredecible.',
      'commercial.kpi4':'<strong>Los acuerdos enterprise se paralizan</strong> — los clientes más grandes requieren facturas locales y documentación tributaria conforme antes de firmar.',
      'commercial.kpi5':'La facturación local con WTM <strong>convierte el cumplimiento en palanca de crecimiento</strong> — una experiencia de compra estructurada y local que mejora el NRR y la conversión.',
      'cc1.title':'Riesgo de churn','cc1.body':'Los clientes pueden cancelar, hacer downgrade o migrar a alternativas localmente conformes a medida que los costos tributarios se vuelven visibles.',
      'cc2.title':'Presión en CAC','cc2.body':'Los ciclos de ventas más largos impulsados por objeciones de compras y tributarias se traducen directamente en mayores costos de adquisición.',
      'cc3.title':'Descalificación en RFPs','cc3.body':'Sin capacidad de facturación local, puede ser eliminado de los procesos de compras enterprise antes de que comiencen las negociaciones.',
      'cc4.title':'Responsabilidad del proveedor','cc4.body':'Como muestra el precedente Netflix/CIDE, los problemas tributarios en Brasil pueden escalar a eventos de nivel de ganancias y riesgo a nivel de directorio.',
      /* CASES */
      'case.eyebrow':'Precedentes reales',
      'case.h2':'Las empresas que ignoraron la exposición tributaria de Brasil lo descubrieron en su llamada de resultados.',
      'case1.meta':'Impacto en resultados · Evento para inversores globales',
      'case1.stat1label':'Gasto relacionado con impuestos conectado a una disputa con las autoridades fiscales brasileñas, contribuyendo a una gran reacción en el mercado de valores.',
      'case1.stat2':'~10% de caída',
      'case1.stat2label':'Caída en el precio de las acciones en una sola sesión de negociación, representando aproximadamente USD 33 mil millones de impacto en el valor de mercado.',
      'case1.l1':'Los problemas tributarios en Brasil pueden convertirse en problemas de resultados.',
      'case1.l2':'Los problemas tributarios en Brasil pueden convertirse en problemas de relaciones con inversores.',
      'case1.l3':'La visibilidad a nivel de directorio aumenta cuando la exposición se vuelve material.',
      'case2.meta':'Sustancia sobre la forma',
      'case2.quote':'Las autoridades brasileñas pueden ir más allá de etiquetas como <em>“facilitador de pagos”</em> o <em>“marketplace”</em> y analizar la sustancia económica del flujo.',
      'case2.quotesub':'Las preguntas que hacen los reguladores: ¿quién cobra al cliente? ¿Quién es efectivamente responsable del tratamiento tributario brasileño? ¿Puede la estructura actual resistir el escrutinio local?',
      'case2.diveyebrow':'La lección para toda empresa de SaaS de EE.UU.',
      'case2.divbody':'Los problemas tributarios en Brasil ya no son solo problemas de cumplimiento local. Pueden convertirse en problemas de resultados, problemas de relaciones con inversores y eventos de riesgo a nivel de directorio — especialmente cuando los ingresos brasileños crecen pero el proveedor permanece sin localización para facturación y fines tributarios.',
      /* QUOTE */
      'quote.line1':'no solo necesita soporte tributario.','quote.line2':'necesita que la transacción funcione.',
      /* SOLUTION */
      'solution.eyebrow':'WTM Merchant of Record',
      'solution.h2':'Un Merchant of Record construido para ambos lados de la transacción.',
      'solution.lead':'WTM opera como su Merchant of Record local en Brasil, eliminando la complejidad tributaria, de pagos y de cumplimiento de su operación y del proceso de compra de su cliente. La solución no es simplemente pagar más impuestos — es diseñar una experiencia de compra conforme.',
      'solution.tagline':'<i data-lucide="sparkles"></i> La mayoría de los MoRs resuelven su problema. WTM resuelve la transacción.',
      'mor.buyer.label':'01. Comprador','mor.buyer.title':'Cliente brasileño',
      'mor.buyer.list':'<li>Compra localmente, en BRL</li><li>Recibe una Nota Fiscal conforme</li><li>Genera créditos tributarios CBS/IBS</li><li>Costo total predecible</li><li>Sin fricción tributaria interna</li>',
      'mor.wtm.label':'02. Merchant of Record','mor.wtm.badge':'Activo en Brasil',
      'mor.wtm.list':'<li>Facturación local &amp; Nota Fiscal (NF-e)</li><li>Procesamiento de pagos en BRL</li><li>Recaudación y remesa de impuestos</li><li>Cumplimiento total CBS/IBS</li><li>Reporte REINF, DCTFWeb</li><li>Conciliación &amp; reportes</li>',
      'mor.seller.label':'03. Vendedor (usted)','mor.seller.title':'Su negocio',
      'mor.seller.list':'<li>Recibe pago limpio</li><li>Cero responsabilidad tributaria brasileña</li><li>Sin necesidad de entidad local</li><li>Menor churn de Brasil</li><li>Escala por toda LATAM</li>',
      /* COMPARE */
      'compare.eyebrow':'Comparación','compare.h2':'Venta directa vs. venta a través de WTM.',
      'compare.h-without':'Sin WTM','compare.h-with':'Con WTM',
      'compare.r1.topic':'Gestión tributaria','compare.r1.without':'<i data-lucide="x"></i>El comprador gestiona impuestos manualmente, frecuentemente de forma incorrecta','compare.r1.with':'<i data-lucide="check"></i>WTM gestiona toda la recaudación y remesa',
      'compare.r2.topic':'Nota Fiscal','compare.r2.without':'<i data-lucide="x"></i>Sin Nota Fiscal — fricción en compras','compare.r2.with':'<i data-lucide="check"></i>NF-e conforme emitida para cada transacción',
      'compare.r3.topic':'Créditos tributarios (CBS/IBS)','compare.r3.without':'<i data-lucide="x"></i>Ningún crédito local generado para el comprador','compare.r3.with':'<i data-lucide="check"></i>El comprador genera créditos CBS/IBS completos',
      'compare.r4.topic':'Responsabilidad del proveedor','compare.r4.without':'<i data-lucide="x"></i>Puede acarrear responsabilidad retroactiva','compare.r4.with':'<i data-lucide="check"></i>Exposición dramáticamente reducida por la estructura WTM',
      'compare.r5.topic':'Riesgo de churn','compare.r5.without':'<i data-lucide="x"></i>Aumento del costo tributario → cancelaciones y downgrades','compare.r5.with':'<i data-lucide="check"></i>El camino conforme elimina el driver de churn',
      'compare.r6.topic':'Acuerdos enterprise','compare.r6.without':'<i data-lucide="x"></i>Descalificación en RFPs sin facturación local','compare.r6.with':'<i data-lucide="check"></i>Documentación completa para finanzas, tributación y compras',
      'compare.r7.topic':'Ciclo de ventas','compare.r7.without':'<i data-lucide="x"></i>Ciclos más largos; mayor CAC por objeciones tributarias','compare.r7.with':'<i data-lucide="check"></i>Experiencia de compra más fluida; menor fricción al cierre',
      /* BENEFITS */
      'benefits.eyebrow':'Por qué WTM','benefits.h2':'Beneficios clave.',
      'b1.title':'Proteja márgenes','b1.body':'Reduzca la exposición a costos tributarios inesperados y distorsión de precios. La correcta incorporación de impuestos previene la erosión oculta de márgenes que sorprende en el momento de la renovación.',
      'b2.title':'Aumente la tasa de conversión','b2.body':'Ofrezca una experiencia de compra local y conforme que elimine la descalificación en RFPs y elimine las objeciones de compras antes de que paralicen el acuerdo.',
      'b3.title':'Reduzca churn & CAC','b3.body':'Un camino de compra local estructurado elimina el principal driver de churn relacionado con impuestos y acorta los ciclos de ventas — mejorando directamente el NRR y reduciendo los costos de adquisición.',
      'b4.title':'Escale con seguridad hasta 2033','b4.body':'Use la infraestructura local de WTM para navegar el período de transición completo hasta 2033 y expandirse por todo el mercado LATAM con confianza.',
      /* ACTIONS */
      'action.eyebrow':'Hoja de ruta estratégica',
      'action.h2':'Actúe antes de que la reforma esté completamente operativa.',
      'action.lead':'El primer paso no es abrir una entidad en Brasil ni elegir un revendedor no verificado. El primer paso es mapear su exposición actual y modelar cómo cambian los costos desde ahora hasta 2033.',
      'a1.step':'Paso 01','a1.title':'Mapee su presencia en Brasil','a1.body':'Identifique todos los clientes brasileños, flujos de ingresos y métodos de pago actuales para comprender el alcance total de su exposición.',
      'a2.step':'Paso 02','a2.title':'Estime la exposición tributaria de los clientes','a2.body':'Evalúe cuánto impuesto lleva cada cliente actualmente — y modele cómo esa carga cambia durante la transición hasta 2033.',
      'a3.step':'Paso 03','a3.title':'Identifique cuentas en riesgo','a3.body':'Marque los clientes más propensos a cancelar, hacer downgrade o retrasar la renovación a medida que aumentan los costos tributarios y el escrutinio de cumplimiento.',
      'a4.step':'Paso 04','a4.title':'Revise el lenguaje contractual','a4.body':'Evalúe si sus acuerdos actuales abordan adecuadamente la responsabilidad tributaria, la asignación de pasivos y las obligaciones de cumplimiento.',
      'a5.step':'Paso 05','a5.title':'Prepare la facturación local con WTM','a5.body':'Diseñe un camino de compra local conforme — factura local, pago en BRL, soporte completo CBS/IBS — listo antes de que los clientes lo soliciten.',
      'a6.step':'Paso 06','a6.title':'Capacite a sus equipos de go-to-market','a6.body':'Alinee los equipos de ventas, finanzas, legal y éxito del cliente sobre cómo posicionar el cumplimiento en Brasil como una ventaja competitiva, no un costo.',
      /* GLOBE */
      'globe.eyebrow':'Presencia global',
      'globe.h2':'Operando donde sus clientes lo necesitan.',
      'globe.lead':'WTM tiene infraestructura local en las Américas, Europa y Oriente Medio — asegurando que su expansión en Brasil esté respaldada por una red que entiende cada mercado.',
      /* CTA */
      'cta.trust':'Con la confianza de <strong>4.000+</strong> empresas en todo el mundo',
      'cta.tagline':'entienda su exposición en brasil<br><span class="accent">antes de que se convierta en un problema de ventas.</span>',
      'cta.leadtext':'Elegida por más de 4.000 empresas que se han expandido a nuevos mercados de manera confiable y simplificada, con total cumplimiento en sus operaciones.',
      'cta.stat1':'Empresas expandidas','cta.stat2':'Años de experiencia','cta.stat3':'Prepárese ahora',
      'cta.body':'Brasil está profesionalizando cómo se compran, gravan, documentan y reportan los servicios digitales extranjeros. Los ganadores serán las empresas que traten el cumplimiento como una ventaja competitiva.',
      'cta.btn1':'Hablar con especialista <i data-lucide="arrow-right"></i>','cta.btn2':'Contacto en LinkedIn',
      /* FOOTER */
      'footer.tagline':'expansión con poder.','footer.privacy':'Política de privacidad','footer.terms':'Términos de uso','footer.contact':'Contacto',
      'footer.copy':'© 2025 WTM. Todos los derechos reservados.',
      'footer.places':'Brasil · EE.UU. · Canadá · México · Perú · Uruguay · Portugal · EAU',
      'footer.since':'Impulsando la expansión global de negocios desde 2003.',
    }
  };"""

# find and replace the entire const T block
old_start = '  const T = {'
old_end = '  };'
start_idx = h.find(old_start)
# find matching closing }; by scanning from old_start
depth = 0
end_idx = start_idx
for i, ch in enumerate(h[start_idx:], start_idx):
    if ch == '{': depth += 1
    elif ch == '}':
        depth -= 1
        if depth == 0:
            end_idx = i + 1
            # consume trailing ;
            if h[end_idx:end_idx+1] == ';':
                end_idx += 1
            break

if start_idx == -1:
    print('ERROR: T block not found')
else:
    h = h[:start_idx] + NEW_T + h[end_idx:]
    print('T object replaced')

with open(f'{BASE}/index.html', 'w', encoding='utf-8') as f:
    f.write(h)
print('Done — index.html written')
