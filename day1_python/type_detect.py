Sample=input("Write anything you want: ")
try:
    Sample=int(Sample)
   
  
except:
    pass

Types= type(Sample)
print(f'Value:{Sample}')
print("Type:",Types.__name__)