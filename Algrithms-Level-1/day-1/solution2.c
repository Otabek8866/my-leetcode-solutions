int firstBadVersion(int n)
{
    int mid = 1 + n / 2;
    int start = 1;
    int end = n;

    while (mid != start)
    {
        if (!isBadVersion(mid))
        {
            if (isBadVersion(mid + 1))
            {
                return mid + 1;
            }
            else
            {
                start = mid;
                mid = start + (end - mid) / 2;
            }
        }
        else
        {
            end = mid;
            mid = start + (end - start) / 2;
        }
    }
    if (isBadVersion(mid))
        return mid;
    else
        return end;
}