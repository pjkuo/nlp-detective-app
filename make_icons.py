"""Render app icons, splash, Play feature graphic with headless Chrome."""
import asyncio, os
from playwright.async_api import async_playwright

A = "/home/claude/app/"
os.makedirs(A + "resources", exist_ok=True); os.makedirs(A + "play", exist_ok=True); os.makedirs(A + "docs/icons", exist_ok=True)
NAVY, CYAN, AMBER = "#0B2545", "#22A6C7", "#F59E0B"

def glyph(size, scale):
    # magnifier with 字 inside; drawn in a size x size box, content scaled around the centre
    s = scale
    return f"""<g transform='translate({size/2},{size/2}) scale({s}) translate(-512,-512)'>
      <line x1='640' y1='640' x2='810' y2='810' stroke='{CYAN}' stroke-width='110' stroke-linecap='round'/>
      <circle cx='470' cy='470' r='250' fill='#FFFFFF' fill-opacity='0.08' stroke='{AMBER}' stroke-width='64'/>
      <text x='470' y='565' text-anchor='middle' font-family='Noto Sans CJK TC' font-weight='900' font-size='270' fill='#FFFFFF'>字</text>
    </g>"""

def svg(size, bg=True, radius=0, scale=1.0, extra=""):
    rect = f"<rect width='{size}' height='{size}' rx='{radius}' fill='{NAVY}'/>" if bg else ""
    return f"<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}' viewBox='0 0 {size} {size}'>{rect}{glyph(size, scale * size / 1024)}{extra}</svg>"

JOBS = {
    A + "resources/icon-only.png": (1024, svg(1024, True, 0, 0.92)),
    A + "resources/icon-foreground.png": (1024, svg(1024, False, 0, 0.62)),
    A + "resources/icon-background.png": (1024, f"<svg xmlns='http://www.w3.org/2000/svg' width='1024' height='1024'><rect width='1024' height='1024' fill='{NAVY}'/></svg>"),
    A + "resources/splash.png": (2732, svg(2732, True, 0, 0.3)),
    A + "resources/splash-dark.png": (2732, svg(2732, True, 0, 0.3)),
    A + "docs/icons/icon-192.png": (192, svg(192, True, 40, 0.9)),
    A + "docs/icons/icon-512.png": (512, svg(512, True, 108, 0.9)),
    A + "docs/icons/maskable-512.png": (512, svg(512, True, 0, 0.7)),
    A + "play/icon-512.png": (512, svg(512, True, 0, 0.92)),
}
FEATURE = f"""<html><head><meta charset='utf-8'><style>body{{margin:0}} #f{{width:1024px;height:500px;background:{NAVY};display:flex;align-items:center;
font-family:'Noto Sans CJK TC';color:#fff;padding:0 64px;box-sizing:border-box;gap:48px}} h1{{font-size:64px;margin:0;font-weight:900}}
p{{font-size:28px;margin:14px 0 0;color:#CFE9F1}} .k{{display:inline-block;background:{AMBER};color:{NAVY};font-weight:900;border-radius:10px;padding:2px 12px;margin-right:8px;font-size:24px}}</style></head>
<body><div id='f'>{svg(300, False, 0, 1.0)}<div><h1>NLP 實作小幫手</h1><p>用中文指揮 AI 寫程式</p>
<p><span class='k'>Colab</span><span class='k'>Gemini</span><span class='k'>CRISP</span></p><p style='font-size:22px'>8 關實作・提示卡・影片・監督日誌</p></div></div></body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for path, (size, s) in JOBS.items():
            pg = await b.new_page(viewport={"width": size, "height": size})
            await pg.set_content(f"<html><body style='margin:0;background:transparent'>{s}</body></html>")
            await pg.wait_for_timeout(150)
            await pg.locator("svg").screenshot(path=path, omit_background=True)
            await pg.close(); print("ok", os.path.basename(path), size)
        pg = await b.new_page(viewport={"width": 1024, "height": 500})
        await pg.set_content(FEATURE); await pg.wait_for_timeout(200)
        await pg.locator("#f").screenshot(path=A + "play/feature-graphic.png"); print("ok feature")
        await b.close()
asyncio.run(main())
