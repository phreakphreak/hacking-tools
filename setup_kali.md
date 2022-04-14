

### Update 
```shell
apt update && apt -y dist-upgrade
```

```
sudo adduser phreakphreak
sudo usermod -aG sudo phreakphreak
```


### Install Kali Linux
```shell
apt update && apt -y install kali-linux-core kali-linux-headless kali-linux-default
```

```shell
apt update && apt -y install kali-desktop-core kali-desktop-xfce
```

```shell
apt update && apt -y install kali-tools-gpu kali-tools-hardware
```

### Oh My Zsh
```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### PowerLevel10k
```shell
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### Node.js

```shell
curl -fsSL https://deb.nodesource.com/setup_17.x | sudo -E bash -
sudo apt-get install -y nodejs
```

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```


```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

```
cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```