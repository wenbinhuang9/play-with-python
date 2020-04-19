import re


## explore re compile

pat = re.compile("1001")

## match function always starts match from the beginning of the string, so 001 can not be matched here
match_obj = re.match(pat, "01001")
print match_obj

## can be matched
match_obj = re.match(pat, "1001")
print match_obj, match_obj.string

## find the first one being matched, unlike match function, the search function don't need to match from the beginning
match_obj = re.search(pat, "01001")
print match_obj, match_obj.groups()

##return all non-overlapping matches of pattern. for 1001001, there are two sustrings of 1001, but they are overlapping ,
# so only one 1001 is returned
match_obj_list = re.findall(pat, "1001001")
print match_obj_list

## two non-overlapping 1001, both of which be returned
match_obj_list = re.findall(pat, "10011001")
print match_obj_list
