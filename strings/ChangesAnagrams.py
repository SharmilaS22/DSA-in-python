'''
author: Sharmila S
Date: 21-04-2021

Topic: Changes to be made to form Anagram 
'''

# Algorithm


def FindChanges(str1, str2):

    count = 0
    notPresent = []

    for i in range(0, len(str1)):

        if (str1[i] in notPresent): # to avoid searching again for same alphabet
            count += 1             # as zero occurance of the letter
            continue
        
        flag = 0
        # check elem in str2 if found del the char from str2
        # if not found count++ add to not present
        for j in range(0, len(str2)):

            if (str1[i] == str2[j]):
                str2 = str2[:j] + str2[j+1:] #del the character
                flag = 1 # set flag so not found
                break

        if (flag == 0):
            count += 1
            notPresent.append(str1[i])
    print(str2)
    # return count + number of remaining char in str2
    return count + len(str2)

s1 = 'abcd'
s2 = 'aecdf'

# del b
# add e and f
        
print(FindChanges(s1, s2))