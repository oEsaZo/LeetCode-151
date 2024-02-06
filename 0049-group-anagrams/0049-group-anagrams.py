class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapA = defaultdict(list)
        for word in strs:
            sortw = ''.join(sorted(word))
            mapA[sortw].append(word)
        
        return(list(mapA.values()))
