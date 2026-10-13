# NVOA-webb – bildvisning för NVOA:s personal

Fristående webbsida (HTML, CSS, vanlig JS, inga externa beroenden). Öppna `index.html` direkt från disken.
Avsedd för intern visning. Ingen publicering. `media/` och `_inventory` ligger i `.gitignore`.

## Så här gör du (lokalt, Windows)
1. Lägg mappen `NVOA-webb` bredvid källmappen `NVOA` (t.ex. `...\Uppdrag\NVOA-webb`).
2. Kräver Python 3 och ffmpeg + ffprobe i PATH (installeras inte automatiskt).
3. `python tools\prepare_media.py --inventory` – listar material, ändrar inget. Stoppar om OneDrive-platshållare hittas.
4. `python tools\prepare_media.py` – skapar `media/` (WebP + JPEG, miniatyrer, H.264 MP4, affischbilder) och `content/manifest.js`.
   Källmappen öppnas endast för läsning. EXIF/GPS tas bort. Omkörning bevarar dina redigerade texter.
5. Redigera `content/manifest.js`: `site` (rubrik, inledning), `themes` (rubrik, text), `items` (`caption`, `theme`, `hero`, `hidden`, `order`).
   Bildtexter som börjar med `TODO` visas inte på sidan. Alt-text blir då en generell text.
6. Öppna `index.html`.

## Anpassning
- Färger och typsnitt: variablerna överst i `css/style.css` (neutral startpalett, byt mot NVOA:s grafiska profil).
- Hero: sätt `"hero": true` på önskat objekt, annars används första videon.
- Presentationsläge: fullskärm, 7 s per bild, video spelas klart. Valfri tangent pausar, mellanslag återupptar, piltangenter bläddrar, Esc avslutar.
