def polindrome(string):
    for i in range(0,len(string)//2):
        if string[i]!=string[-i-1]:
            print("no polindrome")
            return 
    print("palindrome")