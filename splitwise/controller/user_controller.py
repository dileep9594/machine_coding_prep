class UserController(object):

    def __init__(self,UserService):
        self.userService = UserService

    def addUser(self,id,name):
        return self.userService.addUser(id,name)