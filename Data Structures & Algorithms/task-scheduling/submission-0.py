class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1
        max_freq = max(count.values())

        max_freq_count = sum(1 for freq in count.values() if freq == max_freq)
        ans = (max_freq - 1) * (n + 1) + max_freq_count

        return max(ans, len(tasks))
