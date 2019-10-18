

class TextBuffer:
    def _init_(self, init=none):
        pass

    def _str_(self):
        # Printthe contetns of buffer
        pass

    def append(self, string_to_add):
        pass

    def prepend(self, string_to_add):
        pass

    def delete_front(self, chars_to_remove):
        pass

    def delete_back(self, chars_to_remove):
        pass

    def join(self, other_buffer):
        pass

    def split(self, split_location):
        pass

    def join_string(self, string_to_join):
        pass


if __name__ = '__main__':
    text = TextBuffer("super")

    print(text)

    text.join_string("calihdgadasdlasjdl")

    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))
