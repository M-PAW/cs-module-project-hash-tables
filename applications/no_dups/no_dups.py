def no_dups(s):
    # Your code here

    key_list = []

    # Check for for no char and return
    if s == '':
        return ''

    # Divide by spaces
    listed = s.split(' ')

    # Create a dictionary from listed
    dicto = dict.fromkeys(listed)

    # iterate through keys and add them to key list
    for key in dicto.keys():
        key_list.append(key)

    # return keys list with single spacing between words, use .join()
    return ' '.join(key_list) 



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))