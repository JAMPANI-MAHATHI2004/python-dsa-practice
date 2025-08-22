"""Write a program that removes all adjacent duplicate characters recursively in a give string. 
If removing duplicates results in new adjacent duplicates, those should also be remove recursively.
Example:
Input: "azxxzy"        Output: "ay" """

def remove_adjacent_duplicates(s: str) -> str:
    # Helper recursive function
    def recursive_remove(s):
        n = len(s)
        i = 0
        result = []
        removed = False
        
        while i < n:
            # If current char equals next char, skip all duplicates
            if i < n - 1 and s[i] == s[i + 1]:
                removed = True
                # Skip all consecutive same chars
                while i < n - 1 and s[i] == s[i + 1]:
                    i += 1
            else:
                result.append(s[i])
            i += 1
        
        new_str = "".join(result)
        
        # If we removed something, call recursively again
        if removed:
            return recursive_remove(new_str)
        else:
            return new_str
    
    return recursive_remove(s)


# Example test
print(remove_adjacent_duplicates(input("enter:")))
