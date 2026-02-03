# AIエージェントに高品質なLPを作らせる戦略ガイド

## 問題の本質分析

### なぜ従来の方法がうまくいかないのか

1. **抽象的な指示の限界**: 「良いデザイン」「プロっぽく」という指示は、AIにとって解釈の余地が大きすぎる
2. **画像参照の限界**: スクリーンショットからは以下が読み取れない
   - 微妙なスペーシング（8pxと12pxの違い等）
   - ホバー/アクティブ状態のトランジション
   - レスポンシブの挙動
   - カスタムアニメーション
3. **イテレーションの罠**: 40点のものを改善しても、根本的な構造（HTML/CSSの設計）に問題があると限界がある

### 核心的な洞察

> **「参考LPのコーディングが把握できればかなり高水準で踏襲して作れる」**

これが最重要ポイント。AIは「コード→コード」の変換が得意。「イメージ→コード」や「抽象的指示→コード」は苦手。

---

## 戦略1: コンポーネントライブラリ活用法（最も実用的）

### 使用するオープンソースリソース

| ライブラリ | 特徴 | GitHub Stars | URL |
|-----------|------|-------------|-----|
| shadcn-landing-page | LPに必要な全セクション | 1,850+ | github.com/leoMirandaa/shadcn-landing-page |
| Magic UI | 高品質アニメーションコンポーネント | 10,000+ | magicui.design |
| Aceternity UI | 印象的なアニメーション効果 | - | ui.aceternity.com |
| page-ui | コピペで使えるLPキット | 1,600+ | github.com/danmindru/page-ui |

### 実践方法

**ステップ1: コンポーネントコードを取得**

```bash
# 例: shadcn-landing-pageのHeroコンポーネント
curl -s "https://raw.githubusercontent.com/leoMirandaa/shadcn-landing-page/main/src/components/Hero.tsx"
```

**ステップ2: AIに「このコードをベースに改変」と指示**

```
以下のHeroコンポーネントのコードをベースに、
[あなたのサービス名]のLPのHeroセクションを作成してください。

- タイトルは「○○」
- サブタイトルは「○○」
- CTAボタンのテキストは「○○」
- グラデーションカラーは #○○ から #○○
- 右側のカード部分は[製品スクリーンショット]に置き換え

ベースコード:
[ここにコードを貼り付け]
```

### 利用可能なコンポーネント一覧

shadcn-landing-pageから取得できるセクション：
- `Hero.tsx` - ヒーローセクション
- `Features.tsx` - 機能紹介
- `Pricing.tsx` - 料金プラン
- `Testimonials.tsx` - お客様の声
- `FAQ.tsx` - よくある質問
- `CTA.tsx` - コールトゥアクション
- `Footer.tsx` - フッター
- `Navbar.tsx` - ナビゲーション

---

## 戦略2: デザインシステム先行型アプローチ

### 概要

LPを作る前に、厳密なデザインシステムを定義してAIに渡す。

### デザインシステム定義テンプレート

```json
{
  "colors": {
    "primary": "#6366f1",
    "primaryGradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "background": "#ffffff",
    "backgroundSubtle": "#f8fafc",
    "text": "#1e293b",
    "textMuted": "#64748b",
    "border": "#e2e8f0",
    "success": "#22c55e",
    "accent": "#f59e0b"
  },
  "typography": {
    "fontFamily": "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    "h1": { "size": "4rem", "weight": "800", "lineHeight": "1.1", "letterSpacing": "-0.02em" },
    "h2": { "size": "2.5rem", "weight": "700", "lineHeight": "1.2", "letterSpacing": "-0.01em" },
    "h3": { "size": "1.5rem", "weight": "600", "lineHeight": "1.3" },
    "body": { "size": "1.125rem", "weight": "400", "lineHeight": "1.7" },
    "small": { "size": "0.875rem", "weight": "400", "lineHeight": "1.5" }
  },
  "spacing": {
    "sectionPadding": "6rem 0",
    "containerMaxWidth": "1200px",
    "componentGap": "2rem",
    "cardPadding": "2rem",
    "buttonPadding": "0.875rem 2rem"
  },
  "effects": {
    "borderRadius": {
      "small": "0.5rem",
      "medium": "1rem",
      "large": "1.5rem",
      "full": "9999px"
    },
    "shadows": {
      "card": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
      "cardHover": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)",
      "button": "0 4px 14px 0 rgba(99, 102, 241, 0.4)"
    },
    "transitions": {
      "default": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
      "fast": "all 0.15s ease",
      "slow": "all 0.5s ease"
    }
  },
  "animations": {
    "fadeInUp": {
      "from": { "opacity": 0, "transform": "translateY(20px)" },
      "to": { "opacity": 1, "transform": "translateY(0)" }
    },
    "shimmer": "背景グラデーションの横移動アニメーション"
  }
}
```

### AIへの指示方法

```
以下のデザインシステムを厳密に守ってLPを作成してください。
値は一切変更せず、このシステムの値のみを使用してください。

[デザインシステムJSONを貼り付け]

作成するセクション:
1. Hero - キャッチコピー「○○」、サブコピー「○○」
2. Features - 3カラム、各機能の説明
...
```

---

## 戦略3: 高品質コードの抽出テクニック

### 方法A: 開発者ツールによる抽出

```javascript
// ブラウザのコンソールで実行
// 特定のセクションのHTMLとCSSを抽出

function extractSection(selector) {
  const element = document.querySelector(selector);
  if (!element) return null;
  
  // HTMLを取得
  const html = element.outerHTML;
  
  // 適用されているCSSを取得
  const styles = [];
  const allElements = element.querySelectorAll('*');
  allElements.forEach(el => {
    const computed = getComputedStyle(el);
    // 重要なスタイルプロパティを抽出
    styles.push({
      selector: el.tagName.toLowerCase() + (el.className ? '.' + el.className.split(' ').join('.') : ''),
      styles: {
        display: computed.display,
        flexDirection: computed.flexDirection,
        gap: computed.gap,
        padding: computed.padding,
        margin: computed.margin,
        fontSize: computed.fontSize,
        fontWeight: computed.fontWeight,
        color: computed.color,
        background: computed.background,
        borderRadius: computed.borderRadius,
        boxShadow: computed.boxShadow
      }
    });
  });
  
  return { html, styles };
}

// 使用例
console.log(JSON.stringify(extractSection('.hero-section'), null, 2));
```

### 方法B: Wappalyzer + 技術スタック特定

多くの高品質LPは以下の技術を使用：
- Tailwind CSS → クラス名からスタイルを推測可能
- Framer Motion → アニメーションライブラリ
- shadcn/ui → コンポーネントパターンが決まっている

技術スタックが特定できれば、同じライブラリを使って再現可能。

### 方法C: view-source + 整形

```bash
# HTMLを取得してフォーマット
curl -s "https://example-landing-page.com" | npx prettier --parser html
```

---

## 戦略4: 段階的構築法（ボトムアップ）

### 概要

LP全体を一度に作らせるのではなく、コンポーネント単位で高品質に仕上げてから組み合わせる。

### 実践フロー

```
Phase 1: 基盤構築
├── デザイントークン定義（カラー、タイポグラフィ、スペーシング）
├── CSSリセット/ベーススタイル
└── コンテナ/グリッドシステム

Phase 2: 原子コンポーネント
├── ボタン（プライマリ、セカンダリ、ゴースト）
├── テキストスタイル
├── カード
└── バッジ/タグ

Phase 3: セクションコンポーネント（各々を高品質に）
├── Hero（参考コード付きで依頼）
├── Features（参考コード付きで依頼）
├── Testimonials（参考コード付きで依頼）
└── ...

Phase 4: 組み合わせ + 調整
└── 全セクションを結合してLP完成
```

### 各フェーズでの指示例

**Phase 2: ボタンコンポーネント作成時**

```
以下のボタンスタイルを参考に、3種類のボタンを作成してください。

参考コード（Magic UIのShimmer Button）:
[shimmer-buttonのコードを貼り付け]

作成するバリエーション:
1. Primary - シマーエフェクト付き、背景色 #6366f1
2. Secondary - アウトラインスタイル、ホバーで塗りつぶし
3. Ghost - 背景なし、ホバーで薄い背景

必須要件:
- ホバー時にtransform: translateY(-2px)
- アクティブ時にscale(0.98)
- transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)
```

---

## 戦略5: ハイブリッドアプローチ（最も確実）

### 概要

既存の高品質テンプレートを**そのまま使用**し、AIにはカスタマイズ部分のみを担当させる。

### 推奨テンプレート

1. **SaaS Boilerplate** (ixartz/SaaS-Boilerplate)
   - Next.js + Tailwind + shadcn/ui
   - 完成度の高いLPが含まれる
   - MIT License

2. **shadcn-landing-page** (leoMirandaa/shadcn-landing-page)
   - React + Vite + Tailwind
   - シンプルで改変しやすい

### 実践方法

```bash
# テンプレートをクローン
git clone https://github.com/leoMirandaa/shadcn-landing-page.git my-lp

# 依存関係インストール
cd my-lp && npm install
```

AIへの指示：
```
このプロジェクトの src/components/Hero.tsx を編集して、
以下の内容に変更してください。

変更点:
1. タイトルを「○○」に変更
2. サブタイトルを「○○」に変更
3. グラデーションカラーを #○○ → #○○ に変更
4. 右側のカードセクションを削除し、代わりに製品のモックアップ画像を配置

元のコードの構造やアニメーション、スペーシングは維持してください。
```

---

## 戦略6: Cursorでの実践ワークフロー

### Cursor Agent用の最適化プロンプト

```markdown
## 役割
あなたは10年以上の経験を持つフロントエンドデベロッパー兼UIデザイナーです。
Stripe、Linear、Vercelレベルの高品質なLPを作成できます。

## 制約
1. 以下のデザインシステムを厳密に守ること
2. アニメーションには必ずcubic-bezier(0.4, 0, 0.2, 1)を使用
3. スペーシングは8の倍数（8px, 16px, 24px, 32px...）のみ使用
4. 色はデザインシステムで定義された値のみ使用

## 参考コード
以下のコードパターンを踏襲してください:
[ここに高品質なコンポーネントコードを貼り付け]

## 作成するもの
[具体的な要件を記述]
```

### ファイル構成の指定

```
プロジェクト構成:
/
├── index.html
├── styles/
│   ├── reset.css       # CSSリセット
│   ├── tokens.css      # デザイントークン（CSS変数）
│   └── components.css  # コンポーネントスタイル
└── scripts/
    └── animations.js   # アニメーション制御
```

---

## 実際に使えるコードテンプレート集

### 1. 高品質ヒーローセクション（即使用可能）

```html
<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">
      <span class="badge-dot"></span>
      <span>新機能リリース</span>
    </div>
    <h1 class="hero-title">
      <span class="gradient-text">次世代の</span>
      プロダクト管理
    </h1>
    <p class="hero-subtitle">
      チームのコラボレーションを加速し、
      プロジェクトを成功に導くオールインワンプラットフォーム
    </p>
    <div class="hero-cta">
      <button class="btn-primary">
        <span>無料で始める</span>
        <svg><!-- arrow icon --></svg>
      </button>
      <button class="btn-secondary">デモを見る</button>
    </div>
  </div>
  <div class="hero-visual">
    <!-- 製品スクリーンショットまたはアニメーション -->
  </div>
</section>

<style>
.hero {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  padding: 6rem 4rem;
  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(99, 102, 241, 0.1);
  border-radius: 9999px;
  font-size: 0.875rem;
  color: #6366f1;
  margin-bottom: 1.5rem;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: #1e293b;
  margin-bottom: 1.5rem;
}

.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #64748b;
  line-height: 1.7;
  max-width: 500px;
  margin-bottom: 2rem;
}

.hero-cta {
  display: flex;
  gap: 1rem;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.4);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.5);
}

.btn-secondary {
  padding: 1rem 2rem;
  background: transparent;
  color: #1e293b;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-secondary:hover {
  border-color: #6366f1;
  color: #6366f1;
}

.hero-visual {
  position: relative;
}

.hero-visual img {
  width: 100%;
  border-radius: 16px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
    padding: 4rem 2rem;
  }
  
  .hero-subtitle {
    margin-left: auto;
    margin-right: auto;
  }
  
  .hero-cta {
    justify-content: center;
  }
}
</style>
```

### 2. 高品質フィーチャーセクション

```html
<section class="features">
  <div class="features-header">
    <span class="section-label">機能</span>
    <h2 class="section-title">
      すべてが<span class="gradient-text">ひとつに</span>
    </h2>
    <p class="section-subtitle">
      プロジェクト管理に必要な機能をすべて搭載
    </p>
  </div>
  
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-icon">
        <svg><!-- icon --></svg>
      </div>
      <h3>リアルタイムコラボレーション</h3>
      <p>チームメンバーと同時編集。変更は即座に反映されます。</p>
    </div>
    <!-- 他のカード -->
  </div>
</section>

<style>
.features {
  padding: 8rem 4rem;
  background: #ffffff;
}

.features-header {
  text-align: center;
  max-width: 600px;
  margin: 0 auto 4rem;
}

.section-label {
  display: inline-block;
  padding: 0.375rem 1rem;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #6366f1;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
}

.section-subtitle {
  font-size: 1.125rem;
  color: #64748b;
  line-height: 1.7;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  padding: 2rem;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
  border-color: transparent;
}

.feature-icon {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.feature-icon svg {
  width: 24px;
  height: 24px;
  color: white;
}

.feature-card h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.feature-card p {
  font-size: 1rem;
  color: #64748b;
  line-height: 1.6;
}

@media (max-width: 1024px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .features {
    padding: 4rem 1.5rem;
  }
}
</style>
```

---

## まとめ: 推奨ワークフロー

### 最も成功率が高いアプローチ

1. **オープンソーステンプレートをベースにする**
   - shadcn-landing-page または SaaS-Boilerplate をクローン
   - 既に高品質なコードがあるため、AIは改変のみ担当

2. **コンポーネント単位で作業**
   - 一度にLP全体を作らせない
   - Hero → Features → Pricing の順に、各々完成させてから次へ

3. **参考コードを必ず添付**
   - 「このコードをベースに」と明示
   - Magic UIやshadcn-landing-pageからコードを取得して渡す

4. **デザインシステムを事前定義**
   - カラー、スペーシング、アニメーションのルールを厳密に指定
   - AIの裁量を減らすことで品質が安定

5. **テストしながら反復**
   - 各コンポーネント完成後にブラウザで確認
   - 問題があれば具体的に指摘して修正

### 避けるべきこと

- 「良い感じに作って」という抽象的な指示
- LP全体を一度に作らせる
- 参考画像だけを渡す（コードを渡す）
- 40点のものを延々とブラッシュアップ

---

## 付録: 高品質LPで使われる具体的なCSSテクニック

### 1. 洗練されたシャドウシステム

```css
/* 階層的なシャドウ（Tailwindスタイル） */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);

/* プライマリカラーのグロウシャドウ */
--shadow-primary: 0 4px 14px 0 rgba(99, 102, 241, 0.4);
```

### 2. プロレベルのトランジション

```css
/* cubic-bezierでイージングを指定（絶対に linear や ease を使わない） */
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);

/* ホバー時の微妙な浮遊感 */
.card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}

/* クリック時のフィードバック */
.btn:active {
    transform: translateY(0) scale(0.98);
}
```

### 3. グラデーションテキスト

```css
.gradient-text {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

### 4. ガラスモーフィズム（モダンなナビバー）

```css
.navbar {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}
```

### 5. 微妙なアニメーション

```css
/* パルスアニメーション（バッジのドット等） */
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(0.9); }
}

/* フロートアニメーション（フローティングカード） */
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
```

### 6. 8pxグリッドシステム

```css
/* スペーシングは常に8の倍数 */
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
```

---

## 最終結論

**AIに高品質なLPを作らせる最も確実な方法は、「コードで指示する」こと。**

1. オープンソースの高品質テンプレート（shadcn-landing-page等）をクローン
2. 各コンポーネントのコードをAIに渡して「これをベースにカスタマイズ」と指示
3. デザインシステム（カラー、スペーシング、アニメーション）を厳密に定義

これにより、AIの「解釈の余地」を最小化し、確実に高品質なアウトプットを得られる。
