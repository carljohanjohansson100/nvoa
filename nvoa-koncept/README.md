# NVOA – konceptdemo

Klickbar demonstration av hur en publik webbplats för vatten och avfall kan se ut. **Inte NVOA:s officiella webbplats.** All bild och film är illustrationer som skapats för demon.

## Öppna

Öppna `index.html` direkt i en webbläsare. Inget byggsteg, ingen server och inga externa anrop (fungerar offline).

## Mappar

```
index.html            sidan
css/base.css          palett, typografi, sidhuvud, knappar
css/components.css    hjälte, berättelse, spel, galleri, filmer, karta, kontakt
js/media.js           renderar bild/film från manifestet (img, video eller scen)
js/app.js             meny, hjälte, galleri, filmer, kontakt
js/story.js           "Vattnets väg" (scroll)
js/game.js            "Avfallets resa" (sorteringsspel)
js/lightbox.js        förstoringsvy
js/drift.js           driftinformation och karta
js/content.js         texter, spelets föremål och kärl, exempeldata, kontaktplatshållare
media/manifest.js     all media: id, typ, titel, alt/bildtext, källa, sökväg
media/README.md       så byter NVOA ut material (på svenska)
media/generated/      illustrationer (SVG) och filmscener (HTML) skapade för demon
tools/generate_media/ valfritt skript som skapar om de genererade filerna
```

## Platshållare och påhittat innehåll

- Allt i [hakparenteser] är platshållare: kontaktuppgifter, öppettider, adresser, var vattnet kommer från, namn på verk, datum.
- Driftinformationen (tre meddelanden, områden A–C) är påhittad och märkt "Exempeldata". Kartan är en förenklad bild utan verkliga gatunamn.
- Avfallsfraktionerna i spelet är generella och märkta för NVOA att bekräfta.

## NVOA behöver kontrollera eller leverera

1. **Fraktioner och sorteringsregler** i spelet (`js/content.js`): vilka kärl som finns i Nacka och hur varje sak ska sorteras.
2. **Processbeskrivningarna** i "Vattnets väg" och i de tre filmerna: de är generella och kan skilja sig från NVOA:s verkliga system.
3. **Fakta som saknas:** källa för vattnet, reningsverk, kontaktuppgifter, öppettider, jourtelefon, adress.
4. **Riktiga foton och filmer** enligt `media/README.md`, med kontroll av rättigheter, samtycke (GDPR) och tillgänglighet.
5. **Grafisk profil och logotyp.** Demon använder en neutral ordmärkning och egen färgpalett.
6. **Driftinformation:** ersätt exempeldata med en riktig källa.
7. **Tillgänglighetsredogörelse:** demon är testad mot WCAG 2.1 AA med automatiska verktyg och manuell tangentbordstestning, men en riktig webbplats behöver en fullständig granskning och en publicerad tillgänglighetsredogörelse.
