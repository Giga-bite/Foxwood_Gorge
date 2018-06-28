# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Kat", color="#FFFFFF")
define b = Character("Holly", color="#50C878")
define r = Character("Winston", color="#1200ff")
define k = Character("Kezbit")
define e = Character("Ellwood", color="#CCCCFF")
define p = Character("Puck", color="#A52A2A" )

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rya happy

    # These display lines of dialogue.

    mc "Kat's line"
    "Inner Dialog"
    b  "Bubblegum"
    r  "Ryakuma"
    k  "Kezbit"
    e  "Ellwood"
    p  "Puck"
    # This ends the game.

    return
