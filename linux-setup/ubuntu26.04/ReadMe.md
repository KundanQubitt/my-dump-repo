# Ubuntu 26.04

## pre-requirement

+ Set Real-time clock to local time

```bash
timedatectl set-local-rtc 1
```

+ Sync, Update and Upgrade apt package manager and packages
+ install all important packages

```bash
sudo dpkg --add-architecture i386 && \
sudo add-apt-repository universe && \
sudo apt update && \
sudo apt full-upgrade && \
sudo apt autoremove && \
sudo apt install linux-image-generic ubuntu-restricted-extras util-linux-extra build-essential curl extrepo ssh git libfuse2 v4l2loopback-dkms tlp tlp-rdw
```

+ set root password
+ uncomment lines which adds EDITOR and GREP_COLOR to env in /etc/sudoers
+ add `Defaults !pwfeedback` to sudoers to hide asterik while typing password

```bash
sudo passwd root && \
sudo visudo && \
sudo visudo -f /etc/sudoers.d/qubitt
```

+ Disable suspension
  + replace `suspend` with `hibernate` in logind.conf
  + disable suspend and similar in sleep.conf
+ Setup hibernation

```bash
sudo editor /etc/systemd/logind.conf
sudo editor /etc/systemd/sleep.conf
swapon --show
free -h
lsblk -f
# sudo blkid
read -p "Press Enter to continue..."
sudo editor /etc/default/grub
sudo update-grub
sudo update-initramfs -u
```

+ Setup firewall

```bash
sudo ufw enable
sudo ufw allow ssh
```

+ Edit .bashrc
  + also source `.git-app_update`, `.sh_aliases`, `.sh_env` in .bashrc

```bash
editor ~/.bashrc
```

## applications

[Read applications.md](./applications.md "Read Me")
