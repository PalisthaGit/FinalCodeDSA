d = 256  # number of characters in the input alphabet

def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0    # hash value for pattern
    t = 0    # hash value for text
    h = 1
    i = 0
    j = 0

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m-1):
        h = (h*d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n-m+1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            if j == m-1:
                print("Pattern is found at index: " + str(i))

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < n-m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            # We might get negative values of t, converting it to positive
            if t < 0:
                t += q

text = "ABCCDDAEFG"
pattern = "CDD"
q = 101  # A prime number
search(pattern, text, q)
