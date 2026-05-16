# ASUS Firmware Support

```bash
#battery
cat /sys/class/power_supply/BAT0/charge_control_end_threshold
echo 80 | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold
#keyboard light
cat /sys/class/leds/asus\:\:kbd_backlight/kbd_rgb_mode_index
```
