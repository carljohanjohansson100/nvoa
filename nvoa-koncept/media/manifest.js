/*
  Mediamanifest för konceptdemon. En enda källa för all bild och film på sidan.
  Sidan läser den här filen (inte en .json) eftersom webbläsare inte låter en sida
  hämta .json-filer när den öppnas direkt från disken (file://).

  Fält:
    id        unikt namn som sidan använder
    type      "image" eller "video"
    title     rubrik (visas som bildtext)
    alt       alternativtext för bild (krävs för bilder)
    caption   beskrivning av film (krävs för filmer)
    transcript text som återger filmens innehåll (visas under filmen)
    source    "generated" (illustration från demon) eller "nvoa" (NVOA:s eget material)
    path      sökväg från index.html. Filändelsen avgör hur det visas:
              .svg .jpg .jpeg .png .webp -> bild
              .mp4 .webm                 -> video
              .html                      -> animerad scen i ram
    poster    (valfritt, video) stillbild som visas innan uppspelning
    captions  (valfritt, mp4/webm) textfil .vtt med undertexter
    decorative (valfritt) true om bilden bara är utsmyckning intill text
    category  (valfritt, galleri) rubrik för gruppering
  Se media/README.md för hur NVOA byter ut ett objekt.
*/
window.NVOA_MEDIA = {
  "version": 1,
  "items": [
    {"id": "hero-scen", "type": "video", "title": "Vattnets kretslopp", "caption": "Illustrerad film utan ljud: vatten rinner från en sjö via vattenverk till en kran, vidare till reningsverket och tillbaka till sjön.", "source": "generated", "path": "media/generated/films/hero-vattnets-kretslopp.html", "poster": "media/generated/hero-poster.svg"},

    {"id": "steg-kalla", "type": "image", "title": "Källan", "alt": "Illustration av en skogssjö med berg i bakgrunden. En intagsbyggnad står ute i vattnet och ett rör leder in mot land. Ett regnmoln hänger över sjön.", "source": "generated", "path": "media/generated/steg-1-kalla.svg"},
    {"id": "steg-vattenverk", "type": "image", "title": "Vattenverket", "alt": "Illustration av ett vattenverk med en byggnad, tre runda tankar och tre filterbassänger. En medarbetare med hjälm håller ett vattenprov.", "source": "generated", "path": "media/generated/steg-2-vattenverk.svg"},
    {"id": "steg-ledningsnat", "type": "image", "title": "Ledningsnätet", "alt": "Illustration av ett villaområde med ett genomskuret marklager. En blå vattenledning grenar sig upp till husen och ett avloppsrör går parallellt under den.", "source": "generated", "path": "media/generated/steg-3-ledningsnat.svg"},
    {"id": "steg-hemmet", "type": "image", "title": "Hemmet", "alt": "Illustration av ett genomskuret hus. I köket rinner vatten ur en kran, i badrummet finns dusch och toalett, och en vuxen och ett barn står i köket.", "source": "generated", "path": "media/generated/steg-4-hemmet.svg"},
    {"id": "steg-reningsverk", "type": "image", "title": "Reningsverket", "alt": "Illustration av ett reningsverk med byggnad, tre bassänger och en rund bassäng. Renat vatten rinner ut mot en sjö med vass. En medarbetare med hjälm står vid bassängerna.", "source": "generated", "path": "media/generated/steg-5-reningsverk.svg"},

    {"id": "bild-ledningsarbete", "type": "image", "title": "Arbete med vattenledning", "alt": "Illustration: två medarbetare i varselkläder och hjälm arbetar vid en öppen schakt i en gata där ett vattenrör ligger. En grävmaskin och trafikkoner står intill.", "source": "generated", "path": "media/generated/bild-1-ledningsarbete.svg", "category": "Arbete i fält"},
    {"id": "bild-pumpstation", "type": "image", "title": "Servicebesök vid pumpstation", "alt": "Illustration: en liten tegelbyggnad som är en pumpstation. En servicebil står utanför och en tekniker med surfplatta kontrollerar anläggningen.", "source": "generated", "path": "media/generated/bild-2-pumpstation.svg", "category": "Arbete i fält"},
    {"id": "bild-atervinningscentral", "type": "image", "title": "På återvinningscentralen", "alt": "Illustration: en återvinningscentral med fem stora färgade containrar vid en ramp. Några personer bär sorterade säckar och en bil väntar.", "source": "generated", "path": "media/generated/bild-3-atervinningscentral.svg", "category": "Återvinning"},
    {"id": "bild-sorteringskarl", "type": "image", "title": "Kärl för olika material", "alt": "Illustration: sju färgglada sorteringskärl i rad, vart och ett med en enkel symbol, till exempel ett äpple, en flaska och ett batteri.", "source": "generated", "path": "media/generated/bild-4-sorteringskarl.svg", "category": "Återvinning"},
    {"id": "bild-vattenverk-inne", "type": "image", "title": "Inne i vattenverket", "alt": "Illustration: en hall i ett vattenverk med stora blå rör, orange ventiler och en stor tank. En medarbetare med hjälm läser av en mätare.", "source": "generated", "path": "media/generated/bild-5-vattenverk-inne.svg", "category": "Vattenrening"},
    {"id": "bild-provtagning", "type": "image", "title": "Vattenprov i labbet", "alt": "Illustration: en tekniker i vit rock står vid en labbänk med provrör med vatten. På en skärm bakom syns en vattendroppe.", "source": "generated", "path": "media/generated/bild-6-provtagning.svg", "category": "Vattenrening"},
    {"id": "bild-sopbil", "type": "image", "title": "Sophämtning i villaområde", "alt": "Illustration: en grön sopbil på en villagata en solig dag. Två medarbetare i varselkläder tömmer kärl vid tomtgränsen.", "source": "generated", "path": "media/generated/bild-7-sopbil.svg", "category": "I närområdet"},
    {"id": "bild-miljohus", "type": "image", "title": "Grannar vid miljöhuset", "alt": "Illustration: ett miljöhus med fyra kärl. En vuxen och ett barn sorterar förpackningar tillsammans medan en granne vinkar. En hund står bredvid.", "source": "generated", "path": "media/generated/bild-8-miljohus.svg", "category": "I närområdet"},
    {"id": "bild-sjopromenad", "type": "image", "title": "Promenad vid vattnet", "alt": "Illustration: en gångstig längs en sjö i mjukt kvällsljus. Två personer promenerar med en hund, någon sitter på en bänk och barn leker vid vattenbrynet.", "source": "generated", "path": "media/generated/bild-9-sjopromenad.svg", "category": "I närområdet"},

    {"id": "film-reningsverk", "type": "video", "title": "En dag på reningsverket", "caption": "Illustrerad film utan ljud, cirka 28 sekunder, med text i bild. Den visar hur avloppsvatten passerar galler, sedimentering och luftning och släpps ut renat.", "transcript": "Avloppsvatten från hem och verksamheter rinner in till reningsverket. Först fångas det grova. Ett galler tar bort sådant som inte hör hemma i avloppet. I sedimenteringsbassängen sjunker tungt material till botten och blir slam. I luftningsbassängen får bakterier syre av luftbubblor. De bryter ner det som är löst i vattnet. Det renade vattnet leds ut i en sjö. Reningsverket arbetar hela dygnet.", "duration": 28, "source": "generated", "path": "media/generated/films/en-dag-pa-reningsverket.html"},
    {"id": "film-biogas", "type": "video", "title": "Så blir matavfall biogas", "caption": "Illustrerad film utan ljud, cirka 26 sekunder, med text i bild. Den följer matavfallet från köket via sopbil och biogasanläggning till buss och åker.", "transcript": "Matavfallet läggs i en särskild påse i köket. Sopbilen hämtar påsarna och kör dem till en behandlingsanläggning. I en sluten tank rörs matavfallet om utan syre. Bakterier bryter ner det. Då bildas biogas. Den kan bli bränsle till bussar och andra fordon. Det som blir kvar kan användas som biogödsel på åkermark.", "duration": 26, "source": "generated", "path": "media/generated/films/sa-blir-matavfall-biogas.html"},
    {"id": "film-spolning", "type": "video", "title": "Vad händer när du spolar?", "caption": "Illustrerad film utan ljud, cirka 24 sekunder, med text i bild. Den följer avloppsvattnet från toaletten via ledningar och pumpstation till reningsverket och visar vad som kan fastna i pumpar.", "transcript": "Du spolar. Vattnet och det som följer med försvinner ner genom toalettens avlopp. Det rinner i husets rör vidare till ett större ledningsnät under gatan. Pumpstationer hjälper vattnet vidare. Våtservetter och annat som inte ska spolas kan fastna i pumparna. Spola bara kiss, bajs och toalettpapper. Då når avloppsvattnet reningsverket som det ska.", "duration": 24, "source": "generated", "path": "media/generated/films/vad-hander-nar-du-spolar.html"},

    {"id": "karta-drift", "type": "image", "title": "Förenklad karta", "alt": "Förenklad kartillustration av ett kustnära område med en vik, vägar och parker. Tre platser är markerade med siffrorna 1 till 3. Kartan har inga verkliga gatunamn.", "source": "generated", "path": "media/generated/karta-driftinformation.svg"},

    {"id": "item-bananskal", "type": "image", "title": "Bananskal", "alt": "Ett bananskal.", "decorative": true, "source": "generated", "path": "media/generated/items/bananskal.svg"},
    {"id": "item-schampoflaska", "type": "image", "title": "Tom schampoflaska", "alt": "En tom plastflaska med pumplock.", "decorative": true, "source": "generated", "path": "media/generated/items/schampoflaska.svg"},
    {"id": "item-mjolkkartong", "type": "image", "title": "Tom mjölkkartong", "alt": "En tom mjölkkartong.", "decorative": true, "source": "generated", "path": "media/generated/items/mjolkkartong.svg"},
    {"id": "item-syltburk", "type": "image", "title": "Tom syltburk av glas", "alt": "En glasburk med rött lock.", "decorative": true, "source": "generated", "path": "media/generated/items/syltburk.svg"},
    {"id": "item-konservburk", "type": "image", "title": "Tom konservburk", "alt": "En tom konservburk av metall.", "decorative": true, "source": "generated", "path": "media/generated/items/konservburk.svg"},
    {"id": "item-bloja", "type": "image", "title": "Använd blöja", "alt": "En använd blöja.", "decorative": true, "source": "generated", "path": "media/generated/items/bloja.svg"},
    {"id": "item-batteri", "type": "image", "title": "Batteri", "alt": "Ett cylinderformat batteri.", "decorative": true, "source": "generated", "path": "media/generated/items/batteri.svg"},
    {"id": "item-laddare", "type": "image", "title": "Trasig mobilladdare", "alt": "En mobilladdare med sladd.", "decorative": true, "source": "generated", "path": "media/generated/items/laddare.svg"},

    {"id": "bin-mat", "type": "image", "title": "Kärl för matavfall", "alt": "Ett grönt sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/mat.svg"},
    {"id": "bin-plast", "type": "image", "title": "Kärl för plastförpackningar", "alt": "Ett orange sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/plast.svg"},
    {"id": "bin-papper", "type": "image", "title": "Kärl för pappers- och kartongförpackningar", "alt": "Ett blått sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/papper.svg"},
    {"id": "bin-glas", "type": "image", "title": "Kärl för glasförpackningar", "alt": "Ett turkost sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/glas.svg"},
    {"id": "bin-metall", "type": "image", "title": "Kärl för metallförpackningar", "alt": "Ett rödbrunt sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/metall.svg"},
    {"id": "bin-rest", "type": "image", "title": "Kärl för restavfall", "alt": "Ett grått sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/rest.svg"},
    {"id": "bin-el", "type": "image", "title": "Kärl för elavfall och batterier", "alt": "Ett lila sorteringskärl.", "decorative": true, "source": "generated", "path": "media/generated/bins/el.svg"}
  ]
};
