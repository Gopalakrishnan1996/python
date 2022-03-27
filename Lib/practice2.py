class b:
    # Function 1

    # Python3 program to check if
    # a string is perfect reversible or not

    # This function basically checks
    # if string is palindrome or not
    def isReversible(self,str):
        i = 0;
        j = len(str) - 1;

        # iterate from left and right
        while (i < j):
            if (str[i] != str[j]):
                return False;
            i += 1;
            j -= 1;
        return True;
    # Function 2
    def reverseEquation(self,s):

        # Reverse String
        result = ""
        for i in range(len(s)):

            # A space marks the end of the word
            if (s[i] == '+' or s[i] == '-' or s[i] == '/' or s[i] == '*'):

                # insert the word at the beginning
                # of the result String
                result = s[i] + result

            # insert the symbol
            else:
                result = s[i] + result
        return result

    # Function 3
    def leftrotate(self,dir,s, d):
        if(dir == "L"):
          tmp = s[d:] + s[0: d]
        elif(dir == "R"):
            tmp = leftrotate(s, len(s) - d)
        return tmp

    # Function 4
    def printRotatedString(self,str):

        lenn = len(str)

        # Generate all rotations
        # one by one and print
        temp = [0] * (lenn)
        for i in range(lenn):
            j = i  # Current index in str
            k = 0  # Current index in temp

            # Copying the second part from
            # the point of rotation.
            while (j < len(str)):
                temp[k] = str[j]
                k += 1
                j += 1

            # Copying the first part from
            # the point of rotation.
            j = 0
            while (j < i):
                temp[k] = str[j]
                j += 1
                k += 1

            print(*temp, sep="")

    # Function 5
    # Returns count of rotations to get the
    # same string back.
    def findRotations(self,str):

        # tmp is the concatenated string.
        tmp = str + str
        n = len(str)

        for i in range(1, n + 1):

            # substring from i index of
            # original string size.
            substring = tmp[i: i + n]

            # if substring matches with
            # original string then we will
            # come out of the loop.
            if (str == substring):
                return i
        return n

    # Function 6
    def isRotation(self,a: str, b: str) -> bool:
        n = len(a)
        m = len(b)
        if (n != m):
            return False

        # create lps[] that
        # will hold the longest
        # prefix suffix values
        # for pattern
        lps = [0 for _ in range(n)]

        # length of the previous
        # longest prefix suffix
        length = 0
        i = 1

        # lps[0] is always 0
        lps[0] = 0

        # the loop calculates
        # lps[i] for i = 1 to n-1
        while (i < n):
            if (a[i] == b[length]):
                length += 1
                lps[i] = length
                i += 1
            else:
                if (length == 0):
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]
        i = 0

        # Match from that rotating
        # point
        for k in range(lps[n - 1], m):
            if (b[k] != a[i]):
                return False
            i += 1
        return True

    # Function 7
    def isRotated(self,str1, str2):

        if (len(str1) != len(str2)):
            return False

        if (len(str1) < 2):
            return str1 == str2
        clock_rot = ""
        anticlock_rot = ""
        l = len(str2)

        # Initialize string as anti-clockwise rotation
        anticlock_rot = (anticlock_rot + str2[l - 2:] +
                         str2[0: l - 2])

        # Initialize string as clock wise rotation
        clock_rot = clock_rot + str2[2:] + str2[0:2]

        # check if any of them is equal to string1
        return (str1 == clock_rot or
                str1 == anticlock_rot)

    # Function 8
    def wordReverse(self,str):
        i = len(str) - 1
        start = end = i + 1
        result = ''

        while i >= 0:
            if str[i] == ' ':
                start = i + 1
                while start != end:
                    result += str[start]
                    start += 1
                result += ' '
                end = i
            i -= 1
        start = 0
        while start != end:
            result += str[start]
            start += 1
        return result

    # Function 9
    def reverseList(self,A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        return A

    # Function 10
    def reverserWords(self,string):
        st = list()

        # Traverse given string and push all characters
        # to stack until we see a space.
        for i in range(len(string)):
            if string[i] != " ":
                st.append(string[i])

            # When we see a space, we print
            # contents of stack.
            else:
                while len(st) > 0:
                    print(st[-1], end="")
                    st.pop()
                print(end=" ")

        # Since there may not be space after
        # last word.
        while len(st) > 0:
            print(st[-1], end="")
            st.pop()


#Reverse & Rotation :
a1 = b()
n3 = int(input('Please enter the function no:'))
if (n3 == 1):
    str = input('enter a input string here:')
    if (a1.isReversible(str)):
        print("YES");
    else:
        print("NO");
elif (n3 == 2):
    str = input('enter a input string here:')
    print(a1.reverseEquation(str))
elif (n3 == 3):
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    inpno = int(input('enter a input string here:'))
    print(a1.leftrotate(str,str1,inpno))
elif (n3 == 4):
    str = input('enter a input string here:')
    a1.printRotatedString(str)
elif (n3 == 5):
    str = input('enter a input string here:')
    print(a1.findRotations(str))
elif (n3 == 6):
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    print("1" if q1.isRotation(str, str1) else "0")
elif (n3 == 7):
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    if a1.isRotated(str1, str2):
        print("Yes")
    else:
        print("No")
elif (n3 == 8):
    str = input('enter a input string here:')
    print(a1.wordReverse(str))
elif (n3 == 9):
    str = [1, 2, 3, 4, 5, 6]
    print(str)
    print("Reversed list is")
    print(a1.reverseList(str, 0, 5))
elif (n3 == 10):
    str = input('enter a input string here:')
    a1.reverserWords(str)
else:
    print('Method not found')
