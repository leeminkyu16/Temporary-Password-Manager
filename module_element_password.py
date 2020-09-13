import base64

class ElementPassword:
    def __init__(self, name = "", description = "", password = ""):
        self.name = name
        self.description = description
        self.password = password

    def set_value(self, string_encoded):
        string_separator = "-"

        array_string_encoded = string_encoded.split(string_separator)

        if (len(array_string_encoded) != 3):
            return

        self.name = base64.b64decode(array_string_encoded[0].encode()).decode()
        self.description = base64.b64decode(array_string_encoded[1].encode()).decode()
        self.password = base64.b64decode(array_string_encoded[2].encode()).decode()

    def encode_to_base64(self):
        string_name_output = base64.b64encode(self.name.encode()).decode()
        string_description_output = base64.b64encode(self.description.encode()).decode()
        string_password_output = base64.b64encode(self.password.encode()).decode()

        string_separator = "-"

        return string_name_output + string_separator + string_description_output + string_separator + string_password_output




