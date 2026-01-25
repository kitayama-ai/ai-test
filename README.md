# AI Agency System: Startup Guide

## 1. ターゲット抽出・分析ツール (Sales)
**実行方法:**
```bash
python3 research_tool/run_research.py
```
- `research_tool/target_urls.txt` に調査したいURLリストを記入してください。
- `research_tool/leads.csv` に分析結果（スコア・提案戦略）が出力されます。

## 2. エルメ連携AIバックエンド (Operations)
**実行方法:**
```bash
uvicorn backend.main:app --reload
```
- `http://localhost:8000/webhook` がエルメからのWebhook受け皿になります。
- 現在はシミュレーションモードで動作します。

## 3. 管理ダッシュボード (Management)
**実行方法:**
```bash
streamlit run dashboard/app.py
```
- ブラウザで「営業リスト」と「AI対応ログ」を一元管理できます。

---
**ディレクトリ構成:**
- `/research_tool`: スクレイピング・分析ロジック
- `/backend`: FastAPIアプリケーション、DB定義
- `/dashboard`: Streamlitアプリケーション
