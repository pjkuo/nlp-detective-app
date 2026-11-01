# 免費上架平台比較（2026 年 11 月查核）

| 平台 | 費用 | 誰能上架 | 狀態 |
|---|---|---|---|
| **GitHub Releases（首選）** | 免費、無廣告、HTTPS | 任何人；學生不用註冊即可下載 | **已上線**：每版附 APK、離線網頁版、講義、簡報、Colab 範本、QR 海報與 SHA256 檢查碼，固定網址 `releases/latest/download/<檔名>` |
| Obtainium（從 GitHub 自動更新） | 免費、開源 | 不用申請，學生安裝 Obtainium 後一鍵加入 | **已上線**：[obtainium.html](https://pjkuo.github.io/nlp-detective-app/obtainium.html) |
| IzzyOnDroid（F-Droid 相容商店） | 免費 | 開源 App；APK 須正式簽章（不收除錯版）、30 MB 以內、無追蹤 | 資料已備妥，待下面 3 步 |
| F-Droid 官方 | 免費 | 開源 App；由 F-Droid 從原始碼自行建置 | 可行，但 npm 建置流程需另寫配方，耗時較久 |
| Google Play | US$25 一次 | 新個人帳號需 12 人封閉測試 14 天 | 見 PLAY_STORE.md |
| Samsung Galaxy Store | — | 2023 年起只收公司帳號（需 D-U-N-S） | 不適合個人 |
| Amazon Appstore | — | 2025/8/20 起停止支援一般 Android 手機 | 不適合 |

## 上架 IzzyOnDroid：還差 2 步（需你本人）

已完成：MIT 開源授權（LICENSE）。

1. **改用正式簽章**：依 PLAY_STORE.md 第 2 步建立金鑰，在 GitHub Secrets 新增 4 個密鑰。之後每次建置會自動產生正式簽章 APK。
   - 注意：簽章換掉後，手機上舊的除錯版要先移除一次，才能安裝正式版。
2. **送出申請**：到 [IzzyOnDroid 申請頁](https://codeberg.org/IzzyOnDroid/repodata/issues) 開一則 issue，附上 repo 網址 `https://github.com/pjkuo/nlp-detective-app`。

已備妥：fastlane 商店資料（中英文說明、圖示、主題圖、6 張截圖，在 `fastlane/metadata/android/`）、每次建置自動打 tag（v1.0.N）並在 Releases 附 APK。

## 參考
- [IzzyOnDroid App Inclusion Policy](https://izzyondroid.org/docs/general/AppInclusionPolicy/)
- [IzzyOnDroid New app inclusions](https://izzyondroid.org/contributing/NewAppInclusions/)
- [Obtainium](https://github.com/ImranR98/Obtainium)・[Obtainium deep links](https://wiki.obtainium.imranr.dev/deep_links/)
- [Amazon Appstore 公告](https://developer.amazon.com/apps-and-games/blogs/2025/02/upcoming-changes-to-amazon-appstore-for-android-devices-and-coins-program)
- [Samsung Seller Portal 註冊規定討論](https://forum.developer.samsung.com/t/change-to-seller-registration-requirements/22583?page=3)
