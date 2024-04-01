// https://leetcode.com/problems/count-good-triplets/

pub struct Solution;

impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let arr_len = arr.iter().count();
        let mut count = 0;
        for i in 0..arr_len {
            for j in i + 1..arr_len {
                for k in j + 1..arr_len {
                    if (arr[i] - arr[j]).abs() <= a
                        && (arr[j] - arr[k]).abs() <= b
                        && (arr[i] - arr[k]).abs() <= c
                    {
                        count += 1;
                        println!("{} {} {}", i, j, k);
                    }
                }
            }
        }
        count
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
        let arr = vec![3, 0, 1, 1, 9, 7];
        let a = 7;
        let b = 2;
        let c = 3;
        let result = Solution::count_good_triplets(arr, a, b, c);
        assert_eq!(result, 4);
    }

    // Test case 2
    #[test]
    fn case2() {
        let arr = vec![1, 1, 2, 2, 3];
        let a = 0;
        let b = 0;
        let c = 1;
        let result = Solution::count_good_triplets(arr, a, b, c);
        assert_eq!(result, 0);
    }
}
