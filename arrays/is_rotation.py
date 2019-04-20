# check if a string s1 is rotation of another string s2, using isSubstring kind of api, only once!
# e.g. watertank if rotation of tankwater.
# Algorithm: if s1 = xy, then s2=yx. So s2 will be substring of xyxy, i.e. s2 will be substring of s1s1

s1 = 'watertank'
s2 = 'tankwater'

assert s2 in s1 + s1, "Should be True"

s2 = 'tankawter'
assert s2 not in s1 + s1, "Should be False"
