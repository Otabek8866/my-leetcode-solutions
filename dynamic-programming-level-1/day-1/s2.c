int tribonacci(int n)
{
    int seq[38];
    seq[0] = 0;
    seq[1] = 1;
    seq[2] = 1;
    for (int i = 3; i <= n; i++)
        seq[i] = seq[i - 1] + seq[i - 2] + seq[i - 3];
    return seq[n];
}