from splitwise.models.bill import Bill
from splitwise.services.bill_interface_service import BillServiceInterface


class BillService(BillServiceInterface) :
    billDetails = {}
    def addBill(self, id, groupId, amount, contribution, paidBy):
        bill = Bill() 
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill
        return bill

