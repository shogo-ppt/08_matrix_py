import sympy


def main():
    mod = 95
    print('Encrypt mode:1, Decrypt mode:2, Exit:3')
    while True:
        mode = input('Mode:')
        try:
            if mode == '1':
                p_text = input('Input plain text (Max:6):')
                print('Encrypted text:', encrypt(p_text, input_key(), mod))
            elif mode == '2':
                e_text = input('Input encrypted text (Max:6):')
                print('Decrypted text:', decrypt(e_text, input_key(), mod))
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
    return sympy.Matrix([[a, b], [c, d]])


def text_to_mat(text):
    int_list = [(ord(char) - 32) for char in text]
    e, f, g, h, i, j = int_list
    return sympy.Matrix([[e, f, g], [h, i, j]])


def encrypt(p_text, key, mod):
    e, f, g, h, i, j = (key * text_to_mat(p_text)) % mod
    enc_text = ''.join(chr(i + 32) for i in [e, f, g, h, i, j])
    return enc_text


def decrypt(e_text, key, mod):
    e, f, g, h, i, j = (key.inv_mod(mod) * text_to_mat(e_text)) % mod
    dec_text = ''.join(chr(i + 32) for i in [e, f, g, h, i, j])
    return dec_text


if __name__ == '__main__':
    main()
