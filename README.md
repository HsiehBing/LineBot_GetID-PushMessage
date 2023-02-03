## 描述: <br> 此repo是在Linux系統下以FLASK執行LineBot以取得UserID或GroupID，再進一步發送訊息至用戶
### 運作條件
* 以申請完LINE BOT 並取得access token 以及 Channel Secret
* 已經安裝完 nginx 並取得https憑證  
* 使用前須要先輸入 access token 以及 Channel Secret

###操作指南
* 先在getID.py以及app.py中輸入access token 以及 Channel Secret
* 在linux系統中輸入
```
./start_gI.sh 
```
或 
```
sh start_gI.sh 
```
* 執行後可以由error.log中得到UserID或GroupID
* 將UserID或GroupID輸入app.py後再執行start.sh
```
./start.sh
```
*此處預設port為8070*
* 執行後訪問，系統就會自動發送訊息到指定的用戶或群組
```
curl localhost:8070/pum
```
*一般用戶一個月最多500則*
## 參考資料
* 簡易LINE BOT 架設 \
  https://www.youtube.com/watch?v=i8ncIcJs-LA
  *注意heroku已經不能使用，其他影片有提及其他方法，本案例是以EC2架設*
* NGINX\
  https://jeffwen0105.com/1759-2/
* http 取得可以由 no-ip申請短暫免費http網址，在由letsencrypt取得憑證，下方連結有提供教學\
  https://certbot.eff.org/
  

* 主動發送訊息 \
  https://steam.oxxostudio.tw/category/python/example/line-push-message.html
##更新資訊
2023/2/4 首次上傳


