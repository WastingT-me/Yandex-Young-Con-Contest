# -*- coding: utf-8 -*-

def parse_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    c = int(data[0].strip())
    index = 1
    posts = {}

    for _ in range(c):
        line = data[index].strip().split()
        post_name = line[0]
        num_halls = int(line[1])
        halls = []
        index += 1
        for _ in range(num_halls):
            hall_schedule = data[index].strip().split()
            hall_name = hall_schedule[1]
            halls.append((hall_schedule[0], hall_name))
            index += 1
        posts[post_name] = halls

    m = int(data[index].strip())
    index += 1
    requests = []

    for _ in range(m):
        request = data[index].strip().split()
        num_posts = int(request[0])
        post_names = request[1:]
        requests.append(post_names)
        index += 1

    return posts, requests

def find_available_halls(posts, requests):
    results = []

    for request in requests:
        num_posts = len(request)
        available_halls = None

        for hour in range(24):
            current_halls = []
            for post in request:
                halls = posts[post]
                hall_found = False
                for schedule, hall_name in halls:
                    if schedule[hour] == '.':
                        current_halls.append(hall_name)
                        hall_found = True
                        break
                if not hall_found:
                    break

            if len(current_halls) == num_posts:
                available_halls = current_halls
                break

        if available_halls:
            results.append(f"Yes {' '.join(available_halls)}")
        else:
            results.append("No")

    return results

def main():
    posts, requests = parse_input()
    results = find_available_halls(posts, requests)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()