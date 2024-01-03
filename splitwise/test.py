import sys
sys.path.append('/Users/dileeppandey/machine_coding_prep')

from splitwise.controller.user_controller import UserController
from splitwise.controller.group_controller import GroupController
from splitwise.controller.bill_controller import BillController

from splitwise.services.bill_service import BillService
from splitwise.services.group_service import GroupService
from splitwise.services.user_service import UserService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser("user1" ,"dileep")
user2 = userController.addUser("user2" ,"dileeppandey")
user3 = userController.addUser("user3" ,"dileep3")
user4 = userController.addUser("user4" ,"dileep4")
user5 = userController.addUser("user5" ,"dileep5")

member =[user1,user2,user3,user4,user5]
group1 = groupController.addGroup('group1','avenger',member)

# print(group1.getMembers())

paidBy = {"user1" :500 , "user2" : 10,"user3" : 16,"user4" : 10,"user5" : 10 }
contribution = {"user1" :100 , "user2" : 100,"user3" : 100,"user4" : 100,"user5" : 100 }

bill = billController.addBill('bill' ,'group1',500,contribution,paidBy)

balance = billController.getUserBalance('user3')
print(balance)

