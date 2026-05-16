# HyprLand Setup

Basic Installation

```bash
sudo apt install --install-suggests hyprland
sudo apt install hyprland-qtutils hyprpaper hyprland-backgrounds hypridle hyprpolkitagent waybar rofi kitty grim slurp hyprpicker hyprcursor-util mako-notifier nwg-look wl-clipboard cliphist
```

Install required cmd-line tools

```bash
sudo apt install brightnessctl playerctl ranger elinks
```

Fix Auth agent
exec following cmds after restart

```bash
sudo systemctl --global disable hyprpolkitagent.service
systemctl --user stop hyprpolkitagent.service
```
