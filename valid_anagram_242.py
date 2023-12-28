

def isAnagram(s: str, t: str) -> bool:
        sett = set()
        count  = [0]*26
        for word in [s, t]:
            for c in word:
                count[ord('a') - ord(c)] += 1
            if tuple(count) in sett:
                return True
            sett.add(tuple(count))
            count = [0]*26
        return False

print(isAnagram('rat', 'car'))

def isAnagram2(s: str, t: str) -> bool:
        count_s, count_t = {}, {}

        if len(s) != len(t):
              return False

        for ch in s:
              count_s[ch] = 1 + count_s.get(ch, 0)
        for ch in t:
              count_t[ch] = 1 + count_t.get(ch, 0)
        for ch, count in count_s.items():
              if count != count_t.get(ch, 0):
                    return False
        return True

print(isAnagram('rat', 'car'))