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

fn main() {
    println!("main executed")
}

// Import the necessary modules
#[cfg(test)]
mod tests {
    // Import the Solution struct (assuming it's in the same module or crate)
    use super::Solution;

    // Test case 1
    #[test]
    fn case1() {
        let row_index = 3;
        assert_eq!(Solution::get_row(row_index), [1, 3, 3, 1]);
    }

    // Test case 2
    #[test]
    fn case2() {
        let row_index = 0;
        assert_eq!(Solution::get_row(row_index), [1]);
    }

    // Test case 3
    #[test]
    fn case3() {
        let row_index = 1;
        assert_eq!(Solution::get_row(row_index), [1, 1]);
    }

    // Test case 4
    #[test]
    fn case4() {
        let row_index = 2;
        assert_eq!(Solution::get_row(row_index), [1, 2, 1]);
    }
}
