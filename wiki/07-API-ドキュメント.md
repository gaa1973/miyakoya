# 🔌 07. API ドキュメント

## 🌐 外部サービス連携

本プロジェクトでは、静的サイトの限界を補うため、以下の外部 API およびサービスを活用しています。

### 1. Formspree (問い合わせフォーム)

「Contact」セクションのフォームデータ送信に使用しています。

- **Endpoint**: `https://formspree.io/f/xwpgzerj`
- **Method**: `POST`
- **Fields**:
  - `name`: お名前
  - `email`: メールアドレス
  - `message`: 問い合わせ内容
- **連携ファイル**: `index.html` (line 413)

### 2. Google Fonts (フォント)

ブランドの「エレガントさ」を演出するためのウェブフォントを取得。

- **使用フォント**:
  - `Cormorant Garamond`: セリフ体。メイン見出し等。
  - `Noto Serif JP`: 日本語和文フォント。
  - `Shippori Mincho`, `Zen Old Mincho`: 補助。
- **読み込み箇所**: `index.html` (line 16-20)

### 3. SNS / Shop リンク (外部導線)

外部プラットフォームへのシームレスな移行。

- **BASE**: オンラインショップ。注文および決済。
- **Minne**: ハンドメイドマーケット。
- **Instagram**: プロフィールおよび DM（ダイレクトメッセージ）。

## 📸 Instagram DM 連携

特にモバイルにおいて、強力なコンバージョン導線として機能しています。

- **URL 構成**: `https://www.instagram.com/miya_koya.3858/`
- **実装形態**: SVG アイコンとテキストを組み合わせたボタン。

## 🛠️ 将来的な拡張の可能性

- **Headless CMS**: 現在ハードコードされている「Collection」の情報を Contentful 等の CMS から取得。
- **Shop API Integration**: BASE API 等を使用して、最新の在庫状況や価格を LP にリアルタイム表示。

詳細は [テスト戦略](./08-テスト戦略.md) を参照してください。
