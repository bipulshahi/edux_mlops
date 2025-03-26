import Package_demo
#import Package_demo.file1
#import Package_demo.file2

#print(Package_demo.file1.show_output())
#print(Package_demo.file2.show_output())

from Package_demo.file1 import show_output as s1
from Package_demo.file2 import show_output as s2

print(s1())
print(s2())

from Package_demo.sub_pack_1 import sp_file_1
from Package_demo.sub_pack_1 import sp_file_2
from Package_demo.sub_pack_2 import sp_file_3

print(sp_file_1.show_output())
print(sp_file_2.show_output())
print(sp_file_3.show_output())