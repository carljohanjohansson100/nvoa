# Media: så byter NVOA ut illustrationerna mot eget material

All bild och film på sidan hämtas från en enda fil, `media/manifest.js`. Ingen HTML eller JavaScript behöver ändras när ett objekt byts ut. Det räcker att lägga filen i mappen och ändra två rader i manifestet.

> Manifestet är en `.js`-fil och inte `.json` av ett skäl: webbläsare tillåter inte att en sida läser `.json`-filer när den öppnas direkt från disken. Innehållet är vanlig JSON-syntax. Vid publicering på en webbserver kan det flyttas till en riktig `.json` om NVOA vill.

## Byta en bild mot ett foto

1. Lägg fotot (`.jpg`, `.png` eller `.webp`) i en egen mapp, till exempel `media/nvoa/`.
2. Öppna `media/manifest.js` och hitta objektet, till exempel `bild-ledningsarbete`.
3. Ändra `path` till den nya filen och `source` till `"nvoa"`:

```js
{"id": "bild-ledningsarbete", "type": "image", "title": "Arbete med vattenledning",
 "alt": "Två medarbetare i varselkläder lägger ett vattenrör i en schakt.",
 "source": "nvoa", "path": "media/nvoa/ledningsarbete-2025.jpg", "category": "Arbete i fält"}
```

4. **Skriv en ny `alt`-text** som beskriver fotot. Den gamla beskriver illustrationen och blir fel.

Märkningen under bilden i förstoringsvyn ändras av sig själv från "Illustration skapad för konceptdemon" till "Foto: NVOA".

## Byta en film mot en videofil

1. Lägg filen (`.mp4` med H.264, eller `.webm`) i `media/nvoa/`.
2. Ändra `path` och `source`. Lägg till `poster` (en stillbild som visas före uppspelning):

```js
{"id": "film-reningsverk", "type": "video", "title": "En dag på reningsverket",
 "caption": "Film utan ljud som visar arbetet på reningsverket under en dag.",
 "transcript": "Texten som återger vad som sägs och visas i filmen.",
 "duration": 30, "source": "nvoa",
 "path": "media/nvoa/reningsverket.mp4", "poster": "media/nvoa/reningsverket.jpg",
 "captions": "media/nvoa/reningsverket.sv.vtt"}
```

3. Krav för tillgänglighet (WCAG 2.1 AA):
   - `captions`: en undertextfil i formatet WebVTT (`.vtt`) på svenska. Filmer med tal eller viktig text måste ha den.
   - `transcript`: en textversion. Den visas under filmen.
   - `caption`: en kort beskrivning av vad filmen visar.
   - Filmer får inte starta av sig själva med ljud. Sidan startar dem inte automatiskt.

## Hjältebilden högst upp (`hero-scen`)

Samma regel: peka `path` mot en `.mp4`/`.webm` (spelas utan ljud i loop, med knapp för paus) eller mot en `.jpg` (visas som stillbild). Videon bör vara kort, utan ljud och under cirka 5 MB.

## Lägga till eller ta bort bilder i galleriet

Galleriet visar alla bildobjekt som har ett `category`-fält. Lägg till ett objekt för en ny bild, eller ta bort ett för att dölja den. Bilderna i "Vattnets väg" (`steg-*`) byts på samma sätt som ovan.

## Fälten i manifestet

| Fält | Betydelse |
|---|---|
| `id` | Unikt namn som sidan använder. Ändra inte. |
| `type` | `image` eller `video`. |
| `title` | Rubrik, visas som bildtext. |
| `alt` | Alternativtext för bild. **Krävs för varje bild.** |
| `caption`, `transcript` | Beskrivning och textversion för film. **Krävs för varje film.** |
| `source` | `generated` (illustration från demon) eller `nvoa` (eget material). |
| `path` | Sökväg från `index.html`. Filändelsen avgör hur det visas: `.svg/.jpg/.png/.webp` som bild, `.mp4/.webm` som video, `.html` som animerad scen. |
| `poster` | Valfritt, för video: stillbild före uppspelning. |
| `captions` | Valfritt, för video: `.vtt`-fil med undertexter. |
| `decorative` | `true` om bilden bara är utsmyckning bredvid text (tom alt-text). |
| `category` | För galleriet: rubrik som visas över bildtexten. |

## Innan eget material publiceras (NVOA ansvarar)

- **Personer i bild:** kontrollera rättigheter och samtycke. Foton där personer kan identifieras är personuppgifter enligt GDPR.
- **Metadata:** ta bort platsdata (GPS) och annan EXIF-information ur fotona.
- **Upphovsrätt:** bekräfta att NVOA har rätt att använda materialet på webben.
- **Storlek:** komprimera foton (till exempel 1600 px bred, under cirka 300 kB) så att sidan laddas snabbt på mobil.
- **Konceptmärkningen:** banderollen i toppen och texten i sidfoten ligger i `index.html`. De ska tas bort först när sidan inte längre är en demo.

## Så är de genererade filerna uppbyggda

- `media/generated/*.svg`: en illustration per fil, ritad som vektorgrafik. De kan öppnas och ändras i ett vanligt ritprogram.
- `media/generated/films/*.html`: varje film är en egen sida med scenen, spela/pausa, förloppsrad och undertexter. Filmen visas i en ram på huvudsidan. Undertexterna står i filen under `caps`.
- `tools/generate_media/`: valfritt Python-skript som skapar om alla genererade filer. Webbplatsen behöver det inte.
