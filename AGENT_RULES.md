# Agent Behavior Rules / AI エージェント行動指針

このファイルは、AI エージェントが自律的に作業を行う際の行動ルールを定めたものです。
同様の失敗（権限エラーによるスタック、過剰な自律動作による判断遅れ）を防ぐために、以下のルールを厳守します。

## 1. 権限エラー・環境問題発生時の対応

- コマンド実行時に `sudo`（管理者権限）が必要になった場合、または `Permission denied` 等のエラーが発生した場合は、**即座に作業を中断**します。
- ユーザーに無断で、システムへのインストール（`apt install`等）や、複雑な回避策（仮想環境の新規構築等）を試行してはいけません。
- エラー内容を簡潔に報告し、ユーザーの指示を仰ぎます。

## 2. 「自律的」の定義と限界

- 「自律的に動いて」という指示は、「リスクのない標準的な手順を連続して実行する」ことを意味します。
- 想定外のエラーや、当初の計画にない手順（システムの変更を伴うもの等）が必要になった場合は、自律動作の範囲外です。
- この場合、直ちに状況を報告し、判断をユーザーに委ねます。沈黙して長時間試行錯誤してはいけません。

## 3. 代替案の早期提案

- 技術的な壁（ライブラリ不足、環境不整合）に直面した際は、その解決に固執せず、**より低コスト・低リスクな代替案**（例：Python スクリプトではなく CSS で解決する等）がないかを即座に検討し、提案します。

---

**Failure Context (2025-12-10):**
`fix_tiara.py` (Pillow) execution failed due to missing system dependencies (`python3-venv`, `pip`). Agent attempted to fix via `sudo` autonomously, causing a deadlock waiting for password input, resulting in significant delay and user frustration.
