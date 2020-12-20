import subprocess, re
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
terminal = 'termite'
BROWSER = 'brave'
MUSIC_PLAYER = 'spotify'

def is_running(process):
    s = subprocess.Popen(["ps", "axuw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x.decode('utf-8')):
            return True
    return False

def execute_once(process):
    if not is_running(process):
        return subprocess.Popen(process.split())

# start the applications at Qtile startup
@hook.subscribe.startup
def startup():
    execute_once('bash /home/tyler/src/dotfiles/.screenlayout/dockedprimary.sh')
    execute_once('nitrogen --restore')
    execute_once('gnome-keyring-daemon --start')
    execute_once('nm-applet')
    execute_once('dunst')

# add 'PlayPause', 'Next' or 'Previous'
music_cmd = ('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
                     '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.')

def next_prev(action):
    def f(qtile):
        qtile.cmd_spawn(music_cmd + action)
    return f

def app_or_group(group, app):
    def f(qtile):
        if qtile.groupMap[group].windows:
            qtile.groupMap[group].cmd_toscreen()
        else:
            qtile.groupMap[group].cmd_toscreen()
            qtile.cmd_spawn(app)
    return f

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus right in stack pane"),

    # Move windows up or down in current stack
    Key([mod, alt], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, alt], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Resize layout
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # Audio
    Key([], 'XF86AudioMute', lazy.spawn('ponymix toggle')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('ponymix increase 5')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('ponymix decrease 5')),
    Key([], 'XF86AudioPlay', lazy.spawn(music_cmd + 'PlayPause')),
    Key([], 'XF86AudioNext', lazy.function(next_prev('Next'))),
    Key([], 'XF86AudioPrev', lazy.function(next_prev('Previous'))),

    # App shortcuts
    Key([], 'Print', lazy.spawn('flameshot gui')),
    Key([mod],  'm', lazy.function(app_or_group('MUSIC', MUSIC_PLAYER))),
]

# Group SETTINGS
groups = []

# Keys 1 to 9 trigger switch to respective label
group_names = [str(i) for i in range(1, 10)]
group_labels = []
group_layouts = []
group_kwargs = [{} for _ in range(1, 10)]

# Personal space for browsing and discord
group_labels.append('WEB')
group_layouts.append('monadtall')
# group_kwargs.append({
#     'spawn': [
#         'discord',
#         'brave --new-window https://gmail.com'
#     ]
# })

# Personal space for coding
group_labels.append('CODE')
group_layouts.append('monadtall')
# group_kwargs.append({
#     'spawn': [
#         'code',
#         'brave',
#         'termite'
#     ]
# })

# Personal space for writing
group_labels.append('WRITE')
group_layouts.append('monadtall')
group_kwargs.append({})

# Personal space for music
group_labels.append('MUSIC')
group_layouts.append('max')
# group_kwargs.append({
#     'spawn': [
#         'spotify'
#     ]
# })

# Work space for work chat/email/calendar
group_labels.append('WCOMS')
group_layouts.append('stack')
# group_kwargs.append({
#     'spawn': [
#         'teams',
#         'brave --new-window https://outlook.office.com/mail/inbox',
#         'brave --new-window https://outlook.office.com/calendar/view/week'
#     ]
# })

# Work space for work code
group_labels.append('WCODE')
group_layouts.append('monadtall')
# group_kwargs.append({})

# Work space for work research/documentation
group_labels.append('WRSRCH')
group_layouts.append('stack')
# group_kwargs.append({})

# Space for presenting
group_labels.append('PRSNT')
group_layouts.append('monadtall')
# group_kwargs.append({})

# Space for all things random and full screen
group_labels.append('RANDOM')
group_layouts.append('max')
# group_kwargs.append({})

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            **group_kwargs[i]
        ))

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()), 
        Key([mod], "Tab", lazy.screen.next_group()),	   	
        Key([mod, "control"], i.name, lazy.window.togroup(i.name)), 
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()), 
    ])


layouts = [
    layout.Max(),
    layout.Stack(num_stacks=3),
    # layout.Bsp(),
    layout.Columns(),
    layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    layout.RatioTile(),
    layout.Tile(),
    # layout.TreeTab(),
    layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Source Code Pro',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Volume(emoji=True, volume_app='pavucontrol', mouse_callbacks={'Button1': lazy.spawn('pavucontrol')}),
                widget.CPU(format='CPU {load_percent}%'),
                widget.TextBox("|", foreground="#cccccc"),
                widget.Battery(format='Battery {percent:2.0%} {hour:d}:{min:02d}'),                
                widget.TextBox("|", foreground="#cccccc"),
                widget.Systray(),
                widget.TextBox("|", foreground="#cccccc"),
                widget.Clock(format='%a %Y-%m-%d %I:%M %p'),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])

@hook.subscribe.client_new
def set_floating(window):
    floating_types = set(["notification", "toolbar", "splash", "dialog"])
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

auto_fullscreen = True
focus_on_window_activation = "focus" # or smart

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
