FLIPMAP = {
    'a': '\u0250',
    'b': '\u0071',
    'c': '\u0254',
    'd': '\u0070',
    'e': '\u01DD',
    'f': '\u025F',
    'g': '\u0253',
    'h': '\u0265',
    'i': '\u1D09',
    'j': '\u027e',
    'k': '\u029E',
    'l': '\u006C',
    'm': '\u026F',
    'n': '\u0075',
    'o': '\u006F',
    'p': '\u0064',
    'q': '\u0062',
    'r': '\u0279',
    's': '\u0073',
    't': '\u0287',
    'u': '\u006E',
    'v': '\u028C',
    'w': '\u028D',
    'x': '\u0078',
    'y': '\u028E',
    'z': '\u007A',
    'A': '\u2200',
    'B': '\u15FA',
    'C': '\u0186',
    'D': '\u15E1',
    'E': '\u018E',
    'F': '\u2132',
    'G': '\u2141',
    'H': '\u0048',
    'I': '\u0049',
    'J': '\u017F',
    'K': '\uA4D8',
    'L': '\u2142',
    'M': '\u0057',
    'N': '\u004E',
    'O': '\u004F',
    'P': '\u0500',
    'Q': '\u10E2',
    'R': '\u1D1A',
    'S': '\u0053',
    'T': '\uA7B1',
    'U': '\u0548',
    'V': '\u039B',
    'W': '\u004D',
    'X': '\u0058',
    'Y': '\u2144',
    'Z': '\u005A'
}


class UpsideDown:

    def flip(self, c):
        if c in FLIPMAP:
            return FLIPMAP[c]
        else:
            return c

    def __call__(self, str) -> str:
        return ''.join(self.flip(c) for c in str)


upside = UpsideDown()
