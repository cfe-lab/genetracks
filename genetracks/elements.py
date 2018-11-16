"""
basic elements of gene track figures
"""
import drawSvg as draw

class Figure:
    """
    figure class
    """
    def __init__(self, tracks=[], height=100, size=500):
        self.tracks = tracks
        self.height = height
        self.size = size

    def to_svg(self, g):
        pass

    def add_track(self, track):
        self.tracks.append(track)

    def draw(self, i, j, alignments=[]):
        top = self.height
        d = draw.Drawing(max(i.b, j.b), top, origin=(0, 0))

        for e in i.draw(0, 0):
            d.append(e)
        for e in j.draw(0, top - 10):
            d.append(e)

        for aln in alignments:
            for e in aln.draw():
                d.append(e)

        d.setRenderSize(self.size)
        return d

    def to_png(self, d, path):
        d.savePng(path)

class Track:
    """
    individual gene track
    """
    def __init__(self, a, b, label=None, color='lightgrey', ticks=[],
                 regions=[], direction=None):
        self.color = color
        self.a = a
        self.b = b
        self.x = 0
        self.y = 0
        self.ticks = ticks
        self.label = label
        self.direction = direction
        self.regions = regions

    def add_tick(self, tick):
        self.ticks.append(tick)

    def draw(self, x, y):
        self.x = x
        self.y = y
        d = []
        d.append(draw.Rectangle(x + self.a, y, x + (self.b - self.a), y + 10,
                                fill=self.color))
        for tick in self.ticks:
            d.append(draw.Lines(x + self.a + tick, y, x + self.a + tick, y + 10,
                                stroke='red'))
        if self.label:
            d.append(draw.Text(self.label, 10, x - 20, y))

        if 'f' in self.direction:
            d.append(draw.Lines(x + self.b, y, x + self.b + 5, y + 5,
                                x + self.b, y + 10, fill=self.color))
        if 'r' in self.direction:
            d.append(draw.Lines(x + self.a, y, (x + self.a) - 5, y + 5,
                                x + self.a, y + 10, fill=self.color))

        for a, b, color in self.regions:
            d.append(draw.Rectangle(x + a, y, x + (b - a), y + 10, fill=color))
        return d


class Label:
    """
    label wrapper
    """
    def __init__(self, text, style=None):
        pass


class Alignment:
    """
    expressing the alignment of two tracks
    """
    def __init__(self, track1, track2, connections, text=None, style=None):
        self.t1 = track1
        self.t2 = track2
        self.connections = connections

#    def add_alignment(self, a, b):
#        pass

    def draw(self):
        d = []
        for bottom, top in self.connections:
            d.append(draw.Lines(bottom, self.t1.y + 10,
                                top, self.t2.y, stroke='black'))
            d.append(draw.Lines(bottom, self.t1.y,
                                bottom, self.t1.y + 10, stroke='black'))
            d.append(draw.Lines(top, self.t2.y,
                                top, self.t2.y + 10, stroke='black'))
        return d


class Tick:
    """
    wrapper for tick
    """
    def __init__(self, pos, color='red'):
        self.pos = pos
