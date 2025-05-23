import os
import subprocess
import socket
from functools import partial
from libqtile.dgroups import simple_key_binder
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from libqtile.utils import guess_terminal

# Sets mod key to SUPER/WINDOWS
mod = "mod4"
# My terminal of choice
myTerm = guess_terminal()
# My browser of choice
myBrowser = "brave"

defaultFont = "RobotoMono Nerd Font"
defaultFontSize = 14

keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "q", lazy.spawn("flameshot gui")),
    Key(
        [mod, "shift"],
        "f",
        lazy.spawn("flameshot gui"),
    ),
    Key([mod], "Escape", lazy.spawn("betterlockscreen -l")),
    Key([mod], "b", lazy.spawn(myBrowser)),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "c", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "s", lazy.spawn("shutdown now")),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
    ),
    Key(
        [mod],
        "f",
        lazy.window.toggle_floating(),
    ),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod], "n", lazy.layout.normalize()),
    # Stack controls
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

groups = [
    Group("1", layout="columns"),
    Group("2", layout="columns"),
    Group("3", layout="columns"),
    Group("4", layout="columns"),
    Group("5", layout="columns"),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

colors = {
    # Nord Frost palette
    "lightBlue": "#88C0D0",  # Frost 2
    "blue": "#5E81AC",  # Frost 3
    "white": "#ECEFF4",  # Snow Storm 3
    "darkBlue": "#4C566A",  # Polar Night 4
    "dark": "#2E3440",  # Polar Night 1
    "gray": "#D8DEE9",  # Snow Storm 1
    "green": "#A3BE8C",  # Aurora green
    "background": "#3B4252",  # Polar Night 2
    # Additional Nord colors
    # "red": "#BF616A",      # Aurora red
    # "orange": "#D08770",   # Aurora orange
    # "yellow": "#EBCB8B",   # Aurora yellow
    # "purple": "#B48EAD",   # Aurora purple
}


layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors["lightBlue"],
    "border_normal": colors["darkBlue"],
}

layouts = [
    layout.Columns(**layout_theme, num_columns=2),
    layout.RatioTile(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
]

prompt = f"{os.environ['USER']}@{socket.gethostname()}: "


def init_widgets_list():
    left_side_list = [
        widget.GroupBox(
            font=defaultFont,
            fontsize=defaultFontSize,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors["gray"],
            inactive=colors["white"],
            rounded=False,
            highlight_color=colors["dark"],
            highlight_method="line",
            this_current_screen_border=colors["lightBlue"],
            this_screen_border=colors["green"],
            other_current_screen_border=colors["lightBlue"],
            other_screen_border=colors["green"],
        ),
        widget.TextBox(
            text="|",
            font=defaultFont,
            foreground="474747",
            padding=2,
            fontsize=defaultFontSize,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors["gray"],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(foreground=colors["gray"], padding=5),
        widget.TextBox(
            text="|",
            font=defaultFont,
            foreground="474747",
            padding=2,
            fontsize=defaultFontSize,
        ),
        widget.WindowName(foreground=colors["lightBlue"], padding=0),
    ]

    right_side_widgets = [
        # partial(widget.Systray),
        partial(widget.Wlan, interface="wlan0"),
        partial(widget.Volume, fmt="Vol: {}"),
        partial(
            widget.Volume,
            device="Capture",
            fmt="Mic: {}",
            get_volume_command="amixer sget Capture | grep -oP '\\d+%' | head -n 1",
            volume_down_command="amixer sset Capture 2%-",
            volume_up_command="amixer sset Capture 2%+",
            mute_command="amixer sset Capture toggle",
        ),
        partial(
            widget.KeyboardLayout, fmt="Keyboard: {}", configured_keyboards=["pl", "us"]
        ),
        partial(widget.Battery),
        partial(widget.CryptoTicker, crypto="USDT", currency="PLN", update_interval=60),
        partial(widget.Clock, format="%A, %B %d - %H:%M "),
    ]

    m_right_side_widgets = [
        f(padding=10) if index % 2 == 0 else f(padding=10, background=colors["blue"])
        for index, f in enumerate(right_side_widgets)
    ]

    return [*left_side_list, *m_right_side_widgets]


if __name__ in ["config", "__main__"]:
    screens = [
        Screen(
            bottom=bar.Bar(
                widgets=init_widgets_list(),
                opacity=1.0,
                size=25,
                background=[colors["background"]],
            )
        ),
        Screen(
            bottom=bar.Bar(
                widgets=init_widgets_list(),
                opacity=1.0,
                size=25,
                background=[colors["background"]],
            )
        ),
        Screen(
            bottom=bar.Bar(
                widgets=init_widgets_list(),
                opacity=1.0,
                size=25,
                background=[colors["background"]],
            )
        ),
    ]
    widgets_list = init_widgets_list()


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        # tastyworks exit box
        Match(title="Confirmation"),
        # qalculate-gtk
        Match(title="Qalculate!"),
        # kdenlive
        Match(wm_class="kdenlive"),
        # GPG key password entry
        Match(wm_class="pinentry-gtk-2"),
    ]
)


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


@hook.subscribe.startup_complete
def assign_groups_to_screens():
    screen_arrangement = [2, 1, 0]

    for index, screen_number in enumerate(screen_arrangement):
        qtile.groups_map[groups[index].name].cmd_toscreen(screen_number)


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
