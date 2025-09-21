// https://leetcode.com/problems/design-movie-rental-system/

use std::collections::{BTreeSet, HashMap, HashSet};

type Shop = i32;
type Movie = i32;
type Price = i32;

#[derive(Debug, Default)]
struct MovieRentingSystem {
    cheapest_movies: HashMap<Movie, BTreeSet<(Price, Shop)>>,
    prices: HashMap<(Movie, Shop), Price>,
    available_at: HashMap<Movie, HashSet<Shop>>,
    rented: BTreeSet<(Price, Shop, Movie)>,
}

impl MovieRentingSystem {
    fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut system = MovieRentingSystem::default();

        for entry in entries {
            let (shop, movie, price) = (entry[0], entry[1], entry[2]);

            system
                .cheapest_movies
                .entry(movie)
                .or_default()
                .insert((price, shop));

            system.prices.insert((movie, shop), price);

            system.available_at.entry(movie).or_default().insert(shop);
        }

        system
    }

    fn search(&self, movie: i32) -> Vec<i32> {
        match self.cheapest_movies.get(&movie) {
            Some(set) => set.iter().take(5).map(|(_, shop)| *shop).collect(),
            None => vec![],
        }
    }

    fn rent(&mut self, shop: i32, movie: i32) {
        let price = *self
            .prices
            .get(&(movie, shop))
            .expect("movie without price");

        self.cheapest_movies
            .get_mut(&movie)
            .expect("movie without price and shop")
            .remove(&(price, shop));

        self.available_at
            .get_mut(&movie)
            .expect("movie without shops")
            .remove(&shop);

        self.rented.insert((price, shop, movie));
    }

    fn drop(&mut self, shop: i32, movie: i32) {
        let price = *self
            .prices
            .get(&(movie, shop))
            .expect("movie without price");

        self.cheapest_movies
            .get_mut(&movie)
            .expect("movie without price and shop")
            .insert((price, shop));

        self.available_at
            .get_mut(&movie)
            .expect("movie without shops")
            .insert(shop);

        self.rented.remove(&(price, shop, movie));
    }

    fn report(&self) -> Vec<Vec<i32>> {
        self.rented
            .iter()
            .take(5)
            .map(|&(_, shop, movie)| vec![shop, movie])
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::MovieRentingSystem;

    #[test]
    fn case_1() {
        let mut mrs = MovieRentingSystem::new(
            3,
            vec![
                vec![0, 1, 5],
                vec![0, 2, 6],
                vec![0, 3, 7],
                vec![1, 1, 4],
                vec![1, 2, 7],
                vec![2, 1, 5],
            ],
        );

        dbg!(&mrs);

        assert_eq!(mrs.search(1), [1, 0, 2]);
        mrs.rent(0, 1);
        mrs.rent(1, 2);
        assert_eq!(mrs.report(), vec![vec![0, 1], vec![1, 2]]);
        mrs.drop(1, 2);
        assert_eq!(mrs.search(2), vec![0, 1]);
    }

    #[test]
    fn case_2() {
        let mut mrs = MovieRentingSystem::new(
            22,
            vec![
                vec![13, 6406, 5183],
                vec![10, 2926, 931],
                vec![0, 6424, 7126],
                vec![0, 4988, 4028],
                vec![6, 8295, 7660],
                vec![16, 4729, 3008],
                vec![7, 6349, 8844],
                vec![1, 6896, 3047],
                vec![8, 4693, 3264],
                vec![13, 1984, 6267],
                vec![14, 4544, 5627],
                vec![21, 6347, 1327],
                vec![7, 4932, 3085],
                vec![16, 5577, 1542],
                vec![11, 9549, 2609],
                vec![5, 8830, 5502],
                vec![19, 3157, 6780],
                vec![1, 7953, 5964],
                vec![7, 1882, 6571],
                vec![18, 9932, 1146],
                vec![17, 5985, 2625],
                vec![19, 8434, 4176],
                vec![19, 1762, 3420],
                vec![13, 2558, 984],
                vec![4, 4693, 6178],
                vec![17, 6347, 3059],
                vec![17, 5808, 1467],
                vec![21, 7778, 1596],
                vec![1, 47, 7419],
                vec![15, 646, 8719],
                vec![10, 1694, 9782],
                vec![6, 5577, 5867],
                vec![11, 6406, 4180],
                vec![12, 6347, 7325],
                vec![1, 1112, 8378],
                vec![8, 6750, 3274],
                vec![12, 531, 8300],
                vec![8, 7672, 6253],
                vec![17, 5551, 6090],
                vec![14, 4321, 597],
                vec![16, 8872, 2453],
                vec![5, 9630, 3367],
                vec![7, 8872, 9900],
                vec![16, 3238, 5601],
                vec![9, 9630, 9659],
                vec![12, 431, 2143],
                vec![13, 646, 6596],
                vec![12, 7953, 1106],
                vec![17, 1564, 5806],
                vec![9, 4988, 2545],
                vec![20, 3852, 3190],
                vec![16, 7953, 7802],
                vec![19, 646, 7631],
                vec![21, 9816, 46],
                vec![11, 7778, 37],
            ],
        );

        mrs.rent(1, 7953);
        assert_eq!(mrs.report(), vec![vec![1, 7953]]);

        mrs.drop(1, 7953);
        mrs.rent(11, 9549);
        assert_eq!(mrs.report(), vec![vec![11, 9549]]);
        assert_eq!(mrs.report(), vec![vec![11, 9549]]);

        assert_eq!(mrs.search(531), vec![12]);

        mrs.rent(17, 6347);
        assert_eq!(mrs.search(9998), Vec::<i32>::new());

        mrs.rent(12, 431);
        mrs.drop(11, 9549);
        assert_eq!(mrs.report(), vec![vec![12, 431], vec![17, 6347]]);

        mrs.rent(9, 9630);
        assert_eq!(
            mrs.report(),
            vec![vec![12, 431], vec![17, 6347], vec![9, 9630]]
        );

        mrs.rent(12, 6347);
        mrs.rent(14, 4321);
        mrs.drop(9, 9630);
        assert_eq!(
            mrs.report(),
            vec![
                vec![14, 4321],
                vec![12, 431],
                vec![17, 6347],
                vec![12, 6347]
            ]
        );

        mrs.rent(0, 4988);
        mrs.rent(13, 6406);
        mrs.rent(11, 7778);
        assert_eq!(
            mrs.report(),
            vec![
                vec![11, 7778],
                vec![14, 4321],
                vec![12, 431],
                vec![17, 6347],
                vec![0, 4988]
            ]
        );

        mrs.rent(8, 4693);
    }
}
