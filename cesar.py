#!/usr/bin/python

import argparse

def execute(key, text, crypt=True):
    result = ''

    for char in text:
        if char.isalnum():
            result += chr(ord(char) + key) if crypt else chr(ord(char) - key)
            continue

        result += char
    
    print(result)

def crypt(key, text):
    execute(key, text)

def decrypt(key, text):
    execute(key, text, False)

def main():
    parser = argparse.ArgumentParser(description='Exemplo de uso do algoritimo de César')

    parser.add_argument('action',type=str, choices=['crypt', 'decrypt'], help='ação que o algoritimo deve executar')
    parser.add_argument('text', type=str, help='texto a ser processado pelo algoritimo')
    parser.add_argument('key', type=int, help='chave criptográfica a ser utilizada')

    args = vars(parser.parse_args())
    
    action = globals()[args['action']]
    action(args['key'], args['text'])

if __name__ == '__main__':
    main()
