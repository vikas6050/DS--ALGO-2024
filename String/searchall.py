def string_search(big, small):
    result = []
    index = big.find(small)
    while index != -1:
        result.append(index)
        index = big.find(small, index + 1)
    return result

# Example usage:
big_string = "I liked the movie, acting in movie was great!"
small_string = "movie"
result_list = string_search(big_string, small_string)
print(result_list)
