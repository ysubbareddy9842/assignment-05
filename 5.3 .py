fh = open("sample_log.txt", "w") 
try: 
   fh.write("I love Python Programming!") 
finally: 
   fh.close()

# Sample code(2) Write using with statement 
with open("sample_log.txt", "w") as fh: 
   fh.write("I love Python even more!!")