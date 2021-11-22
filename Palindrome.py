while True:
    word=input("\nCheck The Word that is Palindrome or not: ")
    list1=[word]
    list2=[word[::-1]]
    if(list1==list2):
        print("\nThat is Palindrome")

    else:
        print("\nThat is Not Palindrome")

