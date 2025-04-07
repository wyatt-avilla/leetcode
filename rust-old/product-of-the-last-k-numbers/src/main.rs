// https://leetcode.com/problems/product-of-the-last-k-numbers/

struct ProductOfNumbers {
    products: Vec<i32>,
}

impl ProductOfNumbers {
    fn new() -> Self {
        ProductOfNumbers { products: vec![1] }
    }

    fn add(&mut self, num: i32) {
        if num > 0 {
            self.products.push(self.products.last().unwrap() * num);
        } else {
            self.products = vec![1];
        }
    }

    fn get_product(&self, k: i32) -> i32 {
        match self.products.iter().nth_back(k as usize) {
            Some(div) => *self.products.last().expect("problem constraints") / div,
            None => 0,
        }
    }
}

fn main() {
    let mut pom1 = ProductOfNumbers::new();
    pom1.add(3);
    pom1.add(0);
    pom1.add(2);
    pom1.add(5);
    pom1.add(4);
    assert!(pom1.get_product(2) == 20);
    assert!(pom1.get_product(3) == 40);
    assert!(pom1.get_product(4) == 0);
}
