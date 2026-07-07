# Vadim's Clicker

A mouse automation app, controlled by keyboard hotkeys.

Created by the request of Vadim.

## Download for Windows

You can download an executable from the [official website](https://vadimsclicker.pryt.space/).

## Features

### Autoclicker

Click LMB untill prompted to stop.

### Autoholder

Press and hold LBM untill released (either by manual click, or by automatic click)

## Usage

You can turn on and off any mouse automation feature by pressing a key on your keyboard.

By default, it's:

- `f7` for autoclicker,
- `f8` for mouse holder.

### Customizing hotkeys

If you don't like the default hotkeys, you can choose between two ways to change your hotkeys on the fly.

#### A simple GUI

<img alt="GUI window" src="https://vadimsclicker.pryt.space/gui.png" width="250"/>


#### A light TUI

<img alt="Terminal User Interface" src="https://vadimsclicker.pryt.space/tui.png" width="700"/>


## Build from source

### 1. Clone the repository
`git clone https://github.com/prytlubomir/vadim-clicker`
### 2. Open the directory
`cd vadim-clicker`
### 3. Set up the environment
`uv sync`
### Build
`uv run build.py`