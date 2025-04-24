// https://leetcode.com/problems/design-a-food-rating-system/

use std::collections::{BTreeMap, BTreeSet, HashMap};

#[derive(Default, Debug)]
struct RatingMetadata {
    food_to_rating: HashMap<String, i32>,
    rating_to_foods: BTreeMap<i32, BTreeSet<String>>,
}

#[derive(Debug)]
struct FoodRatings {
    food_to_cuisine: HashMap<String, String>,
    cuisine_to_ratings: HashMap<String, RatingMetadata>,
}

impl FoodRatings {
    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let num_foods = foods.len();

        let mut food_to_cuisine: HashMap<String, String> = HashMap::new();
        let mut cuisine_to_ratings: HashMap<String, RatingMetadata> = HashMap::new();

        for i in 0..num_foods {
            food_to_cuisine.insert(foods[i].clone(), cuisines[i].clone());
            let rating_metadata = cuisine_to_ratings.entry(cuisines[i].clone()).or_default();

            rating_metadata
                .rating_to_foods
                .entry(ratings[i])
                .or_default()
                .insert(foods[i].clone());

            rating_metadata
                .food_to_rating
                .insert(foods[i].clone(), ratings[i]);
        }

        FoodRatings {
            food_to_cuisine,
            cuisine_to_ratings,
        }
    }

    fn change_rating(&mut self, food: String, new_rating: i32) {
        let rating_metadata = self
            .cuisine_to_ratings
            .get_mut(
                self.food_to_cuisine
                    .get(&food)
                    .expect("problem constraints"),
            )
            .expect("problem constraints");

        let curr_rating = rating_metadata
            .food_to_rating
            .get_mut(&food)
            .expect("problem constraints");

        rating_metadata
            .rating_to_foods
            .get_mut(curr_rating)
            .expect("problem constraints")
            .remove(&food);

        *curr_rating = new_rating;

        rating_metadata
            .rating_to_foods
            .entry(*curr_rating)
            .or_default()
            .insert(food);
    }

    fn highest_rated(&self, cuisine: String) -> String {
        self.cuisine_to_ratings
            .get(&cuisine)
            .expect("problem constraints")
            .rating_to_foods
            .iter()
            .rev()
            .find(|(_, f)| !f.is_empty())
            .expect("problem constraints")
            .1
            .first()
            .expect("problem constraints")
            .clone()
    }
}

#[cfg(test)]
mod tests {
    use super::FoodRatings;

    #[test]
    fn case_1() {
        let foods = vec![
            "kimchi".to_string(),
            "miso".to_string(),
            "sushi".to_string(),
            "moussaka".to_string(),
            "ramen".to_string(),
            "bulgogi".to_string(),
        ];
        let cuisines = vec![
            "korean".to_string(),
            "japanese".to_string(),
            "japanese".to_string(),
            "greek".to_string(),
            "japanese".to_string(),
            "korean".to_string(),
        ];
        let ratings = vec![9, 12, 8, 15, 14, 7];

        let mut fr = FoodRatings::new(foods, cuisines, ratings);

        assert_eq!(fr.highest_rated("korean".to_string()), "kimchi");
        assert_eq!(fr.highest_rated("japanese".to_string()), "ramen");
        fr.change_rating("sushi".to_string(), 16);
        assert_eq!(fr.highest_rated("japanese".to_string()), "sushi");
        fr.change_rating("ramen".to_string(), 16);
        assert_eq!(fr.highest_rated("japanese".to_string()), "ramen");
    }

    #[test]
    fn case_2() {
        let foods = vec![
            "emgqdbo".to_string(),
            "jmvfxjohq".to_string(),
            "qnvseohnoe".to_string(),
            "yhptazyko".to_string(),
            "ocqmvmwjq".to_string(),
        ];
        let cuisines = vec![
            "snaxol".to_string(),
            "snaxol".to_string(),
            "snaxol".to_string(),
            "fajbervsj".to_string(),
            "fajbervsj".to_string(),
        ];
        let ratings = vec![2, 6, 18, 6, 5];

        let mut fr = FoodRatings::new(foods, cuisines, ratings);

        fr.change_rating("qnvseohnoe".to_string(), 11);
        assert_eq!(fr.highest_rated("fajbervsj".to_string()), "yhptazyko");
        fr.change_rating("emgqdbo".to_string(), 3);
        fr.change_rating("jmvfxjohq".to_string(), 9);
        fr.change_rating("emgqdbo".to_string(), 14);
        assert_eq!(fr.highest_rated("fajbervsj".to_string()), "yhptazyko");
        assert_eq!(fr.highest_rated("snaxol".to_string()), "emgqdbo");
    }
}
