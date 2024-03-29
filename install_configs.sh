#!/bin/bash
set e

DIR=`dirname "$(readlink -f "$0")"`

# bashrc
BASHRC=$HOME/.bashrc
if [ -f "$BASHRC" ]; then
    rm $BASHRC
fi

ln -s $DIR/.bashrc $BASHRC

# bash aliases
BASH_ALIASES=$HOME/.bash_aliases
if [ -f "$BASH_ALIASES" ]; then
    rm $BASH_ALIASES
fi

ln -s $DIR/.bash_aliases $BASH_ALIASES

if ! grep -q "bash_aliases" "$HOME/.bashrc"; then
    echo '''
if [ -e $HOME/.bash_aliases ]; then
    source $HOME/.bash_aliases
fi
    ''' >> $HOME/.bashrc
fi

# conda
CONDA=$HOME/.bash_conda_init
if [ -f "$CONDA" ]; then
    rm $CONDA
fi

ln -s $DIR/.bash_conda_init $CONDA

# termite
mkdir -p $HOME/.config/termite
TERMITE_CONFIG="$HOME/.config/termite/config"
if [ -f "$TERMITE_CONFIG" ]; then
    rm $TERMITE_CONFIG
fi

ln -s $DIR/.config/termite/config $TERMITE_CONFIG

# kitty terminal
mkdir -p $HOME/.config/kitty
KITTY_CONFIG="$HOME/.config/kitty/kitty.conf"
if [ -f "$KITTY_CONFIG" ]; then
    rm $KITTY_CONFIG
fi

ln -s $DIR/.config/kitty/kitty.conf $KITTY_CONFIG

# qtile
mkdir -p $HOME/.config/qtile
QTILE_CONFIG="$HOME/.config/qtile/config.py"
if [ -f "$QTILE_CONFIG" ]; then
    rm $QTILE_CONFIG
fi

ln -s $DIR/.config/qtile/config.py $QTILE_CONFIG

# dunst
mkdir -p $HOME/.config/dunst
DUNST_CONFIG="$HOME/.config/dunst/dunstrc"
if [ -f "$DUNST_CONFIG" ]; then
    rm $DUNST_CONFIG
fi

ln -s $DIR/.config/dunst/dunstrc $DUNST_CONFIG

# custom bin scripts
if [ ! -f "$HOME/.local/bin/brave_new_window" ]; then
    ln -s $DIR/bin/brave_new_window $HOME/.local/bin/brave_new_window
fi

if [ ! -f "$HOME/.local/bin/work_calendar" ]; then
    ln -s $DIR/bin/work_calendar $HOME/.local/bin/work_calendar
fi

if [ ! -f "$HOME/.local/bin/work_email" ]; then
    ln -s $DIR/bin/work_email $HOME/.local/bin/work_email
fi

# starship
STARSHIP=$HOME/.config/starship.toml
if [ -f "$STARSHIP" ]; then
    rm $STARSHIP
fi

ln -s $DIR/.config/starship.toml $STARSHIP

# picom
PICOM=$HOME/.config/picom/picom.conf
mkdir -p $HOME/.config/picom
if [ -f "$PICOM" ]; then
    rm $PICOM
fi

ln -s $DIR/.config/picom/picom.conf $PICOM


# vim
VIM=$HOME/.vim
VIMRC=$HOME/.vimrc
if [[ -f "$VIM" ]] || [[ -d "$VIM" ]]; then
    rm -rf $VIM
fi

if [ -f "$VIMRC" ]; then
    rm $VIMRC
fi

ln -s $DIR/.vim $VIM
ln -s $DIR/.vimrc $VIMRC
