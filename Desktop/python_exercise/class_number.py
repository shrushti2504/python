import functools
class number:
    def __init__(self,numbers):
        self.numbers=numbers

    def get(self):
        return self.numbers

    def change_values(self,func:lambda x : x):
        new_numbers=[]
        change_map=map(func,self.numbers)
        new_numbers = list(change_map)
        return new_numbers
    
    def filter_values(self,filter_func:lambda x:x):
        filter_list= []
        filter_val = filter(filter_func,self.numbers)
        filter_list=list(filter_val)
        return filter_list
    
    def compound_numbers(self, reduce_func: lambda compound, d: compound + d):
        compounds = functools.reduce(reduce_func,self.numbers)
        return compounds

    def sort(self):
        n=len(self.numbers)
        for i in range(n):
            for j in range(i+1):
                if(self.numbers[j]>self.numbers[i]):
                    self.numbers[j],self.numbers[i]=self.numbers[i],self.numbers[j]
        return self.numbers

if __name__ == "__main__": 
    num = [2, 5, 1, 66, 22, 11, 10]

n1=number(num)
print("original value is : ",n1.get())

func=lambda x: x+x
print("new values are : ",n1.change_values(func=func))

filter_func=lambda x:x%2==0
print("filter value is : ",n1.filter_values(filter_func=filter_func))

compound_val = lambda a,b:a+b
print("compount value is :",n1.compound_numbers(reduce_func=compound_val))

print("sort is = ",n1.sort())

