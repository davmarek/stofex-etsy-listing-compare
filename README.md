
- [🐍 Nastavení Pythonu](#-nastavení-pythonu)
  - [Mac](#mac)
    - [Homebrew](#homebrew)
  - [Windows](#windows)
- [⚙️ Nastavení projektu](#️-nastavení-projektu)
- [🚀 Spuštění projektu](#-spuštění-projektu)
- [🤷‍♂️ Něco nejede?](#️-něco-nejede)


# 🐍 Nastavení Pythonu
## Mac
__2 způsoby instalace:__
- manager balíčků [Homebrew](#homebrew) (doporučeno)
- stáhnutí a instalace souboru na [python.org](https://www.python.org/downloads/)

### Homebrew
Přes terminál nainstalujeme Developer Tools:
```
xcode-select --install
```

Pak můžeme nainstalovat **_brew_**
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Restartujeme terminál a oveříme, že se nainstaloval správně:
```
brew --version
```

Pak můžeme nainstalovat Python:
```
brew install python@3.10
```

Oveříme, že se nainstaloval správně:
```
python3 --version
```

Pokud ne, vypni a zapni terminál. Pokud stále nic, **řekni Davidovi**.



## Windows
Nainstalujeme Python z [python.org](https://www.python.org/downloads/)


# ⚙️ Nastavení projektu
Projekt si můžeme třeba otevřít ve VSCode.

V zabudovaném terminálů spustíme:
```bash
# Mac
python3 -m venv venv
# Windows
python -m venv venv
```
Tím jsme si vytvořili virtuální prostředí.

Pokud používáme VSCode, prostředí můžeme zapnout tlačítkem **_"Vybrat interpret"_** vpravo dole, když otevřeme soubor main.py.

Vybereme interpret, u kterého je napsané __venv_.

# 🚀 Spuštění projektu
1. Do složky projektu vložíme dva soubory __.csv__
   - export z Etsy
   - export z Money (musíme ho první otevřít třeba v Excelu a vyexportovat jako _.csv_)
2. Změníme proměné na začátku souboru _**main.py**_ (nastavení názvů _.csv_ souborů)
3. Můžeme spustit

# 🤷‍♂️ Něco nejede?
> Napiš Davidovi 