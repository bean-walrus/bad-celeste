import copy

def permuteWithNoAdjacent(L):
    a = copy.copy(L)
    return solve(a, [])
    
def solve(L, toReturn):
    if L == []:
        return toReturn
    else:
        for i in range(len(L)):
            if isLegal(toReturn, L[i]):
                toReturn.append(L[i])
                L.pop(i)
                maybeSolved = solve(L, toReturn)
                if maybeSolved != None:
                    return maybeSolved
                L.insert(i, toReturn.pop())
        return None
    
def isLegal(toReturn, val):
    return toReturn == [] or abs(toReturn[len(toReturn) - 1] - val) != 1

def isValidPermutation(L):
    return all(abs(L[i] - L[i+1]) != 1 for i in range(len(L)-1))

result = permuteWithNoAdjacent([1, 4, 6])
assert result is not None
assert sorted(result) == [1, 4, 6]
assert isValidPermutation(result)

# ❌ Should return None (no valid permutation exists)
assert permuteWithNoAdjacent([1, 2]) is None
assert permuteWithNoAdjacent([1, 2, 3]) is None

# ✅ Edge cases
assert permuteWithNoAdjacent([]) == []
assert permuteWithNoAdjacent([5]) == [5]

# ✅ Another valid test
result = permuteWithNoAdjacent([2, 4, 6])
assert result is not None
assert sorted(result) == [2, 4, 6]
assert isValidPermutation(result)

print("All tests passed!")