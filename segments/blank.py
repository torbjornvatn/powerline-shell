def add_blank_segment(powerline):
    separator = powerline.separator_thin
    powerline.append('\n', 0, 0, separator, Color.HOSTNAME_BG)
    
