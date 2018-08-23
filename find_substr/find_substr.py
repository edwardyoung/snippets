# Assume the function call_api() will fail due to a substring in the string
# posted to the API.  
# This script will find the substring causing the issue in O(n)

input_str = "kgebzymhpemavdrfodxpaztwfmypnddkclddcttxsyhzurphansweougcnbxwqfaetghddemdqpyfxqvddkobpuomoxwheyeeyjgnlaxouqodzohcowxnzuxvzqroncyvnkenmcgzohratiljfsntnzgqutujllrwktzyfnlkmyktdmpatushllldcpzaievppufblhtghqekdnduoxtvmmmtwsmprtjwfvpparweelzujdmcxjborfjcipqnvjgedxpbsrtsmtidpyyddrzgclkrhjxfsqfgoemigeopjybapdyirctmubatrkwsgzbzltqqobczhschbufybiuqgudrupkirzyioxqfkbwsfqjnkcdwabyqyisjfcdovyddpautvxtzhrnsycbttgdsialsvnutpzmrtwdmenayeyexwrpemguhmxfslislmftwnmoqzhdekhaqivbzxuzxuuizncixesxfyduxqgwklepwcxwmyiz"

def call_api(input):
    substr = "trkwsgzbzl"
    if substr in input:
        return True
    else:
        return False

count = 0
old_string = ""
bad_str = ""
while call_api(input_str):
    old_string = input_str
    input_str = input_str[1:]
    count += 1
    print str(count) + " " + input_str
    
while call_api(old_string):
    bad_str = old_string
    old_string = old_string[:-1]
    count += 1
    print str(count) + " " + old_string

print bad_str
