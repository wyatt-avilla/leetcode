#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <utility>
#include <vector>


#define CACHE_ENABLE true
#define CACHE_INFO false

class Board {
  public:
    Board(int n, const std::set<std::pair<int, int>> qp)
        : n(n), queen_positions(qp), all_spaces(generate_all_spaces()) {
        for (const std::pair<int, int>& q_pos : queen_positions) {
            int q_col = q_pos.first;
            int q_row = q_pos.second;

            if (is_valid_space(q_pos)) {
                occupied_cols.insert(q_col);
                occupied_rows.insert(q_row);
                occupied_pos_diag.insert(q_row + q_col);
                occupied_neg_diag.insert(q_row - q_col);
            } else {
                throw std::invalid_argument("Cannot place (" +
                                            std::to_string(q_col) + "," +
                                            std::to_string(q_row) + ")");
            }
        }
    };

    const int n;
    const std::set<std::pair<int, int>> queen_positions;

    const std::set<std::pair<int, int>>& all_spaces;

    // these should be const, but i dont want a seperate function (and loop)
    // that generates each set within the initializer list
    std::set<int> occupied_cols;
    std::set<int> occupied_rows;
    std::set<int> occupied_pos_diag;
    std::set<int> occupied_neg_diag;

    friend std::ostream& operator<<(std::ostream& os, const Board& b) {
        for (int r = 1; r <= b.n; ++r) {
            os << "[";
            for (int c = 1; c <= b.n; ++c) {
                if (b.queen_positions.find(std::make_pair(c, r)) !=
                    b.queen_positions.end()) {
                    os << "Q";
                } else {
                    os << "*";
                }
            }
            os << "]" << std::endl;
        }
        return os;
    }

    bool is_valid_space(std::pair<int, int> space) {
        int space_col = space.first;
        int space_row = space.second;

        return (occupied_cols.find(space_col) == occupied_cols.end() &&
                occupied_rows.find(space_row) == occupied_rows.end() &&
                occupied_pos_diag.find(space_row + space_col) ==
                    occupied_pos_diag.end() &&
                occupied_neg_diag.find(space_row - space_col) ==
                    occupied_neg_diag.end());
    }

    bool has_n_queens(void) {
        return static_cast<unsigned int>(n) == queen_positions.size();
    }

    int get_first_avail_row(void) {
        for (int i = 1; i <= n; ++i) {
            if (occupied_rows.find(i) == occupied_rows.end()) {
                return i;
            }
        }
        throw std::runtime_error("No more available rows.");
    }

    std::set<std::pair<int, int>> generate_valid_spaces(void) {
        std::set<std::pair<int, int>> valid_spaces;

        for (const std::pair<int, int>& space : all_spaces) {
            if (is_valid_space(space)) {
                valid_spaces.insert(space);
            }
        }

        return valid_spaces;
    }


  private:
    static std::map<int, std::set<std::pair<int, int>>> all_board_spaces_per_n;

    std::set<std::pair<int, int>>& generate_all_spaces(void) {
#ifdef CACHE_ENABLE

        auto it = all_board_spaces_per_n.find(n);
        if (it == all_board_spaces_per_n.end()) {
#if (CACHE_ENABLE && CACHE_INFO)
            std::cout << "[Cache Info] All spaces for " << n
                      << " not found, generating..." << std::endl;
#endif
            std::set<std::pair<int, int>> spaces;
            for (int c = 1; c <= n; ++c) {
                for (int r = 1; r <= n; ++r) {
                    spaces.insert(std::make_pair(c, r));
                }
            }

            all_board_spaces_per_n[n] = spaces;
        }

        return all_board_spaces_per_n[n];

#else

        std::set<std::pair<int, int>> spaces;
        for (int c = 1; c <= n; ++c) {
            for (int r = 1; r <= n; ++r) {
                spaces.insert(std::make_pair(c, r));
            }
        }
        return spaces;

#endif
    }
};

void visualize_occupied(const std::set<std::pair<int, int>>& occupied, int n) {
    for (int r = 1; r <= n; ++r) {
        std::cout << "[";
        for (int c = 1; c <= n; ++c) {
            auto it = occupied.find(std::make_pair(c, r));
            if (it != occupied.end()) {
                std::cout << "X";
            } else {
                std::cout << "*";
            }
        }
        std::cout << "]" << std::endl;
    }
}

void print_pos_set(const std::set<std::pair<int, int>> pos_set) {
    if (pos_set.size() == 0) {
        std::cout << "{}" << std::endl;
        return;
    }
    std::cout << "{" << std::endl;
    for (std::pair<int, int> pos : pos_set) {
        std::cout << "  (" << pos.first << "," << pos.second << ")"
                  << std::endl;
    }
    std::cout << "}" << std::endl;
}

std::vector<std::string> format_answer(Board board) {
    std::vector<std::string> solution;

    int n = board.n;
    for (int row = 1; row <= n; ++row) {
        std::string current_row;
        for (int col = 1; col <= n; ++col) {
            if (board.queen_positions.find(std::make_pair(row, col)) !=
                board.queen_positions.end()) {
                current_row.append("Q");
            } else {
                current_row.append(".");
            }
        }
        solution.push_back(current_row);
    }

    return solution;
}


#ifdef CACHE_ENABLE

// this sucks ? let me initialize this inside the class please...
std::map<int, std::set<std::pair<int, int>>> Board::all_board_spaces_per_n;

#endif

class Solution {
  public:
    std::vector<std::vector<std::string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> solutions;
        std::stack<Board> games;

        Board board(n, {});
        games.push(board);

        while (!games.empty()) {
            Board current_board = games.top();
            games.pop();

            if (current_board.has_n_queens()) {
                solutions.push_back(format_answer(current_board));
                continue;
            }

            int cur_row = current_board.get_first_avail_row();

            for (int i = 1; i <= current_board.n; ++i) {
                std::pair<int, int> current_space = std::make_pair(i, cur_row);
                std::set<std::pair<int, int>> current_queen_positions(
                    current_board.queen_positions);
                current_queen_positions.insert(current_space);
                try {
                    Board new_board(current_board.n, current_queen_positions);
                    if (new_board.has_n_queens()) {
                        solutions.push_back(format_answer(new_board));
                        continue;
                    }

                    games.push(new_board);
                } catch (const std::invalid_argument& e) {
                    // invalid queen placement
                    continue;
                }
            }
        }


        return solutions;
    }
};

void print_solution(std::vector<std::string> solution) {
    for (auto row : solution) {
        std::cout << row << std::endl;
    }
}

int main(void) {
    Solution solution;

    for (int i = 1; i <= 9; ++i) {
        std::cout << i << " +++" << std::endl;
        for (auto sol : solution.solveNQueens(i)) {
            std::cout << "-----------" << std::endl;
            print_solution(sol);
        }
    }


    return 0;
}
