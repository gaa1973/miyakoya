# MIYAKOYA - Elegant Ballet Costume Atelier

バレエ衣装ブランド「MIYAKOYA」のブランド用ランディングページ（LP）。
「Modern Tradition（伝統と現代の融合）」をコンセプトに、見る人を魅了するエレガントで高級感のあるデザインを実装したポートフォリオ・プロジェクトです。

## プロジェクト概要

本プロジェクトは、ハンドメイドのバレエ衣装（チュチュ、ティアラ、アクセサリー）の魅力を最大限に伝え、ブランド価値を高めることを目的としています。
「Elegant Pink」をテーマカラーとし、PC・スマートフォン双方で最適なユーザー体験を提供するレスポンシブデザインを採用しています。

### 主な特徴

*   **世界観の表現**: 明朝体とセリフ体（Google Fonts）を組み合わせ、洗練された「大人バレエ」の雰囲気を演出。
*   **動的なインタラクション**: スクロール連動のフェードイン、画像のパララックス効果など、静止画だけではない「生きている」WEB体験。
*   **モバイルファースト**: スマートフォン閲覧時のCV率向上を意識した、追従型CTA（Call To Action）の実装。
*   **パフォーマンスとSEO**: LCP（Largest Contentful Paint）を意識した最適化と、セマンティックなHTML構造によるSEO対策。

## 技術スタック

*   **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (Vanilla)
    *   フレームワークに依存せず、軽量かつ高速な描画を実現。
    *   CSS Custom Properties (Variables) を活用したテーマ管理。
*   **Tools**:
    *   Google Fonts (Zen Old Mincho, Cinzel, Cormorant Garamond)
    *   Font Awesome (Icons)
*   **Architecture**:
    *   静的サイト（Static Site）として構築。
    *   Vercel 等のホスティングサービスでの運用を想定。

## ディレクトリ構造

```
miyakoya/
├── index.html        # トップページ
├── lookbook.html     # ルックブックページ
├── collection.html   # コレクション詳細
├── assets/           # 画像・メディアリソース
├── css/              # スタイルシート (style.css, mobile.css 等)
├── js/               # フロントエンドロジック (main.js)
└── SPEC.md           # プロジェクト仕様書
```

## 開発・デザインのこだわり

1.  **デザインとタイポグラフィ**:
    *   日本語には「Zen Old Mincho」、英語には「Cormorant Garamond」を採用し、可読性と美しさを両立。
    *   余白（White Space）を贅沢に使い、高級感のあるレイアウトを実現。

2.  **レスポンシブ対応**:
    *   モバイル表示ではハンバーガーメニューを採用し、画面領域を有効活用。
    *   下部固定のCTAボタンにより、スムーズな購買導線を確保。

3.  **SEO・アクセシビリティ**:
    *   適切なメタタグ（Title, Description）の設定。
    *   多様な体型への配慮など、ユーザーに寄り添ったコピーライティング。

---
*Created by [Your Name/Handle]*
