# Debian Setup
_My Custom Debian Setup for Debian 13 trixie._

open in stackedit.io

## Add essentials
`su -`
**root**$ `usermod -aG sudo kundan-qubitt`
**root**$ `exit`
```
sudo dpkg --add-architecture i386
sudo apt update && sudo apt install sed
sudo sed -i.bak 's/\bmain\b.*/main contrib non-free/' /etc/apt/sources.list
```
> ### Cross-Verify
> `sudo editor /etc/apt/sources.list`
> check if it contains `main contrib non-free non-free-firmware` for every deb and deb-src lines.
```
sudo apt update && sudo apt upgrade
sudo apt install firmware-linux linux-headers-$(uname -r) dkms ufw curl wget ssh vim git build-essential sed libfuse2 v4l2loopback-dkms coreutils command-not-found bash-completion ffmpeg pulseaudio-utils atool libarchive-tools tar unzip 7zip
sudo apt install fonts-recommended fonts-dejavu fonts-freefont-ttf fonts-liberation2 gsfonts fonts-noto fonts-noto-extra fonts-font-awesome ttf-mscorefonts-installer
fc-cache -fv
sudo ufw enable
sudo ufw allow ssh
sudo install -m 0755 -d /etc/apt/keyrings
gsettings set org.gnome.desktop.sound allow-volume-above-100-percent true
sudo apt install gnome-tweaks flatpak gnome-software-plugin-flatpak gnome-browser-connector synaptic pavucontrol timeshift neovim fastfetch
sudo apt install python3-full python3-pip python3-gpg python3-chardet python3-bidi default-jdk
echo 'export PATH="$PATH:/sbin:/usr/sbin"
## ALIAS
alias ll='ls -laF'
alias ddebi='sudo apt update && sudo mv ~/Downloads/deb/*.deb /tmp/ && sudo apt install /tmp/*.deb'
## EDITOR
export VISUAL="/usr/bin/nvim"
export EDITOR="$VISUAL"' >> ~/.bashrc
glxinfo | grep "OpenGL"
```
Extras
```
sudo apt install linux-cpupower powertop brightnessctl
```

> ### TTY Setup
> ```
> sudo systemctl disable gdm3
> sudo systemctl set-default multi-user.target
> echo 'TTY=$(tty)
> case "$TTY" in
> 	/dev/tty5)
> 		if [[ ( ! -z "$XDG_RUNTIME_DIR" ) && -z "$DISPLAY" && -z "$WAYLAND_DISPLAY" ]]; then
> 			echo "Starting \`Hyprland\`"
> 			#exec Hyprland
> 		fi
> 		;;
> 	/dev/tty6)
> 		echo "Starting gdm3"
> 		if [[ ( ! -z "$XDG_RUNTIME_DIR" ) && -z "$DISPLAY" && -z "$WAYLAND_DISPLAY" ]]; then
> 			# echo "Starting \`Gnome Desktop Manager\`"
> 			sudo systemctl start gdm3
> 		fi
> 		;;
> esac' >> ~/.bash_temp
> ```
> ```sudo visudo```
> add line `kundan-qubitt ALL=(ALL) NOPASSWD: /bin/systemctl start gdm3` in sudoers
> ### Ranger Setup
> ```sudo apt install ranger fontforge transmission-cli caca-utils ffmpegthumbnailer mediainfo bat highlight jq odt2txt lowdown```
> ### eLinks Setup
> ```sudo apt install elinks```
> ### Zsh Setup
> ```sudo apt install zsh```
> ### Fish Setup
> ```sudo apt install fish```
- A Quick RESTART
```
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
curl -fsS https://dl.brave.com/install.sh | sh
sudo apt install okular arduino fritzing
flatpak install flathub com.mattjakeman.ExtensionManager com.obsproject.Studio
```
> ### Unity Installation
> ```
> sudo apt update && sudo apt upgrade
> curl -fsSL https://hub.unity3d.com/linux/keys/public | sudo gpg --dearmor -o /etc/apt/keyrings/unityhub.gpg
> echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/unityhub.gpg] https://hub.unity3d.com/linux/repos/deb stable main" | sudo tee /etc/apt/sources.list.d/unityhub.list
> sudo apt update && sudo apt install unityhub
> ```

> ### KVM Installation
> ```
> sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager cpu-checker
> kvm-ok
> sudo usermod -aG libvirt $USER
> sudo usermod -aG kvm $USER
> ...
> ```

> ### Docker Installation
> ```
> # Add Docker's official GPG key:
> sudo apt update
> sudo apt install ca-certificates curl
> sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
> sudo chmod a+r /etc/apt/keyrings/docker.asc
> # Add the repository to Apt sources:
> sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
> Types: deb
> URIs: https://download.docker.com/linux/debian
> Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
> Components: stable
> Architectures: $(dpkg --print-architecture)
> Signed-By: /etc/apt/keyrings/docker.asc
> EOF
> sudo apt update
> sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-doc podman-docker containerd runc | cut -f1)
> echo \$(. /etc/os-release && echo "$VERSION_CODENAME")
> sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
> sudo systemctl status docker
> # install docker.deb
> ```

> ### OneDrive Installation
> ```
> wget -qO - https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/Debian_13/Release.key | gpg --dearmor | sudo tee /usr/share/keyrings/obs-onedrive.gpg > /dev/null
> echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/obs-onedrive.gpg] https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/Debian_13/ ./" | sudo tee /etc/apt/sources.list.d/onedrive.list
> sudo apt update && sudo apt install onedrive
> ```


_Last updated: 2026-04-21_