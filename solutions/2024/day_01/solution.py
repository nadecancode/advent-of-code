# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import (
    IntSolution,
    IntSplitSolution,
    StrSplitSolution,
    TextSolution,
    answer
)

class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2430334)
    def part_1(self) -> int:
        A = []
        B = []

        for line in self.input:
            a = ""
            b = ""

            for i in range(len(line)):
                if line[i] == ' ':
                    break

                a += line[i]

            for i in range(len(line) - 1, -1, -1):
                if line[i] == ' ':
                    break

                b += line[i]

            b = "".join(reversed(b))

            a = int(a)
            b = int(b)

            A.append(a)
            B.append(b)

        A.sort()
        B.sort()

        ans = 0
        for i in range(len(A)):
            ans += abs(A[i] - B[i])

        return ans

    @answer(28786472)
    def part_2(self) -> int:
        from collections import defaultdict

        A = []
        freq = defaultdict(int)
        for line in self.input:
            a = ""
            b = ""

            for i in range(len(line)):
                if line[i] == ' ':
                    break

                a += line[i]

            for i in range(len(line) - 1, -1, -1):
                if line[i] == ' ':
                    break

                b += line[i]

            b = "".join(reversed(b))

            a = int(a)
            b = int(b)

            A.append(a)
            freq[b] += 1

        ans = 0
        for a in A:
            ans += a * freq[a]

        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
