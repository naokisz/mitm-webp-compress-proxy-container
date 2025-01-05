# mitm-webp-compress-proxy-container

通信制限がかかったキャリア回線を少しはマシにするプロキシ

## 注意

* 4G/LTEで使うことを前提とするため、グローバルIPを受け入れる設定になっています
* 忘れずにユーザー名とパスワードを設定してください
* 自分で使うことしか考えていないので、セキュリティ周りは雑です

## 使い方

コンテナのビルド
```bash
docker build . -t mitm-webp-compress-proxy
```

コンテナの起動
```bash
docker compose up -d
```

[輻輳制御アルゴリズム TCP BBR の有効化｜株式会社ネットアシスト](https://www.netassist.ne.jp/techblog/13739/)もしておくと、幸せになれるかもしれないし、なれないかもしれない。

## 参考にしたサイト

  * [mitmproxyでhttps対応Data Compression Proxyを作る #HTTPS - Qiita](https://qiita.com/tongari0/items/ffa3297630547c3bb712)
  * [mitmproxy/release/docker at main · mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy/tree/main/release/docker)
