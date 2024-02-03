def induktion(term : str):
    print(f"DEBUG: induktion({term})")
    arr = term.split("=")
    func = arr[1]
    left = arr[0].split("(")
    print(left[1])
    print(func)
    return 0