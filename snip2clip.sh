#!/bin/bash
$HOME/.quicksnips/get_snips.py "$*" | xclip -i -selection clipboard 
