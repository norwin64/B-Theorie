WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def blit_text(surface, text, pos, font, color=BLACK, border=50):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    lines = 1
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width-border:
                x = pos[0]  # Reset the x.
                y += word_height + 4  # Start on new row.
                lines += 1
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.