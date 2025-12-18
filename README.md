# Vadim's mouse

A mouse automation app, controlled by keyboard hotkeys.

Created by the request of Vadim.

## Download for Windows

You can download an executable from the [official website](https://prytlubomir.github.io/vadim-clicker-website/).

## Features

### A simple TUI to manage your hotkeys

You can always check and change your hotkeys on the fly.

<img alt="Terminal User Interface" src="https://prytlubomir.github.io/vadim-clicker-website/tui.png" width="700"/>

### Autoclicker

Click LMB untill prompted to stop.

### Autoholder

Press and hold LBM untill released (either by manual click, or by automatic click)

## Build from source

### 1. Clone the repository
`git clone https://github.com/prytlubomir/vadim-clicker`
### 2. Open the directory
`cd vadim-clicker`
### 3. Set up the environment
`uv sync`
### Build for windows
`uv run build.py`
The executable would be named `main.exe`