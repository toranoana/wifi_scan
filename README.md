# このソースについて

- 技術書典7にて頒布した虎の穴ラボの薄い本vol.3にて掲載した記事「店舗の顧客動向を知りたいfeat. AWS」にて紹介したソースコードのサンプルです。  
- Probe Requestパケットを収集するしてAWS IoTにデータを送信するツールになります。  


# 使い方

## 使用するときは以下の事前準備を行ってください。
- scapyのライブラリをインストール  
- 無線子機をモニタモードにする。（インターフェイス名によってaws_wifi_collection.pyのiface="wlan0"部分を変更する）  
- AWS IoTの設定を行い、認証鍵の設置と送信先URLと鍵のパス(aws_iot.py)を変更する  
- python3で実行。（作者は3.7.1で動作確認）  

## 使用方法
- python ./aws_wifi_collection.pyで実行
- コンソール上にMACアドレスなどと"Connected to AWS IoT"が表示できれば動作している
