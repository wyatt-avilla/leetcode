use std::collections::HashMap;

struct SnapshotArray {
    snap_id: i32,
    arr: Vec<HashMap<i32, i32>>,
}

impl SnapshotArray {
    fn new(length: i32) -> Self {
        SnapshotArray {
            snap_id: 0,
            arr: vec![HashMap::from([(0, 0)]); length as usize],
        }
    }

    fn set(&mut self, index: i32, val: i32) {
        self.arr[index as usize].insert(self.snap_id, val);
    }

    fn snap(&mut self) -> i32 {
        let id = self.snap_id;
        self.snap_id += 1;
        id
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        for i in (0..=snap_id).rev() {
            if let Some(v) = self.arr[index as usize].get(&i) {
                return *v;
            }
        }
        unreachable!("problem contraints");
    }
}

fn main() {
    let mut sa = SnapshotArray::new(3);
    sa.set(0, 5);
    assert!(sa.snap() == 0);
    sa.set(0, 6);
    assert!(sa.get(0, 0) == 5);

    let mut sa2 = SnapshotArray::new(1);
    sa2.set(0, 15);
    sa2.snap();
    sa2.snap();
    sa2.snap();
    assert!(sa2.get(0, 2) == 15);
    sa2.snap();
    sa2.snap();
    assert!(sa2.get(0, 0) == 15);
}
