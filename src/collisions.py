def how_many_before_collisions(buckets, loops=1):
    '''
    Roll random hashes into `buckets` and print
    number of rolls before a hash collision.
    
    Run `loops` number of times.
    '''
    for in in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets