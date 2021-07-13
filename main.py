# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sympy


def main():
    # mod = 95
    print('Encrypt mode:1, Decrypt mode:2, Exit:3')
    while True:
        mode = input('Mode :')
        try:
            if mode == '1':
                p_text = input('Input plain text (Max : 6):')
                key = input_key()
                print('Encrypted text :', encrypt(p_text, key))
            elif mode == '2':
                e_text = input('Input encrypted text (Max : 6):')
                key = input_key()
                print('Decrypted text :', encrypt(e_text, key))
            elif mode == '3':
                break
            else:
                raise ValueError
        except ValueError:
            print('Value error')


def input_key():
    print('Key form : [[a, b], [c, d]]')
    a = input('Input key [a]:')
    b = input('Input key [b]:')
    c = input('Input key [c]:')
    d = input('Input key [d]:')

    return sympy.Matrix([
        [a, b],
        [c, d]
    ])


def encrypt(p_text, key):
    p_int_list = [(ord(char) - 32) for char in p_text]
    e, f, g, h, i, j = p_int_list
    p_mat = sympy.Matrix([
        [e, f, g],
        [h, i, j]
    ])
    e, f, g, h, i, j = (key * p_mat) % 95
    enc_int = [e, f, g, h, i, j]
    enc_text = ''.join(chr(i + 32) for i in enc_int)
    return enc_text


def decrypt(e_text, key):
    enc_int_list = [(ord(char) - 32) for char in e_text]
    e, f, g, h, i, j = enc_int_list
    e_mat = sympy.Matrix([
        [e, f, g],
        [h, i, j]
    ])
    key_inv = key.inv_mod(95)
    e, f, g, h, i, j = (key_inv * e_mat) % 95
    dec_int = [e, f, g, h, i, j]
    dec_text = ''.join(chr(i + 32) for i in dec_int)
    return dec_text


if __name__ == '__main__':
    main()
