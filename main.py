from sys import argv
from src.parkingviolations.api import Service
from os import environ

if __name__ == "__main__":
    app_key = environ.get("APP_KEY")
    # print("APP_KEY={}".format(app_key))
    page_size_str = argv[1]
    page_size = int(page_size_str.split('=')[1])
    num_pages_str = argv[2]
    num_pages = int(num_pages_str.split('=')[1])
    # print(f"page_size={page_size}, num_pages={num_pages}")
    try:
        output = argv[3]
    except Exception:
        output = None
    location = 'nc67-uf89'

    limit_size = int (page_size / num_pages)

    # print(f"limit_size={str(limit_size)}")
    with Service(app_key) as service:
        total_size = service.get_size(location)
        print(f"total_size={total_size}")
        print(service.get_info(location, limit_size))
        offset = 0
        for i in range(num_pages-1):
            print(f"i={i}")
            offset += limit_size
            if offset >= total_size:
                break;
            print(service.get_next_info(location, limit_size, offset))

    # with open(input_fn, "r") as fh, open(output_fn, "w") as fw:
    # 	for line in fh:
    # 		line = line.strip('\n')
    # 		val, base, curr = line.split(' ')
    # 		val = float(val)
    # 		fw.write(f"{convert(val, curr, base)} {curr}\n
