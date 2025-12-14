# SEO & Mobile CTA Optimization Instructions

for MIYAKOYA Website

## Objective

Enhance SEO performance, mobile conversion rate, and inclusivity messaging  
while preserving MIYAKOYA’s premium, atelier-based brand identity.

This update focuses on:

- Search intent for adult ballet dancers
- Size / body-type concerns handled with dignity
- Strong mobile call-to-action (CTA)

---

## 1. SEO Title & Meta Description Optimization

### [MODIFY] index.html

**Title**
MIYAKOYA ｜大人バレエのオーダーメイド衣装・サイズオーダー対応

markdown
コードをコピーする

**Meta Description**
大人バレエや既製サイズが合わない方へ。MIYAKOYA は伝統と現代が織りなす完全オーダーメイドのバレエ衣装アトリエ。一人ひとりに合わせた一着をお仕立てします。

yaml
コードをコピーする

**SEO Intent**

- Target keywords:
  - 大人バレエ
  - バレエ 衣装 オーダーメイド
  - サイズオーダー バレエ衣装
- Appeal to dancers with body-fit concerns without using negative wording

---

### [MODIFY] lookbook.html

**Title**
Collection ｜ MIYAKOYA - 大人バレエ対応・クラシックチュチュ＆衣装一覧

markdown
コードをコピーする

**Meta Description**
MIYAKOYA のバレエ衣装コレクション。大人バレエやサイズオーダーにも対応したクラシックチュチュ、ティアラ、舞台衣装をご紹介します。

yaml
コードをコピーする

**SEO Intent**

- Reinforce adult ballet positioning
- Explicitly state size-order compatibility
- Improve entry points from image / gallery searches

---

## 2. Mobile CTA Enhancement

### Goal

Increase mobile conversions by providing a persistent, elegant CTA  
without disrupting the premium visual experience.

---

### [MODIFY] index.html & lookbook.html

**HTML**

- Add a fixed bottom CTA visible only on mobile (max-width: 768px)
- Button text:
  BASE で衣装を見る

mathematica
コードをコピーする

**Link (Absolute Path)**
https://shop.miyakoyadesign.com/

yaml
コードをコピーする

---

### **CSS Requirements**

- Bottom-fixed
- High z-index (above content)
- Minimal black / white or monochrome design
- Rounded edges, refined typography
- Must not cover text or important UI elements

---

### **Verification**

- Confirm CTA appears only on mobile
- Confirm scrollable content has sufficient bottom padding
- Confirm CTA hides near footer if needed

---

## 3. Inclusive Copy (Body-Type Sensitive Messaging)

### Concept Section Copy Addition

**[ADD] index.html – Concept Section**

既製品では叶わない、あなただけのフィット感を。
サイズや体型に左右されることなく、
すべてのダンサーが舞台で美しく輝けるように。
MIYAKOYA は一着ずつ丁寧に仕立てます。

yaml
コードをコピーする

**Guideline**

- Never use words like “太っている”
- Emphasize custom tailoring as empowerment
- Maintain elegance and reassurance

---

## 4. FAQ Enhancement (Trust & SEO)

### [ADD] index.html – FAQ Section

**Q**
体型に不安がありますが、オーダーできますか？

css
コードをコピーする

**A**
もちろんです。MIYAKOYA のオーダーメイドは、お客様お一人おひとりの身体に合わせて、パターン（型紙）から制作します。
気になる部分を自然にカバーし、長所を引き立てるデザインをご提案いたしますので、安心してご相談ください。

yaml
コードをコピーする

---

## 5. Lookbook Content SEO Reinforcement

### [MODIFY] Lookbook Item Descriptions

**Instruction**

- Add one sentence per item that subtly reinforces:
  - Adult ballet suitability
  - Custom sizing / order flexibility

**Example Sentence (Optional per item)**
大人バレエの舞台や、既製サイズが合わない方にも対応可能な一着です。

python
コードをコピーする

or

サイズオーダーにより、大人の身体に美しくフィットするシルエットを実現します。

yaml
コードをコピーする

---

## 6. Final Verification Checklist

- [ ] All meta tags are correctly reflected in `<head>`
- [ ] Mobile CTA appears only under 768px
- [ ] No CTA overlap with text or footer
- [ ] Tone remains premium and non-commercial
- [ ] Inclusive copy feels reassuring, not explanatory
- [ ] Absolute links are used for all external destinations

---

## Brand Guardrails (Do Not Break)

- No casual or mass-market tone
- No discount or price-driven language
- No negative body-related wording
- Maintain atelier / bespoke positioning at all times
