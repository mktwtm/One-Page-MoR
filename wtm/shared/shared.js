/* =============================================================
   WTM Corporate Site — shared.js
   Each page must define BEFORE this script:
     window.PAGE_SOURCE  — string ID for Supabase (e.g. 'corp_home')
     window.I18N         — { en: {...}, pt: {...}, es: {...} }
   ============================================================= */
(function () {
  'use strict';

  // ── nav scroll state ───────────────────────────────────────────────────────
  var nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', function () {
      nav.classList.toggle('scrolled', window.scrollY > 30);
    }, { passive: true });
  }

  // ── reveals ────────────────────────────────────────────────────────────────
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  }

  // ── i18n ───────────────────────────────────────────────────────────────────
  var T = window.I18N || { en: {}, pt: {}, es: {} };
  var YEAR = new Date().getFullYear();
  var currentLang = 'en';

  function applyLang(lang) {
    var t = T[lang] || T.en || {};
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var k = el.getAttribute('data-i18n');
      if (t[k] != null) el.textContent = t[k];
    });
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var k = el.getAttribute('data-i18n-html');
      if (t[k] != null) {
        el.innerHTML = String(t[k]).replace('YEAR', YEAR);
        if (window.lucide) window.lucide.createIcons({ nodes: [el] });
      }
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var k = el.getAttribute('data-i18n-placeholder');
      if (t[k] != null) el.setAttribute('placeholder', t[k]);
    });
    document.documentElement.lang = lang;
    currentLang = lang;
    syncInternalLangLinks(lang);
  }

  function syncInternalLangLinks(lang) {
    document.querySelectorAll('a[data-keep-lang]').forEach(function (a) {
      var raw = a.getAttribute('data-keep-lang-href') || a.getAttribute('href');
      if (!raw || raw.startsWith('#') || raw.startsWith('mailto:') || raw.startsWith('tel:')) return;
      try {
        if (!a.getAttribute('data-keep-lang-href')) a.setAttribute('data-keep-lang-href', raw);
        var url = new URL(raw, window.location.href);
        if (url.origin !== window.location.origin) return;
        url.searchParams.set('lang', lang);
        a.setAttribute('href', url.pathname + url.search + url.hash);
      } catch (e) { /* ignore */ }
    });
  }

  // Wire language toggles (header + footer share the same class)
  function wireLangToggle(root) {
    root.querySelectorAll('[data-lang]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var lang = btn.getAttribute('data-lang');
        document.querySelectorAll('.lang-toggle [data-lang]').forEach(function (x) {
          x.classList.toggle('on', x.getAttribute('data-lang') === lang);
        });
        applyLang(lang);
      });
    });
  }
  document.querySelectorAll('.lang-toggle').forEach(wireLangToggle);

  // ── Supabase client ────────────────────────────────────────────────────────
  var SUPABASE_URL = 'https://mpamdvrvswwumgpfoskd.supabase.co';
  var SUPABASE_ANON_KEY = 'sb_publishable_GsAWP-wJaQ-IDQjWgGI8Qg_ol_-RdM5';
  var sb = (window.supabase && window.supabase.createClient)
    ? window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, { auth: { persistSession: false } })
    : null;

  // ── Visitor country detection (Cloudflare → ipapi fallback) ────────────────
  var COUNTRY_STORAGE_KEY = 'wtm_country_v1';
  function detectCountry() {
    try {
      var cached = sessionStorage.getItem(COUNTRY_STORAGE_KEY);
      if (cached) return Promise.resolve(JSON.parse(cached));
    } catch (e) { /* ignore */ }

    function fromCloudflare() {
      return fetch('/cdn-cgi/trace', { cache: 'no-store' })
        .then(function (r) { return r.ok ? r.text() : null; })
        .then(function (text) {
          if (!text) return null;
          var map = {};
          text.trim().split('\n').forEach(function (l) {
            var idx = l.indexOf('=');
            if (idx > -1) map[l.slice(0, idx)] = l.slice(idx + 1);
          });
          if (map.loc && /^[A-Z]{2}$/.test(map.loc)) {
            return { country: map.loc, country_region: null, country_source: 'cf' };
          }
          return null;
        })
        .catch(function () { return null; });
    }
    function fromIpapi() {
      return fetch('https://ipapi.co/json/', { cache: 'no-store' })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (data) {
          if (data && /^[A-Z]{2}$/.test(data.country_code || '')) {
            return {
              country: data.country_code,
              country_region: (data.region || data.region_code || null),
              country_source: 'ipapi'
            };
          }
          return null;
        })
        .catch(function () { return null; });
    }

    return fromCloudflare().then(function (r) {
      return r || fromIpapi();
    }).then(function (result) {
      if (result) {
        try { sessionStorage.setItem(COUNTRY_STORAGE_KEY, JSON.stringify(result)); } catch (e) { /* ignore */ }
      }
      return result;
    });
  }
  var _countryPromise = detectCountry();

  // ── UTM capture ────────────────────────────────────────────────────────────
  var UTM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid'];
  var UTM_STORAGE_KEY = 'wtm_utm_v1';
  (function captureUtms() {
    try {
      var params = new URLSearchParams(window.location.search);
      var found = {}, any = false;
      UTM_KEYS.forEach(function (k) {
        var v = params.get(k);
        if (v) { found[k] = v.slice(0, 300); any = true; }
      });
      if (any) {
        found._captured_at = new Date().toISOString();
        found._landing_url = (window.location.origin + window.location.pathname + window.location.search).slice(0, 1000);
        sessionStorage.setItem(UTM_STORAGE_KEY, JSON.stringify(found));
      }
    } catch (e) { /* ignore */ }
  })();
  function readUtms() {
    try {
      var raw = sessionStorage.getItem(UTM_STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  // ── Page veil for navigation transitions ──────────────────────────────────
  var pageVeil = document.getElementById('pageVeil');
  function navigateWithVeil(url) {
    if (document.startViewTransition && 'navigation' in document) {
      window.location.href = url;
      return;
    }
    if (pageVeil) {
      pageVeil.classList.add('show');
      if (window.lucide) window.lucide.createIcons({ nodes: [pageVeil] });
    }
    setTimeout(function () { window.location.href = url; }, 520);
  }

  // ── Modal: Talk to a specialist ────────────────────────────────────────────
  var modal = document.getElementById('specialistModal');
  var MIN_FILL_MS = 2500;
  var modalOpenedAt = 0;

  function openModal() {
    if (!modal) return;
    modalOpenedAt = Date.now();
    modal.hidden = false;
    modal.classList.add('show');
    void modal.offsetWidth;
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { modal.classList.add('open'); });
    });
    document.body.style.overflow = 'hidden';
    var first = modal.querySelector('input, select, textarea');
    if (first) setTimeout(function () { first.focus(); }, 320);
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove('open');
    document.body.style.overflow = '';
    setTimeout(function () {
      modal.classList.remove('show');
      modal.hidden = true;
    }, 380);
  }
  document.querySelectorAll('.js-open-modal').forEach(function (el) {
    el.addEventListener('click', function (e) { e.preventDefault(); openModal(); });
  });
  if (modal) {
    modal.addEventListener('click', function (e) {
      if (e.target === modal || e.target.closest('[data-modal-close]')) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
    });
  }

  // ── Form submission (works for ANY .lead-form on the page) ────────────────
  function buildPayload(form, source) {
    var utms = readUtms();
    var val = function (name) {
      var el = form.elements[name];
      return el ? String(el.value || '').trim() : '';
    };
    var checked = function (name) {
      var el = form.elements[name];
      return el ? !!el.checked : false;
    };
    var asBool = function (v) {
      if (v === '' || v == null) return null;
      var s = String(v).toLowerCase();
      if (s === 'yes' || s === 'true' || s === '1' || s === 'si' || s === 'sí' || s === 'sim') return true;
      if (s === 'no' || s === 'false' || s === '0' || s === 'não' || s === 'nao') return false;
      return null;
    };

    return {
      name: val('name'),
      company: val('company'),
      email: val('email'),
      whatsapp: val('whatsapp') || null,
      sells_latam: asBool(val('sells_latam')),
      has_br_entity: asBool(val('has_br_entity')),
      message: val('message') || null,
      language: currentLang || document.documentElement.lang || 'en',
      source: source || window.PAGE_SOURCE || 'corp_site',
      user_agent: navigator.userAgent.slice(0, 500),
      referrer: document.referrer ? document.referrer.slice(0, 500) : null,
      utm_source: utms.utm_source || null,
      utm_medium: utms.utm_medium || null,
      utm_campaign: utms.utm_campaign || null,
      utm_term: utms.utm_term || null,
      utm_content: utms.utm_content || null,
      gclid: utms.gclid || null,
      fbclid: utms.fbclid || null,
      landing_url: (window.location.origin + window.location.pathname + window.location.search).slice(0, 1000)
    };
  }

  function handleSubmit(form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      // Honeypot + min-fill timing
      var honeypot = (form.elements.website && form.elements.website.value) || '';
      var openedAt = form.dataset.openedAt ? Number(form.dataset.openedAt) : modalOpenedAt;
      var elapsed = Date.now() - (openedAt || 0);
      var isBot = honeypot.trim() !== '' || (openedAt > 0 && elapsed < MIN_FILL_MS);
      if (isBot) {
        console.warn('[anti-spam] submission rejected');
        var lang0 = encodeURIComponent(currentLang || 'en');
        navigateWithVeil('../thankyou.html?lang=' + lang0);
        return;
      }

      var submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.classList.add('is-loading');

      Promise.race([
        _countryPromise,
        new Promise(function (r) { setTimeout(function () { r(null); }, 800); })
      ]).then(function (geo) {
        var payload = buildPayload(form, form.dataset.source);
        if (geo) {
          payload.country = geo.country || null;
          payload.country_region = geo.country_region ? String(geo.country_region).slice(0, 100) : null;
          payload.country_source = geo.country_source || null;
        }
        if (sb) {
          return sb.from('mor_landing_leads').insert(payload).then(function (res) {
            if (res.error) console.error('[supabase] insert failed:', res.error);
          });
        }
        console.warn('[supabase] client not loaded; skipping insert');
        return null;
      }).catch(function (err) {
        console.error('[supabase] unexpected error:', err);
      }).then(function () {
        if (submitBtn) submitBtn.classList.remove('is-loading');

        // Inline success state (for non-modal forms)
        var success = form.parentElement.querySelector('.form-success');
        if (success && !form.closest('.modal-card')) {
          form.style.display = 'none';
          success.classList.add('show');
          if (window.lucide) window.lucide.createIcons({ nodes: [success] });
        }
        if (form.closest('.modal-card')) {
          form.closest('.modal-card').classList.add('is-success');
        }

        var lang = encodeURIComponent(currentLang || 'en');
        setTimeout(function () {
          navigateWithVeil('../thankyou.html?lang=' + lang);
        }, 1200);
      });
    });

    // record opened-at when the user first focuses any field (for inline forms)
    form.addEventListener('focusin', function () {
      if (!form.dataset.openedAt) form.dataset.openedAt = String(Date.now());
    }, { once: true });
  }
  document.querySelectorAll('.lead-form').forEach(handleSubmit);

  // ── bfcache reset ──────────────────────────────────────────────────────────
  window.addEventListener('pageshow', function () {
    if (modal) {
      modal.classList.remove('open');
      modal.classList.remove('show');
      modal.hidden = true;
      var card = modal.querySelector('.modal-card');
      if (card) card.classList.remove('is-success');
    }
    document.querySelectorAll('.lead-form').forEach(function (form) {
      form.style.display = '';
      form.reset();
      form.dataset.openedAt = '';
      var loadBtn = form.querySelector('.is-loading');
      if (loadBtn) loadBtn.classList.remove('is-loading');
    });
    document.querySelectorAll('.form-success.show').forEach(function (s) { s.classList.remove('show'); });
    if (pageVeil) pageVeil.classList.remove('show');
    document.body.style.overflow = '';
  });

  // ── lucide + initial language ──────────────────────────────────────────────
  function init() {
    if (window.lucide) window.lucide.createIcons();
    var params = new URLSearchParams(window.location.search);
    var urlLang = params.get('lang');
    applyLang((urlLang && T[urlLang]) ? urlLang : 'en');

    // mark active nav link based on page slug
    var slug = (location.pathname.split('/').filter(Boolean).pop() || 'home').replace('.html', '');
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      if (a.getAttribute('data-page') === slug) a.classList.add('active');
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose minimal API
  window.WTM = {
    applyLang: applyLang,
    openModal: openModal,
    closeModal: closeModal
  };
})();
