class Solution:
    def groupThePeople(groupSizes):
        IDs = []
        result = []
        groupTypes = {}
        for i in range(len(groupSizes)):
            IDs.append(i)
        cont = True
        i = 0
        for x in groupSizes:
            if x not in groupTypes:
                groupTypes[x] = 1
            else:
                groupTypes[x] += 1
        groups = {}
        n = 0
        for x,n in enumerate(groupTypes):
            groups[n] = groupTypes[n]/n  # how many of each group there are
            n += 1
        for n,i in enumerate(groups):
            print(i)
            print(groups[i])
            for p in range(int(groups[i])):
                theseIDs = []
                for j in range(i):
                    theseIDs.append(IDs[0])
                    IDs.pop(0)
                result.append(theseIDs)
        print(groups)
        return result

sol = Solution
print(sol.groupThePeople([3,3,3,3,3,1,3]))

"""
Input:[3,3,3,3,3,1,3]
Output:[[0,1,2],[3,4,5],[6]]
Expected:[[5],[0,1,2],[3,4,6]]
"""