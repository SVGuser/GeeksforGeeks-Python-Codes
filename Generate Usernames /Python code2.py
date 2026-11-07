class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        string = {}
        res = []
        for x in arr:
            if x not in string:
                res.append(x)
                string[x] = 1
            else:
                count = string[x]
                new_string = x + str(count)
                while (new_string in string) or (new_string in reserved):
                    count += 1
                    new_string = x + str(count)
                res.append(new_string)
                string[x] = count + 1
                string[new_string] = 1
        return res
