if __name__ == '__main__':
    _header = '## Hi there 👋'
    about = open(f'../_pages/about.md').read().strip()
    with open('README.md', 'w') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(about)