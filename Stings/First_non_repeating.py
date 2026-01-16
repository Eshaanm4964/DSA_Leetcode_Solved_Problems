def non_repeating_char(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.grt(ch,0)+1
    for ch in str:
        if freq[ch]==1:
            return ch 