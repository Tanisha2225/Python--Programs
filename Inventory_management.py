p = ["Apple","Banana","Mango","Orange","Pineapple"]
def add_product(items):
    p.append(items)
    print(p)

s = input("Enter the new item:")
add_product(s)

product = input("Search the item:")

if product in p:
    print("Product found\n")
else:
    print("Product not found.\n")

n = input("Remove the item:")
p.remove(n)

print(p)

