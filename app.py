#class for a single account

class User:
 
   '''Class for account'''
 
   def __init__(self, account, username, password=' '):
 
       '''
       Initialize a new accounts class
       '''
       self.account = account
       self.username = username
       self.password = password

   def match(self, filter):
        '''
        Check match when search is done.
        '''  
        return filter in self.username or self.password

#class for all the accounts created

class Credentials:   
    '''
    Class for all the accounts created
    '''
 
    def __init__(self):
     
        '''
        Initialization of the allacount list
        '''
        self.accounts = []

    def new_account(self, account, username, password=''): #initialization of the account
 
       '''
       Creates the new accounts
       '''
       self.accounts.append(User(account, username, password))

    def search_account(self, filter):
     
      '''
      Searches the allacounts and find the match
      '''
      return [ account for account in self.accounts if account.match(filter)] #returns the value of the searched account
