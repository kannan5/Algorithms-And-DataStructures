def word_count(i, word, phrases):
    if i == -1:
        return 1

    count = 0

    for j in range(i, -1, -1):
        if word[j: i + 1] in phrases:
            count += word_count(j - 1, word, phrases)
    return count


def word_count_memo(i, word, phrases, cache):
    if i == -1:
        return 1
    if cache[i] != -1:
        return cache[i]
    count = 0
    for j in range(i, -1, -1):
        if word[j: i + 1] in phrases:
            count += word_count_memo(j - 1, word, phrases, cache)
    cache[i] = count
    return count

def word_count_tab(word, pharses):
    N = len(word)
    dp = [0 for _ in range(0, N+1)]
    dp[0] = 1
    for i in range(1, N+1):
        for j in range(i, 0, -1):
            if word[j -1: i] in phrases:
                dp[i] += dp[j - 1]
    return dp[N]


if __name__ == '__main__':
    word = "pineapplepenapple"
    phrases = {"apple", "pen", "applepen", "pine", "pineapple"}
    dp = [-1 for _ in range(0, len(word)+1)]
    print(word_count_memo(len(word), word, phrases, dp))
    print(word_count_tab(word, phrases))
