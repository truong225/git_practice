print 'hello'

#Khai bao bien bang 1 lenh gan
a=1
a=[1,2,3]
a=[1,'Hello',3]

#Phep toan logic
x = 2
1 < x < 3 # True
10 < x < 20 # False
3 > x <= 2 # True
2 == x < 4 # True

#Toán tử kiểm tra phần tử trong một tập hợp: - in kiểm tra
#có tồn tại - not in kiểm không tồn tại
'good' in 'this is a greate example' # False
'good' not in 'this is a greate example' # True

#Hầuhết các cấu trúc điều khiển đều dựa vào thụt đầu dòng(indention) để tạo thành một block xử lý,
#thay vì sử dụng { … } như các ngôn ngữ khác (PHP, Javascript) ### 2.4.1.
#If…elif…else
if condition1 :
	indentedStatementBlockForTrueCondition1
elif condition2 :
	indentedStatementBlockForFirstTrueCondition2
elif condition3 :
	indentedStatementBlockForFirstTrueCondition3
elif condition4 :
	indentedStatementBlockForFirstTrueCondition4
else:
	indentedStatementBlockForEachConditionFalse

#Python không có cấu trúc switch … case

for iterating_var in sequence:
	statements(s)

for letter in 'Python': # First Example
	print 'Current Letter :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # Second Example
	print 'Current fruit :', fruit

print "Good bye!"

#while expression:
#	statement(s)
#Ví dụ:
count = 0
while (count < 9):
	print 'The count is:', count
	count = count + 1

print "Good bye!"

