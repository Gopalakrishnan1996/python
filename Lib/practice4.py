from locale import str


class d:
    MAX = 256
    #function 1
    def areAnagram(self,str1, str2):
        NO_OF_CHARS = 256
        # Create two count arrays and initialize all values as 0
        count1 = [0] * NO_OF_CHARS
        count2 = [0] * NO_OF_CHARS

        # For each character in input strings, increment count
        # in the corresponding count array
        for i in str1:
            count1[ord(i)] += 1

        for i in str2:
            count2[ord(i)] += 1

        # If both strings are of different length. Removing this
        # condition will make the program fail for strings like
        # "aaca" and "aca"
        if len(str1) != len(str2):
            return 0

        # Compare count arrays
        # for i in xrange(NO_OF_CHARS):
        #     if count1[i] != count2[i]:
        #         return 0

        return 1

    # function 2
    # are same, otherwise false.
    def compare(self,arr1, arr2):
        a1 = d()
        for i in range(a1.MAX):
            if arr1[i] != arr2[i]:
                return False
        return True

    # function 2.1
    # permutations of pat[] in txt[]
    def search(self,pat, txt):
        a1 = d()
        M = len(pat)
        N = len(txt)

        # countP[]:  Store count of
        # all characters of pattern
        # countTW[]: Store count of
        # current window of text
        countP = [0] * a1.MAX

        countTW = [0] * a1.MAX

        for i in range(M):
            countP[ord(pat[i])] += 1
            if(N > i):
             countTW[ord(txt[i])] += 1

        # Traverse through remaining
        # characters of pattern
        for i in range(M, N):

            # Compare counts of current
            # window of text with
            # counts of pattern[]
            if a1.compare(countP, countTW):
                print("Found at Index", (i - M))

            # Add current character to current window
            countTW[ord(txt[i])] += 1

            # Remove the first character of previous window
            countTW[ord(txt[i - M])] -= 1

        # Check for the last window in text
        if a1.compare(countP, countTW):
            print("Found at Index", N - M)

    # FUNCTION 3
    def areAnagram1(self,str1: str, str2: str) -> bool:
        NO_OF_CHARS = 256
        # Create two count arrays and
        # initialize all values as 0
        count = [0] * NO_OF_CHARS
        i = 0

        # For each character in input strings,
        # increment count in the corresponding
        # count array
        while i < len(str1) and i < len(str2):
            count[ord(str1[i])] += 1
            count[ord(str2[i])] -= 1
            i += 1

        # If both strings are of different length.
        # Removing this condition will make the program
        # fail for strings like "aaca" and "aca"
        if len(str1) != len(str2):
            return False

        # See if there is any non-zero value
        # in count array
        for i in range(NO_OF_CHARS):
            if count[i]:
                return False
            return True

    # FUNCTION 3.1
    def findAllAnagrams(self,arr: list, n: int):
        a1 = d()
        for i in range(n):
            for j in range(i + 1, n):
                if a1.areAnagram1(arr[i], arr[j]):
                    print(arr[i], "is anagram of", arr[j])

    # Function 4
    def remAnagram(self,str1, str2):
        CHARS = 26
        # make hash array for both string
        # and calculate
        # frequency of each character
        count1 = [0] * CHARS
        count2 = [0] * CHARS

        # count frequency of each character
        # in first string
        i = 0
        while i < len(str1):
            count1[ord(str1[i]) - ord('a')] += 1
            i += 1

        # count frequency of each character
        # in second string
        i = 0
        while i < len(str2):
            count2[ord(str2[i]) - ord('a')] += 1
            i += 1

        # traverse count arrays to find
        # number of characters
        # to be removed
        result = 0
        for i in range(26):
            result += abs(count1[i] - count2[i])
        return result

    # Function 5
    # k-anagram or not
    def arekAnagrams(self,str1, str2, k):
        MAX_CHAR = 26
        # If both strings are not of equal
        # length then return false
        n = len(str1)
        if (len(str2) != n):
            return False

        count1 = [0] * MAX_CHAR
        count2 = [0] * MAX_CHAR

        # Store the occurrence of all
        # characters in a hash_array
        for i in range(n):
            count1[ord(str1[i]) -
                   ord('a')] += 1
        for i in range(n):
            count2[ord(str2[i]) -
                   ord('a')] += 1

        count = 0

        # Count number of characters that
        # are different in both strings
        for i in range(MAX_CHAR):
            if (count1[i] > count2[i]):
                count = count + abs(count1[i] -
                                    count2[i])

        # Return true if count is less
        # than or equal to k
        return (count <= k)

    # Function 6
    def bit_anagram_check(self,a, b):
        SIZE = 8
        # Find reverse binary representation of a
        # and store it in binary_a[]
        global size
        i = 0
        binary_a = [0] * SIZE
        while (a > 0):
            binary_a[i] = a % 2
            a //= 2
            i += 1

        # Find reverse binary representation of b
        # and store it in binary_a[]
        j = 0
        binary_b = [0] * SIZE
        while (b > 0):
            binary_b[j] = b % 2
            b //= 2
            j += 1

        # Sort two binary representations
        binary_a.sort()
        binary_b.sort()

        # Compare two sorted binary representations
        for i in range(SIZE):
            if (binary_a[i] != binary_b[i]):
                return 0
        return 1

    # Function 7
    def countOfAnagramSubstring(self,s):
        # Returns total number of anagram
        # substrings in s
        n = len(s)
        mp = dict()

        # loop for length of substring
        for i in range(n):
            sb = ''
            for j in range(i, n):
                sb = ''.join(sorted(sb + s[j]))
                mp[sb] = mp.get(sb, 0)

                # increase count corresponding
                # to this dict array
                mp[sb] += 1

        anas = 0

        # loop over all different dictionary
        # items and aggregate substring count
        for k, v in mp.items():
            anas += (v * (v - 1)) // 2
        return anas

    # Function 8
    def countManipulations(self,s1, s2):

        count = 0

        # store the count of character
        char_count = [0] * 26

        for i in range(26):
            char_count[i] = 0

        # iterate though the first String
        # and update count
        for i in range(len(s1)):
            char_count[ord(s1[i]) -
                       ord('a')] += 1

        # iterate through the second string
        # update char_count.
        # if character is not found in
        # char_count then increase count
        for i in range(len(s2)):
            char_count[ord(s2[i]) - ord('a')] -= 1

        for i in range(26):
            if char_count[i] != 0:
                count += abs(char_count[i])

        return count / 2

    # Function 9


#Anagram :
a1 = d()
n3 = int(input('Please enter the function no:'))
if (n3 == 1):
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    print(a1.areAnagram(str,str1))
elif (n3 == 2):
    # txt = "BACDGABCDA"
    # pat = "ABCD"
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    a1.search(str, str1)
elif (n3 == 3):
    arr = ["geeksquiz", "geeksforgeeks",
           "abcd", "forgeeksgeeks", "zuiqkeegs"]
    n = len(arr)
    a1.findAllAnagrams(arr, n)
elif (n3 == 4):
    # str1 = "bcadeh"
    # str2 = "hea"
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    print(a1.remAnagram(str,str1))
elif (n3 == 5):
    # str1 = "anagram"
    # str2 = "grammar"
    # k = 2
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    k = int(input('enter a input string here:'))
    if (a1.arekAnagrams(str, str1, k)):
        print("Yes")
    else:
        print("No")
elif (n3 == 6):
    # a = 8
    # b = 4
    str = int(input('enter a input string here:'))
    str1 = int(input('enter a input string here:'))
    print(a1.bit_anagram_check(str,str1))
elif (n3 == 7):
    # str1 = "xyyx"
    str = input('enter a input string here:')
    print(a1.countOfAnagramSubstring(str))
elif (n3 == 8):
    # s1 = "ddcf"
    # s2 = "cedk"
    str = input('enter a input string here:')
    str1 = input('enter a input string here:')
    print(a1.countManipulations(str, str1))
else:
    print('Method not found')