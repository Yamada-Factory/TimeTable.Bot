# 使い方  
##### はじめに  
作者の都合上，日本語以外でのサーポートは受け付けておりません.  
(We can read Japanese only.)

##### Download  
[ここ](https://github.com/TROMPOT-Project/TimeTable.Bot/releases/download/v1.0/release_v1.zip)でDownload  

## システムについて  

### 概要  
この *LINE_BOT* は学校活動内に存在する課題・行事・時間割変更，そして，日々の時間割を **LINE** を用いて管理するシステムです．課題を登録しておけば前日に通知をし，現在ある課題を確認することができ明日の時間割を時間割変更に対応した状態で知ることができます．ちなみにWebページによる管理も可能．  


## 設置に関して  
---

### Server  
LINE MessageAPIが使えるようにhttps通信のできるServer(Portは自由)を用意してください．また，LINE公式よりLINE botのSDKをダウンロードしてください．

WebControllerを利用する際はbottle.pyが使えるようにしてください．

---
### WebController  
###### はじめに
現段階ではWebControllerはlogin機能がないため，第三者にURLを知られてしまうと改ざんされてしまう可能性があります．十分ご注意ください．

###### Serverの起動
` server.py `の最終行にport指定があります.


### 初期設定  
`setting.py` にて以下のPATHを記述してください  

##### SSL証明書
* certファイル  
* 鍵  
* 中間証明書(option)

##### LINE MassageAPI
* Access token key
* channel select

##### database
* 通常時間割
* イベント
* 課題   
* 時間割変更

##### GroupID(option)
* GroupID

---
### 起動通知，自動通知登録に関して  

##### Systemctl  
LinuxでSystemctlに登録する際に使ってください．  
起動時 : `bash/server_start.sh`  
終了時 : `bash/server_stop.sh`  

##### Crontab
LinuxでCrontabに登録する際 `bash/inform.sh` を使ってください．  
