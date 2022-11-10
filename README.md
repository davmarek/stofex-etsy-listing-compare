
- [Nastavení Pythonu](#nastavení-pythonu)
  - [MacOS](#macos)
    - [Homebrew](#homebrew)
  - [Windows](#windows)


# Nastavení Pythonu
## MacOS
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

