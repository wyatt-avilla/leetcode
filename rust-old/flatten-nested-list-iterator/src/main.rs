// https://leetcode.com/problems/flatten-nested-list-iterator/

use std::iter::Peekable;

#[derive(Debug, PartialEq, Eq)]
enum NestedInteger {
    Int(i32),
    List(Vec<NestedInteger>),
}

struct NestedIterator {
    it: Box<Peekable<Box<dyn Iterator<Item = i32>>>>,
}

fn underlying_nested_integer(ni: NestedInteger) -> Box<dyn Iterator<Item = i32>> {
    match ni {
        NestedInteger::Int(i) => Box::new(std::iter::once(i)),
        NestedInteger::List(v) => Box::new(v.into_iter().flat_map(underlying_nested_integer)),
    }
}

impl NestedIterator {
    fn new(nested_list: Vec<NestedInteger>) -> Self {
        let x: Box<dyn Iterator<Item = i32>> =
            Box::new(nested_list.into_iter().flat_map(underlying_nested_integer));
        NestedIterator {
            it: Box::new(x.peekable()),
        }
    }

    fn next(&mut self) -> i32 {
        self.it
            .next()
            .expect("problem constraits assert next won't be called on an empty iterator")
    }

    fn has_next(&mut self) -> bool {
        self.it.by_ref().peek().is_some()
    }
}

fn main() {
    let x = vec![
        NestedInteger::List(vec![NestedInteger::Int(1), NestedInteger::Int(1)]),
        NestedInteger::Int(2),
        NestedInteger::List(vec![NestedInteger::Int(1), NestedInteger::Int(1)]),
    ];

    let mut nested_list = NestedIterator::new(x);
    assert!(nested_list.has_next());
    assert!(nested_list.next() == 1);

    assert!(nested_list.has_next());
    assert!(nested_list.next() == 1);

    assert!(nested_list.has_next());
    assert!(nested_list.next() == 2);

    assert!(nested_list.has_next());
    assert!(nested_list.next() == 1);

    assert!(nested_list.has_next());
    assert!(nested_list.next() == 1);
}
