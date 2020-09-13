
def file_read_line_by_line(path):
    file_target = open(path, "r")
    list_string_target = [line.rstrip() for line in file_target]
    file_target.close()
    return list_string_target

def file_append(path, string_input):
    file_target = open(path, "a")
    file_target.write(string_input)
    file_target.flush()
    file_target.close()

def file_write(path, string_input):
    file_target = open(path, "w")
    file_target.write(string_input)
    file_target.flush()
    file_target.close()

