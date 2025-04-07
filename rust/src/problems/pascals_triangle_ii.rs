// https://leetcode.com/problems/pascals-triangle-ii/

pub struct Solution;

impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        // can be done without recursion :/
        let mut row: Vec<i32> = vec![1];
        if row_index == 0 {
            return row;
        };

        let prev_row = Solution::get_row(row_index - 1);
        for i in 1..row_index {
            row.push(prev_row[i as usize - 1] + prev_row[i as usize])
        }

        row.push(1);
        row
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let row_index = 3;
        assert_eq!(Solution::get_row(row_index), [1, 3, 3, 1]);
    }

    #[test]
    fn case_2() {
        let row_index = 0;
        assert_eq!(Solution::get_row(row_index), [1]);
    }

    #[test]
    fn case_3() {
        let row_index = 1;
        assert_eq!(Solution::get_row(row_index), [1, 1]);
    }

    #[test]
    fn case_4() {
        let row_index = 2;
        assert_eq!(Solution::get_row(row_index), [1, 2, 1]);
    }
}
