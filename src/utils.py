def create_page_index():
    """
    :return: list: [ '/','/a', '/b', '/c', '/d', ...,'/z']
    """
    list_of_char_index = ['']
    for char_index in range(2):
        list_of_char_index.append(f"/{chr(ord('a') + char_index)}")
    return list_of_char_index