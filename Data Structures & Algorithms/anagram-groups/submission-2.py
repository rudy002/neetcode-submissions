class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dico = {}
        
        for word in strs:
            w = "".join(sorted(word))
            if "".join(sorted(word)) in dico:
                dico[w].append(word)
            else:
                dico[w] = [word]
            
        return list(dico.values())