class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dico = {}
        
        for word in strs:
            if "".join(sorted(word)) in dico:
                dico["".join(sorted(word))].append(word)
            else:
                dico["".join(sorted(word))] = [word]
            
        return list(dico.values())