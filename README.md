#　token　Checker

`tokens.txt` に入っているDiscordトークンの有効/無効をチェックするシンプルなツールです。

## 仕様
- 画面上にはトークン本体を表示せず、`[VALID]` / `[INVALID]` のステータスのみ出力します（画面共有・配信時の誤流出防止）。
- チェック結果は `valid.txt` と `invalid.txt` に自動で振り分けられて保存されます。

## 使い方
1. `tokens.txt` にチェックしたいトークンを1行ずつ記述します。
2. main.pyを実行します。
3. 実行完了後、同階層に `valid.txt` / `invalid.txt` が生成されます。
