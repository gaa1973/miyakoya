# SEO & Content Optimization Plan

Based on `SEO_Content_Update.md`, I will implement the following changes to enhance search visibility and user experience while maintaining the brand's premium tone.

## 1. SEO Optimization

**Goal**: Improve visibility for keywords "Adult Ballet", "Order Made", "Size Order".

### [MODIFY] [index.html](file:///wsl.localhost/Ubuntu/home/gaa/repo/miyakoya/index.html)

- **Title**: `MIYAKOYA ｜大人バレエのオーダーメイド衣装・サイズオーダー対応`
- **Description**: `大人バレエや既製サイズが合わない方へ。MIYAKOYA は伝統と現代が織りなす完全オーダーメイドのバレエ衣装アトリエ。一人ひとりに合わせた一着をお仕立てします。`

### [MODIFY] [lookbook.html](file:///wsl.localhost/Ubuntu/home/gaa/repo/miyakoya/lookbook.html)

- **Title**: `Collection ｜ MIYAKOYA - 大人バレエ対応・クラシックチュチュ＆衣装一覧`
- **Description**: `MIYAKOYA のバレエ衣装コレクション。大人バレエやサイズオーダーにも対応したクラシックチュチュ、ティアラ、舞台衣装をご紹介します。`

## 2. Mobile CTA Enhancement

**Goal**: Increase mobile conversions with a persistent, elegant CTA button.

### [MODIFY] [index.html](file:///wsl.localhost/Ubuntu/home/gaa/repo/miyakoya/index.html) & [lookbook.html](file:///wsl.localhost/Ubuntu/home/gaa/repo/miyakoya/lookbook.html)

- **Feature**: Fixed bottom "View Shop" button.
- **Link**: `https://shop.miyakoyadesign.com/`
- **Text**: `BASE で衣装を見る`
- **CSS Requirements**:
  - Visible only on mobile (`max-width: 768px`)
  - Bottom fixed, high z-index
  - Minimal black/white design
  - Must not cover important text

## 3. Inclusive Copy & FAQ

**Goal**: Address body type concerns with dignity and reassurance.

### [MODIFY] [index.html](file:///wsl.localhost/Ubuntu/home/gaa/repo/miyakoya/index.html)

- **Concept Section**: Add copy reinforcing custom fit.
  - _Text_: `既製品では叶わない、あなただけのフィット感を。サイズや体型に左右されることなく、すべてのダンサーが舞台で美しく輝けるように。MIYAKOYA は一着ずつ丁寧に仕立てます。`
- **FAQ Section**: Add specific Q&A for body concerns.
  - **Q**: `体型に不安がありますが、オーダーできますか？`
  - **A**: `もちろんです。MIYAKOYA のオーダーメイドは、お客様お一人おひとりの身体に合わせて、パターン（型紙）から制作します。気になる部分を自然にカバーし、長所を引き立てるデザインをご提案いたしますので、安心してご相談ください。`

## 4. Lookbook Content SEO Reinforcement

**Goal**: Reinforce "Adult Ballet" and "Size Order" positioning in product details.

### [MODIFY] [lookbook.html](file:///wsl.localhost/Ubuntu/home/gaa/repo/miyakoya/lookbook.html)

- **Item Descriptions**: Add a sentence such as:
  - `サイズオーダーにより、大人の身体に美しくフィットするシルエットを実現します。`
  - Or: `大人バレエの舞台や、既製サイズが合わない方にも対応可能な一着です。`

## 5. Verification

- Verify meta tags in `<head>`.
- Check Mobile CTA visibility and layout on mobile view.
- Verify tone and correctness of Japanese text.
