class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

def reorder_list(lst):
	len_of_ll, last_node = get_len(lst)
	print len_of_ll
	return helper(lst, last_node, 0, len_of_ll)

def get_len(lst):
	counter = 1
	while lst.next:
		counter += 1
		lst = lst.next
	return counter, lst

def helper(left_node, right_node, left, right):
	if left >= right: return
	print lst[left], lst[right]
	helper(lst, left+1, right-1)



reorder_list(one)

print "####"
node = one
while node:
	print node.val
	node = node.next

