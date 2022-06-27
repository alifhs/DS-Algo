
def palindrome(args : str)->bool:
    if len(args) == 1:
        return True
    if args[0] == args[-1]:
        return palindrome(args[1:-1])
    else:
        return False



palindrome("maam");
palindrome('abc');
