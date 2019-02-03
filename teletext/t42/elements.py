from functools import wraps

from teletext.t42.printer import PrinterANSI
from .coding import *


class Element(object):

    def __init__(self, array):
        self._array = array

    def __getitem__(self, item):
        return self._array[item]

    def __setitem__(self, item, value):
        self._array[item] = value

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self._array)})'

    @property
    def errors(self):
        return hamming8_errors(self._array)


class Mrag(Element):

    @property
    def magazine(self):
        magazine = hamming8_decode(self._array[0]) & 0x7
        return magazine or 8

    @property
    def row(self):
        return hamming16_decode(self._array[:2])[0] >> 3

    @magazine.setter
    def magazine(self, magazine):
        if magazine < 0 or magazine > 8:
            raise ValueError('Magazine numbers must be between 0 and 8.')
        self._array[0] = hamming8_encode((magazine & 0x7) | ((self.row&0x1) << 3))

    @row.setter
    def row(self, row):
        if row < 0 or row > 31:
            raise ValueError('Row numbers must be between 0 and 31.')
        self._array[0] = hamming8_encode((self.magazine & 0x7) | ((row & 0x1) << 3))
        self._array[1] = hamming8_encode(row >> 1)

    def __str__(self):
        return f'{self.magazine} {self.row} {self.errors}'

class Displayable(Element):

    def to_ansi(self, colour=True):
        return str(PrinterANSI(self._array, colour))


class Page(Element):

    @property
    def page(self):
        return hamming16_decode(self._array[:2])[0]

    @page.setter
    def page(self, page):
        if page < 0 or page > 0xff:
            raise ValueError('Page numbers must be between 0 and 0xff.')
        self._array[:2] = hamming16_encode(page)


class Header(Page):

    @property
    def subpage(self):
        values = hamming16_decode(self._array[2:6])
        return (values[0] & 0x7f) | ((values[1] & 0x3f) <<8)

    @property
    def control(self):
        values = hamming16_decode(self._array[2:8])
        return (values[0] >> 7) | (values[1] >> 5) | (values[2] << 3)

    @property
    def displayable(self):
        return Displayable(self._array[8:])

    @subpage.setter
    def subpage(self, subpage):
        if subpage < 0 or subpage > 0x3f7f:
            raise ValueError('Subpage numbers must be between 0 and 0x3f7f.')
        control = self.control
        self._array[2:6] = hamming16_encode([
            (subpage & 0x7f) | ((control & 1) << 7),
            (subpage >> 8) | ((control & 6) << 6),
        ])

    @control.setter
    def control(self, control):
        if control < 0 or control > 2047:
            raise ValueError('Control bits must be between 0 and 2047.')
        subpage = self.subpage
        self._array[3] = hamming8_encode(((subpage >> 4) & 0x7) | ((control & 1) << 3))
        self._array[5] = hamming8_encode(((subpage >> 12) & 0x3) | ((control & 6) << 1))
        self._array[6:8] = hamming16_encode(control >> 3)

    def to_ansi(self, colour=True):
        return f'{self.page:02x}{self.displayable.to_ansi(colour)} {self.subpage: x}'

    def ranks(self):
        ranks = [(f.match(self.displayable[:]),f) for f in Finders]
        ranks.sort(reverse=True, key=lambda x: x[0])
        if ranks[0][0] > 20:
            self.name = ranks[0][1].name
            self.finder = ranks[0][1]
            self.displayable_fixed = ranks[0][1].fixup(self.displayable[:].copy())
        else:
            self.name = 'Unknown'
            self.displayable_fixed = self.displayable


class PageLink(Page):

    def __init__(self, array, mrag):
        super().__init__(array)
        self._mrag = mrag

    @property
    def subpage(self):
        values = hamming16_decode(self._array[2:6])
        return (values[0] & 0x7f) | ((values[1] & 0x3f) <<8)

    @property
    def magazine(self):
        values = hamming16_decode(self._array[2:6])
        magazine = ((values[0] >> 7) | (values[1] >> 6)) ^ (self._mrag.magazine & 0x7)
        return magazine or 8

    @subpage.setter
    def subpage(self, subpage):
        if subpage < 0 or subpage > 0x3f7f:
            raise ValueError('Subpage numbers must be between 0 and 0x3f7f.')
        magazine = self.magazine
        self._array[2:6] = hamming16_encode([
            (subpage & 0x7f) | ((magazine & 1) << 7),
            (subpage >> 8) | ((magazine & 6) << 6),
        ])

    @magazine.setter
    def magazine(self, magazine):
        if magazine < 0 or magazine > 8:
            raise ValueError('Magazine numbers must be between 0 and 8.')
        magazine = magazine ^ self._mrag.magazine
        subpage = self.subpage
        self._array[3:6:2] = hamming8_encode([
            ((subpage >> 4) & 0x7) | ((magazine & 1) << 3),
            ((subpage >> 12) & 0x3) | ((magazine & 6) << 1),
        ])

    def __str__(self):
        return f'{self.magazine}{self.page:02x}:{self.subpage:x}'


class BroadcastData(Element):

    def __init__(self, array, mrag):
        super().__init__(array)
        self._mrag = mrag

    @property
    def displayable(self):
        return Displayable(self._array[20:])

    @property
    def initial_page(self):
        return PageLink(self._array[1:7], self._mrag)

    @property
    def dc(self):
        return hamming8_decode(self._array[0])

    @dc.setter
    def dc(self, dc):
        self._array[0] = hamming8_encode(dc)

    def to_ansi(self, colour=True):
        return f'{self.displayable.to_ansi(colour)} DC={self.dc} IP={self.initial_page} '
