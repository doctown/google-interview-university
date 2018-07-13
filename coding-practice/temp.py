def insert_star_between_pairs(a_string):
    starred_string = ""
    return insert_stars(a_string, None, starred_string)


def insert_stars(a_string, prev_ch, starred_string):
    if len(a_string) == 0:
        return starred_string
    star_ch = "*" if a_string[0] == prev_ch else ""
    return insert_stars(a_string[1:], a_string[0], starred_string + star_ch + a_string[0])

print(insert_star_between_pairs("cca"))
