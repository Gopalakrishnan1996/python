from collections import defaultdict


class l:
    # reverse string format
    def descOrder(self, s):
        s.sort(reverse=True)
        str1 = ''.join(s)
        print(str1)

    #alternate sorting
    MAX = 26

    def alternateSort(self,s):
        l1 = l()
        n = len(s)

        # Count occurrences of
        # individual lower case and
        # upper case characters
        lCount = [0 for i in range(l1.MAX)]
        uCount = [0 for i in range(l1.MAX)]
        s = list(s)

        for i in range(n):
            if (s[i].isupper()):
                uCount[ord(s[i]) -
                       ord('A')] += 1
            else:
                lCount[ord(s[i]) -
                       ord('a')] += 1

        # Traverse through count
        # arrays and one by one
        # pick characters. Below
        # loop takes O(n) time
        # considering the MAX
        # is constant.
        i = 0
        j = 0
        k = 0

        while (k < n):
            while (i < l1.MAX and
                   uCount[i] == 0):
                i += 1
            if (i < l1.MAX):
                s[k] = chr(ord('A') + i)
                k += 1
                uCount[i] -= 1
            while (j < l1.MAX and
                   lCount[j] == 0):
                j += 1
            if (j < l1.MAX):
                s[k] = chr(ord('a') + j)
                k += 1
                lCount[j] -= 1

        print("".join(s))

    def printInSortedOrder(self,arr, n):
        index = [0] * n
        for i in range(n):
            index[i] = i
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):

                # with the help of 'index[]'
                # strings are being compared
                if (arr[index[min]] > arr[index[j]]):
                    min = j
            # index of the smallest string is placed
        # at the ith index of 'index[]'
        if (min != i):
            index[min], index[i] = index[i], index[min]
        # printing strings in sorted order
        for i in range(n):
            print(arr[index[i]], end=" ")

    def sortString(self,str, n):

        # To store the final sorted string
        new_str = ""
        # for each character 'i'
        for i in range(ord('a'), ord('z') + 1):
            # if character 'i' is present at a particular
            # index then add character 'i' to 'new_str'
            for j in range(n):
                if (str[j] == chr(i)):
                    new_str += str[j]
        # required final sorted string
        return new_str

    def arrangeString(self,string):
        MAX_CHAR = 26
        char_count = [0] * MAX_CHAR
        s = 0
        for i in range(len(l.string)):
            if l.string[i] >= "A" and l.string[i] <= "Z":
                l.char_count[ord(l.string[i]) - ord("A")] += 1
            else:
                l.s += ord(l.string[i]) - ord("0")
        res = ""
        for i in range(MAX_CHAR):
            ch = chr(ord("A") + i)
            # Append the current character
            # in the string no. of times it
            # occurs in the given string
            while char_count[i]:
                res += ch
                char_count[i] -= 1
        # Append the sum of integers
        if s > 0:
            res += str(s)
        # return resultant string
        return res

    # Calculating factorial
    # of a number
    def factorial(self,n):
        f = 1

        for i in range(1, n + 1):
            f = f * i
            return f

    # Method to find total
    # number of permutations
    def calculateTotal(self,temp, n):
        f = l.factorial(n)
        # Building Map to store
        # frequencies of all
        # characters.
        hm = defaultdict(int)
        for i in range(len(temp)):
            hm[temp[i]] += 1
        # Traversing map and
        # finding duplicate elements.
        for e in hm:
            x = hm[e]
        if (x > 1):
            temp5 = l.factorial(x)
            f //= temp5
        return f

    def nextPermutation(self,temp):
        # Start traversing from
        # the end and find position
        # 'i-1' of the first character
        # which is greater than its successor
        for i in range(len(temp) - 1, 0, -1):
            if (temp[i] > temp[i - 1]):
                break
        # Finding smallest character
        # after 'i-1' and greater
        # than temp[i-1]
        min = i
        x = temp[i - 1]
        for j in range(i + 1, len(temp)):
            if ((temp[j] < temp[min]) and (temp[j] > x)):
                min = j
            # Swapping the above
        # found characters.
        temp[i - 1], temp[min] = (temp[min], temp[i - 1])
        # Sort all digits from
        # position next to 'i-1'
        # to end of the string
        temp[i:].sort()
        # Print the String
        print(''.join(temp))

    def printAllPermutations(self,s):

        # Sorting String
        temp = list(s)
        temp.sort()
        # Print first permutation
        print(''.join(temp))
        # Finding the total permutations
        total = l.calculateTotal(temp, len(temp))
        for i in range(1, total):
            l.nextPermutation(temp)


l1 = l()

# if __name__ == "__main__":
a = int(input("Please enter the function no:"))
if (a == 1):
    n = list(input('enter a input here:'))
    l1.descOrder(n)
elif (a == 2):
    str = input("enter a input here:")
    print(l1.alternateSort(str))
elif (a == 3):
    arr = list(input('enter a list item here'))
    n = 4
    l1.printInSortedOrder(arr, n)
elif (a == 4):
    str = input("enter your string :")
    n = len(str)
    print(l1.sortString(str, n))
elif (a == 5):
    string = input("enter a string here:")
    print(l.arrangeString(string))
elif (a == 6):
    s = input("enter a string:")
    l1.printAllPermutations(s)
else:
    print('Method not found')
