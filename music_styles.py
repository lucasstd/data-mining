from enum import Enum, unique

#########
# Describes all the music styles with enumerations.
#########
@unique
class Music_style(Enum):
    SERTANEJO = "sertanejo"
    ROCK = "rock-roll"
    GOSPEL = "gospelreligioso"
    POP_ROCK = "poprock"
    MPB = "mpb"
    POP = "pop"
    REGGAE = "reggae"
    PAGODE = "pagode"
    HEAVY_METAL = "heavy-metal"
    ALTERNATIVO = "alternativo"