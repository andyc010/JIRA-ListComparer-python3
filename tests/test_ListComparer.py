import unittest
import os
from JIRA_ListComparer_Python3 import jiraListComparer
from JIRA_ListBuilder_Python3 import jiraListBuilder

# use smaller test file
fileAddressSmall = \
    "E:\\Development_projects\\PycharmProjects\\JIRA_List_Comparer_Python3\\tests\\TEST_small_list.xml"
# use larger test file
fileAddressLarge = \
    "E:\\Development_projects\\PycharmProjects\\JIRA_List_Comparer_Python3\\tests\\TEST_large_list.xml"
fileAddressExact = \
    "E:\\Development_projects\\PycharmProjects\\JIRA_List_Comparer_Python3\\tests\\TEST_exact_list.xml"
fileAddressNone = \
    "E:\\Development_projects\\PycharmProjects\\JIRA_List_Comparer_Python3\\tests\\TEST_no_list.xml"

class MyTestCase(unittest.TestCase):
    def test_ListDifference(self):
        listComparer = jiraListComparer(fileAddressSmall, fileAddressLarge)

        testList = listComparer.showListDifference(fileAddressSmall, fileAddressLarge)

        # set up the list difference
        listBuilder = jiraListBuilder()
        listDifference = listBuilder.createList(listBuilder.getRoot(fileAddressExact))

        self.assertCountEqual(testList, listDifference, msg="None")

    def test_ListUnique(self):
        listCompare = jiraListComparer(fileAddressNone, fileAddressLarge)

        testList = listCompare.showListAllUniqueItems(fileAddressNone, fileAddressLarge)

        # set up the list with all unique items (in this case, it is the one with all items)
        listBuild = jiraListBuilder()
        listAllUnique = listBuild.createList(listBuild.getRoot(fileAddressLarge))

        self.assertCountEqual(testList, listAllUnique, msg="None")

if __name__ == '__main__':
    unittest.main()
