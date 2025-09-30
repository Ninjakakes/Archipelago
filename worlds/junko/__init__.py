from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World


class JunkoWeb(WebWorld):
    theme = "ice"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Junko for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ninjakakes"]
    )


class JunkoWorld(World):
    """
    Junko was once the master of her own world, but the subjects that once served her no longer fear her.

    A Yume Nikki-inspired game developed by P. Yoshi for Leeble Game Jam 3.
    """
    game = "Junko"
    web = JunkoWeb()


