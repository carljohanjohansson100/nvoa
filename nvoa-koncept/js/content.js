/* Texter och exempeldata som inte är media. Allt som står inom [hakparenteser] är platshållare. */
window.NVOA_CONTENT = {
  stages: [
    {media: 'steg-kalla', title: 'Källan', text: 'Allt börjar i en sjö, ett vattendrag eller i grundvattnet. Regn och snö fyller på hela tiden. Det råa vattnet är inte redo att drickas ännu.', note: '[Varifrån Nackas vatten kommer – fylls i av NVOA]'},
    {media: 'steg-vattenverk', title: 'Vattenverket', text: 'På vattenverket renas vattnet i flera steg tills det håller dricksvattenkvalitet. Prover tas regelbundet för att kontrollera det. Först därefter går vattnet vidare ut på ledningsnätet.', note: '[Hur NVOA:s vattenförsörjning ser ut – fylls i av NVOA]'},
    {media: 'steg-ledningsnat', title: 'Ledningsnätet', text: 'Under gator och tomter ligger rören som leder vattnet hem till dig. Pumpar och ventiler ser till att trycket räcker. Avloppsvattnet har egna rör som går åt andra hållet.', note: ''},
    {media: 'steg-hemmet', title: 'Hemmet', text: 'Hemma öppnar du kranen och vattnet finns där. Det används till att dricka, laga mat, duscha och tvätta. Det som rinner ut i avloppet är på väg vidare.', note: ''},
    {media: 'steg-reningsverk', title: 'Reningsverket', text: 'Avloppsvattnet renas i flera steg innan det släpps ut i naturen. Det du spolar ner och häller i avloppet påverkar hur bra reningen fungerar. Sedan börjar kretsloppet om.', note: '[Namn på reningsverk och utsläppspunkt – fylls i av NVOA]'}
  ],

  /* Generiska fraktioner. NVOA ska bekräfta indelning och regler. */
  bins: [
    {id: 'mat', label: 'Matavfall'},
    {id: 'plast', label: 'Plast\u00adförpackningar'},
    {id: 'papper', label: 'Pappers- och kartong\u00adförpackningar'},
    {id: 'glas', label: 'Glas\u00adförpackningar'},
    {id: 'metall', label: 'Metall\u00adförpackningar'},
    {id: 'rest', label: 'Rest\u00adavfall'},
    {id: 'el', label: 'El\u00adavfall och batterier'}
  ],
  items: [
    {id: 'bananskal', media: 'item-bananskal', name: 'Bananskal', bin: 'mat', hint: 'Skal och matrester är matavfall.'},
    {id: 'schampoflaska', media: 'item-schampoflaska', name: 'Schampoflaska', bin: 'plast', hint: 'Tomma förpackningar av plast sorteras som plast.'},
    {id: 'mjolkkartong', media: 'item-mjolkkartong', name: 'Mjölkkartong', bin: 'papper', hint: 'Kartong räknas som pappers- och kartongförpackning.'},
    {id: 'syltburk', media: 'item-syltburk', name: 'Syltburk av glas', bin: 'glas', hint: 'Burkar och flaskor av glas är glasförpackningar.'},
    {id: 'konservburk', media: 'item-konservburk', name: 'Konservburk', bin: 'metall', hint: 'Förpackningar av metall sorteras som metall.'},
    {id: 'bloja', media: 'item-bloja', name: 'Blöja', bin: 'rest', hint: 'Det som inte kan återvinnas hamnar i restavfallet.'},
    {id: 'batteri', media: 'item-batteri', name: 'Batteri', bin: 'el', hint: 'Batterier ska lämnas separat. De ska inte vara i vanliga soporna.'},
    {id: 'laddare', media: 'item-laddare', name: 'Trasig laddare', bin: 'el', hint: 'Saker med sladd eller batteri är elavfall.'}
  ],

  /* Påhittade exempel. Platser (x, y) är procent av kartbilden. */
  disruptions: [
    {n: 1, title: 'Planerat arbete på vattenledning', status: 'Planerad', area: '[Område A – exempel]', when: '[Datum och tid – exempel]', text: 'Vattnet kan vara avstängt en kortare tid medan ledningen byts. Fyll gärna några kärl med vatten i förväg. Det här är ett påhittat exempel.', x: 30, y: 46},
    {n: 2, title: 'Driftstörning vid pumpstation', status: 'Pågående', area: '[Område B – exempel]', when: '[Datum och tid – exempel]', text: 'En pump är ur funktion och våra tekniker arbetar med felet. Använd gärna mindre vatten tills vidare. Det här är ett påhittat exempel.', x: 62, y: 63},
    {n: 3, title: 'Ändrad tid för sophämtning', status: 'Information', area: '[Område C – exempel]', when: '[Datum – exempel]', text: 'Hämtningen flyttas en dag. Ställ ut kärlet som vanligt. Det här är ett påhittat exempel.', x: 48, y: 27}
  ],

  contact: [
    {label: 'Kundservice, telefon', value: '[Telefonnummer – fylls i av NVOA]'},
    {label: 'Öppettider kundservice', value: '[Öppettider – fylls i av NVOA]'},
    {label: 'E-post', value: '[E-postadress – fylls i av NVOA]'},
    {label: 'Felanmälan vatten och avlopp', value: '[Kontaktväg för felanmälan – fylls i av NVOA]'},
    {label: 'Besöksadress', value: '[Adress – fylls i av NVOA]'},
    {label: 'Frågor om faktura', value: '[Kontaktväg för fakturafrågor – fylls i av NVOA]'}
  ]
};
