# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       #t = x     
       #x = y
       #y = t%y
       x, y = y, x%y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)