// 離線快取：App 本體與圖解先存起來，沒網路也能看
const CACHE = "nlp-helper-v1";
const ASSETS = ["./", "index.html", "privacy.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png",
  "img/loop.jpg", "img/ui.jpg", "img/two_ways.jpg", "img/mm2crisp.jpg", "img/upload.jpg", "img/crisp.jpg",
  "img/pipeline.jpg", "img/sentiment.jpg", "img/batch.jpg", "img/rag.jpg", "img/key.jpg", "img/top15.jpg"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS))); self.skipWaiting(); });
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET" || url.origin !== location.origin) return;
  e.respondWith(fetch(e.request).then((r) => { const copy = r.clone(); caches.open(CACHE).then((c) => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request).then((r) => r || caches.match("index.html"))));
});
