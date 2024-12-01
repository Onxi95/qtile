#!/usr/bin/env bash 

festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
/usr/bin/emacs --daemon &
conky -c $HOME/.config/conky/doomone-qtile.conkyrc
volumeicon &
nm-applet &

# uncomment while using `philips brilliance`
# xrandr --newmode "5120x1440_55.00"  568.25  5120 5480 6032 6944  1440 1443 1453 1489 -hsync +vsync
# xrandr --addmode DP-2 5120x1440_55.00
# xrandr --output eDP-1 --mode 1920x1080 --pos 5120x236 --rotate normal --output DP-1 --off --output DP-2 --primary --mode 5120x1440_55.00 --pos 0x0 --rotate normal --output DP-3 --off

# uncomment while using seutp with 3 full hd monitors
# xrandr --output eDP-1 --primary --mode 1920x1080 --pos 3840x0 --rotate normal --output DP-1 --off --output DP-2 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-3 --off --output DP-1-1 --off --output DP-1-2 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-1-3 --off

# uncomment while using PBP setup in `philips brilliance`
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 5120x180 --rotate normal --output DP-1 --off --output DP-2 --mode 2560x1440 --pos 2560x0 --rotate normal --output DP-3 --mode 2560x1440 --pos 0x0 --rotate normal

nitrogen --restore &
udiskie &