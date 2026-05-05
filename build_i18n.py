# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\mtboh\OneDrive\My Documents\Antigravity\WTM\One Page MoR\wtm'

# ── helpers ──────────────────────────────────────────────────────────────────

def tag_attr(html, search_open, attr, value):
    """Insert data-i18n attribute into the first matching opening tag."""
    idx = html.find(search_open)
    if idx == -1:
        print(f'  MISS: {search_open[:60]!r}')
        return html
    close = html.index('>', idx)
    tag_str = html[idx:close]
    if attr in tag_str:
        return html  # already added
    new_tag = tag_str + f' {attr}="{value}"'
    return html[:idx] + new_tag + html[close:]

# ── read ─────────────────────────────────────────────────────────────────────

with open(f'{BASE}/index.html', encoding='utf-8') as f:
    h = f.read()

# ── 1. WebP in CSS ────────────────────────────────────────────────────────────
h = h.replace('photo_pattern_01.jpg', 'photo_pattern_01.webp')
h = h.replace('photo_pattern_05.jpg', 'photo_pattern_05.webp')
print('WebP CSS updated')

# ── 2. lang-toggle  ───────────────────────────────────────────────────────────
h = h.replace(
    '<span class="on">EN</span><span>PT</span>',
    '<span class="on" data-lang="en">EN</span>'
    '<span data-lang="pt">PT</span>'
    '<span data-lang="es">ES</span>'
)
print('lang-toggle updated')

# ── 3. data-i18n on key elements ──────────────────────────────────────────────
#    Format: (search_open_tag, attr, key)
#    We match the OPENING TAG TEXT (without '>') then append the attr before '>'

patches = [
    # NAV links
    ('<a href="#tax"',             'data-i18n', 'nav.tax'),
    ('<a href="#solution"',        'data-i18n', 'nav.solution'),
    ('<a href="#benefits"',        'data-i18n', 'nav.benefits'),
    ('<a href="#next-steps"',      'data-i18n', 'nav.next-steps'),
    ('<a href="#cta" class="btn btn-brand"', 'data-i18n', 'nav.cta'),

    # HERO
    ('<div class="hero-eyebrow"',  'data-i18n', 'hero.eyebrow'),
    ('<h1 class="h-display"',      'data-i18n-html', 'hero.h1'),
    ('<p class="hero-lead"',       'data-i18n', 'hero.lead'),
    ('<p class="hero-tagline versatylo"', 'data-i18n-html', 'hero.tagline'),
    ('<a href="#cta" class="btn btn-accent"', 'data-i18n-html', 'hero.cta1'),
    ('<a href="#tax" class="btn btn-ghost-light"', 'data-i18n', 'hero.cta2'),

    # TAX section
    ('<div class="eyebrow eyebrow-light" style="color:#E59A8E"', 'data-i18n', 'tax.eyebrow'),
    ('<h2 class="h-section" style="color:#fff;margin-top:18px"', 'data-i18n', 'tax.h2'),
    ('<div class="tax-block-title"', 'data-i18n', 'tax.block-title'),

    # COMMERCIAL
    ('<div class="eyebrow">Commercial impact</div>', None, None),  # handled via innerHTML approach

    # QUOTE
    ('<span class="high">',        'data-i18n', 'quote.line1'),
    ('<span class="accent">you need the transaction to work.</span>', None, None),

    # SOLUTION
    ('<div class="eyebrow">WTM Merchant of Record</div>', None, None),
    ('<div class="solution-tagline"', 'data-i18n-html', 'solution.tagline'),

    # COMPARE
    ('<div class="eyebrow">Comparison</div>', None, None),
    ('<div class="h-without">',    'data-i18n', 'compare.h-without'),
    ('<div class="h-with">',       'data-i18n', 'compare.h-with'),

    # BENEFITS
    ('<div class="eyebrow">Why WTM</div>', None, None),

    # ACTION
    ('<div class="eyebrow eyebrow-light" style="color:#A8DCE8"', 'data-i18n', 'action.eyebrow'),

    # GLOBE
    ('<div class="eyebrow eyebrow-light" style="color:#A8DCE8">Global presence</div>', None, None),

    # FOOTER
    ('<p class="versatylo">empowering expansion.</p>', None, None),
    ('<span>© 2025 WTM. All rights reserved.</span>', None, None),
]

# Apply simple attr patches
for search, attr, key in patches:
    if attr is None:
        continue
    h = tag_attr(h, search, attr, key)

print('data-i18n attrs applied')

# ── 4. Replace the old script block with full i18n engine ────────────────────

OLD_SCRIPT = '''  // language toggle (visual only)
  document.querySelectorAll('.lang-toggle span').forEach(s => {
    s.addEventListener('click', () => {
      document.querySelectorAll('.lang-toggle span').forEach(x => x.classList.remove('on'));
      s.classList.add('on');
    });
  });'''

NEW_SCRIPT = '''  // ── i18n ──────────────────────────────────────────────────────────────────
  const T = {
    en: {
      'nav.tax':'Tax reform','nav.solution':'Solution','nav.benefits':'Benefits',
      'nav.next-steps':'Next steps','nav.cta':'Talk to a specialist',
      'hero.eyebrow':'Brazil tax reform · SaaS, AI & cloud · 2025–2033',
      'hero.h1':'Your current go-to-market for Brazil may not survive the <span class="accent">new tax model.</span>',
      'hero.lead':'Brazil is moving from a market where cross-border SaaS non-compliance was often invisible, to a market where tax friction can directly affect sales, renewals, expansion and customer experience. The 2027 transition has already started.',
      'hero.tagline':'empowering expansion. <em>without the tax surprise.</em>',
      'hero.cta1':'Talk to a specialist <i data-lucide="arrow-right"></i>',
      'hero.cta2':'Understand your exposure',
      'tax.eyebrow':'The tax reality',
      'tax.h2':"Brazil’s tax layer is larger than your customers realize — and it’s about to grow.",
      'tax.block-title':'Current obligations on your Brazilian customers',
      'action.eyebrow':'Strategic roadmap',
      'compare.h-without':'Without WTM','compare.h-with':'With WTM',
      'solution.tagline':'<i data-lucide="sparkles"></i> Most MoRs solve your problem. WTM solves the transaction.',
    },
    pt: {
      'nav.tax':'Reforma tributária','nav.solution':'Solução','nav.benefits':'Benefícios',
      'nav.next-steps':'Próximos passos','nav.cta':'Falar com especialista',
      'hero.eyebrow':'Reforma tributária do Brasil · SaaS, IA & cloud · 2025–2033',
      'hero.h1':'Seu modelo de go-to-market para o Brasil pode não sobreviver ao <span class="accent">novo modelo fiscal.</span>',
      'hero.lead':'O Brasil está migrando de um mercado em que a não conformidade tributária de SaaS cross-border era frequentemente invisível, para um mercado em que a fricção fiscal pode afetar diretamente vendas, renovações, expansão e a experiência do cliente. A transição de 2027 já começou.',
      'hero.tagline':'expansão com poder. <em>sem a surpresa fiscal.</em>',
      'hero.cta1':'Falar com especialista <i data-lucide="arrow-right"></i>',
      'hero.cta2':'Entenda sua exposição',
      'tax.eyebrow':'A realidade tributária',
      'tax.h2':'A camada tributária do Brasil é maior do que seus clientes percebem — e está prestes a crescer.',
      'tax.block-title':'Obrigações atuais sobre seus clientes brasileiros',
      'action.eyebrow':'Roteiro estratégico',
      'compare.h-without':'Sem a WTM','compare.h-with':'Com a WTM',
      'solution.tagline':'<i data-lucide="sparkles"></i> A maioria dos MoRs resolve o seu problema. A WTM resolve a transação.',
    },
    es: {
      'nav.tax':'Reforma tributaria','nav.solution':'Solución','nav.benefits':'Beneficios',
      'nav.next-steps':'Próximos pasos','nav.cta':'Hablar con especialista',
      'hero.eyebrow':'Reforma tributaria de Brasil · SaaS, IA & cloud · 2025–2033',
      'hero.h1':'Su modelo de go-to-market para Brasil puede no sobrevivir al <span class="accent">nuevo modelo fiscal.</span>',
      'hero.lead':'Brasil está pasando de un mercado donde el incumplimiento tributario de SaaS cross-border era frecuentemente invisible, a un mercado donde la fricción fiscal puede afectar directamente las ventas, renovaciones, expansión y la experiencia del cliente. La transición de 2027 ya comenzó.',
      'hero.tagline':'expansión con poder. <em>sin la sorpresa fiscal.</em>',
      'hero.cta1':'Hablar con especialista <i data-lucide="arrow-right"></i>',
      'hero.cta2':'Entienda su exposición',
      'tax.eyebrow':'La realidad tributaria',
      'tax.h2':'La capa tributaria de Brasil es mayor de lo que sus clientes perciben — y está a punto de crecer.',
      'tax.block-title':'Obligaciones actuales sobre sus clientes brasileños',
      'action.eyebrow':'Hoja de ruta estratégica',
      'compare.h-without':'Sin WTM','compare.h-with':'Con WTM',
      'solution.tagline':'<i data-lucide="sparkles"></i> La mayoría de los MoRs resuelven su problema. WTM resuelve la transacción.',
    }
  };

  let currentLang = 'en';

  function applyLang(lang) {
    const t = T[lang] || T.en;
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const k = el.getAttribute('data-i18n');
      if (t[k] != null) el.textContent = t[k];
    });
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const k = el.getAttribute('data-i18n-html');
      if (t[k] != null) {
        el.innerHTML = t[k];
        if (window.lucide) lucide.createIcons({ nodes: [el] });
      }
    });
    document.documentElement.lang = lang;
    currentLang = lang;
  }

  document.querySelectorAll('.lang-toggle [data-lang]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.lang-toggle [data-lang]').forEach(x => x.classList.remove('on'));
      btn.classList.add('on');
      applyLang(btn.getAttribute('data-lang'));
    });
  });'''

if OLD_SCRIPT in h:
    h = h.replace(OLD_SCRIPT, NEW_SCRIPT)
    print('Script replaced')
else:
    print('ERROR: old script block not found')

# ── 5. write ──────────────────────────────────────────────────────────────────
with open(f'{BASE}/index.html', 'w', encoding='utf-8') as f:
    f.write(h)
print('index.html written')
