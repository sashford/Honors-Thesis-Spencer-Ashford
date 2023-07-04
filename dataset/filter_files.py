import os

toppath = os.path.abspath(__file__)[:-16]
print(toppath)

noise = os.listdir(toppath + "/noise")
noiseless = os.listdir(toppath + "/noiseless")

while True:
   
   original_len = len(noise)

   for n, noise_file in enumerate(noise):
      for s, noiseless_file in enumerate(noiseless):
         if noise_file[-19:] == noiseless_file[-19:]:
            noise.pop(n)
            noiseless.pop(s)
            break
         
   final_len = len(noise)
   if original_len == final_len:
      break
   
print(noise)
print(noiseless)