#!/usr/bin/env bash 

festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
/usr/bin/emacs --daemon &
conky -c $HOME/.config/conky/doomone-qtile.conkyrc
volumeicon &
nm-applet &

xrandr --output eDP-1 --primary --mode 1920x1080 --pos 5120x236 --rotate normal --output DP-1 --off --output DP-2 --mode 5120x1440_55.00 --pos 0x0 --rotate normal --output DP-3 --off
# xrandr --output eDP-1 --mode 1920x1080 --pos 3840x0 --rotate normal --output DP-1 --off --output DP-2 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-3 --off --output DP-1-1 --off --output DP-1-2 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-1-3 --off
### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.xwallpaper &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
nitrogen --restore &
