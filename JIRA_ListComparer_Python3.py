from JIRA_ListBuilder_Python3 import jiraListBuilder

"""
    Given two JIRA XML files -> their filenames & locations, this class helps generate
    lists with values that are not common in either file. 
"""

class jiraListComparer:
    
    """ set variables for filenames """
    firstFileAddress = ""
    secondFileAddress = ""
    
    """ constructor """
    def __init__(self, firstFile, secondFile):
        self.firstFileAddress = firstFile
        self.secondFileAddress = secondFile
        
    def showListDifference(self, firstFileAddress, secondFileAddress):
        """ return a set of items that is not in the first (that has the larger amount of items) list """
        listBuilder = jiraListBuilder()
        firstList = listBuilder.createList(listBuilder.getRoot(firstFileAddress))
        secondList = listBuilder.createList(listBuilder.getRoot(secondFileAddress))
        if len(firstList) > len(secondList):
            set_1 = set(firstList)
            set_2 = set(secondList)
        else:
            set_1 = set(secondList)
            set_2 = set(firstList)
            
        set_difference = set_1 - set_2
        
        return set_difference
    
    def showListAllUniqueItems(self, firstFileAddress, secondFileAddress):
        """ return a set of items that are unique from both lists """
        listBuilder = jiraListBuilder()
        firstList = listBuilder.createList(listBuilder.getRoot(firstFileAddress))
        secondList = listBuilder.createList(listBuilder.getRoot(secondFileAddress))

        set_unique_items = set(firstList).symmetric_difference(set(secondList))

        return set_unique_items