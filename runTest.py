import argparse

from test.algorithms import AlgorithmsTester
from test.data_structures import DataStructuresTester
from test.graph_algorithms import GraphAlgorithmsTester
from test.graph_representations import GraphRepresentationsTester
from test.hash_tables import HashTablesTester
from test.sorting import SortingTester
from test.tree_traversals import TreeTraversalsTester
from test.tree_types import TreeTypesTester

# FOLDERS must match structure of test/ folder
# Any resemblance to structure of code/ folder is human-enforced for
# ease of finding things :)
FOLDERS = {
    'algorithms': (AlgorithmsTester, [
        'binary_search',
    ]),
    'data_structures': (DataStructuresTester, [
        'linked_lists',
    ]),
    'graph_algorithms': (GraphAlgorithmsTester, [
        'astar',
        'dijkstras',
        'kruskals',
    ]),
    'graph_representations': (GraphRepresentationsTester, [
        'adjacency_list',
        'matrix',
        'pointers',
    ]),
    'hash_tables': (HashTablesTester, [
        'bloom_filter',
        'hashmap',
    ]),
    'sorting': (SortingTester, [
        'merge_sort',
        'quick_sort',
    ]),
    'tree_traversals': (TreeTraversalsTester, [
        'bfs',
        'inorder',
        'preorder',
        'postorder',
    ]),
    'tree_types': (TreeTypesTester, [
        'bst',
        'heap',
        'trie',
    ]),
}

def main():
    parser = argparse.ArgumentParser(description='Determines which test to run.')
    subparsers = parser.add_subparsers(dest='folderName')
    for key in FOLDERS.keys():
        parser_a = subparsers.add_parser(key, help='Runs a test from %s.py'%(key))
        parser_a.add_argument('testName', type=str, choices=FOLDERS[key][1],
            help='Runs the test with this testName')
    args = parser.parse_args()

    folderObj = FOLDERS[args.folderName][0]()
    folderObj.runTest(args.testName)

if __name__ == '__main__':
    main()

