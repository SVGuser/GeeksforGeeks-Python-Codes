class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        seen = {}
        res = []
        for x in arr:
            if x not in seen:
                res.append(x)
                seen[x] = 1
            else:
                count = seen[x]
                new_string = f"{x}{count}"
                while new_string in seen or new_string in reserved:
                    count += 1
                    new_string = f"{x}{count}"
                res.append(new_string)
                seen[x] = count + 1
                seen[new_string] = 1
        return res
