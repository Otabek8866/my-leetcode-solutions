/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *middleNode(struct ListNode *head)
{
    struct ListNode *middle = head;
    uint8_t i = 0;
    while (head != NULL)
    {
        if (i % 2 == 1)
            middle = middle->next;
        head = head->next;
        i++;
    }
    return middle;
}