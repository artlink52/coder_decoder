from CoderInterface import CoderInterface


class Coder(CoderInterface):
    def run(self, coder_info: str, string_to_process: str) -> str:
        if coder_info == "code":
            return self._code(string_to_process)
        else:
            return self._decode(string_to_process)

    def _code(self, string_to_code: str) -> str:
        encoded_string = ""
        for char in string_to_code:
            if char.isalpha():
                shifted_char = chr(((ord(char) - 65 + 1) % 26) + 65) if char.isupper() else chr(
                    ((ord(char) - 97 + 1) % 26) + 97)
                encoded_string += shifted_char
            else:
                encoded_string += char
        return encoded_string

    def _decode(self, string_to_code: str) -> str:
        decoded_string = ""
        for char in string_to_code:
            if char.isalpha():
                shifted_char = chr(((ord(char) - 65 - 1) % 26) + 65) if char.isupper() else chr(
                    ((ord(char) - 97 - 1) % 26) + 97)
                decoded_string += shifted_char
            else:
                decoded_string += char
        return decoded_string



