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

#[cfg(test)]
mod tests {
    use super::ProductOfNumbers;

    #[test]
    fn case_1() {
        let mut pom = ProductOfNumbers::new();
        pom.add(3);
        pom.add(0);
        pom.add(2);
        pom.add(5);
        pom.add(4);
        assert_eq!(pom.get_product(2), 20);
        assert_eq!(pom.get_product(3), 40);
        assert_eq!(pom.get_product(4), 0);
    }
}
