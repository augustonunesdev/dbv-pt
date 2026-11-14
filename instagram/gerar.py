"""Gera os carrosséis do Instagram em PNG (1080x1350) a partir de posts.py.

Uso:  python -I instagram/gerar.py
Precisa do Google Chrome instalado. As insígnias e a área de cada especialidade vêm da DBV Wiki
(guardadas em instagram/_fonte/ na primeira execução).
"""
import html
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from posts import POSTS  # noqa: E402

WIKI = "https://wiki.dbv.pt"
FONTE = ROOT / "_fonte"
SAIDA = ROOT / "carrosseis"
LOGO = ROOT.parent / "site" / "assets" / "logo-dbv-forge.svg"
CHROME = next((p for p in [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
] if p.exists()), None) or shutil.which("google-chrome") or shutil.which("chrome")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&display=block');
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 1080px; height: 1350px; }
body {
  font-family: 'Montserrat', sans-serif; color: #12333a; overflow: hidden; position: relative;
  background: radial-gradient(900px 600px at 80% -120px, rgba(244,110,46,.20), transparent 70%), #fbf8f4;
}
.slide { position: absolute; inset: 0; padding: 96px 90px 150px; display: flex; flex-direction: column; }
.kicker { font-weight: 700; font-size: 28px; letter-spacing: .14em; text-transform: uppercase; color: #f46e2c; }
h1 { font-weight: 800; font-size: 104px; line-height: 1.02; color: #145660; letter-spacing: -.02em; }
h2 { font-weight: 800; font-size: 66px; line-height: 1.08; color: #145660; margin: 18px 0 48px; letter-spacing: -.01em; }
b, strong { color: #145660; font-weight: 800; }
em { font-style: italic; }
.footer {
  position: absolute; left: 90px; right: 90px; bottom: 56px; display: flex; align-items: center;
  justify-content: space-between; font-weight: 700; font-size: 28px; color: #145660;
}
.footer .brand { display: flex; align-items: center; gap: 14px; }
.footer img { height: 56px; }
.footer .page { color: #8a9799; font-weight: 600; }

/* capa */
.cover { align-items: center; text-align: center; justify-content: center; padding-top: 60px; }
.cover .badge { width: 430px; height: 430px; object-fit: contain; margin: 10px 0 40px;
  filter: drop-shadow(0 18px 40px rgba(20,86,96,.25)); }
.cover .meta { margin-top: 26px; font-size: 32px; font-weight: 600; color: #5d6b6e; }
.cover .hook { margin-top: 40px; font-size: 40px; font-weight: 700; color: #12333a; max-width: 820px; line-height: 1.25; }
.cover .swipe { margin-top: 46px; display: inline-block; background: #145660; color: #fff; font-weight: 800;
  font-size: 32px; padding: 20px 40px; border-radius: 999px; }

/* listas */
ul.list { list-style: none; display: flex; flex-direction: column; gap: 30px; }
ul.list li { font-size: 42px; line-height: 1.32; font-weight: 500; padding-left: 58px; position: relative; }
ul.list li::before { content: ''; position: absolute; left: 0; top: 18px; width: 24px; height: 24px;
  border-radius: 50%; background: #f46e2c; }
ol.steps { list-style: none; counter-reset: s; display: flex; flex-direction: column; gap: 40px; }
ol.steps li { counter-increment: s; font-size: 44px; line-height: 1.3; font-weight: 500; padding-left: 110px; position: relative; min-height: 80px; }
ol.steps li::before { content: counter(s); position: absolute; left: 0; top: -4px; width: 80px; height: 80px;
  border-radius: 50%; background: #f46e2c; color: #fff; font-weight: 800; font-size: 44px;
  display: grid; place-items: center; }
.pairs { display: flex; flex-direction: column; gap: 26px; }
.pair { background: #fff; border: 2px solid #e6ddd2; border-radius: 28px; padding: 30px 36px; }
.pair .t { font-weight: 800; font-size: 40px; color: #f46e2c; margin-bottom: 6px; }
.pair .d { font-size: 36px; line-height: 1.32; font-weight: 500; }
.nums { display: flex; flex-direction: column; gap: 34px; }
.num { background: #145660; color: #fff; border-radius: 30px; padding: 34px 44px; }
.num .n { font-weight: 800; font-size: 76px; line-height: 1.05; color: #f9a65a; }
.num .d { font-size: 38px; font-weight: 600; margin-top: 4px; }

/* final */
.end { align-items: center; justify-content: center; text-align: center; padding-top: 40px; }
.end .logo { width: 300px; margin-bottom: 50px; }
.end h2 { margin: 0 0 30px; font-size: 64px; }
.end .url { font-weight: 800; font-size: 96px; color: #f46e2c; letter-spacing: -.02em; }
.end .sub { margin-top: 16px; font-size: 36px; font-weight: 600; color: #5d6b6e; }
.end .actions { margin-top: 64px; display: flex; gap: 24px; justify-content: center; }
.end .actions span { background: #fff; border: 2px solid #e6ddd2; border-radius: 999px; padding: 20px 34px;
  font-size: 32px; font-weight: 700; color: #145660; }
"""


def inline(text):
    """**negrito** e *itálico* para HTML, com o resto escapado."""
    out = html.escape(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", out)


def fonte(slug):
    FONTE.mkdir(exist_ok=True)
    meta, badge = FONTE / f"{slug}.json", FONTE / f"{slug}.png"
    if not meta.exists():
        urllib.request.urlretrieve(f"{WIKI}/api/articles/{slug}", meta)
    data = json.loads(meta.read_text(encoding="utf-8"))
    if not badge.exists() and data.get("imageUrl"):
        urllib.request.urlretrieve(WIKI + data["imageUrl"], badge)
    return data, badge


def footer(n, total):
    return (f'<div class="footer"><div class="brand"><img src="{LOGO.as_uri()}" alt="" />dbv.pt</div>'
            f'<div class="page">{n}/{total}</div></div>')


def body(kind, title, items):
    if kind == "lista":
        inner = '<ul class="list">' + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"
    elif kind == "passos":
        inner = '<ol class="steps">' + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ol>"
    elif kind == "pares":
        inner = '<div class="pairs">' + "".join(
            f'<div class="pair"><div class="t">{inline(t)}</div><div class="d">{inline(d)}</div></div>'
            for t, d in items) + "</div>"
    elif kind == "numeros":
        inner = '<div class="nums">' + "".join(
            f'<div class="num"><div class="n">{inline(n)}</div><div class="d">{inline(d)}</div></div>'
            for n, d in items) + "</div>"
    else:
        raise ValueError(kind)
    return f"<h2>{inline(title)}</h2>{inner}"


def page(content, cls=""):
    return (f'<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body><div class="slide {cls}">{content}</div></body></html>')


def slides_for(post):
    data, badge = fonte(post["slug"])
    total = len(post["slides"]) + 2
    area = data.get("categoryName") or post.get("area") or "Especialidade"
    out = [page(
        f'<div class="kicker">Especialidade da semana</div>'
        f'<img class="badge" src="{badge.as_uri()}" alt="" />'
        f'<h1>{inline(post["titulo"])}</h1>'
        f'<div class="meta">{inline(post["nivel"])} · {inline(area)}</div>'
        f'<div class="hook">{inline(post["gancho"])}</div>'
        f'<div class="swipe">Desliza →</div>' + footer(1, total), "cover")]
    for i, (kind, title, items) in enumerate(post["slides"], start=2):
        out.append(page(f'<div class="kicker">{inline(post["titulo"])}</div>' + body(kind, title, items)
                        + footer(i, total)))
    out.append(page(
        f'<img class="logo" src="{(ROOT.parent / "site" / "assets" / "marca-dbv-forge.svg").as_uri()}" alt="" />'
        f'<h2>Requisitos completos e mais dicas</h2>'
        f'<div class="url">dbv.pt</div>'
        f'<div class="sub">Link na bio · DBV Wiki</div>'
        f'<div class="actions"><span>💾 Guarda</span><span>📤 Partilha com a unidade</span></div>'
        + footer(total, total), "end"))
    return out


def render(html_path, png_path):
    subprocess.run([
        str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
        "--window-size=1080,1350", "--virtual-time-budget=6000", "--allow-file-access-from-files",
        f"--screenshot={png_path}", html_path.as_uri(),
    ], check=True, capture_output=True)


def main():
    if not CHROME:
        sys.exit("Não encontrei o Google Chrome.")
    for n, post in enumerate(POSTS, start=1):
        folder = SAIDA / f"{n:02d}-{post['slug']}"
        shutil.rmtree(folder, ignore_errors=True)
        (folder / "html").mkdir(parents=True)
        for i, content in enumerate(slides_for(post), start=1):
            html_path = folder / "html" / f"{i}.html"
            html_path.write_text(content, encoding="utf-8")
            render(html_path, folder / f"{i}.png")
        (folder / "legenda.txt").write_text(post["legenda"] + "\n\n" + post["hashtags"] + "\n", encoding="utf-8")
        print(f"{folder.name}: {len(list(folder.glob('*.png')))} slides")


if __name__ == "__main__":
    main()
