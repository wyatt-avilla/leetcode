#[derive(Debug)]
struct DataStream {
    value: i32,
    k: i32,
    val_count: i32,
}

impl DataStream {
    fn new(value: i32, k: i32) -> Self {
        DataStream {
            value,
            k,
            val_count: 0,
        }
    }

    fn consec(&mut self, num: i32) -> bool {
        if num == self.value {
            self.val_count += 1;
        } else {
            self.val_count = 0;
        }

        self.val_count >= self.k
    }
}

#[cfg(test)]
mod tests {
    use super::DataStream;

    #[test]
    fn case_1() {
        let mut data_stream = DataStream::new(4, 3);

        dbg!(&data_stream);
        assert!(!data_stream.consec(4));
        dbg!(&data_stream);
        assert!(!data_stream.consec(4));
        dbg!(&data_stream);
        assert!(data_stream.consec(4));
        dbg!(&data_stream);
        assert!(!data_stream.consec(3));
    }
}
