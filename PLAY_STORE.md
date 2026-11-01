# 上架 Google Play：教師操作步驟

在正式上架之前，學生可以先用 **網頁版** 或 **APK 直接安裝**（見 README），不受上架進度影響。

## 先知道的規定（2026 年 11 月查核）

| 項目 | 規定 |
|---|---|
| 開發者帳號費用 | 一次性 US$25，需用本人信用卡 |
| 身分驗證 | 可能要求政府核發證件；個人帳號另需用 Android 手機完成裝置驗證 |
| 新個人帳號的測試要求 | 2023/11/13 後建立的個人帳號，要先做「封閉測試」：至少 **12 位測試人員連續 14 天** 保持加入，才能申請正式版 |
| 申請正式版審核 | 通常 7 天內 |
| 目標 API | 新 App 須以 Android 16（API 36）為目標；本專案已是 API 36 |
| 上架格式 | AAB（本專案的 GitHub Actions 會產生） |

這些步驟需要你本人的 Google 帳號、付款與身分證件，只能由你在 Play Console 操作。

## 步驟

### 1. 註冊開發者帳號
1. 前往 Play Console（play.google.com/console），選「個人」帳號。
2. 付 US$25，完成身分驗證。
3. 在手機安裝 Play Console App，完成裝置驗證。

### 2. 建立上傳金鑰，存進 GitHub
在自己的電腦（已安裝 Java）執行：

```bash
keytool -genkeypair -v -keystore upload.jks -alias upload -keyalg RSA -keysize 2048 -validity 10000
base64 -w0 upload.jks > upload.b64        # Windows：certutil -encode upload.jks upload.b64（再刪掉頭尾兩行）
```

到 GitHub repo：**Settings → Secrets and variables → Actions → New repository secret**，新增 4 個：

| 名稱 | 內容 |
|---|---|
| KEYSTORE_BASE64 | upload.b64 的全部內容 |
| KEYSTORE_PASSWORD | 建立金鑰時設的密碼 |
| KEY_ALIAS | upload |
| KEY_PASSWORD | 金鑰密碼（沒另外設就跟上面相同） |

**upload.jks 和密碼請自己保管，不要放進 repo。** 弄丟可向 Google 申請重設上傳金鑰（App 簽署金鑰由 Google 保管）。

### 3. 產生上架檔（AAB）
GitHub repo → **Actions → 建置 Google Play 上架檔（AAB）→ Run workflow**，輸入版本名稱（例如 1.0.0）。約 5–10 分鐘後，在該次執行頁面下方下載 `nlp-helper-aab-1.0.0`，解壓縮得到 `nlp-helper.aab`。

### 4. 在 Play Console 建立應用程式
名稱「NLP 實作小幫手」、預設語言「中文（台灣）」、類型「應用程式」、「免費」。

### 5. 填商店資訊與 App 內容
全部文案、圖片和政策填答都在 `play/listing.md`，圖片在 `play/` 資料夾。

### 6. 封閉測試（至少 12 人、連續 14 天）
1. 測試 → 封閉測試 → 建立測試群組（可用 Google 群組或電子郵件清單）。
2. 上傳 `nlp-helper.aab`，建立版本並送出審核。
3. 把測試連結給至少 12 位學生或助教，請他們加入並安裝，**14 天內不要退出**（退出再加入會重新計算）。

### 7. 申請正式版
14 天後：資訊主頁 → **申請正式版**，填寫「封閉測試」「App 或遊戲」「正式版準備狀況」三部分。審核通過後即可發布。

### 8. 之後要更新
修改 `docs/` → 推送到 GitHub（APK 會自動更新）→ 重跑步驟 3 → 在 Play Console 上傳新的 AAB。

## 參考資料
- [App testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)
- [Target API level requirements for Google Play apps](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en-GB)
- [Register for a Google Play Developer account](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en)
