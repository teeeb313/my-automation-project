users = ['Dave', 'John', 'Sara']

data = ['Dave',  42, True]

emptylist = []

print("Dave" in data)

print(users[0])
print(users[-2])


print(users.index('Sara'))


print(users[0:2])

print(users[1:])

print(users[-3:-1])



print(len(data))


users.append('Elsa')
print(users)

users += ['Jason']
print(users)


users.extend(['Robert', 'Jimmy'])
print(users)

users += [('Ahmed')]
print(users)

users.append('Ahmed')
print(users)



users.insert(0,'Ahmed')
print(users)

users[2:2] = ['Eddie', 'Allex']
print (users)


users[1:3] = ['Robert', 'JPG']
print(users)

users.remove('Ahmed')
print(users)

print(users.pop())

del users[0]
print(users)


data.clear()
print(data)


users[1:2] = ['dave']

users.sort()
print(users)



users.sort(key=str.lower)
print(users)



nums = [4,42,78,1,5]

nums.reverse()
print(nums)


#nums.sort(reverse=True)
#print(nums)


print(sorted(nums, reverse=True))
print(nums)


numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)


print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)


mytuple = tuple(('Dave',43,True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')  

newtuple= tuple(newlist)     
print(newtuple)        

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

