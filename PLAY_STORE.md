# 上架 Google Play：教師操作步驟

在正式上架之前，學生可以先用 **網頁版** 或 **APK 直接安裝**（見 README），不受上架進度影響。

## 目前進度（2026-11-01）

| 項目 | 狀態 |
|---|---|
| App（targetSdk 36）、商店文案、圖示、主題圖、6 張截圖、隱私權政策 | 已備妥 |
| 測試同學招募頁、QR、公告草稿 | 已備妥（`docs/testers.html`、`play/testers-recruit.md`） |
| 申請正式版填答草稿 | 已備妥（`play/production-access.md`） |
| Play Console 開發者帳號 | **尚未建立**（kuo0615@gmail.com 進入 Play Console 時顯示註冊頁） |
| 上傳金鑰（4 個 GitHub Secrets） | **尚未設定** |

## 先知道的規定（2026 年 11 月查核）

| 項目 | 規定 |
|---|---|
| 開發者帳號費用 | 一次性 US$25，需用本人信用卡 |
| 身分驗證 | 政府核發證件；個人帳號另需用 Android 手機安裝 Play Console App 完成裝置驗證 |
| 新個人帳號的測試要求 | 2023/11/13 後建立的個人帳號，要先做「封閉測試」：至少 **12 位測試人員連續 14 天** 保持加入，才能申請正式版 |
| 申請正式版審核 | 通常 7 天內 |
| 目標 API | 新 App 須以 Android 16（API 36）為目標；本專案已是 API 36 |
| 上架格式 | AAB（本專案的 GitHub Actions 會產生） |
| 機構帳號 | 用學校名義可免 12 人測試，但需要 D-U-N-S 編號與學校授權，個人帳號較快 |

**為什麼值得現在就開帳號**：Google 的「開發者驗證」2026/9/30 先在巴西、印尼、新加坡、泰國實施，2027 年擴及全球，屆時連 APK 直接安裝也要求開發者已註冊。Play Console 帳號完成身分驗證後，APK 版之後也能繼續發給學生。

## 時程（約 3～4 週）

| 天數 | 你要做的事 |
|---|---|
| 第 0 天 | 步驟 1～2：開帳號、設定金鑰 |
| 第 1～3 天 | 等身分驗證；步驟 3～5：產生 AAB、建立 App、填資料 |
| 第 3 天 | 步驟 6：上傳封閉測試、發公告招募同學 |
| 第 3～17 天 | 測試 14 天；中間依回饋更新一次 |
| 第 17 天 | 步驟 7：申請正式版 |
| 約第 24 天 | 審核通過，正式上架 |

這些步驟需要你本人的 Google 帳號、付款與身分證件，只能由你在 Play Console 操作。帳號開好後，商店資訊、App 內容、測試群組設定這些填表工作可以交給 Claude 用你的 Chrome 代填（送出前會先問你）。

## 步驟

### 1. 註冊開發者帳號
1. 前往 Play Console（play.google.com/console），帳戶類型選「自己」。
2. 付 US$25，上傳證件完成身分驗證（通常 1～3 天）。
3. 在 Android 手機安裝 Play Console App，完成裝置驗證。

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

**upload.jks 和密碼請自己保管，不要放進 repo。** 弄丟可向 Google 申請重設上傳金鑰（App 簽署金鑰由 Google 保管）。設定後，APK 也會自動改用這把金鑰簽章（IzzyOnDroid 也需要）。

### 3. 產生上架檔（AAB）
GitHub repo → **Actions → 建置 Google Play 上架檔（AAB）→ Run workflow**，輸入版本名稱（例如 1.0.0）。約 5–10 分鐘後，在該次執行頁面下方下載 `nlp-helper-aab-1.0.0`，解壓縮得到 `nlp-helper.aab`。

### 4. 在 Play Console 建立應用程式
名稱「NLP 實作小幫手」、預設語言「中文（台灣）– zh-TW」、類型「應用程式」、「免費」。套件名稱會由第一個上傳的 AAB 決定：`io.github.pjkuo.nlphelper`。

### 5. 填商店資訊與 App 內容
全部文案、圖片和政策填答都在 `play/listing.md`，圖片在 `play/` 資料夾。

### 6. 封閉測試（至少 12 人、連續 14 天）
1. 建立 Google 群組 **nlp-helper-testers**（groups.google.com → 建立群組；「誰可以加入」選「網路上的任何人都能加入」）。若名稱被用走，換個名稱並告訴 Claude 重做 QR。
2. Play Console → 測試 → 封閉測試 → 管理測試群組 → 測試人員選「Google 群組」，填 `nlp-helper-testers@googlegroups.com`；國家/地區選台灣。
3. 上傳 `nlp-helper.aab`，建立版本並送出審查（首次約 1～3 天）。
4. 審查通過後，在 Moodle 發公告（`play/testers-recruit.md`），學生照 https://pjkuo.github.io/nlp-detective-app/testers.html 的 3 步加入。**建議招 20 人**，14 天內不要退出（退出再加入會重新計算）。
5. 測試中段依回饋改一個小地方，重跑步驟 3 上傳新版（申請正式版時會問）。

### 7. 申請正式版
14 天後：資訊主頁 → **申請正式版**，填答草稿在 `play/production-access.md`。審核通過後即可發布。

### 8. 之後要更新
修改 `docs/` → 推送到 GitHub（APK 會自動更新）→ 重跑步驟 3 → 在 Play Console 上傳新的 AAB。

## 參考資料
- [App testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en-GB)
- [Target API level requirements for Google Play apps](https://developer.android.com/google/play/requirements/target-sdk)
- [Register for a Google Play Developer account](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en)
- [Android developer verification](https://support.google.com/android-developer-console/answer/16561738?hl=en)・[What changes on 30 September 2026](https://foresightmobile.com/blog/android-developer-verification-2026)
- [Limited distribution（免費、上限 50 台裝置）](https://developer.android.com/developer-verification/guides/limited-distribution)
