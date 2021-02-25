# Tradovate 自動註冊器
## 目的
想使用 tradovate 免費帳號進行操作練習時，每兩個星期必須更換一次帳號。
本應用優化了註冊流程，僅須一次紀錄關鍵訊息，之後便是一鍵註冊後到自己的郵箱收信。
## 原理
建議登錄自己的 gmail 信箱。本程式會自動添加後綴來建立信箱別名。
每次執行時會自動添加不同的後綴讓系統辨識為不同信箱，但我們皆可以在單一信箱收信。
帳號名稱也會依照計數器自動添加
## 環境
windows + python
## 使用
### 執行程序
1. 雙擊 activate.bat 執行
### 設定 config
1. 點擊 config
![](https://i.imgur.com/wLvLgNc.png)
2. 輸入基本資料
![](https://i.imgur.com/vomhUko.png)
   * Email: 建議填入 gmail，或體確認該信箱適用'+'建立別名
   * User Name: 為避免撞名，請物過短或用單詞。未來會用此名稱+序號作為登陸帳號
   * Password: 這邊如果沒有特別修改，未來建立的帳會會使用同一個密碼
   * Counter: 不需要更改，該值會自動跳號
3. 按下 Save Config

### 執行
1. 點擊 Run Automator
![](https://i.imgur.com/wLvLgNc.png)
2. 程式會在執行完後自動關閉瀏覽器
3. 關閉程式，到自己的信箱收信確認
4. 此時剪貼簿內會記錄「方才建立的帳號」
   或這你可以到應用程式資料夾內「last_account_info.txt」尋找方才建立的帳戶資訊
5. 未來，直接重複執行 Run Automator 即可建立另一個帳號，同樣收信確認後即激活