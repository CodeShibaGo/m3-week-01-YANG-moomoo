def greet(name):

    if not isinstance(name, str) or name == "":
        return "Error: Name must non-empty"
    
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, "+ name + "!"
