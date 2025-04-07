// https://leetcode.com/problems/apply-discount-every-n-orders/

use std::collections::HashMap;

struct Cashier {
    n: u16,
    customers: u16,
    discount: i32,
    prices: HashMap<i32, i32>,
}

impl Cashier {
    fn new(n: i32, discount: i32, products: Vec<i32>, prices: Vec<i32>) -> Self {
        Cashier {
            n: n.try_into().unwrap(),
            customers: 0,
            discount,
            prices: products.into_iter().zip(prices).collect::<HashMap<_, _>>(),
        }
    }

    fn get_bill(&mut self, product: Vec<i32>, amount: Vec<i32>) -> f64 {
        self.customers += 1;

        let bill = f64::from(
            product
                .iter()
                .zip(amount)
                .map(|(pid, am)| self.prices[pid] * am)
                .sum::<i32>(),
        );

        if self.customers % self.n == 0 {
            bill * (f64::from(100 - self.discount) / 100.0)
        } else {
            bill
        }
    }
}

fn main() {
    let mut cs = Cashier::new(
        3,
        50,
        vec![1, 2, 3, 4, 5, 6, 7],
        vec![100, 200, 300, 400, 300, 200, 100],
    );

    assert!(cs.get_bill(vec![1, 2], vec![1, 2]) == 500.0);
    assert!(cs.get_bill(vec![3, 7], vec![10, 10]) == 4000.0);
    dbg!(cs.get_bill(vec![1, 2, 3, 4, 5, 6, 7], vec![1, 1, 1, 1, 1, 1, 1]));
    assert!(cs.get_bill(vec![1, 2, 3, 4, 5, 6, 7], vec![1, 1, 1, 1, 1, 1, 1]) == 800.0);
}
