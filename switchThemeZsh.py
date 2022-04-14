#!/usr/bin/python3

import os
import argparse
import re

THEMES = {
    'default': 'robbyrussell',
    'powerlevel10k': 'powerlevel10k/powerlevel10k',
    'spaceship': 'spaceship',
}

path_home = os.path.expanduser('~')
file_path = os.path.join(path_home, '.zshrc')
parser = argparse.ArgumentParser(description="Change zsh theme")
parser.add_argument(
    '-t',
    '--theme',
    dest='theme',
    type=str,
    nargs='?',
    const='default',
    help='change theme'
)


def if_exists_zsh_file():
    code_status = os.system('ls -la $HOME | grep ".zshrc" > /dev/null')
    if code_status == 0:
        return True
    else:
        print("zsh is not configured")
        return False


def change_theme(theme_select, file):
    try:
        theme = theme_select if theme_select != None else 'default'
        file = open(file, 'r')
        new_config = ""
        for line in file:
            stripped_line = line.strip()
            new_line = re.sub(
                r'ZSH_THEME="(.*)"',
                r'ZSH_THEME="{}"'.format(THEMES[theme]), stripped_line
            )
            new_config += new_line + "\n"
        file.close()
        writing_file = open(file_path, 'w')
        writing_file.write(new_config)
        writing_file.close()
        return (theme, True)
    except:
        return (None, False)


if __name__ == "__main__":
    flag = if_exists_zsh_file()
    if flag:
        args = parser.parse_args()
        theme_select = args.theme
        (theme, status) = change_theme(theme_select, file_path)
        if status:
            print('theme changed to {}'.format(THEMES[theme]), "🚀")
            os.system('exec zsh')
        else:
            print("Something went wrong")
