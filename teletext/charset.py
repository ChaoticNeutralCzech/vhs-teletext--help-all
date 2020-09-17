#	Name:   Map from Teletext G0 character set to Unicode
#	Date:   2018 April 20
#	Author: Rebecca Bettencourt <support@kreativekorp.com>

g0 = {
    0x20: chr(0x0020), # SPACE
    0x21: chr(0x0021), # EXCLAMATION MARK
    0x22: chr(0x0022), # QUOTATION MARK
    0x23: chr(0x00A3), # POUND SIGN
    0x24: chr(0x0024), # DOLLAR SIGN
    0x25: chr(0x0025), # PERCENT SIGN
    0x26: chr(0x0026), # AMPERSAND
    0x27: chr(0x0027), # APOSTROPHE
    0x28: chr(0x0028), # LEFT PARENTHESIS
    0x29: chr(0x0029), # RIGHT PARENTHESIS
    0x2A: chr(0x002A), # ASTERISK
    0x2B: chr(0x002B), # PLUS SIGN
    0x2C: chr(0x002C), # COMMA
    0x2D: chr(0x002D), # HYPHEN-MINUS
    0x2E: chr(0x002E), # FULL STOP
    0x2F: chr(0x002F), # SOLIDUS
    0x30: chr(0x0030), # DIGIT ZERO
    0x31: chr(0x0031), # DIGIT ONE
    0x32: chr(0x0032), # DIGIT TWO
    0x33: chr(0x0033), # DIGIT THREE
    0x34: chr(0x0034), # DIGIT FOUR
    0x35: chr(0x0035), # DIGIT FIVE
    0x36: chr(0x0036), # DIGIT SIX
    0x37: chr(0x0037), # DIGIT SEVEN
    0x38: chr(0x0038), # DIGIT EIGHT
    0x39: chr(0x0039), # DIGIT NINE
    0x3A: chr(0x003A), # COLON
    0x3B: chr(0x003B), # SEMICOLON
    0x3C: chr(0x003C), # LESS-THAN SIGN
    0x3D: chr(0x003D), # EQUALS SIGN
    0x3E: chr(0x003E), # GREATER-THAN SIGN
    0x3F: chr(0x003F), # QUESTION MARK
    0x40: chr(0x0040), # COMMERCIAL AT
    0x41: chr(0x0041), # LATIN CAPITAL LETTER A
    0x42: chr(0x0042), # LATIN CAPITAL LETTER B
    0x43: chr(0x0043), # LATIN CAPITAL LETTER C
    0x44: chr(0x0044), # LATIN CAPITAL LETTER D
    0x45: chr(0x0045), # LATIN CAPITAL LETTER E
    0x46: chr(0x0046), # LATIN CAPITAL LETTER F
    0x47: chr(0x0047), # LATIN CAPITAL LETTER G
    0x48: chr(0x0048), # LATIN CAPITAL LETTER H
    0x49: chr(0x0049), # LATIN CAPITAL LETTER I
    0x4A: chr(0x004A), # LATIN CAPITAL LETTER J
    0x4B: chr(0x004B), # LATIN CAPITAL LETTER K
    0x4C: chr(0x004C), # LATIN CAPITAL LETTER L
    0x4D: chr(0x004D), # LATIN CAPITAL LETTER M
    0x4E: chr(0x004E), # LATIN CAPITAL LETTER N
    0x4F: chr(0x004F), # LATIN CAPITAL LETTER O
    0x50: chr(0x0050), # LATIN CAPITAL LETTER P
    0x51: chr(0x0051), # LATIN CAPITAL LETTER Q
    0x52: chr(0x0052), # LATIN CAPITAL LETTER R
    0x53: chr(0x0053), # LATIN CAPITAL LETTER S
    0x54: chr(0x0054), # LATIN CAPITAL LETTER T
    0x55: chr(0x0055), # LATIN CAPITAL LETTER U
    0x56: chr(0x0056), # LATIN CAPITAL LETTER V
    0x57: chr(0x0057), # LATIN CAPITAL LETTER W
    0x58: chr(0x0058), # LATIN CAPITAL LETTER X
    0x59: chr(0x0059), # LATIN CAPITAL LETTER Y
    0x5A: chr(0x005A), # LATIN CAPITAL LETTER Z
    0x5B: chr(0x2190), # LEFTWARDS ARROW
    0x5C: chr(0x00BD), # VULGAR FRACTION ONE HALF
    0x5D: chr(0x2192), # RIGHTWARDS ARROW
    0x5E: chr(0x2191), # UPWARDS ARROW
    0x5F: chr(0x0023), # NUMBER SIGN
    0x60: chr(0x2500), # BOX DRAWINGS LIGHT HORIZONTAL
    0x61: chr(0x0061), # LATIN SMALL LETTER A
    0x62: chr(0x0062), # LATIN SMALL LETTER B
    0x63: chr(0x0063), # LATIN SMALL LETTER C
    0x64: chr(0x0064), # LATIN SMALL LETTER D
    0x65: chr(0x0065), # LATIN SMALL LETTER E
    0x66: chr(0x0066), # LATIN SMALL LETTER F
    0x67: chr(0x0067), # LATIN SMALL LETTER G
    0x68: chr(0x0068), # LATIN SMALL LETTER H
    0x69: chr(0x0069), # LATIN SMALL LETTER I
    0x6A: chr(0x006A), # LATIN SMALL LETTER J
    0x6B: chr(0x006B), # LATIN SMALL LETTER K
    0x6C: chr(0x006C), # LATIN SMALL LETTER L
    0x6D: chr(0x006D), # LATIN SMALL LETTER M
    0x6E: chr(0x006E), # LATIN SMALL LETTER N
    0x6F: chr(0x006F), # LATIN SMALL LETTER O
    0x70: chr(0x0070), # LATIN SMALL LETTER P
    0x71: chr(0x0071), # LATIN SMALL LETTER Q
    0x72: chr(0x0072), # LATIN SMALL LETTER R
    0x73: chr(0x0073), # LATIN SMALL LETTER S
    0x74: chr(0x0074), # LATIN SMALL LETTER T
    0x75: chr(0x0075), # LATIN SMALL LETTER U
    0x76: chr(0x0076), # LATIN SMALL LETTER V
    0x77: chr(0x0077), # LATIN SMALL LETTER W
    0x78: chr(0x0078), # LATIN SMALL LETTER X
    0x79: chr(0x0079), # LATIN SMALL LETTER Y
    0x7A: chr(0x007A), # LATIN SMALL LETTER Z
    0x7B: chr(0x00BC), # VULGAR FRACTION ONE QUARTER
    0x7C: chr(0x2016), # DOUBLE VERTICAL LINE
    0x7D: chr(0x00BE), # VULGAR FRACTION THREE QUARTERS
    0x7E: chr(0x00F7), # DIVISION SIGN
    0x7F: chr(0x25A0), # BLACK SQUARE
}

g0_cyr2 = {
    0x20: chr(0x0020), # SPACE
    0x21: chr(0x0021), # EXCLAMATION MARK
    0x22: chr(0x0022), # QUOTATION MARK
    0x23: chr(0x00A3), # POUND SIGN
    0x24: chr(0x0024), # DOLLAR SIGN
    0x25: chr(0x0025), # PERCENT SIGN
    0x26: chr(0x044B), # CYRILLIC SMALL LETTER YERU
    0x27: chr(0x0027), # APOSTROPHE
    0x28: chr(0x0028), # LEFT PARENTHESIS
    0x29: chr(0x0029), # RIGHT PARENTHESIS
    0x2A: chr(0x002A), # ASTERISK
    0x2B: chr(0x002B), # PLUS SIGN
    0x2C: chr(0x002C), # COMMA
    0x2D: chr(0x002D), # HYPHEN-MINUS
    0x2E: chr(0x002E), # FULL STOP
    0x2F: chr(0x002F), # SOLIDUS
    0x30: chr(0x0030), # DIGIT ZERO
    0x31: chr(0x0031), # DIGIT ONE
    0x32: chr(0x0032), # DIGIT TWO
    0x33: chr(0x0033), # DIGIT THREE
    0x34: chr(0x0034), # DIGIT FOUR
    0x35: chr(0x0035), # DIGIT FIVE
    0x36: chr(0x0036), # DIGIT SIX
    0x37: chr(0x0037), # DIGIT SEVEN
    0x38: chr(0x0038), # DIGIT EIGHT
    0x39: chr(0x0039), # DIGIT NINE
    0x3A: chr(0x003A), # COLON
    0x3B: chr(0x003B), # SEMICOLON
    0x3C: chr(0x003C), # LESS-THAN SIGN
    0x3D: chr(0x003D), # EQUALS SIGN
    0x3E: chr(0x003E), # GREATER-THAN SIGN
    0x3F: chr(0x003F), # QUESTION MARK
    0x40: chr(0x042E), # CYRILLIC CAPITAL LETTER YU
    0x41: chr(0x0410), # CYRILLIC CAPITAL LETTER A
    0x42: chr(0x0411), # CYRILLIC CAPITAL LETTER BE
    0x43: chr(0x0426), # CYRILLIC CAPITAL LETTER TSE
    0x44: chr(0x0414), # CYRILLIC CAPITAL LETTER DE
    0x45: chr(0x0415), # CYRILLIC CAPITAL LETTER IE
    0x46: chr(0x0424), # CYRILLIC CAPITAL LETTER EF
    0x47: chr(0x0413), # CYRILLIC CAPITAL LETTER GHE
    0x48: chr(0x0425), # CYRILLIC CAPITAL LETTER HA
    0x49: chr(0x0418), # CYRILLIC CAPITAL LETTER I
    0x4A: chr(0x0419), # CYRILLIC CAPITAL LETTER SHORT I
    0x4B: chr(0x041A), # CYRILLIC CAPITAL LETTER KA
    0x4C: chr(0x041B), # CYRILLIC CAPITAL LETTER EL
    0x4D: chr(0x041C), # CYRILLIC CAPITAL LETTER EМ
    0x4E: chr(0x041D), # CYRILLIC CAPITAL LETTER EN
    0x4F: chr(0x041E), # CYRILLIC CAPITAL LETTER O
    0x50: chr(0x041F), # CYRILLIC CAPITAL LETTER PE
    0x51: chr(0x042F), # CYRILLIC CAPITAL LETTER YA
    0x52: chr(0x0420), # CYRILLIC CAPITAL LETTER ER
    0x53: chr(0x0421), # CYRILLIC CAPITAL LETTER ES
    0x54: chr(0x0422), # CYRILLIC CAPITAL LETTER TE
    0x55: chr(0x0423), # CYRILLIC CAPITAL LETTER U
    0x56: chr(0x0416), # CYRILLIC CAPITAL LETTER ZHE
    0x57: chr(0x0412), # CYRILLIC CAPITAL LETTER BE
    0x58: chr(0x042C), # CYRILLIC CAPITAL LETTER SOFT SIGN
    0x59: chr(0x042A), # CYRILLIC CAPITAL LETTER HARD SIGN
    0x5A: chr(0x0417), # CYRILLIC CAPITAL LETTER ZE
    0x5B: chr(0x0428), # CYRILLIC CAPITAL LETTER SHA
    0x5C: chr(0x042D), # CYRILLIC CAPITAL LETTER E
    0x5D: chr(0x0429), # CYRILLIC CAPITAL LETTER SHCHA
    0x5E: chr(0x0427), # CYRILLIC CAPITAL LETTER CHA
    0x5F: chr(0x042B), # CYRILLIC CAPITAL LETTER YERU
    0x60: chr(0x044E), # CYRILLIC SMALL LETTER YU
    0x61: chr(0x0430), # CYRILLIC SMALL LETTER A
    0x62: chr(0x0431), # CYRILLIC SMALL LETTER BE
    0x63: chr(0x0446), # CYRILLIC SMALL LETTER TSE
    0x64: chr(0x0434), # CYRILLIC SMALL LETTER DE
    0x65: chr(0x0435), # CYRILLIC SMALL LETTER IE
    0x66: chr(0x0444), # CYRILLIC SMALL LETTER EF
    0x67: chr(0x0433), # CYRILLIC SMALL LETTER GHE
    0x68: chr(0x0445), # CYRILLIC SMALL LETTER HA
    0x69: chr(0x0438), # CYRILLIC SMALL LETTER I
    0x6A: chr(0x0439), # CYRILLIC SMALL LETTER SHORT I
    0x6B: chr(0x043A), # CYRILLIC SMALL LETTER KA
    0x6C: chr(0x043B), # CYRILLIC SMALL LETTER EL
    0x6D: chr(0x043C), # CYRILLIC SMALL LETTER EM
    0x6E: chr(0x043D), # CYRILLIC SMALL LETTER EN
    0x6F: chr(0x043E), # CYRILLIC SMALL LETTER O
    0x70: chr(0x043F), # CYRILLIC SMALL LETTER PE
    0x71: chr(0x044F), # CYRILLIC SMALL LETTER YA
    0x72: chr(0x0440), # CYRILLIC SMALL LETTER ER
    0x73: chr(0x0441), # CYRILLIC SMALL LETTER ES
    0x74: chr(0x0442), # CYRILLIC SMALL LETTER TE
    0x75: chr(0x0443), # CYRILLIC SMALL LETTER U
    0x76: chr(0x0436), # CYRILLIC SMALL LETTER ZHE
    0x77: chr(0x0432), # CYRILLIC SMALL LETTER BE
    0x78: chr(0x044C), # CYRILLIC SMALL LETTER SOFT SIGN
    0x79: chr(0x044A), # CYRILLIC SMALL LETTER HARD SIGN
    0x7A: chr(0x0437), # CYRILLIC SMALL LETTER ZE
    0x7B: chr(0x0448), # CYRILLIC SMALL LETTER SHA
    0x7C: chr(0x044D), # CYRILLIC SMALL LETTER E
    0x7D: chr(0x0449), # CYRILLIC SMALL LETTER SHCHA
    0x7E: chr(0x0447), # CYRILLIC SMALL LETTER CHE
    0x7F: chr(0x25A0), # BLACK SQUARE
}


#       Name:   Map from Teletext G1 character set to Unicode
#       Date:   2018 April 20
#       Author: Rebecca Bettencourt <support@kreativekorp.com>

g1 = {
    0x20: chr(0x00A0), # NO-BREAK SPACE; unification of EMPTY BLOCK SEXTANT
    0x21: chr(0x1FB00), # BLOCK SEXTANT-1
    0x22: chr(0x1FB01), # BLOCK SEXTANT-2
    0x23: chr(0x1FB02), # BLOCK SEXTANT-12
    0x24: chr(0x1FB03), # BLOCK SEXTANT-3
    0x25: chr(0x1FB04), # BLOCK SEXTANT-13
    0x26: chr(0x1FB05), # BLOCK SEXTANT-23
    0x27: chr(0x1FB06), # BLOCK SEXTANT-123
    0x28: chr(0x1FB07), # BLOCK SEXTANT-4
    0x29: chr(0x1FB08), # BLOCK SEXTANT-14
    0x2A: chr(0x1FB09), # BLOCK SEXTANT-24
    0x2B: chr(0x1FB0A), # BLOCK SEXTANT-124
    0x2C: chr(0x1FB0B), # BLOCK SEXTANT-34
    0x2D: chr(0x1FB0C), # BLOCK SEXTANT-134
    0x2E: chr(0x1FB0D), # BLOCK SEXTANT-234
    0x2F: chr(0x1FB0E), # BLOCK SEXTANT-1234
    0x30: chr(0x1FB0F), # BLOCK SEXTANT-5
    0x31: chr(0x1FB10), # BLOCK SEXTANT-15
    0x32: chr(0x1FB11), # BLOCK SEXTANT-25
    0x33: chr(0x1FB12), # BLOCK SEXTANT-125
    0x34: chr(0x1FB13), # BLOCK SEXTANT-35
    0x35: chr(0x258C), # LEFT HALF BLOCK; unification of BLOCK SEXTANT-135
    0x36: chr(0x1FB14), # BLOCK SEXTANT-235
    0x37: chr(0x1FB15), # BLOCK SEXTANT-1235
    0x38: chr(0x1FB16), # BLOCK SEXTANT-45
    0x39: chr(0x1FB17), # BLOCK SEXTANT-145
    0x3A: chr(0x1FB18), # BLOCK SEXTANT-245
    0x3B: chr(0x1FB19), # BLOCK SEXTANT-1245
    0x3C: chr(0x1FB1A), # BLOCK SEXTANT-345
    0x3D: chr(0x1FB1B), # BLOCK SEXTANT-1345
    0x3E: chr(0x1FB1C), # BLOCK SEXTANT-2345
    0x3F: chr(0x1FB1D), # BLOCK SEXTANT-12345
    0x40: chr(0x0040), # COMMERCIAL AT
    0x41: chr(0x0041), # LATIN CAPITAL LETTER A
    0x42: chr(0x0042), # LATIN CAPITAL LETTER B
    0x43: chr(0x0043), # LATIN CAPITAL LETTER C
    0x44: chr(0x0044), # LATIN CAPITAL LETTER D
    0x45: chr(0x0045), # LATIN CAPITAL LETTER E
    0x46: chr(0x0046), # LATIN CAPITAL LETTER F
    0x47: chr(0x0047), # LATIN CAPITAL LETTER G
    0x48: chr(0x0048), # LATIN CAPITAL LETTER H
    0x49: chr(0x0049), # LATIN CAPITAL LETTER I
    0x4A: chr(0x004A), # LATIN CAPITAL LETTER J
    0x4B: chr(0x004B), # LATIN CAPITAL LETTER K
    0x4C: chr(0x004C), # LATIN CAPITAL LETTER L
    0x4D: chr(0x004D), # LATIN CAPITAL LETTER M
    0x4E: chr(0x004E), # LATIN CAPITAL LETTER N
    0x4F: chr(0x004F), # LATIN CAPITAL LETTER O
    0x50: chr(0x0050), # LATIN CAPITAL LETTER P
    0x51: chr(0x0051), # LATIN CAPITAL LETTER Q
    0x52: chr(0x0052), # LATIN CAPITAL LETTER R
    0x53: chr(0x0053), # LATIN CAPITAL LETTER S
    0x54: chr(0x0054), # LATIN CAPITAL LETTER T
    0x55: chr(0x0055), # LATIN CAPITAL LETTER U
    0x56: chr(0x0056), # LATIN CAPITAL LETTER V
    0x57: chr(0x0057), # LATIN CAPITAL LETTER W
    0x58: chr(0x0058), # LATIN CAPITAL LETTER X
    0x59: chr(0x0059), # LATIN CAPITAL LETTER Y
    0x5A: chr(0x005A), # LATIN CAPITAL LETTER Z
    0x5B: chr(0x2190), # LEFTWARDS ARROW
    0x5C: chr(0x00BD), # VULGAR FRACTION ONE HALF
    0x5D: chr(0x2192), # RIGHTWARDS ARROW
    0x5E: chr(0x2191), # UPWARDS ARROW
    0x5F: chr(0x0023), # NUMBER SIGN
    0x60: chr(0x1FB1E), # BLOCK SEXTANT-6
    0x61: chr(0x1FB1F), # BLOCK SEXTANT-16
    0x62: chr(0x1FB20), # BLOCK SEXTANT-26
    0x63: chr(0x1FB21), # BLOCK SEXTANT-126
    0x64: chr(0x1FB22), # BLOCK SEXTANT-36
    0x65: chr(0x1FB23), # BLOCK SEXTANT-136
    0x66: chr(0x1FB24), # BLOCK SEXTANT-236
    0x67: chr(0x1FB25), # BLOCK SEXTANT-1236
    0x68: chr(0x1FB26), # BLOCK SEXTANT-46
    0x69: chr(0x1FB27), # BLOCK SEXTANT-146
    0x6A: chr(0x2590), # RIGHT HALF BLOCK; unification of BLOCK SEXTANT-246
    0x6B: chr(0x1FB28), # BLOCK SEXTANT-1246
    0x6C: chr(0x1FB29), # BLOCK SEXTANT-346
    0x6D: chr(0x1FB2A), # BLOCK SEXTANT-1346
    0x6E: chr(0x1FB2B), # BLOCK SEXTANT-2346
    0x6F: chr(0x1FB2C), # BLOCK SEXTANT-12346
    0x70: chr(0x1FB2D), # BLOCK SEXTANT-56
    0x71: chr(0x1FB2E), # BLOCK SEXTANT-156
    0x72: chr(0x1FB2F), # BLOCK SEXTANT-256
    0x73: chr(0x1FB30), # BLOCK SEXTANT-1256
    0x74: chr(0x1FB31), # BLOCK SEXTANT-356
    0x75: chr(0x1FB32), # BLOCK SEXTANT-1356
    0x76: chr(0x1FB33), # BLOCK SEXTANT-2356
    0x77: chr(0x1FB34), # BLOCK SEXTANT-12356
    0x78: chr(0x1FB35), # BLOCK SEXTANT-456
    0x79: chr(0x1FB36), # BLOCK SEXTANT-1456
    0x7A: chr(0x1FB37), # BLOCK SEXTANT-2456
    0x7B: chr(0x1FB38), # BLOCK SEXTANT-12456
    0x7C: chr(0x1FB39), # BLOCK SEXTANT-3456
    0x7D: chr(0x1FB3A), # BLOCK SEXTANT-13456
    0x7E: chr(0x1FB3B), # BLOCK SEXTANT-23456
    0x7F: chr(0x2588), # FULL BLOCK; unification of BLOCK SEXTANT-123456
}


#       Name:   Map from Teletext G2 character set to Unicode
#       Date:   2018 April 20
#       Author: Rebecca Bettencourt <support@kreativekorp.com>

g2 = {
    0x20: chr(0x0020), # SPACE
    0x21: chr(0x00A1), # INVERTED EXCLAMATION MARK
    0x22: chr(0x00A2), # CENT SIGN
    0x23: chr(0x00A3), # POUND SIGN
    0x24: chr(0x0024), # DOLLAR SIGN
    0x25: chr(0x00A5), # YEN SIGN
    0x26: chr(0x0023), # NUMBER SIGN
    0x27: chr(0x00A7), # SECTION SIGN
    0x28: chr(0x00A4), # CURRENCY SIGN
    0x29: chr(0x2018), # LEFT SINGLE QUOTATION MARK
    0x2A: chr(0x201C), # LEFT DOUBLE QUOTATION MARK
    0x2B: chr(0x00AB), # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x2C: chr(0x2190), # LEFTWARDS ARROW
    0x2D: chr(0x2191), # UPWARDS ARROW
    0x2E: chr(0x2192), # RIGHTWARDS ARROW
    0x2F: chr(0x2193), # DOWNWARDS ARROW
    0x30: chr(0x00B0), # DEGREE SIGN
    0x31: chr(0x00B1), # PLUS-MINUS SIGN
    0x32: chr(0x00B2), # SUPERSCRIPT TWO
    0x33: chr(0x00B3), # SUPERSCRIPT THREE
    0x34: chr(0x00D7), # MULTIPLICATION SIGN
    0x35: chr(0x00B5), # MICRO SIGN
    0x36: chr(0x00B6), # PILCROW SIGN
    0x37: chr(0x00B7), # MIDDLE DOT
    0x38: chr(0x00F7), # DIVISION SIGN
    0x39: chr(0x2019), # RIGHT SINGLE QUOTATION MARK
    0x3A: chr(0x201D), # RIGHT DOUBLE QUOTATION MARK
    0x3B: chr(0x00BB), # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x3C: chr(0x00BC), # VULGAR FRACTION ONE QUARTER
    0x3D: chr(0x00BD), # VULGAR FRACTION ONE HALF
    0x3E: chr(0x00BE), # VULGAR FRACTION THREE QUARTERS
    0x3F: chr(0x00BF), # INVERTED QUESTION MARK
    0x40: chr(0x00A0), # NO-BREAK SPACE
    0x41: chr(0x02CB), # MODIFIER LETTER GRAVE ACCENT
    0x42: chr(0x02CA), # MODIFIER LETTER ACUTE ACCENT
    0x43: chr(0x02C6), # MODIFIER LETTER CIRCUMFLEX ACCENT
    0x44: chr(0x02DC), # SMALL TILDE
    0x45: chr(0x02C9), # MODIFIER LETTER MACRON
    0x46: chr(0x02D8), # BREVE
    0x47: chr(0x02D9), # DOT ABOVE
    0x48: chr(0x00A8), # DIAERESIS
    0x49: chr(0x02CC), # MODIFIER LETTER LOW VERTICAL LINE
    0x4A: chr(0x02DA), # RING ABOVE
    0x4B: chr(0x00B8), # CEDILLA
    0x4C: chr(0x005F), # LOW LINE
    0x4D: chr(0x02DD), # DOUBLE ACUTE ACCENT
    0x4E: chr(0x02DB), # OGONEK
    0x4F: chr(0x02C7), # CARON
    0x50: chr(0x2500), # BOX DRAWINGS LIGHT HORIZONTAL
    0x51: chr(0x00B9), # SUPERSCRIPT ONE
    0x52: chr(0x00AE), # REGISTERED SIGN
    0x53: chr(0x00A9), # COPYRIGHT SIGN
    0x54: chr(0x2122), # TRADE MARK SIGN
    0x55: chr(0x266A), # EIGHTH NOTE
    0x56: chr(0x20A0), # EURO-CURRENCY SIGN
    0x57: chr(0x2030), # PER MILLE SIGN
    0x58: chr(0x03B1), # GREEK SMALL LETTER ALPHA
    0x5C: chr(0x215B), # VULGAR FRACTION ONE EIGHTH
    0x5D: chr(0x215C), # VULGAR FRACTION THREE EIGHTHS
    0x5E: chr(0x215D), # VULGAR FRACTION FIVE EIGHTHS
    0x5F: chr(0x215E), # VULGAR FRACTION SEVEN EIGHTHS
    0x60: chr(0x03A9), # GREEK CAPITAL LETTER OMEGA
    0x61: chr(0x00C6), # LATIN CAPITAL LETTER AE
    0x62: chr(0x00D0), # LATIN CAPITAL LETTER ETH
    0x63: chr(0x00AA), # FEMININE ORDINAL INDICATOR
    0x64: chr(0x0126), # LATIN CAPITAL LETTER H WITH STROKE
    0x66: chr(0x0132), # LATIN CAPITAL LIGATURE IJ
    0x67: chr(0x013F), # LATIN CAPITAL LETTER L WITH MIDDLE DOT
    0x68: chr(0x0141), # LATIN CAPITAL LETTER L WITH STROKE
    0x69: chr(0x00D8), # LATIN CAPITAL LETTER O WITH STROKE
    0x6A: chr(0x0152), # LATIN CAPITAL LIGATURE OE
    0x6B: chr(0x00BA), # MASCULINE ORDINAL INDICATOR
    0x6C: chr(0x00DE), # LATIN CAPITAL LETTER THORN
    0x6D: chr(0x0166), # LATIN CAPITAL LETTER T WITH STROKE
    0x6E: chr(0x014A), # LATIN CAPITAL LETTER ENG
    0x6F: chr(0x0149), # LATIN SMALL LETTER N PRECEDED BY APOSTROPHE
    0x70: chr(0x0138), # LATIN SMALL LETTER KRA
    0x71: chr(0x00E6), # LATIN SMALL LETTER AE
    0x72: chr(0x0111), # LATIN SMALL LETTER D WITH STROKE
    0x73: chr(0x00F0), # LATIN SMALL LETTER ETH
    0x74: chr(0x0127), # LATIN SMALL LETTER H WITH STROKE
    0x75: chr(0x0131), # LATIN SMALL LETTER DOTLESS I
    0x76: chr(0x0133), # LATIN SMALL LIGATURE IJ
    0x77: chr(0x0140), # LATIN SMALL LETTER L WITH MIDDLE DOT
    0x78: chr(0x0142), # LATIN SMALL LETTER L WITH STROKE
    0x79: chr(0x00F8), # LATIN SMALL LETTER O WITH STROKE
    0x7A: chr(0x0153), # LATIN SMALL LIGATURE OE
    0x7B: chr(0x00DF), # LATIN SMALL LETTER SHARP S
    0x7C: chr(0x00FE), # LATIN SMALL LETTER THORN
    0x7D: chr(0x0167), # LATIN SMALL LETTER T WITH STROKE
    0x7E: chr(0x014B), # LATIN SMALL LETTER ENG
    0x7F: chr(0x25A0), # BLACK SQUARE
}


#       Name:   Map from Teletext G3 character set to Unicode
#       Date:   2018 April 20
#       Author: Rebecca Bettencourt <support@kreativekorp.com>

g3 = {
    0x20: chr(0x1FB3C), # LOWER LEFT BLOCK DIAGONAL LOWER MIDDLE LEFT TO LOWER CENTRE
    0x21: chr(0x1FB3D), # LOWER LEFT BLOCK DIAGONAL LOWER MIDDLE LEFT TO LOWER RIGHT
    0x22: chr(0x1FB3E), # LOWER LEFT BLOCK DIAGONAL UPPER MIDDLE LEFT TO LOWER CENTRE
    0x23: chr(0x1FB3F), # LOWER LEFT BLOCK DIAGONAL UPPER MIDDLE LEFT TO LOWER RIGHT
    0x24: chr(0x1FB40), # LOWER LEFT BLOCK DIAGONAL UPPER LEFT TO LOWER CENTRE
    0x25: chr(0x25E3), # BLACK LOWER LEFT TRIANGLE
    0x26: chr(0x1FB41), # LOWER RIGHT BLOCK DIAGONAL UPPER MIDDLE LEFT TO UPPER CENTRE
    0x27: chr(0x1FB42), # LOWER RIGHT BLOCK DIAGONAL UPPER MIDDLE LEFT TO UPPER RIGHT
    0x28: chr(0x1FB43), # LOWER RIGHT BLOCK DIAGONAL LOWER MIDDLE LEFT TO UPPER CENTRE
    0x29: chr(0x1FB44), # LOWER RIGHT BLOCK DIAGONAL LOWER MIDDLE LEFT TO UPPER RIGHT
    0x2A: chr(0x1FB45), # LOWER RIGHT BLOCK DIAGONAL LOWER LEFT TO UPPER CENTRE
    0x2B: chr(0x1FB46), # LOWER RIGHT BLOCK DIAGONAL LOWER MIDDLE LEFT TO UPPER MIDDLE RIGHT
    0x2C: chr(0x1FB68), # UPPER AND RIGHT AND LOWER TRIANGULAR THREE QUARTERS BLOCK
    0x2D: chr(0x1FB69), # LEFT AND LOWER AND RIGHT TRIANGULAR THREE QUARTERS BLOCK
    0x2E: chr(0x1FB70), # VERTICAL ONE EIGHTH BLOCK-2
    0x2F: chr(0x2592), # MEDIUM SHADE
    0x30: chr(0x1FB47), # LOWER RIGHT BLOCK DIAGONAL LOWER CENTRE TO LOWER MIDDLE RIGHT
    0x31: chr(0x1FB48), # LOWER RIGHT BLOCK DIAGONAL LOWER LEFT TO LOWER MIDDLE RIGHT
    0x32: chr(0x1FB49), # LOWER RIGHT BLOCK DIAGONAL LOWER CENTRE TO UPPER MIDDLE RIGHT
    0x33: chr(0x1FB4A), # LOWER RIGHT BLOCK DIAGONAL LOWER LEFT TO UPPER MIDDLE RIGHT
    0x34: chr(0x1FB4B), # LOWER RIGHT BLOCK DIAGONAL LOWER CENTRE TO UPPER RIGHT
    0x35: chr(0x25E2), # BLACK LOWER RIGHT TRIANGLE
    0x36: chr(0x1FB4C), # LOWER LEFT BLOCK DIAGONAL UPPER CENTRE TO UPPER MIDDLE RIGHT
    0x37: chr(0x1FB4D), # LOWER LEFT BLOCK DIAGONAL UPPER LEFT TO UPPER MIDDLE RIGHT
    0x38: chr(0x1FB4E), # LOWER LEFT BLOCK DIAGONAL UPPER CENTRE TO LOWER MIDDLE RIGHT
    0x39: chr(0x1FB4F), # LOWER LEFT BLOCK DIAGONAL UPPER LEFT TO LOWER MIDDLE RIGHT
    0x3A: chr(0x1FB50), # LOWER LEFT BLOCK DIAGONAL UPPER CENTRE TO LOWER RIGHT
    0x3B: chr(0x1FB51), # LOWER LEFT BLOCK DIAGONAL UPPER MIDDLE LEFT TO LOWER MIDDLE RIGHT
    0x3C: chr(0x1FB6A), # UPPER AND LEFT AND LOWER TRIANGULAR THREE QUARTERS BLOCK
    0x3D: chr(0x1FB6B), # LEFT AND UPPER AND RIGHT TRIANGULAR THREE QUARTERS BLOCK
    0x3E: chr(0x1FB75), # VERTICAL ONE EIGHTH BLOCK-7
    0x3F: chr(0x2588), # FULL BLOCK
    0x40: chr(0x2537), # BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY
    0x41: chr(0x252F), # BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY
    0x42: chr(0x251D), # BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY
    0x43: chr(0x2525), # BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY
    0x44: chr(0x1FBA4), # BOX DRAWINGS LIGHT DIAGONAL UPPER CENTRE TO MIDDLE LEFT TO LOWER CENTRE
    0x45: chr(0x1FBA5), # BOX DRAWINGS LIGHT DIAGONAL UPPER CENTRE TO MIDDLE RIGHT TO LOWER CENTRE
    0x46: chr(0x1FBA6), # BOX DRAWINGS LIGHT DIAGONAL MIDDLE LEFT TO LOWER CENTRE TO MIDDLE RIGHT
    0x47: chr(0x1FBA7), # BOX DRAWINGS LIGHT DIAGONAL MIDDLE LEFT TO UPPER CENTRE TO MIDDLE RIGHT
    0x48: chr(0x1FBA0), # BOX DRAWINGS LIGHT DIAGONAL UPPER CENTRE TO MIDDLE LEFT
    0x49: chr(0x1FBA1), # BOX DRAWINGS LIGHT DIAGONAL UPPER CENTRE TO MIDDLE RIGHT
    0x4A: chr(0x1FBA2), # BOX DRAWINGS LIGHT DIAGONAL MIDDLE LEFT TO LOWER CENTRE
    0x4B: chr(0x1FBA3), # BOX DRAWINGS LIGHT DIAGONAL MIDDLE RIGHT TO LOWER CENTRE
    0x4C: chr(0x253F), # BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY
    0x4D: chr(0x2022), # BULLET
    0x4E: chr(0x25CF), # BLACK CIRCLE
    0x4F: chr(0x25CB), # WHITE CIRCLE
    0x50: chr(0x2502), # BOX DRAWINGS LIGHT VERTICAL
    0x51: chr(0x2500), # BOX DRAWINGS LIGHT HORIZONTAL
    0x52: chr(0x250C), # BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x53: chr(0x2510), # BOX DRAWINGS LIGHT DOWN AND LEFT
    0x54: chr(0x2514), # BOX DRAWINGS LIGHT UP AND RIGHT
    0x55: chr(0x2518), # BOX DRAWINGS LIGHT UP AND LEFT
    0x56: chr(0x251C), # BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x57: chr(0x2524), # BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x58: chr(0x252C), # BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x59: chr(0x2534), # BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x5A: chr(0x253C), # BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x5B: chr(0x2B62), # RIGHTWARDS TRIANGLE-HEADED ARROW
    0x5C: chr(0x2B60), # LEFTWARDS TRIANGLE-HEADED ARROW
    0x5D: chr(0x2B61), # UPWARDS TRIANGLE-HEADED ARROW
    0x5E: chr(0x2B63), # DOWNWARDS TRIANGLE-HEADED ARROW
    0x5F: chr(0x00A0), # NO-BREAK SPACE
    0x60: chr(0x1FB52), # UPPER RIGHT BLOCK DIAGONAL LOWER MIDDLE LEFT TO LOWER CENTRE
    0x61: chr(0x1FB53), # UPPER RIGHT BLOCK DIAGONAL LOWER MIDDLE LEFT TO LOWER RIGHT
    0x62: chr(0x1FB54), # UPPER RIGHT BLOCK DIAGONAL UPPER MIDDLE LEFT TO LOWER CENTRE
    0x63: chr(0x1FB55), # UPPER RIGHT BLOCK DIAGONAL UPPER MIDDLE LEFT TO LOWER RIGHT
    0x64: chr(0x1FB56), # UPPER RIGHT BLOCK DIAGONAL UPPER LEFT TO LOWER CENTRE
    0x65: chr(0x25E5), # BLACK UPPER RIGHT TRIANGLE
    0x66: chr(0x1FB57), # UPPER LEFT BLOCK DIAGONAL UPPER MIDDLE LEFT TO UPPER CENTRE
    0x67: chr(0x1FB58), # UPPER LEFT BLOCK DIAGONAL UPPER MIDDLE LEFT TO UPPER RIGHT
    0x68: chr(0x1FB59), # UPPER LEFT BLOCK DIAGONAL LOWER MIDDLE LEFT TO UPPER CENTRE
    0x69: chr(0x1FB5A), # UPPER LEFT BLOCK DIAGONAL LOWER MIDDLE LEFT TO UPPER RIGHT
    0x6A: chr(0x1FB5B), # UPPER LEFT BLOCK DIAGONAL LOWER LEFT TO UPPER CENTRE
    0x6B: chr(0x1FB5C), # UPPER LEFT BLOCK DIAGONAL LOWER MIDDLE LEFT TO UPPER MIDDLE RIGHT
    0x6C: chr(0x1FB6C), # LEFT TRIANGULAR ONE QUARTER BLOCK
    0x6D: chr(0x1FB6D), # UPPER TRIANGULAR ONE QUARTER BLOCK
    0x70: chr(0x1FB5D), # UPPER LEFT BLOCK DIAGONAL LOWER CENTRE TO LOWER MIDDLE RIGHT
    0x71: chr(0x1FB5E), # UPPER LEFT BLOCK DIAGONAL LOWER LEFT TO LOWER MIDDLE RIGHT
    0x72: chr(0x1FB5F), # UPPER LEFT BLOCK DIAGONAL LOWER CENTRE TO UPPER MIDDLE RIGHT
    0x73: chr(0x1FB60), # UPPER LEFT BLOCK DIAGONAL LOWER LEFT TO UPPER MIDDLE RIGHT
    0x74: chr(0x1FB61), # UPPER LEFT BLOCK DIAGONAL LOWER CENTRE TO UPPER RIGHT
    0x75: chr(0x25E4), # BLACK UPPER LEFT TRIANGLE
    0x76: chr(0x1FB62), # UPPER RIGHT BLOCK DIAGONAL UPPER CENTRE TO UPPER MIDDLE RIGHT
    0x77: chr(0x1FB63), # UPPER RIGHT BLOCK DIAGONAL UPPER LEFT TO UPPER MIDDLE RIGHT
    0x78: chr(0x1FB64), # UPPER RIGHT BLOCK DIAGONAL UPPER CENTRE TO LOWER MIDDLE RIGHT
    0x79: chr(0x1FB65), # UPPER RIGHT BLOCK DIAGONAL UPPER LEFT TO LOWER MIDDLE RIGHT
    0x7A: chr(0x1FB66), # UPPER RIGHT BLOCK DIAGONAL UPPER CENTRE TO LOWER RIGHT
    0x7B: chr(0x1FB67), # UPPER RIGHT BLOCK DIAGONAL UPPER MIDDLE LEFT TO LOWER MIDDLE RIGHT
    0x7C: chr(0x1FB6E), # RIGHT TRIANGULAR ONE QUARTER BLOCK
    0x7D: chr(0x1FB6F), # LOWER TRIANGULAR ONE QUARTER BLOCK
}
