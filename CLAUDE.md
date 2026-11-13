# Verejný repozitár owlandorder.github.io

Tento repozitár aj stránka https://owlandorder.github.io sú verejné. Vidí ich ktokoľvek na internete.
Pravidlá výroby sú v súkromnom repozitári AlexanderSekerak/owlandorder-tovaren (CLAUDE.md); platia aj tu.

## Čo sem patrí
- Stránka odkazov pre profily na sociálnych sieťach (`links.json` → `build.py` → `index.html`).
- Neskôr bezplatné nástroje a verejné obrázky pinov.

## Čo sem nikdy nepatrí
Generátory, dáta o trhu a konkurencii, čísla predajov, údaje zákazníkov, heslá, kľúče, interné plány.

## Pravidlá
- Mení sa len `links.json`; `index.html` sa vždy vyrobí príkazom `python3 build.py`.
- Odkazy na Etsy vždy v tvare `https://owlandorder.etsy.com/...`, aby platilo Share & Save.
- Texty po anglicky a podľa skillu poctive-texty. Žiadne „bestseller", počty zákazníkov ani falošná naliehavosť.
- Žiadne sledovanie, cookies ani externé písma, takže stránka nepotrebuje cookie lištu.
- Adresu tejto stránky nedávaj do Etsy listingov ani profilu na Etsy, keď na nej bude odkaz na nákup
  mimo Etsy (Payhip). Etsy odkazy na nákup mimo Etsy zakazuje.
- Každú zmenu zapíš do `ZMENY.md` v repozitári owlandorder-tovaren.
