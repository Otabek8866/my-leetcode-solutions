int lengthOfLongestSubstring(char *s)
{
    int map[128] = {0}, l = 0;
    char *end = s, *start = s;

    while (*end)
    {
        if (map[*end])
        {
            l = (end - start > l) ? end - start : l;
            while (*start != *end)
            {
                map[*start] = 0;
                start++;
            }
            end++;
            start++;
        }
        else
        {
            map[*end] = 1;
            end++;
        }
    }
    l = (end - start > l) ? end - start : l;
    return l;
}