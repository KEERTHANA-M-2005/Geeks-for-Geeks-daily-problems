# You are given an array arr[] of size n, where arr[i] represents the number of soldiers in the i-th troop. You are also given an integer k. A troop is considered "lucky" if its number of soldiers is a multiple of k. Find the minimum total number of soldiers to add across all troops so that at least ⌈n / 2⌉ troops become lucky.

def minSoldiers(arr, k):
    n = len(arr)
    target = (n+1) // 2
    
    lucky_count = sum(1 for x in arr if x % k == 0)
    if lucky_count >= target:
        return 0
    
    costs = [k-(x%k)  for x in arr if x % 2 != 0]
    costs.sort()
    
    need = target - lucky_count
    return sum(costs[:need])

arr = []
n = int(input("How many troops are there? "))
for i in range(n):
    soldiers = int(input(f"Enter number of soldiers in troop {i+1}: "))
    arr.append(soldiers)

k = int(input("Enter k value: "))

result = minSoldiers(arr, k)
print("Minimum soldiers to add:", result)