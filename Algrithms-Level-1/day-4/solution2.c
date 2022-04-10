

char *reverseWords(char *s)
{
    int i = 0;
    int j = 0;
    int k = 0;
    char ch = s[k];
    char tmp;
    while (1)
    {
        if ((ch == ' ') || (ch == '\0'))
        {
            j = k - 1;
            while (i < j)
            {
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
                i++;
                j--;
            }
            i = k + 1;
        }
        if (ch == '\0')
            break;
        k++;
        ch = s[k];
    }
    return s;
}