# Applications for Ubuntu 26.04

## Imp Apps

+ Brave

```bash
curl -fsS https://dl.brave.com/install.sh | sh
```

+ Flatpak, Synaptic
+ Tweaks, Browser Connector
+ Synaptic, dConf Editor
+ + #gdebi
+ GParted, TimeShift
+ FastFetch, pavuControl
+ hTop, PowerTop
+ + restart and add flatpak repo
+ Flatseal, Extension Manager

```bash
sudo apt install flatpak gnome-software-plugin-flatpak gnome-tweaks gnome-browser-connector synaptic dconf-editor gparted timeshift fastfetch pavucontrol htop powertop
# after reboot
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.github.tchx84.Flatseal com.mattjakeman.ExtensionManager
```

+ VLC
+ GIMP, Inkscape
+ Audacity, OBS Studio
+ Transmission
+ Okular

```bash
sudo apt install vlc gimp inkscape audacity obs-studio transmission okular
```

+ Java, Python3
+ Arduino, Fritzing

```bash
sudo apt install arduino fritzing python3-full python3-pip default-jdk python3-gpg
```

### py venv

```bash
python3 -m venv ~/Dev/.venv
```

add following line `source ~/Dev/.venv/bin/activate` to .bashrc  

### Node.JS 24.15.0

```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"
# Download and install Node.js:
nvm install 24
# Verify the Node.js version:
node -v # Should print "v24.15.0".
# Verify npm version:
npm -v # Should print "11.12.1".
```

## docker

```bash
```

unable to connect to university/office wifi  

exec `ping <wifi-login-url> && ip route`  
if ping resolves to a.b.x.x (say 172.17.17.1) and docker also uses a.b.x.x (say 172.17.0.1)  
then you just need to change docker subnet edit `/etc/docker/daemon.json` and add

```bash
{
  "bip": "192.168.250.1/24"
}
```

## git n github

git

```bash
git config --global user.name "Kundan Qubitt"
git config --global user.email "keshavkundan.dev@gmail.com"
git config --global init.defaultBranch main
ssh-keygen -t ed25519 -C "keshavkundan.dev@gmail.com"
```

github cli

```bash
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y))
sudo mkdir -p -m 755 /etc/apt/keyrings
out=$(mktemp)
wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg
cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
sudo mkdir -p -m 755 /etc/apt/sources.list.d
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh -y
```

## Git AppImage Apps

use `update-app` func in `.git-app_update` script file  

NeoVim `update-app "neovim/neovim" "nvim-linux-x86_64.appimage";`  
Pulsar Editor `update-app "pulsar-edit/pulsar" "Linux.Pulsar-{VERSION}.AppImage";`  
draw.io `update-app "jgraph/drawio-desktop" "drawio-x86_64-{VERSION}.AppImage";`  
Obsidian `update-app "obsidianmd/obsidian-releases" "Obsidian-{VERSION}.AppImage";`  

## neovim

```bash
sudo apt install neovim
```

## zsh

```bash
sudo apt install zsh
```

## kvm

Check CPU supports virtualization  
`egrep -c '(vmx|svm)' /proc/cpuinfo` Output should be > 0

Detailed check  
`lscpu | grep Virtualization`  
or use `kvm-ok` in package cpu-checker

Check KVM module is available  
`lsmod | grep kvm`  
if not exec `modprobe kvm`

Install required packages

```bash
sudo apt install \
    qemu-system-x86 \
    qemu-utils \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils \
    virtinst \
    virt-manager \
    ovmf
```

Add your user to libvirt and kvm groups  
`sudo usermod -aG kvm,libvirt $USER`

Enable libvirt daemon  
`sudo systemctl enable --now libvirtd`

## others

+ hollywood

```bash
sudo apt install hollywood
```
