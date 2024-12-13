# 野菜・果物でわかるMBTI性格診断テスト 🥑 🍎 🍊

## プロジェクト概要
このアプリケーションは、MBTI性格診断をベースに、ユーザーの性格を野菜や果物で表現する診断テストです。個性豊かな野菜や果物のキャラクターを通じて、自己理解を深め、楽しみながら性格特性を発見できます。

## 技術スタック

### バックエンド
- **Flask** (Python 3.11) - 軽量で拡張性の高いWebフレームワーク
- **SQLAlchemy** - Pythonの代表的なORMツール
- **PostgreSQL/SQLite** - データベース（開発環境ではSQLite、本番環境ではPostgreSQL）

### フロントエンド
- **TailwindCSS 3.4** - ユーティリティファーストのCSSフレームワーク
  - レスポンシブデザイン
  - カスタマイズ可能なコンポーネント
  - 最適化されたビルド
- **PostCSS** - モダンなCSSツール
  - 自動プレフィックス
  - CSSモジュール
  - 最適化
- **JavaScript (Vanilla)** - クライアントサイドの機能実装
  - アニメーション制御
  - フォーム検証
  - 非同期通信

### ビルドツール
- **Node.js 20** - TailwindCSSのビルド環境
- **PostCSS CLI** - CSSのビルドツール

### その他のコンポーネント
- **Jinja2** - Pythonの強力なテンプレートエンジン
- **Werkzeug** - WSGIユーティリティライブラリ

## アーキテクチャ

### 設計方針
- **ブループリントパターン** - モジュール性と保守性を重視
- **MVCライクな構造**
  - Models: データモデルとビジネスロジック
  - Views (Templates): Jinja2テンプレート
  - Controllers (Routes): リクエスト処理とルーティング
- **環境別設定管理**
  - development.py: 開発環境設定
  - production.py: 本番環境設定

## セットアップ手順

### システム要件
- Python 3.11以上
- Node.js 20.0.0以上
- npm 9.0.0以上

### 開発環境のセットアップ
1. リポジトリのクローン
```bash
git clone [リポジトリURL]
cd [プロジェクトディレクトリ]
```

2. Python仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows
```

3. 依存パッケージのインストール
```bash
# Pythonパッケージ
pip install -r requirements.txt

# Node.jsパッケージ
npm install
```

### 環境変数の設定
`.env`ファイルを作成し、以下の環境変数を設定:
```bash
FLASK_SECRET_KEY=your-secret-key           # セッション暗号化キー
DATABASE_URL=sqlite:///mbti.db             # 開発用DB
FLASK_ENV=development                      # 環境設定
```

### 開発サーバーの起動
1. データベースの初期化
```bash
flask db upgrade
```

2. Flaskサーバーの起動
```bash
python main.py
```

3. TailwindCSSの開発ビルド
```bash
# ビルドの実行
npm run build-css

# 開発時の監視モード
npm run watch-css
```

## プロジェクト構造
```
app/
├── blueprints/          # 機能別ルート管理
│   ├── quiz/           # 診断テスト機能
│   └── result/         # 結果表示機能
├── config/             # 環境別設定
│   ├── development.py
│   └── production.py
├── models/             # データモデル
├── static/             # 静的ファイル
│   ├── css/           # スタイルシート
│   ├── js/            # JavaScriptファイル
│   └── images/        # 画像ファイル
└── templates/          # テンプレート
    ├── layouts/       # 基本レイアウト
    └── components/    # 再利用可能なコンポーネント
```

## 開発ガイドライン

### コーディング規約
- PEP 8準拠のPythonコード
- ESLint/Prettierに準拠したJavaScript
- コンポーネントベースのCSS設計

### コミットメッセージ
- feat: 新機能
- fix: バグ修正
- docs: ドキュメント
- style: フォーマット
- refactor: リファクタリング
- test: テスト関連
- chore: その他

## ライセンス
Copyright © 2024 Coenoma LLC. All rights reserved.
