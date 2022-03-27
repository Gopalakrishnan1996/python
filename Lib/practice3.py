from math import pow
class c:
    # Function 1
    # Function to remove all spaces from a given string
    def removeSpaces(self,string):
        a1 = c()
        # To keep track of non-space character count
        count = 0

        list = []

        # Traverse the given string. If current character
        # is not space, then place it at index 'count++'
        for i in xrange(len(string)):
            if string[i] != ' ':
                list.append(string[i])

        return a1.toString(list)
    # function 1.1
    # Utility Function
    def toString(self,List):
        return ''.join(List)

    # function 2
    # Function to find spaces and move to beginning
    def moveSpaceInFront(self,s):
        # Traverse from end and swap spaces
        i = len(s) - 1;
        for j in range(i, -1, -1):
            if (s[j] != ' '):
                s = swap(s, i, j);
                i -= 1;
        return s;

    # function 2.1
    def swap(self,c, i, j):
        c = list(c)
        c[i], c[j] = c[j], c[i]
        return ''.join(c)

    # function 3
    def amendSentence(self,string):
        string = list(string)

        # Traverse the string
        for i in range(len(string)):

            # Convert to lowercase if its
            # an uppercase character
            if string[i] >= 'A' and string[i] <= 'Z':
                string[i] = chr(ord(string[i]) + 32)

                # Print space before it
                # if its an uppercase character
                if i != 0:
                    print(" ", end="")

                # Print the character
                print(string[i], end="")

            # if lowercase character
            # then just print
            else:
                print(string[i], end="")

    # function 4
    def removing_extra_spaces(self,input_string):
        output_string = []
        space_flag = False  # Flag to check if spaces have occured

        for index in range(len(input_string)):

            if input_string[index] != ' ':
                if space_flag == True:
                    if (input_string[index] == '.'
                            or input_string[index] == '?'
                            or input_string[index] == ','):
                        pass
                    else:
                        output_string.append(' ')
                    space_flag = False
                output_string.append(input_string[index])
            elif input_string[index - 1] != ' ':
                space_flag = True

        print(''.join(output_string))

    # function 5
    def replaceSpaces(self,string):
        MAX = 1000
        # Remove remove leading and trailing spaces
        string = string.strip()

        i = len(string)

        # count spaces and find current length
        space_count = string.count(' ')

        # Find new length.
        new_length = i + space_count * 2

        # New length must be smaller than length
        # of string provided.
        if new_length > MAX:
            return -1

        # Start filling character from end
        index = new_length - 1

        string = list(string)

        # Fill string array
        for f in range(i - 2, new_length - 2):
            string.append('0')

        # Fill rest of the string from end
        for j in range(i - 1, 0, -1):

            # inserts %20 in place of space
            if string[j] == ' ':
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index = index - 3
            else:
                string[index] = string[j]
                index -= 1

        return ''.join(string)

    # function 6
    def firstLetterWord(self,str):
        result = ""
        # Traverse the string.
        v = True
        for i in range(len(str)):
            # If it is space, set v as true.
            if (str[i] == ' '):
                v = True
            # Else check if v is true or not.
            # If true, copy character in output
            # string and set v as false.
            elif (str[i] != ' ' and v == True):
                result += (str[i])
                v = False
        return result

    # function 7
    def printSubsequences(self,str):
        n = len(str)
        opsize = int(pow(2, n - 1))

        for counter in range(opsize):
            for j in range(n):
                print(str[j], end="")
                if (counter & (1 << j)):
                    print(" ", end="")

            print("\n", end="")

    # function 8
    def printPattern(self,string):
        a1=c()
        n = len(string)

        # Buffer to hold the string
        # containing spaces

        # 2n - 1 characters and 1 string terminator
        buff = [0] * (2 * n)

        # Copy the first character as it is,
        # since it will be always
        # at first position
        buff[0] = string[0]

        a1.printPatternUtil(string, buff, 1, 1, n)
    # function 8.1
    def printPatternUtil(self,string, buff, i, j, n):
        a1 = c()
        if i == n:
            buff[j] = '&# 092;&# 048;'
            print (a1.toString(buff))
            return

        # Either put the character
        buff[j] = string[i]
        a1.printPatternUtil(string, buff, i + 1,
                         j + 1, n)

        # Or put a space followed by next character
        buff[j] = ' '
        buff[j + 1] = string[i]

        a1.printPatternUtil(string, buff, i + 1,
                         j + 2, n)
    # function 8.2
    def toString(self,List):
        s = ""
        for x in List:
            if x == '&# 092;&# 048;':
                break
            s += x
        return s

    # function 9






#Spacing :
a1 = c()
n3 = int(input('Please enter the function no:'))
if (n3 == 1):
    str = input('enter a input string here:')
    print(a1.removeSpaces(str))
elif (n3 == 2):
    str = input('enter a input string here:')
    s = a1.moveSpaceInFront(str);
    print(s);
elif (n3 == 3):
    str = input('enter a input string here:')
    a1.amendSentence(str);
elif (n3 == 4):
    str = input('enter a input string here:')
    a1.removing_extra_spaces(str);
elif (n3 == 5):
    str = input('enter a input string here:')
    print(a1.replaceSpaces(str));
elif (n3 == 6):
    str = input('enter a input string here:')
    print(a1.firstLetterWord(str));
elif (n3 == 7):
    str = input('enter a input string here:')
    a1.printSubsequences(str);
elif (n3 == 8):
    str = input('enter a input string here:')
    a1.printPattern(str);
else:
    print('Method not found')

