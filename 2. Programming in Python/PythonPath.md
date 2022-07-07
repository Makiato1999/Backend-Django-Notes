# Installing Python paths for MacOS
- first, check python version `python --version`
- By default, an Apple Mac has Python installed with version 2.7
- so, check `python3 --version`
- if it exists, then we will change the default path
  - first, check the PATH `brew info python`
  - then, find ``Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
    `python3`, `python3-config`, `pip3` etc., respectively, have been installed into
    /usr/local/opt/python@3.9/libexec/bin``
  - so far, we get the PATH, which is `/usr/local/opt/python@3.9/libexec/bin`, PATH could be different, it depends on your own mac.
  - open the shell `vim ~/.zshrc`, my shell is zsh, bash is `vim ~/.bashrc`
    - when you open zshrc, there is `Found a swap file by the name...`, delete it.
  - then press `i`, switch to the insert mode, and input on the next line `PATH="/usr/local/opt/python@3.9/libexec/bin:${PATH}"`
  - press `esc`, then press`:`, then input `wq` to exit zshrc.
  - compile it with `source ~/.zshrc`
  - then check `python --version`, look if the default version is updated.
- if it doesn't exist, we will install new version Python
  - install brewhouse first, then `brew info python`
