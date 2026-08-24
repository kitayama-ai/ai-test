# WebToolBox デプロイ・収益化ガイド

## 📁 サイト構成

```
/
├── index.html          # トップページ
├── css/
│   └── style.css      # 共通スタイル
├── js/
│   └── common.js      # 共通JavaScript
├── tools/
│   ├── character-counter.html   # 文字数カウンター
│   ├── json-formatter.html      # JSON整形
│   ├── qr-generator.html        # QRコード生成
│   ├── password-generator.html  # パスワード生成
│   ├── color-converter.html     # カラーコード変換
│   ├── image-compressor.html    # 画像圧縮
│   ├── date-calculator.html     # 日付計算
│   └── text-converter.html      # テキスト変換
├── sitemap.xml        # サイトマップ
├── robots.txt         # ロボット設定
├── manifest.json      # PWAマニフェスト
└── ads.txt           # 広告認証
```

## 🚀 デプロイ手順

### 方法1: Vercel（推奨・無料）

1. **GitHubにプッシュ**（すでに完了している場合はスキップ）
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Vercelアカウント作成**
   - https://vercel.com にアクセス
   - GitHubアカウントでサインアップ

3. **プロジェクトをインポート**
   - 「New Project」をクリック
   - GitHubリポジトリを選択
   - 「Deploy」をクリック

4. **カスタムドメイン設定**（オプション）
   - プロジェクト設定 → Domains
   - 購入したドメインを追加

### 方法2: Netlify（無料）

1. https://app.netlify.com にアクセス
2. GitHubアカウントでログイン
3. 「Add new site」→「Import an existing project」
4. GitHubリポジトリを選択
5. 「Deploy site」をクリック

### 方法3: GitHub Pages（無料）

1. リポジトリ設定 → Pages
2. Source: Deploy from a branch
3. Branch: main / root
4. Save

## 💰 収益化設定

### Step 1: Google AdSense申請

1. **申請条件**
   - オリジナルコンテンツがある
   - プライバシーポリシーがある
   - 問い合わせ先がある
   - 一定のアクセスがある（推奨：1日100PV以上）

2. **申請手順**
   - https://www.google.com/adsense にアクセス
   - 「今すぐ開始」をクリック
   - サイトURLを入力
   - 審査を待つ（数日〜数週間）

3. **承認後の設定**
   - AdSenseコードを取得
   - 各HTMLファイルの `<head>` に追加
   - `ads.txt` を更新

### Step 2: 広告コードの設置

承認後、各ページの広告スペース（`ad-container`）を実際の広告コードに置き換え：

```html
<!-- 広告スペース (728x90) を以下に置き換え -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXXXX"
     data-ad-slot="XXXXXXXX"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

### Step 3: アフィリエイト設定

1. **A8.net に登録**（日本最大級）
   - https://www.a8.net
   - 開発ツール、サーバー、ドメイン関連の案件が豊富

2. **関連サービスを紹介**
   - ドメイン取得サービス（お名前.com等）
   - レンタルサーバー（ConoHa等）
   - クラウドサービス（AWS等）

## 📈 SEO対策

### すでに実装済み
- ✅ メタディスクリプション
- ✅ OGPタグ
- ✅ サイトマップ
- ✅ robots.txt
- ✅ 構造化されたURL
- ✅ モバイル対応

### 追加で行うこと
1. **Google Search Console に登録**
   - https://search.google.com/search-console
   - サイトマップを送信

2. **Google Analytics 設置**
   - https://analytics.google.com
   - トラッキングコードを各ページに追加

3. **キーワード最適化**
   - 「○○ ツール 無料」
   - 「○○ オンライン」
   - 「○○ 変換」
   などで検索されることを意識

## 📊 収益目標と予測

### 月10万円達成のシミュレーション

| 指標 | 必要値 |
|------|--------|
| 月間PV | 100,000 PV |
| 広告クリック率(CTR) | 1% |
| クリック単価(CPC) | 100円 |
| **月間収益** | **100,000円** |

### 現実的なステップ
1. **月1-3**: SEO対策、コンテンツ追加 → 1,000〜5,000 PV
2. **月4-6**: SNS活用、被リンク獲得 → 10,000〜30,000 PV
3. **月7-12**: 安定運用、機能追加 → 50,000〜100,000 PV

## 🔧 今後の拡張案

### 追加ツール候補
- Base64エンコード/デコード
- URL短縮
- ハッシュ計算（MD5, SHA256）
- 正規表現テスター
- CSS/HTML圧縮
- ユニットコンバーター
- Lorem Ipsum生成
- Favicon生成

### 収益向上施策
- 有料プラン（広告非表示、API提供）
- ブログ記事追加（使い方解説）
- YouTube動画作成

## ⚠️ 注意事項

1. **AdSense利用規約を遵守**
   - 自己クリック禁止
   - 不正なトラフィック禁止

2. **著作権に注意**
   - 画像や文章は自作またはライセンス確認

3. **定期的なメンテナンス**
   - 壊れた機能の修正
   - 新しいブラウザ対応

---

**作成者**: AI Assistant  
**最終更新**: 2024年
