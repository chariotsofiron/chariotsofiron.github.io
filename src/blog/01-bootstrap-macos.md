# Bootstrap macOS for development

My personal setup. Not advice.

## Erase all content and settings

I factory reset my computer once a year to

- test backup strategies
- consider which tools and applications I still enjoy using in my workflow
- clear out loose files that accumulate on the system
- make the computer feel like new

Since macOS Monterey, Apple made it easier to reset a Mac using the "Erase All Content and Settings" feature. [Apple Guide](https://support.apple.com/en-ca/HT212749).


## Install command line tools

Run the command below to install command line tools such as `git`, `make`, etc. under `/Library/Developer/CommandLineTools/usr/bin/`.

```bash
xcode-select --install
```


## Install dotfiles

I tried to make everything work out of $XDG_CONFIG_HOME, but not all tools follow the convention. Instead, I define my own dotfile structure and then symlink the files to their appropriate locations.

[Programs](https://wiki.archlinux.org/title/Dotfiles#Tools) exist to manage dotfiles, but I appreciate the simplicity of my current setup.

```bash
git clone git@github.com:chariotsofiron/dotfiles.git ~/repos/dotfiles/
cd ~/repos/dotfiles/./install.sh
```

## Install Homebrew

Homebrew provides a way of installing, upgrading, and uninstalling command line tools and applications. Visit https://brew.sh for installation instructions.


## Install brew packages

```bash
# tools
brew install rg fd sd bat tree qsv git-delta
# rust applications
brew install zellij helix
brew install --cask karabiner-elements kitty 1password iina qbittorrent ogdesign-eagle orion


# python
brew install python pyright ruff
pip3 install edir # useful tool for renaming files


# rust
brew install rustup
rustup-init
rustup component add rust-analyzer


# markdown
brew install marksman mdformat
```

## Change default shell to `fish`

```bash
brew install fish
echo /usr/local/bin/fish | sudo tee -a /etc/shells
chsh -s /usr/local/bin/fish
````

Restart computer afterwards.


## Mac App Store apps

- Wipr



## Set up Github

SSH keys


## Computer settings

Not worth configuring with `defaults`.

**System preferences**

- Control center -> battery -> show percentage
- Control center -> spotlight -> don't show in menu bar
- Desktop and dock -> automatically hide and show dock
- Desktop and dock -> don't suggest recent apps
- Desktop and dock -> don't automatically rearrange spaces
- Siri and spotlight -> disable ask Siri
- Siri and spotlight -> Search results -> applications, calculator, conversion, definition
- Keyboard -> press globe -> nothing
- Keyboard -> Touch Bar -> shows expanded control strip
- Keyboard -> shortcuts -> Mission control -> switch to desktop 1-9
- Keyboard -> text input -> edit -> disable all
- Trackpad -> secondary click -> click in bottom right corner
- Trackpad -> tap to click

**Safari**

- General -> remove history items manually
- General -> don't open safe files after downloading
- Tabs -> Tab layout -> compact
- AutoFill -> disable all (use 1password)
- Passwords -> disable all
- Advanced -> show full website address
- Advanced -> show features for web developers

**Finder**

- General -> New finder window shows ~/home
- Advanced -> Show all filename extensions
- Advanced -> Don't show warning before changing an extensions
- Advanced -> Don't show warning before removing from iCloud
- Advanced -> Don't show warning before emptying trash
- Advanced -> Keep folders on top when sorting by name
- Advanced -> When performing a search, search the current folder


## Further reading

- [Hardening macOS](https://www.bejarano.io/hardening-macos/)
- [macOS setup guide](https://sourabhbajaj.com/mac-setup/)
- [Ask HN: What feature did you find after years of using macOS? (2020)](https://news.ycombinator.com/item?id=24091707)
- [Making macOS behave itself](https://danmackinlay.name/notebook/macos_hacks.html)
- [macOS command line](https://git.herrbischoff.com/awesome-macos-command-line/about/)

