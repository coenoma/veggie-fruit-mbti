# 野菜・果物でわかるMBTI性格診断テスト

## プロジェクト概要
このアプリケーションは、MBTI性格診断をベースに、ユーザーの性格を野菜や果物で表現する診断テストです。

## セットアップ手順

### 必要条件
- Python 3.8以上
- Node.js 14.0.0以上

### インストール
1. リポジトリのクローン
```bash
git clone [リポジトリURL]
cd [プロジェクトディレクトリ]
```

2. Python依存パッケージのインストール
```bash
pip install -r requirements.txt
```

3. Node.js依存パッケージのインストール
```bash
npm install
```

### 環境変数の設定
```bash
FLASK_SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///mbti.db
```

### 開発サーバーの起動
1. Flaskサーバー
```bash
python main.py
```

2. TailwindCSSビルド
```bash
npm run build-css
```

## プロジェクト構造
```
app/
├── blueprints/      # ルート管理
├── config/          # 設定ファイル
├── models/          # データモデル
├── static/          # 静的ファイル
└── templates/       # テンプレート
```

## 開発ガイドライン

### コーディング規約
- PEP 8準拠
- インデント：4スペース
- 行の最大長：79文字

### コミットメッセージ
- feat: 新機能
- fix: バグ修正
- docs: ドキュメント
- style: フォーマット
- refactor: リファクタリング
- test: テスト関連
- chore: その他
