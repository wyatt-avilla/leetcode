from __future__ import annotations


class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        person_transactions: dict = {}
        possibly_invalids: list[str] = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                possibly_invalids.append(transaction)
            elif name not in person_transactions:
                person_transactions.update({name: [(time, amount, city)]})
            else:
                same_name_diff_city = set()
                for prev_transaction in person_transactions[name]:
                    if (
                        abs(prev_transaction[0] - time) <= 60
                        and prev_transaction[2] != city
                    ):
                        same_name_diff_city.add(transaction)
                        same_name_diff_city.add(
                            name
                            + ","
                            + ",".join(str(data) for data in prev_transaction),
                        )
                for transaction in same_name_diff_city:
                    possibly_invalids.append(transaction)
                person_transactions[name].append((time, amount, city))

        return possibly_invalids


def check_tests(test_pairs: list[tuple[list[str], list[str]]]) -> None:
    for case in test_pairs:
        result = Solution().invalidTransactions(case[0])
        expected = case[1]
        transaction_in_result = {trans: result.count(trans) for trans in result}
        transactions_in_expected = {trans: expected.count(trans) for trans in expected}
        if transaction_in_result != transactions_in_expected:
            print("---------------- K - R - S")
            all_keys = set(
                list(transaction_in_result) + list(transactions_in_expected),
            )
            for key in all_keys:
                print(
                    f"{key} -- {transaction_in_result.get(key)} - {transactions_in_expected.get(key)}",
                )
            print(case[0])
            print("----------")
            continue
        print(f"{expected} passed")


test_cases = [  # input, expected
    (
        ["alice,20,800,mtv", "alice,50,100,beijing"],
        ["alice,20,800,mtv", "alice,50,100,beijing"],
    ),
    (["alice,20,800,mtv", "alice,50,1200,mtv"], ["alice,50,1200,mtv"]),
    (["alice,20,800,mtv", "bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
    (
        ["alice,20,1220,mtv", "alice,20,1220,mtv"],
        ["alice,20,1220,mtv", "alice,20,1220,mtv"],
    ),
    (
        ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"],
        ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"],
    ),
    (["alice,20,800,mtv", "bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
    (
        [
            "alice,20,800,mtv",
            "bob,50,1200,mtv",
            "alice,20,800,mtv",
            "alice,50,1200,mtv",
            "alice,20,800,mtv",
            "alice,50,100,beijing",
        ],
        [
            "alice,20,800,mtv",
            "bob,50,1200,mtv",
            "alice,20,800,mtv",
            "alice,50,1200,mtv",
            "alice,20,800,mtv",
            "alice,50,100,beijing",
        ],
    ),
]

check_tests(test_cases)


# assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])) == set(["alice,20,800,mtv","alice,50,100,beijing"])
# assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"])) == set(["alice,50,1200,mtv"])
# assert set(Solution().invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"])) == set(["bob,50,1200,mtv"])
# assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])) == set(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])
# assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])) == set(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])
