class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def __unicode(self, text, encode_flag=True):
        special_key = self.key * (len(text) // len(self.key)) + self.key[:len(text) % len(self.key)]
        result = ""
        for i in range(len(text)):
            try:
                vingere_row = self.vingere_row_create(i, special_key)
                if encode_flag:
                    result += vingere_row[self.alphabet.index(text[i])]
                else:
                    result += self.alphabet[vingere_row.index(text[i])]
            except ValueError:
                result += text[i]
        return result

    def vingere_row_create(self, i, key):

        return self.alphabet[self.alphabet.index(key[i]):] + \
            self.alphabet[:self.alphabet.index(key[i])]

    def encode(self, text: str):

        return self.__unicode(text)

    def decode(self, text):

        return self.__unicode(text, False)