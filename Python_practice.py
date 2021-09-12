print("Hello World")
type(3)
type(73.81)
print(8+22*2-4)
counties =["Arapahoe","Denver","Jefferson"]
print(counties[-1])
print(len(counties))
counties.insert(1,"Arizona")
print(counties)
counties.insert(2,"Jefferson")
print(counties)
counties.remove("Arapahoe")
print(counties)
counties.remove("Jefferson")
print(counties)
counties.pop(2)
counties[1]="Arizona"
print(counties)
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
counties_dict = {"Arapahoe": 42                                                                                                                                                                                                                                                                                                         , "Denver": 463353, "Jefferson": 432438}  
for voters in counties_dict.values():
    print(voters) 
for county in counties_dict.keys():
    print(counties_dict[county])
for county in counties_dict:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    print(county)
    print(counties_dict[county])
    print(county + " has " + str(counties_dict[county]) + " registered voters. ")
x = 0
while x <= 5:
    print(x)
    x = x + 1


