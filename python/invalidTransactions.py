from typing import List, Dict, Tuple


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        personTransactions: Dict = {}
        possiblyInvalids: List[str] = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                possiblyInvalids.append(transaction)
            elif name not in personTransactions.keys():
                personTransactions.update({name: [tuple([time, amount, city])]})
            else:
                sameNameDiffCity = set()
                for prevTransaction in personTransactions[name]:
                    if abs(prevTransaction[0] - time) <= 60 and prevTransaction[2] != city:
                        sameNameDiffCity.add(transaction)
                        sameNameDiffCity.add(name + "," + ",".join(str(data) for data in prevTransaction))
                for transaction in sameNameDiffCity:
                    possiblyInvalids.append(transaction)
                personTransactions[name].append(tuple([time, amount, city]))
                
        return (possiblyInvalids)

def checkTests(testPairs: List[Tuple[List[str], List[str]]]):
    for case in testPairs:
        result = Solution().invalidTransactions(case[0])
        expected = case[1]
        transactionsInResult = {trans: result.count(trans) for trans in result}
        transactionsInExpected = {trans: expected.count(trans) for trans in expected}
        if transactionsInResult != transactionsInExpected:
            print("---------------- K - R - S")
            allKeys = set([key for key in transactionsInResult.keys()] + [key for key in transactionsInExpected.keys()])
            for key in allKeys:
                print(f"{key} -- {transactionsInResult[key] if key in transactionsInResult.keys() else None} - {transactionsInExpected[key] if key in transactionsInExpected.keys() else None}")
            print(case[0])
            print("----------")
            continue
        print(f"{expected} passed")






testCases = [ # input, expected
        (["alice,20,800,mtv","alice,50,100,beijing"], ["alice,20,800,mtv","alice,50,100,beijing"]),
        (["alice,20,800,mtv","alice,50,1200,mtv"], ["alice,50,1200,mtv"]),
        (["alice,20,800,mtv","bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
        (["alice,20,1220,mtv","alice,20,1220,mtv"], ["alice,20,1220,mtv","alice,20,1220,mtv"]),
        (["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"], ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]),
        (["alice,20,800,mtv","bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
        (["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"], ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"])
            ]

checkTests(testCases)


#assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])) == set(["alice,20,800,mtv","alice,50,100,beijing"])
#assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"])) == set(["alice,50,1200,mtv"])
#assert set(Solution().invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"])) == set(["bob,50,1200,mtv"])
#assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])) == set(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])
#assert set(Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])) == set(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])

