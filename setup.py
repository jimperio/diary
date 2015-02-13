from setuptools import setup, find_packages

def main():
  setup(name='jimperio.diary',
        version='0.1.0',
        description="Simple shared diary using Flask and React",
        packages=find_packages('.'),
        package_dir={'':'.'},
        install_requires=[
          'flask == 0.10.1',
          'flask-sqlalchemy == 2.0',
        ],)

if __name__ == "__main__":
  main()