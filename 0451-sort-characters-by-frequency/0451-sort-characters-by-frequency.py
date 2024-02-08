class Solution:
    def frequencySort(self, s: str) -> str:
       freq = Counter(s)

       sorted_chr = sorted(freq, key = freq.get, reverse = True)

       sorted_str = ''.join( [char*freq[char] for char in sorted_chr])
       return sorted_str