def magic_string():
    setattr(magic_string, "i", getattr(magic_string, "i", -1) + 1)
    return "Holberton, " * magic_string.i + "Holberton"
