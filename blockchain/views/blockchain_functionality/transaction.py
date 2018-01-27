"""
class Transaction

Created by Shibo Chen, Data:1/26/2018
University of Michigan, class of 2019
email: chshibo@umich.edu
"""

class Transaction(object):
    """Transaction class"""
    def __init__(self, sender, receiver, value):
        """
        Initialize transaction instance

        Parameters
        ----------
        sender : Int
            sender's id
        receiver : Int
            receiver's id
        value : Double
            value transfered from sender to receiver
        """
        self.sender = sender
        self.receiver = receiver
        self.value = value

    def __str__(self):
        """
        Return transaction String

        Returns
        -------
        transaction_str : String
            String of Transaction
        """
        transaction_dict = {}
        transaction_dict['sender'] = self.sender
        transaction_dict['receiver'] = self.receiver
        transaction_dict['value'] = self.value
        return transaction_dict.__str__()
