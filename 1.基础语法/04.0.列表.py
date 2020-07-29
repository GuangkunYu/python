"""
列表 [] ：一系列按照特定顺序排列的元素组成。
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0])
print(bicycles[0].title())

# 索引从0开始
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

# 使用列表中的各个值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表中添加元素
## append() 方法：在列表末尾添加元素
motorcycles.append('honda')
print(motorcycles)
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

## insert() 方法：在列表指定位置中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 从列表中删除元素
## del 语句删除任意位置元素
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

## pop() 方法：删除列表末尾的元素并返回这个值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

## pop(i)：弹出列表中任何位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)

## remove() 方法：根据元素值删除元素,只能删除第一个指定的值
motorcycles.remove('suzuki')
print(motorcycles)

# 组织列表
## sort() 方法： 对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

## sorted() 方法：对列表进行临时排序
