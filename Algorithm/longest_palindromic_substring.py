# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:07:37 2018

@author: guoyunyi
"""
s = 'babad'
s = 'abaabd'
s = 'aaaa'
s = ''
palindromic_map1 = {}
palindromic_map2 = {}
for i in range(0, len(s)):
    j = 1
    while i-j >= 0 and i + j <= len(s)-1:
        if s[i-j] == s[i+j]:
            j = j + 1
        else:
            break    
    palindromic_map1[i] = j-1

for i in range(0, len(s)):
    j = 0
    while i-j >= 0 and i + j < len(s)-1:
        if s[i-j] == s[i+j+1]:
            j = j + 1
        else:
            break    
    palindromic_map2[i] = j
    
if len(palindromic_map1)==0:
    pal_str = s 
else:
    max_j1 = max(palindromic_map1.values())
    max_j2 = max(palindromic_map2.values())
    if 2*max_j1 +1 > 2*max_j2:
        keys = [k for k, v in palindromic_map1.items() if v == max_j1][0]
        pal_str = s[(keys-max_j1):(keys+max_j1+1)]
    else:
        keys = [k for k, v in palindromic_map2.items() if v == max_j2][0]
        pal_str = s[(keys-max_j2+1):(keys+max_j2+1)]
    
bool(palindromic_map1.values) 
palindromic_map
pal_s = s[(i-j-1) : (i+j-1)]