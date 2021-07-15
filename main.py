import sympy
import random


def main():
    mod = 95
    print('<<<Select mode>>>\n| *Generate key:0\n| *Encrypt mode:1\n| *Decrypt mode:2\n| *Exit:3\n')
    while True:
        mode = input('Mode >> ')
        try:
            if mode == '0':
                print(gen_key(mod), '\n')
            elif mode == '1':
                p_text = input('Input plain text >> ')
                print('Encrypted text >>', encrypt(p_text, input_key(), mod), '\n')
            elif mode == '2':
                e_text = input('Input encrypted text >> ')
                print('Decrypted text >>', decrypt(e_text, input_key(), mod), '\n')
            elif mode == '3':
                break
            else:
                raise ValueError
        except ValueError:
            print('Value error')


def input_key():
    print('\nKey form : [[a, b], [c, d]]')
    a = input('Input key [a] >> ')
    b = input('Input key [b] >> ')
    c = input('Input key [c] >> ')
    d = input('Input key [d] >> ')
    return sympy.Matrix([[a, b], [c, d]])


def gen_key(mod):
    try:
        key = [random.randint(0, mod) for i in range(4)]
        dec_key = sympy.Matrix(2, 2, key).inv_mod(mod)
    except sympy.matrices.common.NonInvertibleMatrixError:
        key = gen_key(mod)
        # print('hello')
    return key


def text_to_mat(text):
    int_list = [(ord(char) - 32) for char in text]
    len_list = len(int_list)
    if len_list % 2 == 1:
        int_list.append(31)
        len_list += 1
    return sympy.Matrix(2, len_list // 2, int_list)


def encrypt(p_text, key, mod):
    e_mat = (key * text_to_mat(p_text)) % mod
    e_mat_len = len(e_mat)
    e_list = []
    for i in range(2):
        for j in range(e_mat_len // 2):
            e_list.append(e_mat[i, j])
    enc_text = ''.join(chr(i + 32) for i in e_list)
    return enc_text


def decrypt(e_text, key, mod):
    d_mat = (key.inv_mod(mod) * text_to_mat(e_text)) % mod
    d_mat_len = len(d_mat)
    d_list = []
    for i in range(2):
        for j in range(d_mat_len // 2):
            d_list.append(d_mat[i, j])
    if d_list[d_mat_len - 1] == 31:
        d_list.pop(d_mat_len - 1)
    dec_text = ''.join(chr(i + 32) for i in d_list)
    return dec_text


if __name__ == '__main__':
    main()
