// https://leetcode.com/problems/simple-bank-system/

struct Bank {
    n: i32,
    account_balances: Vec<i64>,
}

impl Bank {
    fn is_valid_account(&self, account_id: i32) -> bool {
        account_id > 0 && account_id <= self.n
    }

    fn new(balance: Vec<i64>) -> Self {
        Bank {
            n: i32::try_from(balance.len()).expect("problem constraints"),
            account_balances: std::iter::once(0).chain(balance).collect(),
        }
    }

    fn transfer(&mut self, account1: i32, account2: i32, money: i64) -> bool {
        if self.is_valid_account(account1)
            && self.is_valid_account(account2)
            && self.account_balances[account1 as usize] >= money
        {
            self.account_balances[account1 as usize] -= money;
            self.account_balances[account2 as usize] += money;
            true
        } else {
            false
        }
    }

    fn deposit(&mut self, account: i32, money: i64) -> bool {
        if self.is_valid_account(account) {
            self.account_balances[account as usize] += money;
            true
        } else {
            false
        }
    }

    fn withdraw(&mut self, account: i32, money: i64) -> bool {
        if self.is_valid_account(account) && self.account_balances[account as usize] >= money {
            self.account_balances[account as usize] -= money;
            true
        } else {
            false
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Bank;

    #[test]
    fn test_bank() {
        let mut bank = Bank::new(vec![10, 100, 20, 50, 30]);

        assert!(bank.withdraw(3, 10));
        assert!(bank.transfer(5, 1, 20));
        assert!(bank.deposit(5, 20));
        assert!(!bank.transfer(3, 4, 15));
        assert!(!bank.withdraw(10, 50));
    }
}
