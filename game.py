blocks = []



def init():
    init_block(Block(0, 0, "Grass", Texture(Colored_chr(chr(9608), (1, 142, 14)))))
    init_block(Block(0, 0, "Tree", Texture([Colored_chr(chr(9532), (98, 78, 44)), Colored_chr(chr(9600), (130,212,53))])))


def init_block(block):
    blocks.insert(block.id_value, block)


class Player:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture


class Block:
    def __init__(self, id_value, damage_value, name, texture):
        self.id_value = id_value
        self.damage_value = damage_value
        self.name = name
        self.texture = texture


class Texture:
    def __init__(self, colored_chr):
        self.colored_chr = colored_chr


class Colored_chr:
    def __init__(self, character, color=(255, 255, 255)):
        self.character = character
        self.color = color

