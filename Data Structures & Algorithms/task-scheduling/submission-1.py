class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1
        max_freq = max(count.values())

        max_freq_count = 0
        for freq in count.values():
            if freq == max_freq:
                max_freq_count += 1

        ans = (max_freq - 1) * (n + 1) + max_freq_count
        return max(ans, len(tasks))
