class a:
    # funtion 1
    def func(self, a, b):
        print(a + b)

    # funtion 2
    def copy_str(self, x, y):
        a1 = a()
        if len(y) == 0:
            print(x)
        else:
            c = a1.copy_str(x, (y)[1:-1])
            print(c)

    # funtion 3

    def checkPangram(self, s):
        List = []
        # create list of 26 characters and set false each entry
        for i in range(26):
          List.append(False)

        # converting the sentence to lowercase and iterating
        # over the sentence
        for c in s.lower():
          if not c == " ":
            # make the corresponding entry True
            List[ord(c) - ord('a')] = True

        # check if any character is missing then return False
        for ch in List:
          if ch == False:
            return False
        return True

    # function 4
    def missingChars(self,Str):
        # A boolean array to store characters
        # present in string.
        MAX_CHAR = 26
        present = [False for i in range(MAX_CHAR)]

        # Traverse string and mark characters
        # present in string.
        for i in range(len(Str)):
            if (Str[i] >= 'a' and Str[i] <= 'z'):
                present[ord(Str[i]) - ord('a')] = True
            elif (Str[i] >= 'A' and Str[i] <= 'Z'):
                present[ord(Str[i]) - ord('A')] = True

        # Store missing characters in alphabetic
        # order.
        res = ""

        for i in range(MAX_CHAR):
            if (present[i] == False):
                res += chr(i + ord('a'))

        return res

    # function 5.1
    def panLipogramChecker(self,s):
        s.lower()
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        # variable to keep count of all the letters
        # not found in the string
        counter = 0

        # traverses the string for every
        # letter of the alphabet
        for ch in alphabets:
            # character not found in string then increment count
            if (s.find(ch) < 0):
                counter += 1

        if (counter == 0):
            result = "Pangram"
        elif (counter == 1):
            result = "Pangrammatic Lipogram"
        else:
         result = "Not a pangram but might a lipogram"

        return result
    # Driver program to test above function

    # function 5
    def main(self):
        a1 = a()
        print(a1.panLipogramChecker("The quick brown fox \
                                    jumped over the lazy dog"))

        print(a1.panLipogramChecker("The quick brown fox \
                                      jumps over the lazy dog"))

        print(a1.panLipogramChecker("The quick brown fox jum\
                                             over the lazy dog"))
    # function 6

    # Python program to remove punctuation from a given string
    # Function to remove punctuation
    def Punctuation(self,string):

        # punctuation marks
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        # traverse the given string and if any punctuation
        # marks occur replace it with null
        for x in string.lower():
            if x in punctuations:
                string = string.replace(x, "")

        # Print string without punctuation
        print(string)

    # function 7.1
    def getMaxCountChar(self,count):
        maxCount = 0
        for i in range(26):
            if count[i] > maxCount:
                maxCount = count[i]
                maxChar = chr(i + ord('a'))

        return maxCount, maxChar

    # function 7
    # Main function for rearranging the characters
    def rearrangeString(self,S):
        a1 = a()
        n = len(S)

        # if length of string is None return False
        if not n:
            return False

        # create a hashmap for the alphabets
        count = [0] * 26
        for char in S:
            count[ord(char) - ord('a')] += 1

        maxCount, maxChar = a1.getMaxCountChar(count)

        # if the char with maximum frequency is more than the half of the
        # total length of the string than return False
        if maxCount > (n + 1) // 2:
            return False

        # create a list for storing the result
        res = [None] * n

        ind = 0

        # place all occurrences of the char with maximum frequency in
        # even positions
        while maxCount:
            res[ind] = maxChar
            ind += 2
            maxCount -= 1

        # replace the count of the char with maximum frequency to zero
        # as all the maxChar are already placed in the result
        count[ord(maxChar) - ord('a')] = 0

        # place all other char in the result starting from remaining even
        # positions and then place in the odd positions
        for i in range(26):
            while count[i] > 0:
                if ind >= n:
                    ind = 1
                res[ind] = chr(i + ord('a'))
                ind += 2
                count[i] -= 1

        # convert the result list to string and return
        return ''.join(res)

    # function 8
    def isNumber(self,s):

        for i in range(len(s)):
            if s[i].isdigit() != True:
                return False

        return True

    # function 9
    def allCharactersSame(self,s):
        n = len(s)
        for i in range(1, n):
            if s[i] != s[0]:
                return False

        return True
    # function 10
    def printInitials(self,name):
        if (len(name) == 0):
            return
        print(name[0].upper()),
        for i in range(1, len(name) - 1):
            if (name[i] == ' '):
                print(name[i + 1].upper()),

    # function 11

    # Function to check whether
    # the given number is duck number or not.
    def check_duck(self,num):
        # Length of the number(number of digits)
        n = len(num)
        # Ignore leading 0s
        i = 0
        while (i < n and num[i] == '0'):
            i = i + 1

        # Check remaining digits
        while (i < n):
            if (num[i] == "0"):
                return True
            i = i + 1

        return False
    # function 11
    def round(self,n):

        # Smaller multiple
        a = (n // 10) * 10

        # Larger multiple
        b = a + 10

        # Return of closest of two
        return (b if n - a > b - n else a)

    # function 12
    # function for converting the string
    def conversion(self,charSet, str1):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        s2 = ""
        for i in str1:
            # find the index of each element of the
            # string in the modified set of alphabets
            # replace the element with the one having the
            # same index in the actual set of alphabets
            s2 += alphabets[charSet.index(i)]

        return s2

    # function 13
    # Python3 program to find extra character
    # in one string
    def findExtraCharacter(self,strA, strB):

        # store string values in map
        m1 = {}

        # store second string in map
        # with frequency
        for i in strB:
            if i in m1:
                m1[i] += 1
            else:
                m1[i] = 1

        # store first string in map
        # with frequency
        for i in strA:
            m1[i] -= 1

        for h1 in m1:

            # if the frequency is 1 then this
            # character is which is added extra
            if m1[h1] == 1:
                return h1

#Basics
a1 = a()
n3 = int(input('Please enter the function no:'))
if (n3 == 1):
    n = int(input('enter a first number here:'))
    n1 = int(input('enter a second number here:'))
    a1.func(n, n1)
elif (n3 == 2):
    x = input('enter a first name here:')
    y = input('enter a second name here:')
    a1.copy_str(x, y)
elif (n3 == 3):
    x = input('enter a sentence here:')
    if (a1.checkPangram(x)):
        print('"' + x + '"')
        print("is a pangram")
    else:
        print('"' + x + '"')
        print("is not a pangram")
elif (n3 == 4):
    x = input('enter a sentence here:')
    print(a1.missingChars(x))
elif (n3 == 5):
    if __name__ == '__main__':
        a1.main()
elif (n3 == 6):
    x = input('enter a Punctuation string here:')
    a1.Punctuation(x)
elif (n3 == 7):
    str = input('enter a Rearrange string here:')
    res = a1.rearrangeString(str)
    if res:
        print(res)
    else:
        print('Not valid string')
elif (n3 == 8):
    x = input('enter a string/Integer here:')
    # Store the input in a str variable
    # Function Call
    if a1.isNumber(x):
       print("Integer")
    else:
       print("String")
elif (n3 == 9):
    x = input('enter a validation string here:')
    if a1.allCharactersSame(x):
       print("Yes")
    else:
       print("No")
elif (n3 == 10):
    x = input('enter a Punctuation string here:')
    a1.printInitials(x)
elif (n3 == 11):
    x = input('enter a input here:')
    if (a1.check_duck(x)):
        print("It is a duck number")
    else:
        print("It is not a duck number")
elif (n3 == 12):
    x = int(input('enter a input value here:'))
    print(a1.round(x))
elif (n3 == 13):
    x = input('enter a input value here:')
    y = input('enter a input value here:')
    print(a1.conversion(x,y))
elif (n3 == 14):
    x = input('enter a input value here:')
    y = input('enter a input value here:')
    print(a1.findExtraCharacter(x, y))
else:
    print('Method not found')
