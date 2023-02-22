def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0,len(text),tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words,words[1:]+['']):