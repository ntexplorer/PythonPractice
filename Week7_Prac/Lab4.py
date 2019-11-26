# Capture any 0 or more occurence of a, then of b, then of c... and so on, until the en
s = 'This is not an empty string. We are beefily learning regex, it is hard.'
abc = r'\ba*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*\b'
print(set([k for k in re.findall(abc,s) if k]))
# Match words with 'bze' at the end of a sentence
s = 'It was very cold, almost subzero. This is abzelutely great.'
bzedot = r'\w*bze\w*\.'
print(re.findall(bzedot,s))
# Match words with 'sp' and at least two occurrences of letter 'r'
4# The possibilities are:
# 1) sp followed by two occurrences of r
# 2) r followed by sp followed by r
# 3) two occurences of r followed by sp
# Note that these rs do not necessarily have to apear together
sp_rr = r'\b(\w*sp\w*r\w*r\w*|\w*r\w*sp\w*r\w*|\w*r\w*r\w*sp\w*)\b'
s = 'He grasped his sparring, who was soft as a raspberry.'
print(re.findall(sp_rr,s))
# Match words written only with the top row of the keyboard
# At least one occurence of either q,w,e... and so on.
# This only matches words with all characters belonging to the top row of the keyboard
s = 'Their repertoire was as good as a meal of port and trout'
top = r'\b[qwertyuiop]+\b'
print('The longest possible word is: ',max(re.findall(top,s), key= lambda x:len(x)))
