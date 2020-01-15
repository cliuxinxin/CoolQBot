async def write_file(msg):
    with open('recorder.txt', 'a') as f:
        f.write(msg)
        f.write('\n')
