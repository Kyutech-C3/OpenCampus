# OpenCampus 2020

## tl;dr
弊部員のオープンキャンパス向け作品を公開するためのWebサイト

## 開発
**担当チームに分けて，GithubのIssueを用いて相談しつつ開発．**  
**毎週木曜18:00から，Discordのボイスチャットにて集会をしましょう**  
ほか，チームの垣根を超えた相談や質問は，Discordのテキストチャットにてどうぞ．  

それぞれのチームのブランチを切って開発．  
暫定版は`develop`ブランチにマージし，
安定版は`master`ブランチにマージします．

## 担当チーム
* embedding_\*チームの皆さんは自分のチームの実装が終わったらentire_designチーム（上回生の場合はserverチームの場合もあります）を手伝ってあげてね

### entire_design
**サイト全体のデザイン，実装を担当**

とりあえずデザインを紙に起こしてみて，みんなで相談しましょう．  
[FlexBox](https://www.webcreatorbox.com/tech/css-flexbox-cheat-sheet#flexbox14)を使うと簡単にレスポンシブデザインができる（はず．たしか．）のでおすすめ  
というか可能ならば[Bulma](https://bulma.io/)などのCSSフレームワークを使うのもおすすめ

### embedding_unity
**Unityのゲームをサイトに埋め込む部分の実装を担当**  

Unityは標準でWeb（HTML）書き出し機能が有りますが，1ページ分のHTMLが出てくる感じなので，これをサイトの一部として埋め込める形にする

### embedding_video
**動画をサイトに埋め込む部分の実装を担当**  

[Video.js](https://videojs.com/)あたりのモジュールを使って，Web上で動画を埋め込めるように，かつ動画プレイヤーの見た目のデザインをする

### embedding_3D
**3Dモデルをサイトに埋め込む部分の実装を担当**

[Sketchfab](https://help.sketchfab.com/hc/en-us/articles/203509907-Embedding-your-models)らへんを使うことになると思われる．割とウェイト低め

### server
**サーバーの実装，コメントのバックエンドとフロントエンドの実装を担当．**  

PostgreSQL上に作品データとコメントをストアして，みんなの作ってくれたモジュールをテンプレートとして利用するFlask or Djangoのサーバーを実装する．コメントのフロントエンドも実装．

## Contributers
## LICENCE
