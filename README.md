# NLP 實作小幫手

「Colab × Gemini 中文 NLP 實作」課程的手機 App：用中文指揮 AI 寫程式，你負責想清楚、按執行、對答案。

## 學生：掃 QR code 就能用

| 1 手機直接用 | 2 下載 Android App | 3 開啟 Colab 筆記本 |
|:---:|:---:|:---:|
| ![App](qr/app.png) | ![APK](qr/apk.png) | ![Colab](qr/colab.png) |
| [開啟網頁版](https://pjkuo.github.io/nlp-detective-app/) | [下載 APK](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/nlp-helper.apk) | [在 Colab 開啟](https://colab.research.google.com/github/pjkuo/nlp-detective-app/blob/main/notebook/nlp_colab_template.ipynb) |
| 用瀏覽器開，選「加到主畫面」 | 第一次安裝要允許不明來源 | 先「儲存副本」再開始 |

**Android 自動更新（免費）**：先安裝 [Obtainium](https://github.com/ImranR98/Obtainium/releases/latest)，再開啟 [一鍵加入頁](https://pjkuo.github.io/nlp-detective-app/obtainium.html)，之後有新版會自動通知。

![Obtainium](qr/obtainium.png)

**全部下載（GitHub Releases，免費、無廣告）**：<https://github.com/pjkuo/nlp-detective-app/releases/latest>

| 檔案 | 內容 | 固定下載網址（永遠是最新版） |
|---|---|---|
| nlp-helper.apk | Android App | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/nlp-helper.apk) |
| nlp-web-offline.zip | 離線網頁版（Windows／Mac／Chromebook，解壓縮後開 index.html） | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/nlp-web-offline.zip) |
| nlp-handout.pdf | 教學講義 | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/nlp-handout.pdf) |
| nlp-slides.pdf | 上課簡報 | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/nlp-slides.pdf) |
| nlp_colab_template.ipynb | Colab 範本筆記本 | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/nlp_colab_template.ipynb) |
| qr-poster-A4.pdf | 教室 QR 海報 | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/qr-poster-A4.pdf) |
| SHA256SUMS.txt | 檔案檢查碼 | [下載](https://github.com/pjkuo/nlp-detective-app/releases/latest/download/SHA256SUMS.txt) |

**安裝 APK**：點下載 → 開啟 nlp-helper.apk → 手機問「允許安裝不明來源的應用程式」時選允許 → 安裝。之後有新版，重新下載安裝即可覆蓋（資料會保留）。

App 裡有：8 個關卡（白話說明、步驟圖解、CRISP 提示卡、小測驗）、拍心智圖與寫 IPO 自動組提示、12 支「看完就動手」的影片、監督日誌。照片和日誌只存在自己的手機。

## 教師：怎麼更新

| 想改什麼 | 改哪裡 | 結果 |
|---|---|---|
| App 內容 | `docs/index.html` | 推送後網頁版立即更新；APK 由 GitHub Actions 自動重建並發布到 Releases |
| 講義、簡報、海報 PDF | `materials/` | 推送後自動發布新版 Release，固定網址不變 |
| Colab 筆記本 | `notebook/nlp_colab_template.ipynb` | Colab 連結自動用最新版 |
| 圖示 | `resources/` 後執行 `npx @capacitor/assets generate --android` | 下次建置套用 |
| 上架 Google Play | 見 [PLAY_STORE.md](PLAY_STORE.md) | 手動產生 AAB 並上傳 |
| 招募 Play 測試同學 | [testers.html](https://pjkuo.github.io/nlp-detective-app/testers.html)、`play/testers-recruit.md` | 學生 3 步加入封閉測試 |
| 免費上架平台 | 見 [STORES.md](STORES.md) | Obtainium 已可用；IzzyOnDroid 資料已備妥 |

**第一次需要的設定**：Settings → Pages → Source 選「Deploy from a branch」、Branch 選 `main`、資料夾選 `/docs`。

## 專案結構

```
docs/          網頁 App（GitHub Pages 與 APK 共用）
notebook/      Colab 範本筆記本
android/       Android 專案（Capacitor 8，targetSdk 36）
resources/     App 圖示與啟動畫面原始檔
materials/     隨 Release 發布的講義、簡報、海報 PDF
play/          Google Play 商店素材、教室用 QR 海報
fastlane/      IzzyOnDroid／F-Droid 商店資料
ci/            固定的除錯簽章（讓 APK 新版能覆蓋舊版）
.github/       自動建置 APK、上架用 AAB
```

課程：郭博仁｜國立屏東科技大學資訊管理系｜影片頻道 [youtube.com/@paulkuo4106](https://www.youtube.com/@paulkuo4106)

授權：[MIT](LICENSE)
