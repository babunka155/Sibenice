def vykresleni(neuspesne_pokusy):
    if neuspesne_pokusy == 0:
        return """
        ~~~~~~~
        """
    elif neuspesne_pokusy == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif neuspesne_pokusy == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """
