# UI / SEO Optimization Instructions (MIYAKOYA)

This document defines concrete implementation instructions for improving SEO structure, accessibility, internal linking, and mobile CTA usability.
All changes must preserve the premium, elegant brand tone of MIYAKOYA.

---

## 1. h1 タグ構造の最適化（SEO 最重要）

### Goal

Ensure each page has exactly **one `<h1>`**, clearly representing the page’s main value proposition.
Improve SEO crawlability and semantic structure.

### Rules

- Each HTML page must contain **only one `<h1>`**
- `<h1>` must describe the page’s main concept, not a generic brand name
- Visual design may remain unchanged using CSS (font-size, style)

### Implementation Instructions

#### index.html

- Replace current hero title structure with `<h1>`
- Use the following text exactly:

```html
<h1 class="hero-title">
  世界に一着。あなたのためだけのプライベート・アトリエ。
</h1>
Move supporting copy to
<h2>
  or
  <p>html コードをコピーする</p>

  <h2 class="hero-subtitle">
    ダンサーの夢を叶える、唯一無二のオーダーメイドバレエ衣装
  </h2>
  lookbook.html Set
  <h1>
    at the top of the page: html コードをコピーする
    <h1>MIYAKOYA バレエ衣装コレクション｜オーダーメイド＆レンタル対応</h1>
    Item titles should be
    <h2>
      or
      <h3>
        2. 画像 alt 属性の完備（SEO + アクセシビリティ） Goal Improve Google
        Image Search visibility and accessibility. Describe what the image
        represents, not just the filename. Rules All <img /> must include an alt
        attribute Include: Product type Target (大人バレエ / オーダーメイド)
        Brand name (MIYAKOYA) Avoid keyword stuffing Implementation Examples
        Hero Image (CSS background image) If possible, add a visually hidden
        <img /> for SEO fallback: html コードをコピーする
        <img
          src="assets/hero_bg_optimized.jpg"
          alt="大人バレエ向けオーダーメイド衣装アトリエ MIYAKOYA"
          class="visually-hidden"
        />
        Collection / Lookbook Images html コードをコピーする
        <img
          src="assets/tutu_lilac.jpg"
          alt="大人バレエ対応 クラシックチュチュ オーダーメイド｜MIYAKOYA"
        />
        html コードをコピーする
        <img
          src="assets/collection_tiara.png"
          alt="舞台映えするバレエ用ティアラ オーダーメイド対応｜MIYAKOYA"
        />
        3. 内部リンクの最適化（SEO評価向上） Goal Guide users and search engines
        through a clear content flow: Concept → Collection → Shop → Contact
        Rules Use descriptive anchor text (avoid「こちら」「詳しく」) Link
        related sections naturally inside content Ensure no orphan pages exist
        Required Internal Links index.html Hero section: html コードをコピーする
        <a href="/lookbook.html">オーダーメイド衣装コレクションを見る</a>
        Concept section: html コードをコピーする
        <a href="#service">オーダー・レンタルの詳細を見る</a>
        FAQ section: html コードをコピーする
        <a href="#contact">不安な点はお問い合わせください</a>
        lookbook.html Each item block: html コードをコピーする
        <a href="https://shop.miyakoyadesign.com/..." class="btn-outline">
          この衣装をBASEで見る
        </a>
        Footer: html コードをコピーする
        <a href="/index.html#contact">オーダー・相談はこちら</a>
        4. モバイル CTA の視認性強化と固定動作調整 Goal Maximize mobile
        conversion rate by keeping CTA always reachable without harming premium
        UX. Design Rules Mobile only (max-width: 768px) Button height ≥ 44px
        High contrast, minimal text Elegant (black / white / gold)
        Implementation Instructions HTML (index.html & lookbook.html) html
        コードをコピーする
        <div class="mobile-cta">
          <a href="https://shop.miyakoyadesign.com/" class="mobile-cta-btn">
            BASEで商品を見る
          </a>
        </div>
        CSS css コードをコピーする .mobile-cta { display: none; } @media
        (max-width: 768px) { .mobile-cta { display: block; position: fixed;
        bottom: 0; left: 0; width: 100%; padding: 12px 16px; background:
        rgba(255,255,255,0.95); box-shadow: 0 -4px 16px rgba(0,0,0,0.08);
        z-index: 9999; } .mobile-cta-btn { display: block; width: 100%;
        text-align: center; padding: 14px 0; font-size: 16px; letter-spacing:
        0.05em; background: #000; color: #fff; border-radius: 30px; } } Optional
        Enhancement Hide CTA when footer is visible (IntersectionObserver)
        Change CTA text on Lookbook pages: 「この衣装をBASEで見る」 Final
        Checklist Each page has exactly one
        <h1>
          All images include meaningful alt No orphan pages (every page linked
          internally) Mobile CTA visible on scroll, easy to tap Premium tone
          preserved (no aggressive wording) End of Instructions
        </h1>
      </h3>
    </h2>
  </h1>
</h2>
```
