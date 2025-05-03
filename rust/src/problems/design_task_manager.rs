// https://leetcode.com/problems/design-task-manager/

use std::collections::{BTreeSet, HashMap};

type UserId = i32;
type TaskId = i32;
type Priority = i32;

#[derive(Default, Debug)]
struct Tasks {
    sorted_tasks: BTreeSet<(Priority, TaskId)>,
    priority_for: HashMap<TaskId, Priority>,
}

#[derive(Default, Debug)]
struct TaskManager {
    tasks_for: HashMap<UserId, Tasks>,
    user_for: HashMap<TaskId, UserId>,
    global_tasks: BTreeSet<(Priority, TaskId)>,
}

impl TaskManager {
    fn new(tasks: Vec<Vec<i32>>) -> Self {
        let mut task_manger = TaskManager::default();
        for triple in tasks {
            task_manger.add(triple[0], triple[1], triple[2]);
        }

        task_manger
    }

    fn add(&mut self, user_id: i32, task_id: i32, priority: i32) {
        self.user_for.insert(task_id, user_id);

        let tasks = self.tasks_for.entry(user_id).or_default();

        tasks.priority_for.insert(task_id, priority);

        self.global_tasks.insert((priority, task_id));
        tasks.sorted_tasks.insert((priority, task_id));
    }

    fn edit(&mut self, task_id: i32, new_priority: i32) {
        let tasks = self
            .tasks_for
            .get_mut(self.user_for.get(&task_id).unwrap())
            .unwrap();

        let prio = tasks.priority_for.get_mut(&task_id).unwrap();

        let task_pair = (*prio, task_id);

        self.global_tasks.remove(&task_pair);
        tasks.sorted_tasks.remove(&task_pair);

        *prio = new_priority;

        tasks.sorted_tasks.insert((new_priority, task_id));
        self.global_tasks.insert((new_priority, task_id));
    }

    fn rmv(&mut self, task_id: i32) {
        let user_id = self.user_for.remove(&task_id).unwrap();

        let tasks = self.tasks_for.get_mut(&user_id).unwrap();
        let prio = tasks.priority_for.get(&task_id).unwrap();

        let task_pair = (*prio, task_id);

        tasks.sorted_tasks.remove(&task_pair);
        self.global_tasks.remove(&task_pair);

        self.user_for.remove(&task_id);
    }

    fn exec_top(&mut self) -> i32 {
        if let Some((_, task_id)) = self.global_tasks.pop_last() {
            let user_id = *self.user_for.get(&task_id).unwrap();
            self.rmv(task_id);

            user_id
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::TaskManager;

    #[test]
    fn test_task_manager_behavior() {
        let mut task_manager =
            TaskManager::new(vec![vec![1, 101, 10], vec![2, 102, 20], vec![3, 103, 15]]);

        task_manager.add(4, 104, 5);
        task_manager.edit(102, 8);
        dbg!(&task_manager);
        assert_eq!(task_manager.exec_top(), 3);
        task_manager.rmv(101);
        task_manager.add(5, 105, 15);
        assert_eq!(task_manager.exec_top(), 5);
    }
}
