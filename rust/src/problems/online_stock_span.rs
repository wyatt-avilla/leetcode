// https://leetcode.com/problems/online-stock-span/

#[derive(Debug)]
struct StockSpanner {
    stack: Vec<(i32, i32)>,
}

impl StockSpanner {
    fn new() -> Self {
        StockSpanner { stack: vec![] }
    }

    fn next(&mut self, price: i32) -> i32 {
        if self.stack.last().is_none_or(|(p, _)| *p > price) {
            self.stack.push((price, 1));
            return 1;
        }

        let to_fold = self
            .stack
            .iter()
            .rev()
            .take_while(|(p, _)| *p <= price)
            .count();

        let folded = self
            .stack
            .split_off(self.stack.len() - to_fold)
            .iter()
            .fold((price, 1), |(p, acc_s), (_, s)| (p, acc_s + s));

        self.stack.push(folded);

        folded.1
    }
}

#[cfg(test)]
mod tests {
    use super::StockSpanner;

    #[test]
    fn case_1() {
        let mut ss = StockSpanner::new();
        assert_eq!(ss.next(100), 1);
        assert_eq!(ss.next(80), 1);
        assert_eq!(ss.next(60), 1);
        assert_eq!(ss.next(70), 2);
        assert_eq!(ss.next(60), 1);
        assert_eq!(ss.next(75), 4);
        assert_eq!(ss.next(85), 6);
    }

    #[test]
    fn case_2() {
        let mut ss = StockSpanner::new();
        assert_eq!(ss.next(29), 1);
        assert_eq!(ss.next(91), 2);
        assert_eq!(ss.next(62), 1);
        dbg!(&ss);
        assert_eq!(ss.next(76), 2);
        assert_eq!(ss.next(51), 1);
    }

    #[test]
    fn case_3() {
        let mut ss = StockSpanner::new();
        assert_eq!(ss.next(90), 1);
        assert_eq!(ss.next(21), 1);
        assert_eq!(ss.next(21), 2);
        assert_eq!(ss.next(68), 3);
        assert_eq!(ss.next(94), 5);
        assert_eq!(ss.next(13), 1);
        assert_eq!(ss.next(1), 1);
        assert_eq!(ss.next(37), 3);
        assert_eq!(ss.next(3), 1);
        assert_eq!(ss.next(61), 5);
        assert_eq!(ss.next(86), 6);
        assert_eq!(ss.next(19), 1);
        assert_eq!(ss.next(12), 1);
        assert_eq!(ss.next(35), 3);
        assert_eq!(ss.next(96), 15);
    }
}
